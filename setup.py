from setuptools import setup, find_packages

setup(
    name='screening_task',
    version='1.0',
    description='this is for screening_test',
    author='Adharv',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
 
)
