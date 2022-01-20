import os
from setuptools import setup, find_packages


cwd = os.path.abspath(os.path.dirname(__file__))

# Get package dependencies
with open(os.path.join(cwd, "requirements.txt")) as file:
    requirements = file.read().splitlines()


# Get README text
with open(os.path.join(cwd, "README.md")) as file:
    readme = file.read()


setup(
    name="pygsearch",
    author="Vitaman02",
    url="https://github.com/Vitaman02/pygsearch",
    project_urls={},
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    description="Python library to get google search results.",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ]
)