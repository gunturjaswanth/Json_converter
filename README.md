# ConfigParser Module

## Overview
This Python module reads `.yaml`, `.cfg`, and `.conf` configuration files and flattens them into a dictionary. It can then output the configurations into `.env` or `.json` files, or set them directly as OS environment variables.

## Installation
Follow the steps below to make  available as a pip package,

Generate a build of our package for that execute the below command

   **python setup.py sdist bdist_wheel** 

This will build all the necessary packages that Python will require. The sdist and bdist_wheel commands will create a source distribution and a wheel that you can later upload to PyPI.
Install twine for creating build execute the below command

   **pip install twine**

Upload package to PyPI,

   **twine upload dist/***

This command will upload the contents of the dist folder that was automatically generated when we ran python setup.py. You will get a prompt asking you for your PyPi username and password, so go ahead and type those in.

## Usage
Install the Package

  **pip install json_converter**

Use the below code for reading and conversion of yaml files into Json

    from config_parser import ConfigParser
    config_parser = ConfigParser()
    config = config_parser.read_yaml('your yaml file name.yml')
    config_parser.write_to_json(config, 'output.json')
    config_parser.set_os_environ(config)
