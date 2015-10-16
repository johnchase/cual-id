=======
cual-id
=======
|Build Status| |Coverage Status|

cual-id paper
=============
Preprint outlining implications and uses of cual-id.
`cual-id globally unique, correctable, and human-friendly sample identifiers for comparative
-omics studies <https://peerj.com/preprints/1431/>`__.

Peer review is currently in progress


Install
=======
cual-id may be installed either with conda or pip.

.. code:: bash

    conda install -c https://conda.anaconda.org/johnchase cual-id


or

.. code:: bash

    pip install cual-id


Usage
=====

Getting help
------------

.. code:: bash

   cual-id --help


Creating a list of IDs
----------------------

.. code:: bash

   cual-id create ids 42 # writes 42 ids to stdout
   cual-id create ids 42 > my-ids.txt # writes 42 ids to my-ids.txt



Creating a PDF of ID labels
---------------------------

If you need to label sample containers with stickers, you can create a
printable PDF for those stickers. Currently the only sticker sheet format
supported is a 4 by 9 sheet. We designed this printout for
`Electronic Imaging Materials #80402 label sheets
<http://barcode-labels.com/?s=80402&submit=Search>`_. When printing PDFs make
sure to check `Actual Size` in the print dialog box.

.. code:: bash

   cual-id create labels my-ids.txt --output-pdf my-labels.pdf
   cual-id create labels my-ids.txt --output-pdf my-labels.pdf --suppress-ids # don't print the ids, only the barcodes
   cual-id create labels my-ids.txt --output-pdf my-labels.pdf --barcode none # don't print barcodes, just the ids


Correcting a list of ids
------------------------

.. code:: bash

   cual-id fix examples/modified-ids.txt --correct-ids examples/ids.txt # report fixed, unfixable and duplicates, the default
   cual-id fix examples/modified-ids.txt --correct-ids examples/ids.txt --show FN # report only fixed and unfixable IDs

Result code definitions
~~~~~~~~~~~~~~~~~~~~~~~
* D: duplicate
* F: fixed
* N: not fixable
* V: valid (didn't need correction)

Output Format
~~~~~~~~~~~~~

::

   input-id <tab> output-id <tab> result-codes


For example:

::

   1a529f8b	1a529f88	F
   d60d0e2b	d60d0c2b	F
   439628o9	43962809	F
   439628o9	43962809	DF
   df47deb4	df47deba	F


Python API
----------

.. code:: python

   from cualid import create_ids
   create_ids(10) # Creates a list of tuples containing a UUID and a cualid


.. |Build Status| image:: https://travis-ci.org/johnchase/cual-id.svg?branch=master
   :target:  https://travis-ci.org/johnchase/cual-id
.. |Coverage Status| image:: https://coveralls.io/repos/johnchase/cual-id/badge.svg?branch=master&service=github
   :target:  https://coveralls.io/github/johnchase/cual-id?branch=master
