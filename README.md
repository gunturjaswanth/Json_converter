# ConfigParser Module

## Overview
This Python module reads `.yaml`, `.cfg`, and `.conf` configuration files and flattens them into a dictionary. It can then output the configurations into `.env` or `.json` files, or set them directly as OS environment variables.

## Usage
Install the Package
use the below code for reading and conversion of yaml files into Json

    from config_parser import ConfigParser
    config_parser = ConfigParser()
    config = config_parser.read_yaml('your yaml file name.yml')
    config_parser.write_to_json(config, 'output.json')
    config_parser.set_os_environ(config)