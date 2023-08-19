import os
import configparser

from pathlib import Path


'''
config.iniの値を環境変数に設定
'''
def set_environ(config_dir: Path):
    config = configparser.ConfigParser()
    config.read(config_dir, 'UTF-8')
    keys_by_section = {section: config.options(section) for section in config.sections()}
    for section, keys in keys_by_section.items():
        for key in keys:
            os.environ[key] = config.get(section, key)
