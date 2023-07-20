from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="KedavraC2",
    version="0.1.0",
    description="A death making, python-based C2",
    long_description=readme,
    author="Opulence",
    url="https://github.com/theophane-droid/KedavraC2",
    license=license,
    packages=find_namespace_packages(include=["opulence.*"]),
    install_requires=requirements,
    python_requires=">=3.6.*, <4",
)
