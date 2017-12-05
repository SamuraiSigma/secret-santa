## Makefile for Secret Santa project

# -------------------------------------------------------------
# Directories

SRCDIR:= secret_santa

# -------------------------------------------------------------
# Bash Commands

MKDIR:= mkdir -p
RMDIR:= rm -rf

# -------------------------------------------------------------
# Python Options

PYTHON:= python3

# =============================================================

.PHONY: test syntax style count clean

# Run automated tests
test:
	@$(PYTHON) -m nose --rednose --py3where=$(SRCDIR)

# Check code for syntax errors
syntax:
	@find $(SRCDIR) -name *.py ! -name __init__.py | xargs $(PYTHON) -m py_compile

# Check if code follows Python conventions
style:
	@$(PYTHON) -m pycodestyle $(SRCDIR); $(PYTHON) -m pep257 $(SRCDIR)

# Count number of lines of code written
count:
	@find $(SRCDIR) -name *.py ! -name __init__.py | xargs wc -l

# Remove all Python-generated files
clean:
	@find $(SRCDIR) -name __pycache__ -o -name *.pyc | xargs $(RMDIR)
	@echo "Successfully removed Python-generated files!"
