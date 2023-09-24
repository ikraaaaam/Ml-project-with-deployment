from setuptools import setup, find_packages
from typing import List

hyphen_e_dot= '-e .'

def get_requirements( file_path:str)->List[str]:

    '''
    this function will return the list of requiremtns
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", " ")for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements





# Define package metadata
NAME = "my_package"
VERSION = "1.0.0"
DESCRIPTION = "A sample Python package"
AUTHOR = "ikraam"
AUTHOR_EMAIL = "dabisiku@gmail.com"
#URL = "https://github.com/yourusername/my_package"
LICENSE = "MIT"
PACKAGES = find_packages()



INSTALL_REQUIRES = get_requirements('requirements.txt')


# Create the setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    #url=URL,
    license=LICENSE,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    # You can add more configuration options as needed
    # Entry points, scripts, classifiers, etc.
)