from distutils.core import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="airnowpy",
    version="2.3.2",
    description="Python Library for the AirNow API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karjanme/airnowpy",
    author="Karl Jansen",
    author_email="jnsnkrl@live.com",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pytz",
        "requests"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Software Development :: Libraries"
    ]
)
