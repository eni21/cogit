install_requirements:
	pip3 install -r ./src/requirements.txt -t ./src/packages
	pip3 install -r ./build/requirements.txt -t ./build/packages

save_requirements:
	echo "do it manually"

###
### BUILDING
###

install_build_requirements:
	pip3 install pyinstaller

build_windows:
	pyinstaller.exe --onefile src/cogit.py

build_linux:
	pyinstaller --onefile src/cogit.py
	rm cogit.spec
