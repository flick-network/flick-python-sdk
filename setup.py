from setuptools import setup,find_packages
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "flick-python-sdk",
    version = "0.0.13",
    author = "Sivadas Rajan",
    author_email = "sivadasrajan@gmail.com",
    description = "A Python wrapper for interacting with APIs from Flick.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires=["requests>=2.25.0"],
    url = "https://test.pypi.org/project/flick-python-sdk/",
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
