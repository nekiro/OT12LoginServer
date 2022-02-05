# OT12LoginServer

Small, portable and cross-platform HTTP login server written in python.

## Features

- Handles client 12 login requests
- Config handler

## Installation

OT12LoginServer requires [Python](https://www.python.org/) 3.7+ to run

Main dependencies:
- Tornado
- PyYAML
- mysql

Install the dependencies

Windows:
```sh
cd OT12LoginServer
python -m pip install -r requirements.txt
```

Linux:
```sh
cd OT12LoginServer
sudo apt install python3-pip
pip3 install -r requirements.txt
```

## How to use
Windows:
```sh
cd OT12LoginServer
python main.py
```
Linux:
```sh
cd OT12LoginServer
python3 main.py
```

## License

MIT
