#!/usr/bin/env python
# File created on 14 Jun 2013
from __future__ import division

from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def get_x_y_coordinates(columns, rows, x_start, y_start):
    x = 51.6
    y = -28.42
    for column in range(columns):
        for row in range(rows):
            x_coord = x_start + (x*column)
            y_coord = y_start + (y*row)
            yield (x_coord*mm, y_coord*mm)


def get_barcodes(input,
                 output_fp,
                 suppress_ids,
                 barcode_type='128',
                 columns=4,
                 rows=9,
                 x_start=1.9,
                 y_start=257.2):

    ids = [e.strip().split('\t')[1] for e in input]
    barcode_canvas = canvas.Canvas(output_fp)
    xy_coords = list(get_x_y_coordinates(columns, rows, x_start, y_start))

    c = 0
    for id_ in ids:
        x = xy_coords[c][0]
        y = xy_coords[c][1]

        # If we ever add new barcodes this should query a dictionary of
        # different barcode generators
        if barcode_type == 'none':
            pass
        else:
            barcode = code128.Code128(id_, barWidth=0.19*mm,
                                      barHeight=11*mm)

            barcode.drawOn(barcode_canvas, x, y)
            barcode_canvas.setFont("Helvetica", 8)

        if suppress_ids:
            barcode_canvas.drawString((x + 12 * mm), (y - 4 * mm), '')
        else:
            barcode_canvas.drawString((x + 12 * mm), (y - 4 * mm), id_)

        if c < ((rows*columns) - 1):
            c += 1
        else:
            c = 0
            barcode_canvas.showPage()
    return barcode_canvas
