Barcode-pdf-generator
====================

[![BuildStatus](https://travis-ci.org/johnchase/Barcode-pdf-generator.svg?branch=master)](https://travis-ci.org/johnchase/Barcode-pdf-generator)
[![Coverage Status](https://coveralls.io/repos/johnchase/Barcode-pdf-generator/badge.svg)](https://coveralls.io/r/johnchase/Barcode-pdf-generator)

Barcode Generator is a tool to generate pdfs with barcodes. These will likely be used for sticker sheets. Currently the only sticker sheet format supported is a 4 by 9 sheet.

To use Barcode-pdf-generator first clone this repository then run:

        pip install -e .

In order create a pdf of barcodes for a list of sample IDs from a tab separated text file:

        BC-generator foo_map.txt bar.pdf
