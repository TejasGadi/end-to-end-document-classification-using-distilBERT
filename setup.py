from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Get the list of requirements from a requirements file.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of requirements.

    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='newsgroup_document_classification',
    version='0.0.1',
    author='Shagun',
    author_email='kala.shagun@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)