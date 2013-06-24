SHELL      := /bin/bash

SCRIPT     := notebook.py
BACKGROUND := notebook.eps
NOTEBOOK   := notebook.pdf
CMD 	   := python $(SCRIPT) && for i in {1..2}; do xelatex notebook.tex; done
ACC        := .log .aux .tex


.PHONY: all clean distclean

all: $(NOTEBOOK)

$(NOTEBOOK): $(SCRIPT)
	@echo Building notebook...
	$(CMD)

clean:
	@- $(RM) $(NOTEBOOK) $(ACC)

distclean: clean
