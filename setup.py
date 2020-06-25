import os

from setuptools import find_packages, setup

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, "requirements.txt")

with open(REQUIREMENTS) as f:
    reqs = f.read()

setup(
    name='Firework',
    version='1.0.0',
    author='Simon Münker',
    url='https://github.com/smnmnkr/firework',
    description='Python 3 and pyGame based simple Firework',
    packages=find_packages(exclude=("config", "tests")),
    install_requires=reqs.strip().split("\n"),
    entry_points={"console_scripts": ["firework = main:main"]},
)
