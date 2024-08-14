import setuptools
setuptools.setup(     
     name='json_converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'config_parser=config_parser.config_parser:main',
        ],
    },
)
