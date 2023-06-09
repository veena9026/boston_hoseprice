from setuptools import find_packages,setup
from typing import List

HYPEN_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_DOT in requirements :
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name="BOSTON_project",
    version="0.0.1",
    author="Veena",
    author_email="chinta.veena26@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)