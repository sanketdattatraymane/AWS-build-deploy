from setuptools import setup, find_packages

setup(
    name='my-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'boto3'
    ]
)
