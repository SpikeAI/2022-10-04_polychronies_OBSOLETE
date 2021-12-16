---
title: Review on Polychrony detection in biological and artificial raster plots
keywords:
- neurons
- code
- time
lang: en-US
date-meta: '2021-12-16'
author-meta:
- Antoine Grimaldi
- Laurent U Perrinet
citekey-aliases:
  Abeles1991: isbn:9780521376174
  Perrinet2001: doi:10.1016/S0925-2312(01)00460-X
  Perrinet2002: doi:10.1016/S0925-2312(02)00374-0
  Ikegaya2004: doi:10.1126/science.1093173
  Bienenstock1995: doi:10.1088/0954-898x_6_2_004
  Yuste2005: doi:10.1038/nrn1686
  Luczak2015: pmid:26507295
  gan: https://papers.nips.cc/paper/5423-generative-adversarial-nets
  alexnet: http://dl.acm.org/citation.cfm?doid=3098997.3065386
  zotero: https://www.zotero.org/
  vgg: https://arxiv.org/abs/1409.1556
  googlenet: https://ieeexplore.ieee.org/document/7298594
  resnet: https://ieeexplore.ieee.org/document/7780459
  Grossberger2018: doi:10.1371/journal.pcbi.1006283
  Agus2010: doi:10.1016/j.neuron.2010.04.014
  Agus2010pdf: http://audition-backend.ens.fr/dp/pdfs/AgusThorpePressnitzer-2010-noise_memory.pdf
  Moser2014: doi:10.1109/TSP.2014.2305642
  Stringer2019nature: doi:10.1038/s41586-019-1346-5
  Stringer2019science: doi:10.1126/science.aav7893
  Stringer2021: doi:10.1016/j.cell.2021.03.042
  Pachitariu2018: doi:10.1523/JNEUROSCI.3339-17.2018
  Ravello2016droplets: arXiv:1611.06834
  Russo2017: doi:10.7554/eLife.19428
  Grün2002: doi:10.1162/089976602753284464
  Torre2016: 10.1371/journal.pcbi.1004939
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Review on Polychrony detection in biological and artificial raster plots" />
  <meta name="citation_title" content="Review on Polychrony detection in biological and artificial raster plots" />
  <meta property="og:title" content="Review on Polychrony detection in biological and artificial raster plots" />
  <meta property="twitter:title" content="Review on Polychrony detection in biological and artificial raster plots" />
  <meta name="dc.date" content="2021-12-16" />
  <meta name="citation_publication_date" content="2021-12-16" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Antoine Grimaldi" />
  <meta name="citation_author_institution" content="Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université" />
  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />
  <meta name="twitter:creator" content="@WWWWWWWWWWWWW" />
  <meta name="citation_author" content="Laurent U Perrinet" />
  <meta name="citation_author_institution" content="Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université" />
  <meta name="citation_author_orcid" content="0000-0002-9536-010X" />
  <meta name="twitter:creator" content="@laurentperrinet" />
  <link rel="canonical" href="https://SpikeAI.github.io/polychronies/" />
  <meta property="og:url" content="https://SpikeAI.github.io/polychronies/" />
  <meta property="twitter:url" content="https://SpikeAI.github.io/polychronies/" />
  <meta name="citation_fulltext_html_url" content="https://SpikeAI.github.io/polychronies/" />
  <meta name="citation_pdf_url" content="https://SpikeAI.github.io/polychronies/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://SpikeAI.github.io/polychronies/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://SpikeAI.github.io/polychronies/v/be035f7de66ad723e99015997daee04bcf6060fa/" />
  <meta name="manubot_html_url_versioned" content="https://SpikeAI.github.io/polychronies/v/be035f7de66ad723e99015997daee04bcf6060fa/" />
  <meta name="manubot_pdf_url_versioned" content="https://SpikeAI.github.io/polychronies/v/be035f7de66ad723e99015997daee04bcf6060fa/manuscript.pdf" />
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
([permalink](https://SpikeAI.github.io/polychronies/v/be035f7de66ad723e99015997daee04bcf6060fa/))
was automatically generated
from [SpikeAI/polychronies@be035f7](https://github.com/SpikeAI/polychronies/tree/be035f7de66ad723e99015997daee04bcf6060fa)
on December 16, 2021.
</em></small>

## Authors



+ **Antoine Grimaldi**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [XXXX-XXXX-XXXX-XXXX](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [XXXXXXXX](https://github.com/XXXXXXXX)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [WWWWWWWWWWWWW](https://twitter.com/WWWWWWWWWWWWW)<br>
  <small>
     Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université
     · Funded by Grant XXXXXXXX
  </small>

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
     · Funded by Grant APROVIS3D; Grant AgileNeuroBot
  </small>



## Abstract {.page_break_before}

A crucial advantage of Spiking Neural Networks (SNNs) architectures lies in its processing of temporal information. Yet, most SNNs encode the temporal signal as an analog signal and try to “cross-compile” classical Neural Network to a spiking architecture. To go beyond the state-of-the-art, we will review here on one core computation of a spiking neuron, that is, is its ability to switch from the classical integrator mode (summing analog currents on its synapses) to a synchrony detector where it emits a spike whenever presynaptic spiking inputs are synchronized. To overcome the diversity of input presynaptic patterns, we will explore different existing architectures to learn to detect stable “polychronous“ events, that is, volleys of spikes which are stable up to certain synaptic delays. These models will be compared in light of neuroscientific and computational perspectives.


## introduction

### ultra fast neural codes

Most importantly, it will provide with a detection ability requiring only a few spikes, and therefore in line with the performance observed in biological systems, like the ability for humans to detect the presence of an animal in an image in a few milliseconds (Thorpe et al (1996). Speed of processing in the human visual system. Nature, 381(6582), 520-522). Such biological observations would serve as benchmarks to compare our proposed architecture  to conventional solutions.
(1] S Thorpe, D Fize, and C Marlot, Nature 381.6582 (1996), pp.520-522.



The approach which is currently most prominent in the Spiking Neural Networks community is to use existing algorithms from machine learning and to adapt them to the specificity of spiking architectures. One such example is to adapt the successes of deep learning algorithms and to transfer the back-propagation algorithm to SNNs, for instance with a surrogate gradient. This approach is quite successful, and SNNs approach in some case the performance of Deep Learning algorithms, for instance on the N-MNIST dataset for categorizing digits in a stream of events. However, most biological neural systems use spikes and are obviously more efficient than current state-of-the-art vision systems, both in terms of efficiency (accuracy), in speed (latency), and energy consumption. There is therefore an immense gap in the way we understand biology to translate it to the efficiency of SNNs. Our approach will be to focus on the temporal representation of information directly. In particular, our objective is to fully exploit the capacity of spiking neurons to detect synchronous patterns.

While my previous expertise was based on the modeling of how SNNs process information (Perrinet, Samuelides and Thorpe, 2004) and how these networks may be tuned in a unsupervised manner to their input (Perrinet, Samuelides and Thorpe, 2003), many different SNN architectures may provide robust solutions. Since that time, I have worked on exploring the space of all solutions which are the most efficient to solve a given problem using Bayesian methods. This culminated in defining a hierarchical model performing predictive coding (Boutin et al, 2020).  However, this network is analog and simulations perform too slowly, even on advanced GPU architectures, to be used for real life situation. We have recently developed a similar architecture but based on a SNN architecture.  In particular, this model is event-based from one end (sensory input from event-based cameras) to the other (classification) and its intermediate layers are learned in a self-supervised fashion (Grimaldi et al, 2021: a, b).

### timing encodes profile



Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural (Perrinet, Adams, Friston, 2012) and behavioral (Khoei et al, 2017) levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network (Grimaldi et al, 2021: a, b) will be crucial in the swift realization of this project.


Celebrini

[4] T Gollisch and M Meister, Science 319.5866 (2008), pp. 1108-1111.

### synfire chains

[@Abeles1991]: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.

M. Diesmann, M. O. Gewaltig, A. Aertsen, Nature402, 529 (1999).

 * [@Bienenstock1995] : from synfire chains to Synfire braids



### cortical songs [@Ikegaya2004]

* "We find precise repetitions of spontaneous patterns of synaptic inputs in neocortical neurons in vivo and in vitro. These patterns repeat after minutes, maintaining millisecond accuracy."
* Precisely repeating motifs of spontaneous synaptic activity in slices: duration around 1s +/- .5 s. Some events in motifs are of similar size but sometimes absent - better described by Bernouilli than SE (and covariance)
* *in vivo*  spontaneous activity also reveals repeating sequences. About 3000 sequences, each involving 3-10 cells out of about 900, and last up to 3 seconds
* topography: "Sequences had specific topographic structures, in some cases involving only a particular layer or a vertical column of cells or cells located in a cluster (Fig. 4, A and B, and fig. S3B). (...) Therefore, repeating temporal patterns of activation (...) were associated with a structured spatial organization of the neurons that formed them."
* "Cortical songs: modular assemblies of repeated sequences": hierarchical detection.
* in cotical songs, there is a "compressing timing" which may be taken into account by a similar mechanism as maxpooling in CNNs for space, but in time. Or there may be a mechanism for controlling the replay speed (pulvinar, ... ,  ?)

![Fig. 1. from  [@Ikegaya2004] Repeated motifs of spontaneous synaptic activity in vitro and in vivo. (A) Repeated motifs of intracellular activity from layer 5 pyramidal neurons in slices. Panels show segments (red) of the same voltage-clamp recording from the same cell repeating seconds or minutes after the initial occurrence (blue). Arrows indicate timings of repeated PSCs. (i) Upper trace: low–temporal resolution display of spontaneous activity of a neuron. Lower traces: higher resolution display of the repeated motif at indicated regions of the trace (a to c). (ii) Example of a longer motif. (B) Three repetitions of a motif. The top traces show the motifs superimposed on each other (blue, green, and red), the middle traces show these same traces individually, and the bottom traces show temporally magnified regions of the motifs (a to c). (C) Repeated sequences of intracellular current-clamp recordings in vivo. Two (i) and three (ii) repetitions of motifs are shown. Shuffle tests were performed on traces (i), a to c, yielding significantly fewer repeats (fig. S2, P < 0.02). In (i), the blue trace is shifted –2.75 mV; in (ii), the blue trace is shifted –1.58 mV, and the green +0.79 mV.](images/Ikegaya2004zse0150424620001.jpeg)

[@Luczak2015] Luczak A, McNaughton BL, Harris KD. Packet-based communication in the cortex. Nat Rev Neurosci. 2015;16(12):745–55.


### polychronization

Rapid Formation of Robust Auditory Memories: Insights from Noise [@Agus2010]




## Detecting patterns in raster plots

### Paper by [@Grossberger2018]

* Temporally ordered multi-neuron patterns likely encode information in the brain. We introduce an unsupervised method, SPOTDisClust (Spike Pattern Optimal Transport Dissimilarity Clustering), for their detection from high-dimensional neural ensembles. SPOTDisClust measures similarity between two ensemble spike patterns by determining the minimum transport cost of transforming their corresponding normalized cross-correlation matrices into each other (SPOTDis).
* Detecting these temporal patterns represents a major methodological challenge.
* Many approaches to this problem are supervised, that is, they take patterns occurring concurrently with a known event, such as the delivery of a stimulus for sensory neurons or the traversal of a running track for hippocampal place fields, as a “template” and then search for repetitions of the same template in spiking activity :
 * Nadasdy Z, Hirase H, Czurko A, Csicsvari J, Buzsaki G. Replay and time compression of recurring spike sequences in the hippocampus. J Neurosci. 1999;19(21):9497–507. pmid:10531452
 * Lee AK, Wilson MA. A combinatorial method for analyzing sequential firing patterns involving an arbitrary number of neurons based on relative time order. J Neurophysiol. 2004;92(4):2555–73. pmid:15212425
 * Davidson TJ, Kloosterman F, Wilson MA. Hippocampal replay of extended experience. Neuron. 2009;63(4):497–507. pmid:19709631
* only one spike per neuron: fig 1A = "For each pattern and each neuron, a random position was chosen for the activation pulse."
 * t-SNE projection with HDBSCAN labels shows that our clustering method can retrieve all patterns from the data.
* data available @ https://doi.org/10.1371/journal.pcbi.1006283.s013


![Fig 1 of @Grossberger2018: "Simulated example illustrating the steps in SPOTDisClust. A) Structure of five “ground-truth” patterns (...). For each pattern and each neuron, a random position was chosen for the activation pulse. B) Neuronal output is generated according to an inhomogeneous Poisson process, with rates dictated by the patterns in (A)."](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1006283/2/pcbi.1006283.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20211206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211206T141911Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=e02aea1035ceeae4a9f78125ae56023b4175eff75b2b5ccf17df20242d3507c0ae38a4532e0d7f846545d70a69b8a9a4c7d04389aa190f71c71cdaaebe2790b4520135b30e5cfbce58cd00a1730e4c2347b01e81fbdf2ff1374cea9498c740df44087a56e7d143301656f1016432ea9cbf69b94dda26976f5db0597e10e215e340f5a59ca5fe4a33f45c8aae73b326206c97cb7a46cce97cfa0700555baa4b3925497c8a168454a49808c175015385277ea8edb794b7d7ac921c0833c27681ae9fc8301ed5e29da386fa0fc572ee490db1f5d93a938508fdcd20438c9d2bec19e64ef525471e41bbf7a1e14145f2ca8d71e02eb6c17ea681360628d563f7eee7){#fig:G2018-1 width="7in"}

### Russo et al 2017 [@Russo2017]

* "Here we present such a unifying methodological and conceptual framework which detects assembly structure at many different time scales, levels of precision, and with arbitrary internal organization. " by @Russo2017
* sliding window as in [@Grün2002] ("Numerous other statistical procedures for detecting assemblies or sequential patterns have been proposed previously") - extended to multiple lags [@Torre2016]
* based on a "non-stationarity-corrected parametric test statistic for assessing the independence of pairs" and "an agglomerative, heuristic clustering algorithm for fusing significant pairs into higher-order assemblies"

### Rastermap

* https://www.janelia.org/lab/stringer-lab
* described in [@Pachitariu2018]
* [rastermap](https://github.com/MouseLand/rastermap)
 * deconvolution strategy
 * based on a linear model

#### Stringer et al 2019, Nature [@Stringer2019nature]

* "A neuronal population encodes information most efficiently when its stimulus responses are high-dimensional and uncorrelated, and most robustly when they are lower-dimensional and correlated. Here we analysed the dimensionality of the encoding of natural images by large populations of neurons in the visual cortex of awake mice. "
* Data availability: All of the processed deconvolved calcium traces are available on [figshare](https://figshare.com/articles/Recordings_of_ten_thousand_neurons_in_visual_cortex_in_response_to_2_800_natural_images/6845348), together with the image stimuli.
* Code availability: The code is available on [GitHub](https://github.com/MouseLand/stringer-pachitariu-et-al-2018b).

#### Stringer et al 2019, Science [@Stringer2019science]

* Stringer et al. analyzed spontaneous neuronal firing, finding that neurons in the primary visual cortex encoded both visual information and motor activity related to facial movements. The variability of neuronal responses to visual stimuli in the primary visual area is mainly related to arousal and reflects the encoding of latent behavioral states.

* see also the work showing that you can encode very precise orientation information by using many neurons: [@Stringer2021]

#### Paper by [@Moser2014]

On Stability of Distance Measures for Event Sequences Induced by Level-Crossing Sampling



### outline

The rest of this review paper is organized as follows:

* polychronization

* We review theoretical foundations of spike time coding in a neuron: We will describe the Spike-Time Dependent Plasticity (STDP) rule which implement an unsupervised learning aiming at optimizing the detection of polychronous patterns, that is volleys of spikes which are synchronized, up to some stable pattern of pre-synaptic delays. This STDP rule will be based by the inversion of the generative model for spike formation and will therefore be derived by a Bayesian approach. This will decouple the active synapses (similarly to a logistic regression) from the values of possible synaptic delays.

* Application to Image processing using sparse spiking representations: Using the core computational unit defined, extension of the computation to a topographic representation similar to that observed in the primary visual cortex of mammals. design of micro-circuits with specific lateral interactions will allow us to design efficient micro-circuits for the sparse representation of images.

* Discussion on Ultra-fast vision:  existing datasets recorded in natural settings or indoor scenes with event-based cameras.



## Models of polychronization

### Izhikevitch



## Learning to detect polychronous groups

### Learning delays: STDP

[@Perrinet2002] : coherence detection
[@Perrinet2001] : STDP



## Learning delays

### STDP

[@Perrinet2002] : coherence detection
[@Perrinet2001] : STDP


::: {.cell .markdown nteract="{\"transient\":{\"deleting\":false}}"}
### test notebook
:::

::: {.cell .code execution_count="1" collapsed="true" execution="{\"iopub.execute_input\":\"2021-12-02T10:36:25.737Z\",\"iopub.status.busy\":\"2021-12-02T10:36:25.734Z\",\"iopub.status.idle\":\"2021-12-02T10:36:26.390Z\",\"shell.execute_reply\":\"2021-12-02T10:36:26.395Z\"}" jupyter="{\"outputs_hidden\":false,\"source_hidden\":false}" nteract="{\"transient\":{\"deleting\":false}}"}
``` python
import numpy as np
print(f'{np.pi=}')
```

::: {.output .stream .stdout}
    np.pi=3.141592653589793
:::
:::

::: {.cell .code collapsed="true" jupyter="{\"outputs_hidden\":false,\"source_hidden\":false}" nteract="{\"transient\":{\"deleting\":false}}"}
``` python
```
:::



### results on natural images

in  [@natural],  we generate raster plots from natural images

A natural documentary, Planet Earth with David Attenborough

```
filename = './nat_inputs/PlanetEarth.mp4'  # filename of the movie
```




## Detecting patterns in raster plots

In generic linear non linear lnl models, the output is assumed to be poisson As such a simple decoding strategy is to asscume it is to b inferned foran tuning curves (Jayazeri) or simply by a simple regression (Berens) This latter model aissunes a Bernouilt model for the generation of spites such that the decoding amounts to a single logistic regression.


### Paper by [@Grossberger2018]

* Temporally ordered multi-neuron patterns likely encode information in the brain. We introduce an unsupervised method, SPOTDisClust (Spike Pattern Optimal Transport Dissimilarity Clustering), for their detection from high-dimensional neural ensembles. SPOTDisClust measures similarity between two ensemble spike patterns by determining the minimum transport cost of transforming their corresponding normalized cross-correlation matrices into each other (SPOTDis).
* Detecting these temporal patterns represents a major methodological challenge.
* Many approaches to this problem are supervised, that is, they take patterns occurring concurrently with a known event, such as the delivery of a stimulus for sensory neurons or the traversal of a running track for hippocampal place fields, as a “template” and then search for repetitions of the same template in spiking activity :
 * Nadasdy Z, Hirase H, Czurko A, Csicsvari J, Buzsaki G. Replay and time compression of recurring spike sequences in the hippocampus. J Neurosci. 1999;19(21):9497–507. pmid:10531452
 * Lee AK, Wilson MA. A combinatorial method for analyzing sequential firing patterns involving an arbitrary number of neurons based on relative time order. J Neurophysiol. 2004;92(4):2555–73. pmid:15212425
 * Davidson TJ, Kloosterman F, Wilson MA. Hippocampal replay of extended experience. Neuron. 2009;63(4):497–507. pmid:19709631
* only one spike per neuron: fig 1A = "For each pattern and each neuron, a random position was chosen for the activation pulse."
 * t-SNE projection with HDBSCAN labels shows that our clustering method can retrieve all patterns from the data.
* data available @ https://doi.org/10.1371/journal.pcbi.1006283.s013


![Fig 1 of @Grossberger2018: "Simulated example illustrating the steps in SPOTDisClust. A) Structure of five “ground-truth” patterns (...). For each pattern and each neuron, a random position was chosen for the activation pulse. B) Neuronal output is generated according to an inhomogeneous Poisson process, with rates dictated by the patterns in (A)."](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1006283/2/pcbi.1006283.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20211206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211206T141911Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=e02aea1035ceeae4a9f78125ae56023b4175eff75b2b5ccf17df20242d3507c0ae38a4532e0d7f846545d70a69b8a9a4c7d04389aa190f71c71cdaaebe2790b4520135b30e5cfbce58cd00a1730e4c2347b01e81fbdf2ff1374cea9498c740df44087a56e7d143301656f1016432ea9cbf69b94dda26976f5db0597e10e215e340f5a59ca5fe4a33f45c8aae73b326206c97cb7a46cce97cfa0700555baa4b3925497c8a168454a49808c175015385277ea8edb794b7d7ac921c0833c27681ae9fc8301ed5e29da386fa0fc572ee490db1f5d93a938508fdcd20438c9d2bec19e64ef525471e41bbf7a1e14145f2ca8d71e02eb6c17ea681360628d563f7eee7){#fig:G2018-1 width="7in"}

### Russo et al 2017 [@Russo2017]

* "Here we present such a unifying methodological and conceptual framework which detects assembly structure at many different time scales, levels of precision, and with arbitrary internal organization. " by @Russo2017
* sliding window as in [@Grün2002] ("Numerous other statistical procedures for detecting assemblies or sequential patterns have been proposed previously") - extended to multiple lags [@Torre2016]
* based on a "non-stationarity-corrected parametric test statistic for assessing the independence of pairs" and "an agglomerative, heuristic clustering algorithm for fusing significant pairs into higher-order assemblies"

### Rastermap

* https://www.janelia.org/lab/stringer-lab
* described in [@Pachitariu2018]
* [rastermap](https://github.com/MouseLand/rastermap)
 * deconvolution strategy
 * based on a linear model

#### Stringer et al 2019, Nature [@Stringer2019nature]

* "A neuronal population encodes information most efficiently when its stimulus responses are high-dimensional and uncorrelated, and most robustly when they are lower-dimensional and correlated. Here we analysed the dimensionality of the encoding of natural images by large populations of neurons in the visual cortex of awake mice. "
* Data availability: All of the processed deconvolved calcium traces are available on [figshare](https://figshare.com/articles/Recordings_of_ten_thousand_neurons_in_visual_cortex_in_response_to_2_800_natural_images/6845348), together with the image stimuli.
* Code availability: The code is available on [GitHub](https://github.com/MouseLand/stringer-pachitariu-et-al-2018b).

#### Stringer et al 2019, Science [@Stringer2019science]

* Stringer et al. analyzed spontaneous neuronal firing, finding that neurons in the primary visual cortex encoded both visual information and motor activity related to facial movements. The variability of neuronal responses to visual stimuli in the primary visual area is mainly related to arousal and reflects the encoding of latent behavioral states.

* see also the work showing that you can encode very precise orientation information by using many neurons: [@Stringer2021]

#### Paper by [@Moser2014]

On Stability of Distance Measures for Event Sequences Induced by Level-Crossing Sampling



## Discussion


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
