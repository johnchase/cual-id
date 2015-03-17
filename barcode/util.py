#!/usr/bin/env python
# File created on 14 Jun 2013
from __future__ import division

from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import os
from sys import exit
from os.path import exists

def get_ids(input_fp, comment, sep, column):

    id_df = pd.read_csv(fh, sep=sep, comment=comment)
    if column:
        id_list = id_df[column]
    else:
        id_list = id_df.ix[:,0]

    return id_list



def get_barcodes(input_fp, output_fp, comment, sep, column, columns=4, rows=9):

    barcode_canvas = canvas.Canvas(output_fp, pagesize=letter)

    #x coordinates
    x_coords = []
    x_start = 0.0
    for i in range(columns):
        x_coords.append(round(x_start, 4))
        x_start += 2.2

    #y coordinates
    y_coords = []
    y_start = 10
    for i in range(rows):
        y_coords.append(round(y_start, 4))
        y_start -= 1.21

    xy_coords = []
    for x_coord in x_coords:
        for y_coord in y_coords:
            xy_coords.append((x_coord*inch , y_coord*inch))
    c = 0
    for record in in_table:
        new_record = record[:]
        sample_id = new_record[0]
        x = xy_coords[c][0]
        y = xy_coords[c][1]
        # Create the barcodes and sample_id text and draw them on the canvas
        barcode = code128.Code128(sample_id, barWidth=0.009*inch, barHeight=0.4*inch)
        barcode.drawOn(barcode_canvas, x, y)
        #the offset for the text will change automatically as x and y coordinates are
        #changed therefore the the following values do not need to be changed.
        barcode_canvas.drawString((x + .47 * inch), (y - .15 * inch), sample_id)
        if c < ((rows*columns) - 1):
            c += 1
        else:
            c = 0
            barcode_canvas.showPage()
    barcode_canvas.save()
