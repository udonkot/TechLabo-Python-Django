#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import configparser

from pathlib import Path

"""
コンフィグファイル
"""
BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = os.path.join(BASE_DIR, 'database', 'config', 'config.ini')


"""
環境変数を設定
"""
def set_environ(config_file):
    config = configparser.ConfigParser()
    config.read(config_file, "UTF-8")

    os.environ["log_file_app"] = config.get("log_setting", "log_file_app")
    os.environ["log_file_django"] = config.get("log_setting", "log_file_django")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    set_environ(CONFIG_FILE)
    main()
