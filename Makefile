################################################
SRC = brainsci-2069565_accepted
SRC_rev = manuscript_rev1
# SRC_rev = brainsci-2069565
#LATEXMK = latexmk -pdf -pdflatex=lualatex
LATEXMK = latexmk -pdf
BIBTEX = bibtex
################################################
default: diff
pdf: $(SRC).pdf 2022-12-28_coverletter.pdf 
diff: $(SRC)_trackedchanges.pdf
################################################
LATEXMK = latexmk -bibtex -pdf
#  -pdflatex=pdflatex
################################################

install_local:
	python3 -m pip install --user -r requirements.txt

install_global:
	python3 -m pip install -r requirements.txt

# post-production
$(SRC)_trackedchanges.tex: $(SRC).tex $(SRC_rev).tex
	latexdiff --graphics-markup=both $(SRC_rev).tex $(SRC).tex > $(SRC)_trackedchanges.tex

response_to_reviewers.pdf: response_to_reviewers.tex $(SRC).tex $(SRC).bib
	$(LATEXMK) response_to_reviewers.tex

touch:
	touch *.tex

git:
	git pull
	git commit -am'Another pass'
	git push

# macros
%.pdf: %.tex
	$(LATEXMK) $<

%.pdf: %.svg
	$(INKSCAPE) --without-gui $< --export-pdf=$@

%.png: %.svg
	$(INKSCAPE) --without-gui $< --export-png=$@ -d 450

# cleaning macro
clean:
	rm -f *.dvi *.fls *.ilg *.ind *idx *.bcf *.run.xml *.dvi *.ps *.out *.log *.aux *.bbl *.blg  *.fdb_latexmk *.snm *.nav *.toc *.info *.synctex.gz* 
