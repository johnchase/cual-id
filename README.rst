=======
cual-id
=======
|Build Status| |Coverage Status| |Conda Install|

Install
=======

Miniconda
---------

We strongly recommend installing `cual-id` using `Miniconda <http://conda.pydata.org/miniconda.html>`__. which greatly simplifies Python package management. To do this, you should first choose which version of Miniconda to install from `the install page <http://conda.pydata.org/docs/install/quick.html>`__. You can choose either the Python 2 or 3 version. After you've installed Miniconda, you should run:  

.. code:: bash

    conda create -c https://conda.anaconda.org/johnchase -n cual-id python=3 cual-id
    
After this completes (it should take less than a minute), you can activate your ``cual-id`` environment by running:

.. code:: bash

    source activate cual-id

Then, to see the available ``cual-id`` commands, run:

.. code:: bash

    cual-id --help

pip
---

If you prefer to install with pip, and already have a Python 3 development environment configured, you can do this with the following command:

.. code:: bash

    pip install cual-id

Usage
=====

Activating your environment
---------------------------

If you installed cual-id using Miniconda, to start using cual-id you'll need to run the following command when you open a new terminal:

.. code:: bash

    source activate cual-id

Getting help
------------

.. code:: bash

   cual-id --help


Creating a list of IDs
----------------------

.. code:: bash

   cual-id create ids 42 # writes 42 ids to stdout
   cual-id create ids 42 > my-ids.txt # writes 42 ids to my-ids.txt
   cual-id create ids 42 --existing-ids my-ids.txt # creates ids that do not
   overlap with existing ids. Note this will only compare new ids to the first
   column of the file



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

Citing cual-id
==============

cual-id is currently under review at mSystems. Our pre-print of that manuscript is available on PeerJ:

`cual-id globally unique, correctable, and human-friendly sample identifiers for comparative
-omics studies <https://peerj.com/preprints/1431/>`__.

Please cite this pre-print if you use cual-id in any published work. 

.. |Build Status| image:: https://travis-ci.org/johnchase/cual-id.svg?branch=master
   :target:  https://travis-ci.org/johnchase/cual-id
.. |Coverage Status| image:: https://coveralls.io/repos/johnchase/cual-id/badge.svg?branch=master&service=github
   :target:  https://coveralls.io/github/johnchase/cual-id?branch=master
.. |Conda Install| image:: https://anaconda.org/johnchase/cual-id/badges/installer/conda.svg?branch=master
   :target: https://anaconda.org/johnchase/cual-id
