from setuptools import setup

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/rsfellman/ds5100-finalproject-dbm4bj',
    author='Rachel Fellman',
    description='DS 5100 Final Project Package. Creates a Monte Carlo sumulation and allows the user to create and "roll" die and generate the results of their rolls.',
    packages= ['montecarlo'],    
    install_requires=['numpy', 'pandas']
)