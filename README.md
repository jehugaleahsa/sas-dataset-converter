# SAS Dataset Converter
This is a sample project for converting SAS XPORT V5+ and SAS7BDAT file formats to an experimental JSON format, for storing dataset data. This is not the [CDISC Dataset-JSON format](https://www.cdisc.org/standards/data-exchange/dataset-json), but an independent research project with similar goals.

The big difference is this JSON format does not imply any ties to a particular platform or industry, such CDISC libraries or the clinical industry. Instead, this is a format that can be used by any organization interested in defining a schema and transferring data. This proposal also doesn't enforce that the dataset data be transferred in JSON, as there may be benefits to other formats. So, features are provided that would allow organizations to transfer data in other formats, such as [SQLite files](https://www.sqlite.org/index.html), [Apache Avro](https://avro.apache.org/), [Google Protobuf](https://protobuf.dev/overview/), [JSON Lines](https://jsonlines.org/), etc.

## Setup
On the command line, navigate to the parent folder, and clone the project from GitHub by typing this command:

```
git clone https://github.com/jehugaleahsa/sas-dataset-converter.git
```

Then `cd` into the created `sas-dataset-converter` directory.

Make sure Python >=3.10 is installed.

> On many systems, both Python 2 and 3 are installed. You need to ensure you are using Python 3. Often the alias `python3` can be used.

Create a virtual environment for the project by typing:

```
python -m venv env
```

After a few moments, a `env` sub-directory will be created.

On Mac/Linux, you can activate the environment by typing:

```
source env/bin/activate
```

On Windows, you can active the environment by typing:

```
env/Scripts/activate
```

> You might need to specify `activate.bat` or `Activate.ps1` explicitly depending on whether you're using cmd or PowerShell.

Now you can install any project dependencies by running the following command:

```
python -m pip install -r requirements.txt
```

## Running a conversion
After completing the setup, you should be able to run a conversion with the following command:

```
python converter.py --input=<path-to-input> --output=<path-to-output>
```

Replace `<path-to-input>` with the path to the directory containing XPT or SAS7BDAT files. Make sure to provide an absolute path. Replace `<path-to-output>` with the path to the directory where you want to store the converted dataset file.

> If your directory paths contain spaces or other special characters, you might need to wrap the paths in quotes (`"`).

For a full list of the conversion options, type the following command:

```
python converter.py -h
```

In particular, the `-t` or `--threads` parameter can be used to control how many threads/processes are used to convert the datasets. By default, the number of threads matches the CPU count of the machine.

## Proposal
This proposal discusses an extensible JSON-based specification for the representation of tabular data and its metadata.

Here is a quick example of a proposed dataset metadata (formatted for readability):

```json
{
    "version": "1.0.0",
    "name": "AE",
    "metadata": {
        "creationDateTime": "2023-12-01T12:32:31.184200",
        "modificationDateTime": "2023-12-01T12:32:31.184200",
        "label": "Adverse Events",
        "recordCount": 16
    },
    "columns": [
        {
            "name": "STUDYID",
            "metadata": {
                "label": "Study Identifier",
                "length": 7
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "DOMAIN",
            "metadata": {
                "label": "Domain Abbreviation",
                "length": 2
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "USUBJID",
            "metadata": {
                "label": "Unique Subject Identifier",
                "length": 14
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AESEQ",
            "metadata": {
                "label": "Sequence Number"
            },
            "type": "f64",
            "nullable": false
        },
        {
            "name": "AESPID",
            "metadata": {
                "label": "Sponsor-Defined Identifier",
                "length": 4
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AETERM",
            "metadata": {
                "label": "Reported Term for the Adverse Event",
                "length": 25
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AEMODIFY",
            "metadata": {
                "label": "Modified Reported Term",
                "length": 9
            },
            "type": "string",
            "nullable": true
        },
        {
            "name": "AEDECOD",
            "metadata": {
                "label": "Dictionary-Derived Term",
                "length": 18
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AEBODSYS",
            "metadata": {
                "label": "Body System or Organ Class",
                "length": 52
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AESEV",
            "metadata": {
                "label": "Severity/Intensity",
                "length": 8
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AESER",
            "metadata": {
                "label": "Serious Event",
                "length": 1
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AEACN",
            "metadata": {
                "label": "Action Taken with Study Treatment",
                "length": 30
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AEREL",
            "metadata": {
                "label": "Causality",
                "length": 16
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AESTDTC",
            "metadata": {
                "label": "Start Date/Time of Adverse Event",
                "length": 10
            },
            "type": "string",
            "nullable": false
        },
        {
            "name": "AEENDTC",
            "metadata": {
                "label": "End Date/Time of Adverse Event",
                "length": 10
            },
            "type": "string",
            "nullable": true
        },
        {
            "name": "AESTDY",
            "metadata": {
                "label": "Study Day of Start of Adverse Event"
            },
            "type": "f64",
            "nullable": false
        },
        {
            "name": "AEENDY",
            "metadata": {
                "label": "Study Day of End of Adverse Event"
            },
            "type": "f64",
            "nullable": true
        },
        {
            "name": "AEENRF",
            "metadata": {
                "label": "End Relative to Reference Period",
                "length": 5
            },
            "type": "string",
            "nullable": true
        }
    ]
}
```

Notice the metadata is formatted JSON, and there is no row data. In a real file, the metadata would not be formatted and only the first line in the JSON file would contain the dataset metadata. Each subsequent line would contain one row of data, like so:

```json
["CDISC01", "AE", "CDISC01.100008", 1.0, "1", "AGITATED", "AGITATION", "Agitation", "Psychiatric disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05", null, 3.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.100008", 2.0, "2", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "MODERATE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05-13", null, 15.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.100008", 3.0, "3", "DECREASED APPETITE", null, "Decreased appetite", "Metabolism and nutrition disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-08-19", "2003-09-15", 113.0, 140.0, null]
[ "CDISC01", "AE", "CDISC01.100014", 1.0, "1", "DIARRHEA", null, "Diarrhoea", "Gastrointestinal disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.100014", 2.0, "2", "HEMORRHOIDS", null, "Haemorrhoids", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.100014", 3.0, "3", "HEADACHE", null, "Headache", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-27", null, 105.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.100014", 4.0, "4", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "MODERATE", "N", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-03", "2004-02-03", 112.0, 112.0, null]
[ "CDISC01", "AE", "CDISC01.100014", 5.0, "5", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "SEVERE", "Y", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-04", "2004-02-09", 113.0, 118.0, null]
[ "CDISC01", "AE", "CDISC01.200001", 1.0, "1", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null]
[ "CDISC01", "AE", "CDISC01.200001", 2.0, "5", "LEFT KNEE PAIN WORSENING", null, "Arthralgia", "Musculoskeletal and connective tissue disorders", "SEVERE", "N", "DRUG WITHDRAWN", "NOT RELATED", "2004-02-02", null, 126.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.200001", 3.0, "3", "CONSTIPATION", null, "Constipation", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2003-12-25", null, 87.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.200001", 4.0, "4", "TIREDNESS", null, "Fatigue", "General disorders and administration site conditions", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-12-25", null, 87.0, null, "AFTER"]
[ "CDISC01", "AE", "CDISC01.200001", 5.0, "2", "NAUSEA INTERMITTENT", null, "Nausea", "Gastrointestinal disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null]
[ "CDISC01", "AE", "CDISC01.200002", 1.0, "3", "LIGHTHEADEDNESS", null, "Dizziness", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-02-26", "2004-02-26", 140.0, 140.0, null]
[ "CDISC01", "AE", "CDISC01.200002", 2.0, "1", "MUSCLE SPASMS", null, "Muscle spasms", "Musculoskeletal and connective tissue disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER" ]
["CDISC01", "AE", "CDISC01.200002", 3.0, "2", "PALPITATIONS INTERMITTENT", null, "Palpitations", "Cardiac disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER"]
```

The underlying file format is known as [JSON Lines](https://jsonlines.org/). Only the first row may contain dataset metadata. The first row must be formatted such that a newline (\n) does not appear. Each subsequent line is an array of row data, which also must be formatted such that a newline (\n) does not appear. Each line can there therefore be parsed as an independent JSON object/array.

If the data should be stored in a separate file, the first line must provide an `external` object, describing the location of the data. The `metadata` object can be used to provide more details, such as a file format, if necessary. 

## Object definitions
Definitions:
* File/Dataset [object]
    * `version` [string]
    * `name` [string]
    * `metadata` [object] (optional)
    * `columns` [array[Column]]
    * `external` [ExternalReference] (optional)
* Column [object]
    * `name` [string]
    * `metadata` [object] (optional)
    * `type` [string]
    * `nullable` [bool] (optional, default=`true`)
    * `categories` [array[*]] (optional)
* ExternalReference
    * `location` [string]
    * `metadata` [object] (optional)

## Supporting extensibility
The `metadata` objects are provided at all levels to allow for extensibility. Organizations can include additional information inside these objects for their internal use. The order and type of attributes within `metadata` is undefined and are optional, unless controlled by another organization.

> Organizations should define and enforce which metadata is required. This is not enforced by this specification. It is the responsibility of each organization to ensure the compatibility of their attributes across versions, and their application.

## Rules
These are the rules governing each section, object, and attribute:

* File/Dataset:
    * The file must be encoded in UTF-8 only.
    * There must be a `version` attribute, which specifies which version of this format to use.
        * The `version` attribute must be set to `1.0.0`.
    * A `name` attribute is required, representing the name of the dataset.
        * The `name` must be a string.
        * The `name` cannot be blank (all whitespace).
        * The `name` is case-sensitive, so the names `a` and `A` are distinct.
        * The `name` can contain any valid UTF-8 characters.
    * A `metadata` attribute is optional.
        * The file `metadata` must be an object.
        * The file `metadata` object may be empty.
    * A `columns` attribute is required.
        * The `columns` attribute must be an array of objects, referred to as `Column` below.
        * The `columns` array cannot be empty.
        * The order columns appear in the array controls the order the data appears in the rows.
    * An `external` attribute is optional.
        * The `external` attribute must be an object, referred to as `ExternalReference` below.

* Column
    * A `name` attribute is required for each column.
        * The `name` must be a string.
        * The `name` cannot be blank (all whitespace).
        * The `name` must be unique within the dataset.
        * The `name` is case-sensitive, so the names `a` and `A` are distinct.
        * The `name` can contain any valid UTF-8 characters.
    * The column can optionally have a `metadata` attribute.
        * The `metadata` must be an object.
        * The `metadata` object may be empty.
    * The `type` attribute is required and must be one of the following values:
        * `string` - UTF-8 encoded text.
        * `i8` - An 8-bit signed integer value.
        * `i16` - A 16-bit signed integer value.
        * `i32` - A 32-bit signed integer value.
        * `i64` - A 64-bit signed integer value.
        * `int` - An arbitrary precision integer value. 
        * `u8` - An 8-bit unsigned integer value.
        * `u16` - A 16-bit unsigned integer value.
        * `u32` - A 32-bit unsigned integer value.
        * `u64` - A 64-bit unsigned integer value.
        * `f32` - A 32-bit [IEEE floating point number](https://en.wikipedia.org/wiki/IEEE_754).
        * `f64` - A 64-bit [IEEE floating point number](https://en.wikipedia.org/wiki/IEEE_754).
        * `decimal` - A arbitrary-precision numeric value.
        * `bool` - A Boolean value of `true` or `false`.
        * `localDate` - A ISO-8601 formatted date, with no time zone information.
        * `localTime` - An ISO-8601 formatted time, without the leading `T`, with no time zone information.
        * `localDateTime` - An ISO-8601 formatted date and time, with no time zone information.
        * `offsetTime` - An ISO-8601 formatted time, with a time zone offset.
        * `offsetDateTime` - An ISO-8601 formatted date and time, with a time zone offset.
        * `instant` - An ISO-8601 formatted date/time (ending in `Z`), representing an instant in time.
        * `year` - A valid 4-digit year.
        * `yearMonth` - A ISO-8601 formatted year/month.
        * `duration` - An ISO-8601 formatted duration (i.e., time span).
    * The `nullable` attribute is optional. 
        * If provided, the `nullable` attribute must be set to `true` or `false` (Boolean).
        * If not provided, the column defaults to being `nullable`.
    * The `categories` attribute is optional.
        * The column `categories` is an array of values.
        * If provided, `categories` cannot be empty.
        * The values within `categories` must be unique (case-sensitive).
        * `null` is not a valid category value - use `"nullable": true` for this.
        * The categories are ordered by appearance, if [ordered](https://en.wikipedia.org/wiki/Ordinal_data).
        * The category value type must match the column's `type`.
        * The row data must only contain values listed in `categories` for the column (or `null` if the column is nullable).

* External Reference (Optional)
    * The `location` attribute is required.
        * The `location` is a string representing relative path, using posix file system notation.
        * Paths must use Unix-style, so `/` must be used instead of `\`, and paths are case-sensitive.
        * Paths must only include characters that are valid across modern OS file systems. E.g., `0-9A-Za-z /.-_`
    * The `metadata` attribute is optional.
        * The `metadata` must be an object.
        * The `metadata` object may be empty.
    * If `external` is provided, no data rows can be provided in the file.

* Data (lines for each row in the dataset)
    * Each dataset row must be an array.
    * Each row in the dataset must have the same number of values as there are columns defined under `columns`.
    * The index or position of a value must correspond to the position of its column definition.
    * The type of the value must correspond to the `type` specified on the column, unless missing.
    * Missing values must be specified as `null`.
    * The floating point numeric values of `NaN`, `Inf`, and `-Inf` are illegal.
    * A value may only be `null` if the column is nullable.
    * If a column has a `category`, the row value must be present in the list of values (or be null if the column is nullable).
    * Data can only be provided if `external` is not provided.

> If a new version of this format is created at a later date, parsing libraries can use the `version` attribute to select the correct parser for that version.

> Each object in the metadata (first line), regardless of depth, has an optional `metadata` attribute. Any data provided in these `metadata` objects is optional, and can be used to provide additional information. For example, an organization may dictate that all datasets must provide the creation date, last modified date, the source system, etc. Validating metadata is not part of this specification and must be enforced by each organization.

> All the values in a column must be of the same type, corresponding with the `type` specified in the column definition. The `null` value can be any type and can appear in any column where `nullable` is either undefined or set to `true`. For IEEE-754 floating point numbers, `null` must be used instead of `NaN`.

## Efficient Parsing
This specification applies no limitations to the size of datasets. However, the limitations of computer hardware needs to be considered carefully. There are no requirements in this specification on how the JSON data should be formatted, beyond using JSON lines. Minimal whitespace is recommended to reduce the size of files.

> Using JSON lines, the resultant metadata ends up being on a single line of JSON. For large files (100MB+) manual editing is impractical and special tools will be needed.

JSON lines was chosen because finding the next newline in a file can be done easily in any mainstream programming language - efficiently. With normal JSON, either the entire file must be read into memory, which may be impactical for larger datasets, or the JSON must be read one token at a time in a streaming fashion, which is a significant challenge in any language. Furthermore, being able to serialize/deserialize between JSON and a predefined model without excessive memory usage was an important design tradeoff. The design of this specification makes it possible to load JSON datasets into memory using as little memory as possible while keeping coding simple.

See the following sections for more details about how the specification can reduce memory usage while processing files.

### Type metadata and storage optimization
The column `type` attribute can be a large variety of values. If the author of the dataset cannot provide more specific details, using `string` for textual data and `decimal` for numeric data is recommended. The `decimal` type implies no limitations on the precision or scale of the numeric data. It is up to the JSON processor to decide how best to interpret and represent this information.

Providing more specific type information allows JSON processors to store the dataset in memory (or database) more efficiently. For text, a maximum length (in characters or bytes) can be specified using the `metadata` section. For example, text with a maximum length of 10 characters can be given a type of `string`, and then in the `metadata` section given a `"length": 10`. Since computing the length of a column can be computational intensive when generating a dataset, and unnecessary for certain column types, this specification does not make it a required or built-in field.

For numeric values, the precision and scale can be specified using `metadata`, as well. For example, a number with 10 digits total with 5 digits after the decimal point can be defined as `decimal`, with `"precision": 10` and `"scale": 5` in the `metadata` object. Since the `metadata` objects are controlled by organizations, not this specification, these can be adjusted to fit your organizational needs.

While this specification doesn't limit the maximum length, precision, or scale, downstream JSON processors may choose to ignore limits they cannot support - this may result in truncation or a loss in precision. A JSON processor may also choose to reject such datasets.

A JSON processor may (and *should*) reject a dataset if the value in a row doesn't match the specified column type.

Modern computer hardware is memory efficient at storing contiguous blocks of primitive numeric values. The `i8`, `i16`, `i32`, and `i64` types are for storing signed integer values, with the corresponding number of bits. The `u8`, `u16`, `u32`, and `u64` types are for storing unsigned integer values. The types `f32` and `f64` are for storing IEEE-754 floating point numbers. Future versions of this specification may introduce support for extended precision numeric values. A JSON processor may choose to represent `decimal` values using IEEE-754, so some loss in precision may occur.

All temporal types must be stored in the dataset JSON using ISO-8601 format. If no time zone/offset information is provided, the type must be one of the "local" data types. For `instant`, the `Z` time zone suffix must be included. This is not the most compact storage format; however, this format avoids ambiguity, in terms of locality, and avoids defining an epoch. If space is a concern, a different representation may be used, again using `metadata` attributes to control the JSON processor. Also recall, a JSON processor can convert temporal values in the JSON to a more memory-efficient format, so the formatting has no impact on its memory utilization, just the size of the JSON file itself.

Use the `bool` type to represent `true` or `false`. The value can also be `null`, when `nullable` is `true` or unspecified, to indicate "unknown" or "unspecified". A JSON processor can choose whatever representation it wants to store boolean values.

JSON processors lacking support for a type may store values in another format.

#### Nullable
Software systems can often more efficiently represent text and numeric values if `null` (a.k.a, missing) is not possible. If provided, a JSON processor may reject a dataset if it inaccurately sets `nullable` to `false`. It is legal to specify a column is `nullable` (the default), even if no `null` values are present.

#### Categories
Many columns in a dataset are comprised of a limited number of values. Processors can avoid repeatedly storing the same values in memory if the full list of possible values is known up front. A JSON processor may reject a dataset if a row contains a value not listed in the categories. The JSON processor may (and *should*) reject a dataset if the type of a column and the categorical values are not the same.

> Future versions of this specification may add support for categorizing numbers within ranges; however, this is not yet included in this specification.

> NOTE: The row data must contain the category values. An alternative would have been to simply store the category index instead. JSON processors can represent categorical data any way they want, but in the JSON the full values must be provided.

### External Data with `external`
Rather than using subsequent lines for each row, a dataset can specify that its data is located externally, in a separate file using `external`. Since an external dataset can be of any type, the JSON producer and processor must agree on what external formats are supported. For now, there are limited details around what must be contained in the `location` string. The expectation is that it is a file path, relative to the current file. The format/contents of the data file are not currently specified either.

This specification is purposefully vague on details regarding using external files, as it might be advantageous to store data in other formats, such as [Parquet](https://parquet.apache.org/), [SQLite](https://www.sqlite.org/index.html), Excel, CSV, etc. Organizations extending this specification can refine how `external` should be used. The `metadata` section can be used to control a JSON processor's interpretation of an external data file.

## Converting SAS XPORT to JSON lines in Python
In Python, writing data rows to separate lines leads to faster conversions between SAS XPORT V5 and JSON. Python seems to lack good libraries for exporting JSON incrementally. This results in building entire objects in memory prior to calling `json.dump`, which leads to allocating Python objects from numpy arrays. This overhead could be avoided by building the JSON manually in combination with calls to `json.dumps`, but building JSON from scratch seems like a waste of time (reinventing the wheel).

There is an [open issue](https://github.com/pandas-dev/pandas/issues/56304) on the pandas GitHub discussing extending the `to_json` method(s) to improve the performance of exporting JSON, as there is overhead in iterating over each individual row.