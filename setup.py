from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="housing-prediction"
VERSION="0.0.3"
AUTHOR="SANDHYA"
DESCRIPTION="THIS IS MY FIRST PROJECT"

REQUIREMENTS_FILE_NAME="Requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as file:
        file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)