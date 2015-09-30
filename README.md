# cual-id

[![BuildStatus](https://travis-ci.org/johnchase/cual-id.svg?branch=master)](https://travis-ci.org/johnchase/cual-id)
[![Coverage Status](https://coveralls.io/repos/johnchase/cual-id/badge.svg?branch=master&service=github)](https://coveralls.io/github/johnchase/cual-id?branch=master)

## Install
```bash
pip install cual-id
```

## Usage

### Getting help

```bash
cual-id --help
```

### Creating a list of IDs
```bash
cual-id create ids 42 # writes 42 ids to stdout
cual-id create ids 42 > my-ids.txt # writes 42 ids to my-ids.txt
cual-id create ids 42 --prefix my-study- # prefix ids with "my-study-"
```

### Creating a PDF of ID labels

If you need to label sample containers with stickers, you can create a printable PDF for those stickers. Currently the only sticker sheet format supported is a 4 by 9 sheet. We designed this printout for [Electronic Imaging Materials #80402 label sheets](http://barcode-labels.com/?s=80402&submit=Search). When printing PDFs make sure to check `Actual Size` in the print dialog box.

```bash
cual-id create labels my-ids.txt --output-pdf my-labels.pdf
cual-id create labels my-ids.txt --output-pdf my-labels.pdf --suppress-ids # don't print the ids, only the barcodes
cual-id create labels my-ids.txt --output-pdf my-labels.pdf --barcode none # don't print barcodes, just the ids
```

### Correcting a list of ids

```bash
cual-id fix examples/modified-ids.txt --correct-ids examples/ids.txt # report fixed, unfixable and duplicates, the default
cual-id fix examples/modified-ids.txt --correct-ids examples/ids.txt --show FN # report only fixed and unfixable IDs
```

#### Result code definitions
* D: duplicate
* F: fixed
* N: not fixable
* V: valid (didn't need correction)

#### Output Format

```
input-id <tab> output-id <tab> result-codes
```

For example:
```
greg.5UXY8WYRSAH8W	greg.5UXY8WYRSAH8W	V
greg.6GZ0BWVBVWBDA	greg.6GZ0BWVBVWBDA	D
greg.6GZ0BVBVWBDA	greg.6GZ0BWVBVWBDA	DF
```

## Python API

```python
from cualid import create_ids
create_ids(10) # Creates a list of tuples containing a UUID and a cualid
```
