.PHONY: install
install:
	python setup.py install

.PHONY: test
test:
	flake8 .
	nosetests --nocapture --where tests

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	rm -rf .ipynb_checkpoints .cache .config .ipython .jupyter .local
	rm -rf python_helpers.egg-info dist target build
