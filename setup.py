from setuptools import setup
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "flick-python-sdk",
    version = "1.0.0",
    author = "Sivadas Rajan",
    author_email = "sivadasrajan@gmail.com",
    description = "A Python wrapper for interacting with APIs from Flick.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires=["aiohttp>=3.5.0"],
    url = "https://pypi.org/project/flick-python-sdk/",
    maintainer="Sivadas Rajan",
    maintainer_email="sivadasrajan@gmail.com",
    project_urls = {
        "Bug Tracker": "https://github.com/flick-network/flick-python-sdk/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = ['flick'],
    python_requires = ">=3.6"
)
