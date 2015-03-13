import click

from barcode.generate_barcode_pdfs import get_barcodes

@click.command()
@click.option('-m', '--mapping', type=str, multiple=True,
              help='Pass if comment lines should be ignored')
@click.argument('input', type=click.File('U'), required=False)
@click.argument('output', type=click.File('w'), required=False)
def cli(input, output, mapping):
    """This scripts generates a pdf of barcodes"""
    get_barcodes(input, output, mapping, columns=4, rows=9)

if __name__ == '__main__':
    main()
