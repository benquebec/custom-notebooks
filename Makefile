SHELL      := /bin/bash

NAME		:= notebook
MD_DIR  	:= md_dir
IMG_DIR		:= ../img_dir
VOL			:= 1
PAGES	    := 10
SCRIPT      := $(NAME).py
BACKGROUND  := $(NAME).eps
NOTEBOOK    := $(NAME).pdf
TEX 		:= $(NAME).tex
PY_CMD 	    := python $(SCRIPT) $(MD_DIR) $(IMG_DIR) $(VOL) $(PAGES)
TEX_CMD 	:= for i in {1..2}; do xelatex $(TEX); done
CMD 		:= $(PY_CMD) && $(TEX_CMD)
ACC         := $(NAME).log $(NAME).aux $(NAME).tex *.png

.PHONY: all clean distclean

all: $(NOTEBOOK) clean

$(NOTEBOOK): $(SCRIPT)
	@echo Building notebook...
	mkdir -p $(MD_DIR) $(IMG_DIR)
	$(CMD)

clean:
	@- $(RM) $(ACC)

distclean: clean
