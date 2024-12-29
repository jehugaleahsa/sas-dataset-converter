from io import TextIOWrapper
from pathlib import Path
from datetime import datetime
from argparse import ArgumentParser
import multiprocessing
from multiprocessing.pool import Pool
import collections
import json
import numpy as np
import pandas as pd
import pyreadstat


pandas_type_map = {
    np.dtypes.StrDType: "string",
    np.dtypes.Int64DType: "i64",
    np.dtypes.Int32DType: "i32",
    np.dtypes.BoolDType: "bool",
    np.dtypes.Int16DType: "i16",
    np.dtypes.Int8DType: "i8",
    np.dtypes.UInt64DType: "u64",
    np.dtypes.UInt32DType: "u32",
    np.dtypes.UInt16DType: "u16",
    np.dtypes.UInt8DType: "u8",
    np.dtypes.Float64DType: "f64",
    np.dtypes.Float32DType: "f32",
}

def convert_sas7bdat(input: Path, output: Path):
    file = { "version": "1.0.0" }
    data_frame = convert_sas7bdat_dataset(file, input)
    write_file(output, file, data_frame)

def convert_xport(input: Path, output: Path):
    file = { "version": "1.0.0" }
    data_frame = convert_xport_dataset(file, input)
    write_file(output, file, data_frame)

def convert_sas7bdat_dataset(file: dict, input: Path) -> pd.DataFrame:
    data_frame, file_metadata = pyreadstat.read_sas7bdat(
        input, 
        encoding="utf-8",
        disable_datetime_conversion=True
    )
    add_dataset_metadata(file, data_frame, file_metadata)
    return data_frame

def convert_xport_dataset(file: dict, input: Path) -> pd.DataFrame:
    data_frame, file_metadata = pyreadstat.read_xport(
        input, 
        encoding="utf-8", 
        disable_datetime_conversion=True
    )
    add_dataset_metadata(file, data_frame, file_metadata)
    return data_frame

def add_dataset_metadata(file: dict, data_frame: pd.DataFrame, file_metadata):
    file["name"] = file_metadata.table_name
    file["metadata"] = get_default_file_metadata(file)
    enrich_metadata(file["metadata"], data_frame, file_metadata)

    columns = [get_column_metadata(file_metadata, column_name) for column_name in file_metadata.column_names]
    file["columns"] = convert_dataset_columns(columns, data_frame)

def get_default_file_metadata(file: dict) -> dict:
    now = datetime.now()
    return {
        "creationDateTime": now.isoformat(),
        "modificationDateTime": now.isoformat()
    }

def enrich_metadata(metadata: dict, data_frame: pd.DataFrame, file_metadata):    
    if file_metadata.number_rows is not None:
        metadata["recordCount"] = file_metadata.number_rows
    else:
        metadata["recordCount"] = len(data_frame.index)

    if file_metadata.creation_time is not None:
        metadata["creationDateTime"] = file_metadata.creation_time.isoformat()
    if file_metadata.modification_time is not None:
        metadata["modificationDateTime"] = file_metadata.modification_time.isoformat()

def get_column_metadata(file_metadata, column_name: str) -> dict:
    metadata = {}
    metadata["name"] = column_name
    label = file_metadata.column_names_to_labels.get(column_name)
    if not is_blank(label):
        metadata["label"] = label
    type = file_metadata.readstat_variable_types.get(column_name)
    if not is_blank(type):
        metadata["type"] = "number" if type == "double" else "string"
    length = file_metadata.variable_storage_width.get(column_name)
    if length is not None:
        metadata["length"] = length
    format = file_metadata.variable_to_label.get(column_name)
    if not is_blank(format):
        metadata["format"] = format
    return metadata

def is_blank(value: str) -> bool:
    return value is None or len(value.rstrip()) == 0

def convert_dataset_columns(columns: list[dict], data: pd.DataFrame) -> dict:
    return [convert_dataset_column(column, data) for column in columns]

def convert_dataset_column(column_metadata: dict, data: pd.DataFrame) -> dict:
    column = {}
    name = column_metadata.get("name")
    column["name"] = name
    metadata = convert_column_metadata(column_metadata)
    if len(metadata) > 0:
        column["metadata"] = metadata
    column["type"] = derive_type(column_metadata, data, name)
    column["nullable"] = bool(data[name].isnull().any())
    return column

def convert_column_metadata(metadata: dict) -> dict:
    keys = ["label", "length"]
    return prune(metadata, keys)

def prune(data: dict, keys: list[str]) -> dict:
    return { key: data.get(key) for key in keys if key in data }

def derive_type(metadata: dict, data: pd.DataFrame, name: str) -> str:
    pandas_type = type(data.dtypes[name])
    data_type = pandas_type_map.get(pandas_type)
    if data_type is not None:
        return data_type
    
    return "f64" if metadata["type"] == "number" else "string"

def write_file(output: Path, file: dict, data_frame: pd.DataFrame):
    with open(output, 'w') as out:
        write_json_line(out, file)

        # Replace empty strings, NaN, Inf, and -Inf with None
        data_frame.replace(["", np.nan, np.Inf, -np.Inf], None, inplace=True)

        # Currently, this is the only way to write 
        for _, row in data_frame.iterrows():
            values = row.to_list()
            write_json_line(out, values)

def write_json_line(out: TextIOWrapper, file: dict | list):
    separators = (',', ':')
    json.dump(
        file, 
        out, 
        ensure_ascii=False, 
        indent=None, 
        check_circular=False, 
        separators=separators
    )
    out.write("\n")

def get_input_files(input: Path, extension: str) -> list[Path]:
    if input.is_dir():
        return [*input.rglob("*" + extension)]
    elif input.is_file() and input.suffix == extension:
        return [input]
    else:
        return []
    
def run_task(task):
    converter, params = task
    converter(*params)

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="python converter.py",
        description="Converts XPORT V5+ and SAS7BDAT files to Dataset-JSON",
        allow_abbrev=False
    )
    parser.add_argument(
        "-i", 
        "--input", 
        required=True, 
        type=Path,
        help="The path to a SAS file, or directory containing SAS files."
    )
    parser.add_argument(
        "-o", 
        "--output", 
        required=True, 
        type=Path,
        help="The path to the directory to store the converted JSON file(s)."
    )
    parser.add_argument(
        "-t",
        "--threads",
        required=False,
        default=None,
        type=int,
        help="The maximum number of threads to run in parallel."
    )

    arguments = parser.parse_args()
    input: Path = arguments.input
    output: Path = arguments.output
    threads: int = arguments.threads

    try:
        output.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        print("Could not create the output directory.")
        exit(1)
    except OSError:
        print("The specified output directory is a file path.")
        exit(1)

    if threads is None or threads <= 0:
        threads = multiprocessing.cpu_count() - 1
        
    sas7bdat_inputs = get_input_files(input, ".sas7bdat")
    xport_inputs = get_input_files(input, ".xpt")
    
    tasks = []
    for sas7bdat_input in sas7bdat_inputs:
        current_in = sas7bdat_input
        current_out = output / Path(sas7bdat_input.name).with_suffix(".jsonl")
        params = (current_in, current_out)
        tasks.append((convert_sas7bdat, params))

    for xport_input in xport_inputs:
        current_in = xport_input
        current_out = output / Path(xport_input.name).with_suffix(".jsonl")
        params = (current_in, current_out)
        tasks.append((convert_xport, params))

    threads = max(min(threads, len(tasks)), 1)
    with Pool(processes=threads) as pool:
        queue = pool.imap_unordered(run_task, tasks)
        collections.deque(queue, maxlen=0)
