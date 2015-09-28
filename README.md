# cual-id

[![BuildStatus](https://travis-ci.org/johnchase/Cual-ID.svg?branch=master)](https://travis-ci.org/johnchase/Cual-ID)
[![Coverage Status](https://coveralls.io/repos/johnchase/Cual-ID/badge.svg)](https://coveralls.io/r/johnchase/Cual-ID)

## Install

## Usage

### Getting help

```bash
cual-id --help
```

### Creating a list of IDs
```bash
cual-id create ids 42 # writes 42 ids to stdout
cual-id create ids 42 > my-samples.txt # writes 42 ids to my-samples.txt
cual-id create ids 42 --prefix 'my-study-' # prefix ids with "my-study-"
```

### Creating a PDF of ID labels

If you need to label sample containers with stickers, you can create a printable PDF for those stickers. Currently the only sticker sheet format supported is a 4 by 9 sheet. We designed this printout for [Electronic Imaging Materials #80402 label sheets](http://barcode-labels.com/?s=80402&submit=Search). When printing PDFs make sure to check `Actual Size` in the print dialog box.

```bash
cual-id create labels my-samples.txt --output-pdf my-labels.pdf
cual-id create labels my-samples.txt --output-pdf my-labels.pdf --suppress-ids
cual-id create labels my-samples.txt --output-pdf my-labels.pdf --barcode none # don't print barcodes, just the ids
cual-id create labels my-samples.txt --output-pdf my-labels.pdf --barcode 128 # the default
cual-id create labels my-samples.txt --output-pdf my-labels.pdf --suppress-ids --barcode none # fails b/c there is nothing to print
```

### Correcting a list of ids

```bash
cual-id fix ids-to-be-corrected --correct-ids my-samples.txt --show DFN # report corrected, uncorrectable and duplicates, the default
cual-id fix ids-to-be-corrected --correct-ids my-samples.txt --all #
```

#### Result code definitions
* D: duplicate
* F: fixed
* N: not fixable
* V: valid (didn't need correction)

#### Output

```
input-id <tab> output-id <tab> result-codes
```

For example:
```
greg.5UXY8WYRSAH8W	greg.5UXY8WYRSAH8W	V
greg.6GZ0BWVBVWBDA	greg.6GZ0BWVBVWBDA	D
greg.6GZ0BVBVWBDA	greg.6GZ0BWVBVWBDA	DF
```

## Paper discussion notes

IDs are something that humans should never see, but unfortunately they do, and even more unfortunately they're often manually entered by several different people some times.

Variables: base of characters, length of ids, how often can we tolerate a duplicate
* minimize ambiguity for correctibility
* minimize length of ids (can we get these to 6 or 8)
* maximize the number of ids we can have (size of the sample space)
* maximize uniqueness across studies

Ultimately we should probably be using a more sane approach for managing sample metadata. We hope that the ids that are generated with this system are a step in that direction that is compatible with what people are doing now, and that these ids would ultimately be compatible with better systems (e.g., as primary keys in a relational database).


## Old text...

**This repository is being very actively developed so things may not work as planned in every instance.**

``cual-id`` is a tool to generate pdfs with barcodes. Currently the only barcode format supported is [Code 128](http://en.wikipedia.org/wiki/Code_128). The barcodes generated will likely be used for label sheets. Currently the only sticker sheet format supported is a 4 by 9 sheet such as Electronic Imaging Materials&copy; #80402 label sheets.

## Install

To use Barcode-pdf-generator first clone this repository then run:

        pip install -e .
Check the install and get script information:

        BC-generator --help

In order create a pdf of barcodes for a list of sample IDs from a tab separated text file:

        BC-generator foo_map.txt bar.pdf
