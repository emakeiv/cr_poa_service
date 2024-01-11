install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
ocr-setup:
	./scripts/ocr_engine_provision.sh
format:
	# format code
	black *.py src/*.py tst/*/*.py
lint:
	pylint --disable=R,C *.py src/*.py tst/*/*.py
test:
	python -m pytest -vv --cov=src tst/*/*_tests.py
one-test:
	# single_test
	# python -m pytest --v tests/hello_test.py::test_my_model
debug:
	# debug
debugthree:
	# python -m pytest --vv --pdb --maxfail=4 # drop to PDB for first three failures
build:
	docker build -t cr_poa_service:latest .
run:
	# run container
	# docker run -p 8080:8080 cr_poa_service:latest
deploy:
	# deploy
	
all: install lint test format deploys