---
title: Polychrony detection in raster plots
keywords:
- neurons
- code
- time
lang: en-US
date-meta: '2021-12-02'
author-meta:
- Laurent U Perrinet
- John Doe
- Jane Roe
citekey-aliases:
  my-url: https://openreview.net/forum?id=HkwoSDPgg
  Ikegaya2004: doi:10.1126/science.1093173
  gan: https://papers.nips.cc/paper/5423-generative-adversarial-nets
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Polychrony detection in raster plots" />
  <meta name="citation_title" content="Polychrony detection in raster plots" />
  <meta property="og:title" content="Polychrony detection in raster plots" />
  <meta property="twitter:title" content="Polychrony detection in raster plots" />
  <meta name="dc.date" content="2021-12-02" />
  <meta name="citation_publication_date" content="2021-12-02" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Laurent U Perrinet" />
  <meta name="citation_author_institution" content="Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université" />
  <meta name="citation_author_orcid" content="0000-0002-9536-010X" />
  <meta name="twitter:creator" content="@laurentperrinet" />
  <meta name="citation_author" content="John Doe" />
  <meta name="citation_author_institution" content="Department of Something, University of Whatever" />
  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />
  <meta name="twitter:creator" content="@johndoe" />
  <meta name="citation_author" content="Jane Roe" />
  <meta name="citation_author_institution" content="Department of Something, University of Whatever" />
  <meta name="citation_author_institution" content="Department of Whatever, University of Something" />
  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />
  <link rel="canonical" href="https://SpikeAI.github.io/polychronies/" />
  <meta property="og:url" content="https://SpikeAI.github.io/polychronies/" />
  <meta property="twitter:url" content="https://SpikeAI.github.io/polychronies/" />
  <meta name="citation_fulltext_html_url" content="https://SpikeAI.github.io/polychronies/" />
  <meta name="citation_pdf_url" content="https://SpikeAI.github.io/polychronies/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://SpikeAI.github.io/polychronies/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://SpikeAI.github.io/polychronies/v/8cf9bd9c54ec854c5a60fa496d97e1ec02c8d4ef/" />
  <meta name="manubot_html_url_versioned" content="https://SpikeAI.github.io/polychronies/v/8cf9bd9c54ec854c5a60fa496d97e1ec02c8d4ef/" />
  <meta name="manubot_pdf_url_versioned" content="https://SpikeAI.github.io/polychronies/v/8cf9bd9c54ec854c5a60fa496d97e1ec02c8d4ef/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://SpikeAI.github.io/polychronies/v/8cf9bd9c54ec854c5a60fa496d97e1ec02c8d4ef/))
was automatically generated
from [SpikeAI/polychronies@8cf9bd9](https://github.com/SpikeAI/polychronies/tree/8cf9bd9c54ec854c5a60fa496d97e1ec02c8d4ef)
on December 2, 2021.
</em></small>

## Authors



+ **Laurent U Perrinet**
  · [https://laurentperrinet.github.io/](https://laurentperrinet.github.io/)<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-9536-010X](https://orcid.org/0000-0002-9536-010X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [laurentperrinet](https://github.com/laurentperrinet)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [laurentperrinet](https://twitter.com/laurentperrinet)<br>
  <small>
     Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université
     · Funded by Grant XXXXXXXX
  </small>

+ **John Doe**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [XXXX-XXXX-XXXX-XXXX](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [johndoe](https://github.com/johndoe)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [johndoe](https://twitter.com/johndoe)<br>
  <small>
     Department of Something, University of Whatever
     · Funded by Grant XXXXXXXX
  </small>

+ **Jane Roe**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [XXXX-XXXX-XXXX-XXXX](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [janeroe](https://github.com/janeroe)<br>
  <small>
     Department of Something, University of Whatever; Department of Whatever, University of Something
  </small>



## Abstract {.page_break_before}








speed
(1] S Thorpe, D Fize, and C Marlot, Nature 381.6582 (1996), pp.520-522.

sparse in time and space
[2] AL Barth and JF Poulet
Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.

timing encodes profile
Celebrini
[4] T Gollisch and M Meister, Science 319.5866 (2008), pp. 1108-1111.


surrogate gradients

 F Zenke and S Ganguli, Neural Computation 30.6 (2018), pp. 1514-1541.

 G Bellec et al., arXiv:1803.09574 [cs, q-bio] (2018) arXiv: 1803.09574.

 SB Shrestha and G Orchard, arXiv:1810.08646 /cs, stat) (2018) . arXiv: 1810.08646.

## cortical songs

Ikegaya Y, Aaron G, Cossart R, Aronov D, Lampl I, Ferster D, Yuste R. 2004. Synfire chains and cortical songs: temporal modules of cortical activity. Science (New York, NY) 304:559–564. [@Ikegaya2004]


Gan were introduced in [@gan]


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
