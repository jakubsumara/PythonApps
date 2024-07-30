# cli.py

import click
from fleet.ambulance import Ambulance
from personnel.employee import Employee

@click.group()
def cli():
    pass

@cli.command()
@click.argument('ambulances', type=int)
@click.argument('employees', type=int)
def check_resources(ambulances, employees):
    if ambulances < 1 or employees < 1:
        click.echo("Resources must be greater than zero.")
        return

    click.echo(f"Checking resources for {ambulances} ambulances and {employees} employees...")

    # Example logic
    if employees < ambulances * 2:
        click.echo("Not enough employees to operate all ambulances.")
    else:
        click.echo("Sufficient resources available.")

if __name__ == '__main__':
    cli()
