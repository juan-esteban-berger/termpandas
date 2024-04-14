from setuptools import setup, find_packages

# Load the README file and use it as the long_description.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='termpandas',
    version='0.0.8',
    url='https://github.com/juan-esteban-berger/termpandas',
    author='Juan Esteban Berger',
    author_email='juanestebanberger@gmail.com',
    description='Scrollable pandas dataframes in the terminal.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.1.4',
        'blessings>=1.7',
        'curtsies>=0.4.2',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Source Code': 'https://github.com/juan-esteban-berger/termpandas'
    }
)
