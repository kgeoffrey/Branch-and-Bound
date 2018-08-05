
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cavemanstatistics",
    version="0.5",
    author="Geoffrey Kasenbacher",
    author_email="gkasenbacher@gmail.com",
    description="Exhaustive-Search for best R^2 in Linear Regression Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kgeoffrey/cavemanstats",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas', 'scikit-learn', 'tabulate', 'scipy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)
