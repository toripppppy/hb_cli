from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name='hbcli',
    version='1.0',
    description='Play Hit&Blow on your terminal!',
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        'console_scripts':
            'hb = hb.core:main'
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)