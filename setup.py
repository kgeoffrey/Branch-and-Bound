
# coding: utf-8

# In[1]:


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cavemanstats",
    version="1.0",
    author="Geoffrey Kasenbacher",
    author_email="gkasenbacher@gmail.com",
    description="Brute force, Exhaustive-Search for best R^2 in Linear Regression Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kgeoffrey/Caveman-Stats",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas', 'sklearn.linear_model', 'tabulate'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)

