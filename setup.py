from setuptools import setup, find_packages

setup(
    name='hbcli',
    version='1.0',
    description='Play Hit&Blow on your terminal!',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            'hb = hb.core:main'
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)