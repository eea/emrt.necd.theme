# Make sure to: pip install twine
# https://github.com/pypa/twine

PACKAGE=emrt.necd.theme

VERSION=$(shell grep "VERSION = " setup.py | grep -o '[0-9.]*')

all:

build:
	python2 setup.py bdist_wheel
	python2 setup.py bdist_egg

release: build
	twine upload ./dist/${PACKAGE}-${VERSION}-*.whl
	twine upload ./dist/${PACKAGE}-${VERSION}-*.egg

clean:
	rm -rf build/ dist/
