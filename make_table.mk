# table.mk

LATEX = /usr/bin/pdflatex


test.pdf: table.tex test.tex
	$(LATEX) test.tex

table.tex: sample.dat
	./latex_table-creator.py

