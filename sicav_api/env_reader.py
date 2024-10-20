import os

from pathlib import Path


def read_env_file() -> None:
    BASE_DIR = Path(__file__).resolve().parent.parent

    with open(BASE_DIR / ".env") as f:
        for line in f.readlines():
            config_line = line.strip()
            if config_line.startswith("#"):
                continue
            key, value = config_line.split("=", 1)
            os.environ[key] = value


if __name__ == "__main__":
    read_env_file()
