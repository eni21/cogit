req__install:
	pip3 install -r ./src/requirements.txt -t ./src/packages
	pip3 install -r ./build/requirements.txt -t ./build/packages

req__save:
	echo "do it manually"

### RUNNING

run__help:
	python3 src/cogit.py --help

run__config:
	python3 src/cogit.py config

run__version:
	python3 src/cogit.py version

run__change_log:
	python3 src/cogit.py change-log --limit 3

run__next_version:
	python3 src/cogit.py next-version

run__current_version:
	python3 src/cogit.py current-version

run__bump:
	python3 src/cogit.py bump 0.0.0

run__debug_git_messages_raw:
	python3 src/cogit.py debug-git-messages-raw

run__debug_git_messages:
	python3 src/cogit.py debug-git-messages

run__debug_git_versions:
	python3 src/cogit.py debug-git-versions

run__debug_convention:
	python3 src/cogit.py debug-convention

### TESTING

test__all:
	python3 -m unittest discover -s tests -v

test__core:
	python3 -m unittest discover -s tests/test__core -v

test__services:
	python3 -m unittest discover -s tests/services -v

test__git_parser:
	python3 -m unittest discover -s tests/core -p test_git_parser.py -v

test__git_bumper:
	python3 -m unittest discover -s tests/test__providers -p test__bumper.py -v

### RELEASE

release:
	scripts/release.sh

### BUILDING

install__build_requirements:
	pip3 install pyinstaller
	pip3 install stickytape

build__windows:
	pyinstaller.exe --onefile src/cogit.py
	del /s /q cogit.spec
	rmdir build

build__linux:
	pyinstaller --onefile src/cogit.py
	rm cogit.spec
	rm -rf build

build__zipapp:
	python3 -m zipapp src -m cogit:cli -o dist/cogit.pyz

build__stickytape:
	stickytape src/cogit.py --add-python-path . > dist/cogit.py
