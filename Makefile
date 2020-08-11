LATEX=xelatex
LATEXOPT=--shell-escape
NONSTOP=--interaction=nonstopmode

PDFLATEX=pdflatex
PDFLATEXOPT=-synctex=1 -shell-escape $(NONSTOP)

LATEXMK=latexmk
LATEXMKOPT=-xelatex
CONTINUOUS=-pvc

MAIN=main
SOURCES=$(MAIN).tex Makefile abstract/abstract.tex introduction/introduction.tex background/background.tex method/method.tex result/result.tex discussion/discussion.tex preamble.tex title.tex bibliography/references.bib
#FIGURES := $(shell find resources/* figures/* images/* -type f)

all: $(MAIN).pdf

.refresh:
	touch .refresh

$(MAIN).pdf: $(MAIN).tex .refresh $(SOURCES) #$(FIGURES)
	$(PDFLATEX) $(PDFLATEXOPT) $(MAIN)
	#$(LATEXMK) -xelatex $(CONTINUOUS) $(MAIN)
force:
	touch .refresh
	rm $(MAIN).pdf
	$(PDFLATEX) $(PDFLATEXOPT) $(MAIN)
	#$(LATEXMK) -xelatex $(CONTINUOUS) $(MAIN)

clean:
	#$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk

once:
	$(LATEXMK) $(LATEXMKOPT) $(MAIN)

debug:
	$(LATEX) $(LATEXOPT) $(MAIN)

.PHONY: clean force once all
