from setuptools import find_packages ,setup
from typing import List

## we make the function to send the packaes to setup.py from requrinments.txt
## list[str] we will return the list of string in get
def get_requrinments()->list[str]:

    requrinments_list  = list[str] =[]

    return requrinments_list 

setup(
    name = 'sensor',
    version="0.0.1",
    author="Saad",
    author_email="sayyedsaad1634@gmail.com",
    packages= find_packages(),
    install_requires = get_requrinments()

)