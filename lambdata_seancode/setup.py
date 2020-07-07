""" lambdata - a collection of Data Science helper functions
"""
import setuptools
REQUIRED = [
    "numpy",
    "pandas"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
setuptools.setup(
    name="lambdata_seancode",
    version="0.3.1",
    author="Sean Backstrom",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/seanbackstrom/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licgit ense :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)