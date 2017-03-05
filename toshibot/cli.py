#! /usr/bin/env python

import click
import sh
import os
from sh import git, sudo

@click.group()
def cli():
    pass

@cli.command()
def update():
	"""
	Upgrades the `moment` CLI command to the latest version on Github.
	"""

	import subprocess
	subprocess.call("pip install git+ssh://git@github.com/shantanubala/toshibot.git -U", shell=True)

if __name__ == "__main__":
	cli()
