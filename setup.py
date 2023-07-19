from setuptools import find_packages,setup
from typing import List  # import list for recognizable in Line "5"

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
 # Meta data information about the project 
setup(
name='mlproject',
version='0.0.1',
author='Leela',
author_email='leelavathi.rajan@gmail.com',
packages=find_packages(),  # this will find the package __init__ under the folder "src" & you can use it as like "pandas or seaborn"
install_requires=get_requirements('requirements.txt')

)