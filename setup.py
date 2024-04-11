from setuptools import setup, find_packages

setup(
    name='termpandas',
    version='0.0.1',
    url='https://github.com/username/termpandas',
    author='Author Name',
    author_email='author@gmail.com',
    description='Scrollable pandas dataframes in the terminal',
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
)
