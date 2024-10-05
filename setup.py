from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="basic_package",
    version="0.0.1",
    author="GustavoRaia",
    author_email="my_email",
    description="Basic package to demonstrate packaging in Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GustavoRaia/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)