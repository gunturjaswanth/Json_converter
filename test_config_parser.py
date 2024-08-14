import os
from config_parser import ConfigParser


def test_read_yaml():
    config_parser = ConfigParser()
    config = config_parser.read_yaml('example.yml')

    print("Parsed YAML configuration:", config)
    assert isinstance(config, dict)

    assert len(config) > 0

    for key, value in config.items():
        print(f"Key: {key}, Value type: {type(value)}")
        assert isinstance(key, str)  # Check that the key is a string
        assert isinstance(value, (dict, list, str, int, float, bool, type(None)))  # Allow common data types


def test_write_to_json():
    config_parser = ConfigParser()
    config = config_parser.read_yaml('example.yml')

    config_parser.write_to_json(config, 'test_output.json')

    assert os.path.exists('test_output.json')
    with open('test_output.json', 'r') as f:
        json_content = f.read()

    assert json_content.strip() != ""


def test_set_os_environ():
    config_parser = ConfigParser()
    config = config_parser.read_yaml('example.yml')

    config_parser.set_os_environ(config)

    for key in config.keys():
        value = os.getenv(key)
        print(f"Key: {key}, Value: {value}")
        assert value is not None
        break
