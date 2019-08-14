import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="databinner",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="Powerful correct binner for data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CxAalto/databinner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ],
)
