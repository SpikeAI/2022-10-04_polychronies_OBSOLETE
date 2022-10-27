import re

if False:
    latex = r"""
    blablabla
    Author et. al \cite{author92} bla bla. % should match
    \citep{author93} % should match
    \nocite{author94} % should match
    100\%\nocite{author95} % should match
    100\% \nocite{author95} % should match
    %\nocite{author96} % should not match
    \cite{author97, author98, author99} % should match
    \nocite{*} % should not match
    """
else:
    with open('manuscript.tex') as f:
        latexlines = f.readlines()

    # latex = ''.join(line.strip() for line in latexlines)
    latex = ''.join(line for line in latexlines)
    # latex = latex.replace('\\', '\')

rx = re.compile(r'''(?<!\\)%.+|(\\(?:no)?citep?\{((?!\*)[^{}]+)\})''')
# rx = re.compile(r'''^(?!(%\\(?:no)?cite\w*\{([^}]*?)\}))[^*\n]*$''')
# rx = re.compile(r'''^(?!(%\\(?:no)?cite\w*\{([^}]*?)\}))[^*\n]*$''')

citekeys = [m.group(2) for m in rx.finditer(latex) if m.group(2)]
# print(citekeys)

citekey_list = []
for citekey in citekeys:
    for citekey_ in citekey.split(', '):
        citekey_list.append(citekey_)
import numpy as np
citekey_list = np.unique(citekey_list)
# print(citekey_list)


with open('references.bib') as f:
        bibtexlines = f.readlines()

# latex = ''.join(line.strip() for line in latexlines)
bibtex = ''.join(line for line in bibtexlines)

rx = re.compile(r'''@\w+{([\w:-]+)''')
bibkeys = [m.group(1) for m in rx.finditer(bibtex) if m.group(1)]
bibkeys = np.unique(bibkeys)
# print(bibkeys)
    
for bibkey in bibkeys:
    if not(bibkey in citekey_list):
        print('This key in not used in the paper', bibkey)

