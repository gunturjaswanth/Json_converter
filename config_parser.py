import os
import yaml
import json
import configparser
from collections.abc import MutableMapping


class ConfigParser:

    @staticmethod
    def _flatten(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f'{parent_key}{sep}{k}' if parent_key else k
            if isinstance(v, MutableMapping):
                items.extend(ConfigParser._flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def read_yaml(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return self._flatten(config)

    def read_cfg(self, file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        flat_config = {section: dict(config.items(section)) for section in config.sections()}
        return self._flatten(flat_config)

    def read_conf(self, file_path):
        return self.read_cfg(file_path)

    def write_to_json(self, config, output_path):
        with open(output_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

    def write_to_env(self, config, output_path):
        with open(output_path, 'w') as env_file:
            for key, value in config.items():
                env_file.write(f'{key}={value}\n')

    def set_os_environ(self, config):
        for key, value in config.items():
            os.environ[key] = str(value)

    def parse_and_convert(self, file_path, output_format, output_path=None):
        extension = file_path.split('.')[-1]
        if extension == 'yaml' or "yml":
            config = self.read_yaml(file_path)
        elif extension in ['cfg', 'conf']:
            config = self.read_cfg(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")

        if output_format == 'json':
            if not output_path:
                raise ValueError("Output path is required for JSON output")
            self.write_to_json(config, output_path)
        elif output_format == 'env':
            if not output_path:
                raise ValueError("Output path is required for ENV output")
            self.write_to_env(config, output_path)
        elif output_format == 'os':
            self.set_os_environ(config)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

