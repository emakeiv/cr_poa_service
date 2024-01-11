install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lib-setup:
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
	aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 605822515341.dkr.ecr.eu-north-1.amazonaws.com
	docker build -t cp_poa_service_entry .
	docker tag cp_poa_service_entry:latest 605822515341.dkr.ecr.eu-north-1.amazonaws.com/cp_poa_service_entry:latest
	docker push 605822515341.dkr.ecr.eu-north-1.amazonaws.com/cp_poa_service_entry:latest

all: install lib-setup lint test deploy