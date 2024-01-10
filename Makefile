install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	black *.py src/*.py
lint:
	pylint --disable=R,C *.py src/*.py
test:
	# test
one-test:
	# single_test
	# python -m pytest --v tests/hello_test.py::test_my_model
debug:
	# debug
debugthree:
	# python -m pytest --vv --pdb --maxfail=4 # drop to PDB for first three failures
build:
	# build
deploy:
	# deploy
	
all: install lint test format deploys