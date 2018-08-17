# Reset suffix list
.SUFFIXES:
.SUFFIXES: .tex

# Use spaces instead of tabs
.RECIPEPREFIX != ps

PATHT := tex/

AUX := $(tex/*.aux)
LOG := $(tex/*.log)
TOC := $(tex/*.toc)
DVI := $(tex/*.dvi)
PDF := databook.pdf schedule.pdf

# Phony targets

.PHONY: all clean

all : $(PDF)

clean :
  -rm -f $(PDF) $(AUX) $(LOG) $(TOC) $(DVI)

%.pdf :
  $(eval BASE := $(PATHT)$(@:.pdf=))
  latex -output-directory=$(PATHT) $(BASE).tex
  dvipdf $(BASE).dvi $@
