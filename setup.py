import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klang-globconf",
    version="0.0.6",
    author="Steffen Schumacher",
    author_email="ssch@wheel.dk",
    description="global configparser object to be used across modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/steffenschumacher/globconf",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)