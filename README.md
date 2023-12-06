# SAS Dataset Converter
This is a sample project for converting SAS XPORT V5+ and SAS7BDAT file formats to a JSON format. This is not the CDISC Dataset-JSON format, but an independent research project with similar goals. 

The big difference is this JSON format does not imply any ties to a particular platform or industry, such CDISC libraries or the clinical industry. Instead, this is a format that can be used by any organization interested in defining a schema and transferring data. This proposal also doesn't enforce that the dataset data be transferred in JSON, as this format doesn't scale beyond a few hundred megabytes, and includes features that would allow organizations to transfer and send data in other formats, such as [SQLite files](https://www.sqlite.org/index.html), [Apache Avro](https://avro.apache.org/), [Google Protobuf](https://protobuf.dev/overview/), [JSON Lines](https://jsonlines.org/) etc.

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

In particular, the `-t` or `--threads` parameter can be used to control how many threads/processes are used to convert the datasets. By default, only a single thread is used.

## Proposal
This proposal discusses an extensible JSON-based specification for the representation of tabular data and its metadata. 

Here is a quick, full example of a proposed dataset format:

```json
{
    "version": "1.0.0",
    "metadata": {
        "creationDateTime": "2023-12-01T12:32:31.184200",
        "modificationDateTime": "2023-12-01T12:32:31.184200"
    },
    "datasets": [
        {
            "name": "AE",
            "metadata": {
                "creationDateTime": "2021-01-04T11:18:56",
                "modificationDateTime": "2021-01-04T11:18:56",
                "label": "Adverse Events",
                "recordCount": 16
            },
            "columns": [
                {
                    "name": "STUDYID",
                    "metadata": {
                        "label": "Study Identifier"
                    },
                    "type": "string(7)",
                    "nullable": false
                },
                {
                    "name": "DOMAIN",
                    "metadata": {
                        "label": "Domain Abbreviation"
                    },
                    "type": "string(2)",
                    "nullable": false
                },
                {
                    "name": "USUBJID",
                    "metadata": {
                        "label": "Unique Subject Identifier"
                    },
                    "type": "string(14)",
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
                        "label": "Sponsor-Defined Identifier"
                    },
                    "type": "string(4)",
                    "nullable": false
                },
                {
                    "name": "AETERM",
                    "metadata": {
                        "label": "Reported Term for the Adverse Event"
                    },
                    "type": "string(25)",
                    "nullable": false
                },
                {
                    "name": "AEMODIFY",
                    "metadata": {
                        "label": "Modified Reported Term"
                    },
                    "type": "string(9)",
                    "nullable": true
                },
                {
                    "name": "AEDECOD",
                    "metadata": {
                        "label": "Dictionary-Derived Term"
                    },
                    "type": "string(18)",
                    "nullable": false
                },
                {
                    "name": "AEBODSYS",
                    "metadata": {
                        "label": "Body System or Organ Class"
                    },
                    "type": "string(52)",
                    "nullable": false
                },
                {
                    "name": "AESEV",
                    "metadata": {
                        "label": "Severity/Intensity"
                    },
                    "type": "string(8)",
                    "nullable": false
                },
                {
                    "name": "AESER",
                    "metadata": {
                        "label": "Serious Event"
                    },
                    "type": "string(1)",
                    "nullable": false
                },
                {
                    "name": "AEACN",
                    "metadata": {
                        "label": "Action Taken with Study Treatment"
                    },
                    "type": "string(30)",
                    "nullable": false
                },
                {
                    "name": "AEREL",
                    "metadata": {
                        "label": "Causality"
                    },
                    "type": "string(16)",
                    "nullable": false
                },
                {
                    "name": "AESTDTC",
                    "metadata": {
                        "label": "Start Date/Time of Adverse Event"
                    },
                    "type": "string(10)",
                    "nullable": false
                },
                {
                    "name": "AEENDTC",
                    "metadata": {
                        "label": "End Date/Time of Adverse Event"
                    },
                    "type": "string(10)",
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
                        "label": "End Relative to Reference Period"
                    },
                    "type": "string(5)",
                    "nullable": true
                }
            ],
            "rows": [
                ["CDISC01", "AE", "CDISC01.100008", 1.0, "1", "AGITATED", "AGITATION", "Agitation", "Psychiatric disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05", null, 3.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.100008", 2.0, "2", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "MODERATE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05-13", null, 15.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.100008", 3.0, "3", "DECREASED APPETITE", null, "Decreased appetite", "Metabolism and nutrition disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-08-19", "2003-09-15", 113.0, 140.0, null], 
                [ "CDISC01", "AE", "CDISC01.100014", 1.0, "1", "DIARRHEA", null, "Diarrhoea", "Gastrointestinal disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.100014", 2.0, "2", "HEMORRHOIDS", null, "Haemorrhoids", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.100014", 3.0, "3", "HEADACHE", null, "Headache", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-27", null, 105.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.100014", 4.0, "4", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "MODERATE", "N", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-03", "2004-02-03", 112.0, 112.0, null], 
                [ "CDISC01", "AE", "CDISC01.100014", 5.0, "5", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "SEVERE", "Y", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-04", "2004-02-09", 113.0, 118.0, null], 
                [ "CDISC01", "AE", "CDISC01.200001", 1.0, "1", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null], 
                [ "CDISC01", "AE", "CDISC01.200001", 2.0, "5", "LEFT KNEE PAIN WORSENING", null, "Arthralgia", "Musculoskeletal and connective tissue disorders", "SEVERE", "N", "DRUG WITHDRAWN", "NOT RELATED", "2004-02-02", null, 126.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.200001", 3.0, "3", "CONSTIPATION", null, "Constipation", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2003-12-25", null, 87.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.200001", 4.0, "4", "TIREDNESS", null, "Fatigue", "General disorders and administration site conditions", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-12-25", null, 87.0, null, "AFTER"], 
                [ "CDISC01", "AE", "CDISC01.200001", 5.0, "2", "NAUSEA INTERMITTENT", null, "Nausea", "Gastrointestinal disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null], 
                [ "CDISC01", "AE", "CDISC01.200002", 1.0, "3", "LIGHTHEADEDNESS", null, "Dizziness", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-02-26", "2004-02-26", 140.0, 140.0, null], 
                [ "CDISC01", "AE", "CDISC01.200002", 2.0, "1", "MUSCLE SPASMS", null, "Muscle spasms", "Musculoskeletal and connective tissue disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER" ], 
                ["CDISC01", "AE", "CDISC01.200002", 3.0, "2", "PALPITATIONS INTERMITTENT", null, "Palpitations", "Cardiac disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER"]
            ]
        }
    ]
}
```

## Object definitions

Definitions:
* File [object]
    * `version` [string]
    * `metadata` [object] (optional)
    * `datasets` [array[Dataset]]
* Dataset [object]
    * `name` [string]
    * `metadata` [object] (optional)
    * `columns` [array[Column]]
    * `external` [ExternalReference]
    * `rows` [array[array[*]]] (optional)
* Column [object]
    * `name` [string]
    * `metadata` [object] (optional)
    * `type` [string]
    * `nullable` [bool] (default=`true`)
    * `categories` [array[*]] (optional)
* ExternalReference
    * `location` [string]
    * `metadata` [object] (optional)

> The order attributes appear in a JSON document is non-deterministic according to the [JSON specification](https://www.json.org/json-en.html), where it states an object is comprised of *unordered* key/value pairs. However, for performance reasons, implementations of this specification may reject a dataset whose attributes do not match the order specified below, except within `metadata` objects where the order *must not* be enforced. This specification is knowingly non-compliant with the JSON specification.

## Supporting extensibility
The `metadata` objects are provided to allow for extensibility. Organizations can include additional information inside these objects for their internal use. The order of attributes within `metadata` is undefined and are optional, unless controlled by the organization.

> Organizations should define and enforce which metadata is required. This is not enforced by this specification. It is the responsibility of each organization to ensure the compatibility of their attributes across versions, and their application.

## Rules
These are the rules governing each section, object, and attribute:
* The top-evel object contains information about the file itself.
* The file must be encoded in UTF-8 only.
* The first attribute *must be* `version`, which specifies which version of this format to use.
* The `version` attribute must be set to `1.0.0`.

> If a new version of this format is created at a later date, parsing libraries can use this `version` attribute to select the correct parser for that version.

* The next, optional attribute is `metadata`.
* The file `metadata` must be an object.
* The file `metadata` object may be empty.

> Each object in the document, regardless of depth, has an optional `metadata` attribute. Any data provided in these `metadata` objects is optional, and can be used to provide additional information. For example, an organization may dictate that all datasets must provide the creation date, last modified date, the source system, etc. Validating metadata is not part of this specification and must be enforced by each organization.

* The next, required attribute is `datasets`.
* `datasets` is an array of objects, referred to as "dataset" below.
* The `datasets` array may be empty.
* A dataset is required to have a `name` attribute as its first attribute.
* The dataset `name` must be a string.
* The dataset `name` cannot be blank (all whitespace).
* Each dataset should have a unique `name`, even if stored across separate files.
* The `name` of a dataset is case-sensitive, so the names `a` and `A` are distinct.
* The dataset `name` can contain any valid UTF-8 characters.
* A dataset can optionally have a `metadata` attribute.
* The dataset `metadata` must be an object.
* The dataset `metadata` object may be empty.
* The next, required dataset attribute is `columns`.
* `columns` must be an array of objects, referred to as "column" below.
* The `columns` array cannot be empty.
* The order columns appear in the array controls the order the data appears in the rows.
* Each column object must first have a `name` attribute.
* The column `name` must be a string.
* The column `name` cannot be blank (all whitespace).
* The column `name` must be unique within the dataset.
* The column `name` is case-sensitive, so the names `a` and `A` are distinct.
* The column `name` can contain any valid UTF-8 characters.
* The column can optionally have a `metadata` attribute.
* The column `metadata` must be an object.
* The column `metadata` object may be empty.
* The next, required column attribute is `type`.
* The `type` must be one of the following values:
    * `string` - UTF-8 encoded text.
    * `string(L)` - UTF-8 encoded text, with a maximum length in characters, where L is the length.
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
    * `decimal(P, S)` - A fixed-precision numeric value where P is the precision and S is the scale.
    * `bool` - A Boolean value of `true` or `false`.
    * `localDate` - A ISO-8601 formatted date, with no time zone information.
    * `localTime` - An ISO-8601 formatted time, without the leading `T`, with no time zone information.
    * `localDateTime` - An ISO-8601 formatted date and time, with no time zone information.
    * `utcTime` - An ISO-8601 formatted time, at the UTC time zone, with the 'Z' suffix.
    * `utcDateTime` - An ISO-8601 formatted date and time, at the UTC time zone, with the `Z` suffix.
    * `offsetTime` - An ISO-8601 formatted time, with a time zone offset.
    * `offsetDateTime` - An ISO-8601 formatted date and time, with a time zone offset.
    * `year` - A valid 4-digit year.
    * `yearMonth` - A ISO-8601 formatted year/month.
    * `duration` - An ISO-8601 formatted duration (i.e., time span).
* The column can optionally have a `nullable` attribute next. 
* If provided, the `nullable` attribute must be set to `true` or `false`.
* If not provided, the column defaults to being `nullable`.
* The column can optionally have a `categories` attribute next.
* The column `categories` is an array of values.
* If provided, `categories` cannot be empty.
* The values within `categories` must be unique (case-sensitive).
* `null` is not a valid category value.
* The categories are ordered by appearance, if [ordered](https://en.wikipedia.org/wiki/Ordinal_data).
* The category value type must match the column's `type`.
* The row data must only contain values listed in `categories`, or be `null`, for the column.
* The next dataset attribute is `external`.
* If `external` is provided, it must be an object.
* The first `external` attribute is `location`, which is required.
* The `location` is a string representing relative path, using posix file system notation.
    * Paths must use Unix-style, so `/` must be used instead of `\`, and paths are case-sensitive.
    * Paths must only include characters that are valid across modern OS file systems. E.g., `0-9A-Za-z /.-_`
* The next dataset attribute is `rows`.
* The dataset `rows` attribute must be an array.
* The dataset `rows` array will contain an array for each row in the dataset.
* The dataset `rows` array may be empty.
* Each row in the dataset must have the same number of values as there are columns defined under `columns`.
* The index or position of a value must correspond to the position of its column definition.
* The type of the value must correspond to the `type` specified on the column, unless missing.
* Missing values must be specified as `null`.
* The floating point numeric values of `NaN`, `Inf`, and `-Inf` are illegal. Use `null` to represent `NaN`.
* Exactly one of `external` or `rows` must appear - one or the other, not both.

> All the values in a column must be of the same type, corresponding with the `type` specified in the column definition. The `null` value can be any type and can appear in any column where `nullable` is either undefined or set to `true`. For IEEE-754 floating point numbers, `null` must be used instead of `NaN`.

## Efficient Parsing
This specification applies no limitations to the size of datasets. However, the limitations of computer hardware needs to be considered carefully. There are no requirements in this specification on how the JSON data should be formatted. However, in practice, when converting a 500MB SAS XPORT V5 file to JSON, the resultant JSON files were larger. If unformatted JSON was produced (i.e., no excess whitespace), the file size was approximately 1GB (nearly doubling in size). When formatting was applied, the JSON file was >3GB in size (a more than a 6 time size increase). Little benefit was gained using BSON (a binary representation of JSON).

When no formatting is applied, the resultant JSON ends up being on a single line. Most modern text editors have difficulty opening and viewing large, single-line files. When formatting *is* applied, text editors are slightly more responsive; however, they still struggle when editing. Due to indentation, a significant portion of the file size of formatted JSON is for whitespace characters (i.e., spaces, tabs, and newlines). The conclusion, therefore, is that for large files (100MB+) manual editing is impractical and special tools will be needed.

Loading large datasets into memory is also challenging. Most programming environments support reading JSON files iteratively; however, the complexity of that code is much greater. Environments that perform analysis often need to load the entire dataset into memory anyway, unless extra effort is made to break datasets into smaller batches. The design of this specification makes it possible to load JSON datasets into memory using as little memory as possible. See the following sections for more details.

### Types
The column `type` attribute can be a large variety of values. If the author of the dataset cannot provide more specific details, using `string` for textual data and `decimal` for numeric data is recommended. The `decimal` type implies no limitations on the precision or scale of the numeric data. It is up to the JSON processor to decide how best to interpret and represent this information.

Providing more specific type information allows JSON processors to store the dataset in memory (or database) more efficiently. For text, a maximum length (in characters, not bytes) can be specified. For example, text with a maximum length of 10 characters can be given a type of `string(10)`.

> No whitespace around the parentheses is permitted. No grouping separators are permitted within the number. For example `string (1,000 )` is illegal and must instead be `string(1000)`.

For numeric values, the precision and scale can be specified. For example, a number with 10 digits total with 5 digits after the decimal point can be defined as `decimal(10, 5)`. 

> No whitespace around the parenthesis is permitted. A *single* space may appear after the comma, but is optional. The scale must be provided, even if `0`.

While this specification doesn't limit the maximum length, precision, or scale, downstream JSON processors may choose to ignore limits they cannot support - this may result in truncation or a loss in precision.

A JSON processor may (and *should*) reject a dataset if the value in a row doesn't match the specified column type.

Modern computer hardware is memory efficient at storing contiguous blocks of primitive numeric values. The `i8`, `i16`, `i32`, and `i64` types are for storing signed integer values, with the corresponding number of bits. The `u8`, `u16`, `u32`, and `u64` types are for storing unsigned integer values. The types `f32` and `f64` are for storing IEEE-754 floating point numbers. Future versions of this specification may introduce support for extended precision numeric values. A JSON processor may choose to represent `decimal` values using IEEE-754, so some loss in precision may occur.

All temporal types must be stored in the dataset JSON using ISO-8601 format. If no time zone/offset information is provided, the type must be "local". For UTC date/times, the `Z` time zone suffix must be included. This is not the most compact storage format; however, this format avoids ambiguity, in terms of locality, and avoids defining an epoch. A JSON processor can store temporal values in a more memory-efficient format, so the formatting has no impact on its memory utilization.

Use the `bool` type to represent `true` or `false`. The value can also be `null`, when `nullable` is `true` or unspecified, to indicate "unknown" or "unspecified". A JSON processor can choose whatever representation it wants to store boolean values.

JSON processors lacking supporting for a type may store values in another format.

### Nullable
Software systems can often more efficiently represent text and numeric values if `null` (a.k.a, missing) is not possible. If provided, a JSON processor may reject a dataset if it inaccurately sets `nullable` to `false`. It is legal to specify a column is `nullable` (the default), even if no `null` values are present.

### Categories
Many columns in a dataset are comprised of a limited number of values. Processors can avoid repeatedly storing the same values in memory if the full list of possible values is known up front. A JSON processor may reject a dataset if a row contains a value not listed in the categories. The JSON processor may (and *should*) reject a dataset if the type of a column and the categorical values are not the same.

> Future versions of this specification may add support for categorizing numbers within ranges; however, this is not yet included in this specification.

> NOTE: The row data must contain the category values. An alternative would have been to simply store the category index instead. JSON processors can represent categorical data any way they want, but in the JSON the full values must be provided.

### External Data with `reference`
Rather than using `rows`, a dataset can specify that its data is located externally, in a separate file using `reference`. For now, there are limited details around what must be contained in the `reference` string. The expectation is that it is a file path, relative to the current file. The contents of the data file are not specified either.

In practice, the referenced data will be stored in a [JSON lines](https://jsonlines.org/) document, where each line in the file corresponds to a row. In which case, it's as if the contents of `rows` were moved into a separate file, without the need of comma separators. For example:

```json
["CDISC01", "AE", "CDISC01.100008", 1.0, "1", "AGITATED", "AGITATION", "Agitation", "Psychiatric disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05", null, 3.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.100008", 2.0, "2", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "MODERATE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-05-13", null, 15.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.100008", 3.0, "3", "DECREASED APPETITE", null, "Decreased appetite", "Metabolism and nutrition disorders", "MILD", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-08-19", "2003-09-15", 113.0, 140.0, null]
["CDISC01", "AE", "CDISC01.100014", 1.0, "1", "DIARRHEA", null, "Diarrhoea", "Gastrointestinal disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.100014", 2.0, "2", "HEMORRHOIDS", null, "Haemorrhoids", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-06", null, 84.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.100014", 3.0, "3", "HEADACHE", null, "Headache", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-27", null, 105.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.100014", 4.0, "4", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "MODERATE", "N", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-03", "2004-02-03", 112.0, 112.0, null]
["CDISC01", "AE", "CDISC01.100014", 5.0, "5", "VOMIT", "VOMITING", "Vomiting", "Gastrointestinal disorders", "SEVERE", "Y", "DRUG INTERRUPTED", "POSSIBLY RELATED", "2004-02-04", "2004-02-09", 113.0, 118.0, null]
["CDISC01", "AE", "CDISC01.200001", 1.0, "1", "ANXIETY", null, "Anxiety", "Psychiatric disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null]
["CDISC01", "AE", "CDISC01.200001", 2.0, "5", "LEFT KNEE PAIN WORSENING", null, "Arthralgia", "Musculoskeletal and connective tissue disorders", "SEVERE", "N", "DRUG WITHDRAWN", "NOT RELATED", "2004-02-02", null, 126.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.200001", 3.0, "3", "CONSTIPATION", null, "Constipation", "Gastrointestinal disorders", "MODERATE", "N", "DOSE NOT CHANGED", "NOT RELATED", "2003-12-25", null, 87.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.200001", 4.0, "4", "TIREDNESS", null, "Fatigue", "General disorders and administration site conditions", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-12-25", null, 87.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.200001", 5.0, "2", "NAUSEA INTERMITTENT", null, "Nausea", "Gastrointestinal disorders", "SEVERE", "N", "DOSE NOT CHANGED", "POSSIBLY RELATED", "2003-10-16", "2003-10-20", 17.0, 21.0, null]
["CDISC01", "AE", "CDISC01.200002", 1.0, "3", "LIGHTHEADEDNESS", null, "Dizziness", "Nervous system disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-02-26", "2004-02-26", 140.0, 140.0, null]
["CDISC01", "AE", "CDISC01.200002", 2.0, "1", "MUSCLE SPASMS", null, "Muscle spasms", "Musculoskeletal and connective tissue disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER"]
["CDISC01", "AE", "CDISC01.200002", 3.0, "2", "PALPITATIONS INTERMITTENT", null, "Palpitations", "Cardiac disorders", "MILD", "N", "DOSE NOT CHANGED", "NOT RELATED", "2004-01-05", null, 88.0, null, "AFTER"]
```

In experiments, using JSON lines reduces the overall size of the JSON documents, slightly. When the same data is serialized to formatted JSON using `rows`, the leading whitespace for each row, for indentation, consumes 16 bytes when using 4-space indentation. This overhead can be minimized by reducing the number of spaces used for indentation, to as little as 4-bytes per record (plus one byte for the trailing comma), while still formatting.

In Python, writing data to a separate file also leads to faster conversions between SAS XPORT V5 and JSON. Python seems to lack good libraries for exporting JSON incrementally. This results in building the entire object in memory prior to calling `json.dump`, which leads to allocating Python objects from numpy arrays. This overhead could be avoided by building the JSON manually in combination with calls to `json.dumps`.

The major advantage to using a separate file is that humans can still read and edit metadata in reasonably-sized files, while the data can be reserved primarily for machine consumption. This specification is purposefully vague on details regarding the external file, as it might be advantageous to store data in other formats, such as [Parquet](https://parquet.apache.org/), [SQLite](https://www.sqlite.org/index.html), Excel, CSV, etc. Organizations extending this specification can refine how `external` should be used.