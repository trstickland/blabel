#!/usr/bin/env python3

from blabel import LabelWriter

label_writer = LabelWriter("item_template.html",
                           default_stylesheets=("style.css",))
records= [
    dict(sample_id="0123456789_1", sample_name="Sample 1"),
    dict(sample_id="0123456789_2", sample_name="Sample 2")
]

label_writer.write_labels(records, target='barcode_and_label.pdf')
