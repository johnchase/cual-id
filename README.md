Barcode-pdf-generator
====================

[![BuildStatus](https://travis-ci.org/johnchase/Cual-ID.svg?branch=master)](https://travis-ci.org/johnchase/Cual-ID)
[![Coverage Status](https://coveralls.io/repos/johnchase/Barcode-pdf-generator/badge.svg)](https://coveralls.io/r/johnchase/Barcode-pdf-generator)

Barcode Generator is a tool to generate pdfs with barcodes. Currently the only barcode format supported is [Code 128](http://en.wikipedia.org/wiki/Code_128). The barcodes generated will likely be used for label sheets. Currently the only sticker sheet format supported is a 4 by 9 sheet such as Electronic Imaging Materials&copy; #80402 label sheets.

To use Barcode-pdf-generator first clone this repository then run:

        pip install -e .
Check the install and get script information:

        BC-generator --help

In order create a pdf of barcodes for a list of sample IDs from a tab separated text file:

        BC-generator foo_map.txt bar.pdf

When printing PDFs make sure to check `Actual Size` in the print dialog box.
