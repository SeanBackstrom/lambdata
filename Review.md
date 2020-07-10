
At least 2 things to compliment and at least 1 constructive criticism. 

**Compliment:** Liked the simplicuty of the code in the nullfinder. The ideal scenario is to have the simplest code which achieves the objectives. Excellent work on that.

**Compliment:** Consistent explanation of what the  two functions  do inside the triple quotes. Any subsequent user will be able to fully and clearly understand what each function does before delving into the actual code.

**Compliment:** The concept of classes and objects is often very elusive and often difficult to understand. A clear explanation of the creation of your 'song' class which instantiates (represents by an instance) 'song' objects. This resonates extremely well with your passion for and expertise in music.

**Potential Area of Development:** Can elaborate on your Setup file to include more information as detailed below:

#setup.py file
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SeanBackstrom",  # the name that you will install via pip
    version="1.0",
    author="Sean Backstrom",
    author_email="sean-backstrom@lambdastudents.com",
    description="The Set up file",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    #license="MIT",
    url="https://github.com/SeanBackstrom/lambdata",
    #keywords="",
    packages=find_packages()  # ["lambdata"]
)

**Overall:** Simplicity is the ultimate sophistication. Very simple code which achieves the intended results. Any user, even non techincal users will be able to follow through. Good work, keep it up. 
