from setuptools import setup, find_packages

setup(
    name="heart-disease-prediction-ann",
    version="0.1",
    author="Ayush Shinde",
    author_email="ayushshinde495@gmail.com",
    description="A deep learning project to predict heart disease using ANN",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'tensorflow',
        'sklearn',
        'matplotlib',
        'seaborn'
    ],
)