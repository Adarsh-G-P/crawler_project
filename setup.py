from setuptools import setup

"""responsible for configuring the project 
and generating the necessary files for packaging and distribution"""

setup(
    name='lyrics',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
    entry_points={
        'console_scripts': [
            'lyrics = lyrics.cli:main',
        ]
    }
)
