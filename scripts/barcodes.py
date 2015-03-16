import click

from barcode.generate_barcode_pdfs import get_barcodes

@click.command()
@click.option('--sep', type=str, default='tsv',
              help="Pass 'tsv' if file separator is tab-separator, "
                   "pass 'csv' if file is comma separated (default=tsv)")
@click.option('-m', '--mapping', type=str, multiple=True,
              help='Pass if comment lines should be ignored')
@click.argument('input', type=click.File('U'), required=False)
@click.argument('output', type=click.File('w'), required=False)

def cli(input, output, mapping, sep):
    """This scripts generates a pdf of barcodes"""
    get_barcodes(input, output, mapping)

if __name__ == '__main__':
    main()
