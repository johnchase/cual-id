import click

from barcode.util import get_barcodes

@click.command()
@click.option('--sep', type=str, default='tsv',
              help="Pass 'tsv' if file separator is tab-separator, "
                   "pass 'csv' if file is comma separated (default=tsv)")
@click.option('-c', '--comment', type=str, multiple=True,
              help='Pass if comment lines should be ignored')
@click.option('-l', '--column', type=str, default=None,
              help='The label of the column that contains the IDs to '
                   'generate barcodes for')
@click.argument('input', type=click.File('U'), required=False)
@click.argument('output', type=click.File('w'), required=False)

def cli(input, output, comment, sep, column):
    """This scripts generates a pdf of barcodes"""
    get_barcodes(input, output, mapping)

if __name__ == '__main__':
    main()
