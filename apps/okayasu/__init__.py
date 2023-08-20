import os

from pathlib import Path

from apps.python_library.config import init

# config情報を環境変数に設定
base_dir = Path(__file__).resolve().parent.parent
user_dir = os.environ['APP']
config_dir = os.path.join(base_dir,  user_dir, 'config', 'config.ini')
init.set_environ(config_dir)
