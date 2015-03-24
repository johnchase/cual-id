#!/usr/bin/env python
# File created on 14 Jun 2013
from __future__ import division

from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import pandas as pd
import numpy as np


def get_ids(input_fh):

    id_df = pd.read_csv(input_fh)
    id_list = id_df.ix[:, 0]

    return list(id_list)


def get_x_y_coordinates(columns, rows, x_start, y_start):

    x_coords = np.arange(x_start, (columns*2.2), 2.2)
    y_coords = np.arange(y_start, (y_start - (rows*1.21)), -1.21)

    xy_coords = []
    for x_coord in x_coords:
        for y_coord in y_coords:
            xy_coords.append((x_coord*inch, y_coord*inch))

    return xy_coords


def get_barcodes(input_fh,
                 output_fp,
                 columns=4,
                 rows=9,
                 x_start=0,
                 y_start=10):
    sample_ids = get_ids(input_fh)

    barcode_canvas = canvas.Canvas(output_fp, pagesize=letter)

    xy_coords = get_x_y_coordinates(columns, rows, x_start, y_start)

    c = 0
    for sample_id in sample_ids:
        x = xy_coords[c][0]
        y = xy_coords[c][1]
        barcode = code128.Code128(sample_id, barWidth=0.009*inch,
                                  barHeight=0.4*inch)

        barcode.drawOn(barcode_canvas, x, y)
        barcode_canvas.setFont("Helvetica", 8)
        barcode_canvas.drawString((x + .47 * inch), (y - .15 * inch),
                                  sample_id)
        if c < ((rows*columns) - 1):
            c += 1
        else:
            c = 0
            barcode_canvas.showPage()
    barcode_canvas.save()
