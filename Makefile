MODULE_PATH="confit"
VENV_PATH=".venv"

install:
	test -d ${VENV_PATH} || python3 -m venv ${VENV_PATH} || :
	source ${VENV_PATH}/bin/activate && pip install --upgrade pip
	source ${VENV_PATH}/bin/activate && pip install -e .[dev]

black:
	black ${MODULE_PATH}

flake8:
	flake8 ${MODULE_PATH}

prepare: black flake8
