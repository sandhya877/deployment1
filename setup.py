from setuptools import setup
from typing import List




PROJECT_NAME="housing-prediction"
VERSION="0.0.1"
AUTHOR="SANDHYA"
DESCRIPTION="THIS IS MY FIRST PROJECT"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="Requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as file:
        file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)