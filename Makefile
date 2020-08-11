PDFLATEXOPT=--synctex=1 --shell-escape --interaction=batchmode --halt-on-error

MAIN=main
SOURCES=$(MAIN).tex Makefile tex/abstract.tex tex/introduction.tex tex/background.tex tex/method.tex tex/result.tex preamble.tex tex/title.tex bibliography/references.bib

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex .refresh $(SOURCES)
	pdflatex $(PDFLATEXOPT) $(MAIN)

clean:
	rm -f $(MAIN).pdfsync
	rm -f main.synctex.gz main.toc .refresh
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk
