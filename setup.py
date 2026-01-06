'''
The setup/py file is an essential part of packaging and distributing
python projects. It is used by setuptools to define the 
configuration of your project,
such as its metadata, dependencies, and more
'''
#it search for  all folder and where is this init file it 
# consider it as the package

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read line form the file
            lines=file.readlines()
            ## process eacch lines
            for line in lines:
                requirement=line.strip()
                if requirement in requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


setup(
    name="Network-Security",
    version="0.0.1",
    author="Parveen kumar",
    author_email="parveenyadavpy57377@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)