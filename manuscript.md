---
title: Review on Polychrony detection in biological and artificial raster plots
keywords:
- neurons
- code
- time
lang: en-US
date-meta: '2022-03-02'
author-meta:
- Camille Besnainou
- Antoine Grimaldi
- Laurent U Perrinet
citekey-aliases:
  Abeles1991: isbn:9780521376174
  Izhikevich2006: doi:10.1162/089976606775093882
  Thorpe1996: doi:10/c4v35x
  Grimaldi2021: doi:10.1109/CBMI50038.2021.9461901
  Grimaldi2022: doi:10.36227/techrxiv.18003077.v1
  Perrinet2004: doi:10.1109/TNN.2004.833303
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
  Torre2016: doi:10.1371/journal.pcbi.1004939
  Orban2016: doi:10.1016/j.neuron.2016.09.038
  Gollish2008: doi:10.1016/j.neuron.2010.04.014
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
  <meta name="dc.date" content="2022-03-02" />
  <meta name="citation_publication_date" content="2022-03-02" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Camille Besnainou" />
  <meta name="citation_author_institution" content="Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université" />
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
  <link rel="alternate" type="text/html" href="https://SpikeAI.github.io/polychronies/v/91e282d8b2518dd0a3160af83ec329ed4729bcde/" />
  <meta name="manubot_html_url_versioned" content="https://SpikeAI.github.io/polychronies/v/91e282d8b2518dd0a3160af83ec329ed4729bcde/" />
  <meta name="manubot_pdf_url_versioned" content="https://SpikeAI.github.io/polychronies/v/91e282d8b2518dd0a3160af83ec329ed4729bcde/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.bib
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://SpikeAI.github.io/polychronies/v/91e282d8b2518dd0a3160af83ec329ed4729bcde/))
was automatically generated
from [SpikeAI/polychronies@91e282d](https://github.com/SpikeAI/polychronies/tree/91e282d8b2518dd0a3160af83ec329ed4729bcde)
on March 2, 2022.
</em></small>

## Authors



+ **Camille Besnainou**<br>
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [camillebesnainou](https://github.com/camillebesnainou)<br>
  <small>
     Institut de Neurosciences de la Timone, CNRS / Aix-Marseille Université
     · Funded by Grant AgileNeuroBot
  </small>

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


Why do neurons communicate through action potentials, or spikes? An action potential is a binary event —it can occur or not, without further details— and asynchronous, i.e. it can occur at any time. In the living world, neurons almost systematically use this so-called event-based representation, though we do not yet have a clear idea why. A better understanding of this phenomenon remains a fundamental challenge in neurobiology in order to better interpret the masses of recorded data. It is also an emerging challenge in computer science to allow the efficient exploitation of a new class of sensors and impulse computers, called neuromorphic, which could allow significant gains in computing time and energy consumption —a major societal challenge in the age of the digital economy and of global warming.


The response of a biological neuron depends largely on the precise timing of the sequence of presynaptic spikes as they reach the basal dendritic tree. This *event-based representation* present in the neuronal code is essential in understanding information processing in the brain but also applies to other fields, for instance to the output of an event-based camera. However, most neuronal models do not take advantage of this minute temporal dimension, especially in exploiting the variety of synaptic delays on the dendritic tree. Our goal here is to bring an interdisciplinary perspective on the computational advantage of time series representations for the brain and for information processing machines. In particular, we will formalize mathematically a representation in an assembly of neurons based on a set of patterns of different relative spike times. Following the terminology of [@Izhikevich2006], we will define such motifs of precise temporal patterns as **polychronous groups** and this manuscript reviews current litterature on *polychrony detection* in generic raster plots. It is work in progress, where anybody interested can *openly* join. This hypothesis is directly inspired by neurobiological observations in the hippocampus, and it expands the capabilities of analog representations based on the firing rate by considering a representation based on repetitions of these polychronous groups at precise times of occurrence. This formalization is particularly well suited to neuromorphic computing, and allows for supervised or self-supervised learning of polychronous groups in any event-driven data.

We will first review some biological and theoretical evidence for polychrony in the neural information processing. We will then present some models for the detection of such polychronous groups in arbitrary raster plots, synthetic, biological or artificial (notably from event-based cameras). Then, we will try to outline some possible strategies for learning these patterns and finally discuss possible perspectives.


## Introduction: precise temporal patterns in the brain

### Ultra fast neural codes for ultra fast vision

Let us start our review of the state of the art on the role of dynamics in vision by presenting some surprising results that have been obtained in neuroscience. Indeed, Simon Thorpe's group has shown that humans can categorize briefly presented images in a fraction of a second.
This experiment consisted in asking subjects to categorize images that contain or do not contain animals [@Thorpe1996]. The results showed that humans were able to perform this task very well (with a success rate of more than 95%) but above all that a differential activity for the two categories of images could be observed by electroencephalography, showing that this differentiation emerges at a very early latency in neuronal activity. These results have been extended to several species including primates but also extended to different experimental protocols and have shown for example that the response could be extremely fast of the order of 120 ms when the task was to perform a saccade [@doi:10/d8gpjq].

This fast processing also explains the surprising experiments of fast serial detection which consists in presenting a fast succession of different images and to decode via the EEG if the observer can detect for example the presence of an animal. The performances decrease progressively as the frequency of presentation of the images increases. However, it has been shown in the macaque that a significant performance could be maintained with an image presentation time of only 14 ms per image [@doi:10.1162/089892901564199].

This speed of the visual cortex, although surprising, is quite compatible with the latencies that are recorded at the neuro-physiological level. Indeed, when an image is presented on the retina, the visual information is rapidly propagated to the thalamus and then to the primary visual cortex takes about 55 ms in the macaque [@doi:10.1007/978-1-4757-9625-4_5]. This functioning of visual processing as a forward pass is most prominent in fast processing but can be complemented with feedback loops from the higher areas to the sensory areas [@doi:10/ccv3w2].

### How timing encodes analogous profile

An important characteristic of neuronal information is that it consists mainly in the transfer of action potentials, or spikes, which consist of brief impulses that propagate along the axons of neurons. These have the particularity of being essentially binary in their amplitude (that is to say, they are prototypical, all or nothing). An important consequence of the speed of processing is that it implies that it is carried out using only very few spikes. Indeed, if we consider that a behavioral response in only 120 ms consists of about ten processing stages following the "forward" pathways of the visual system, then this imposes that the processing in a single area is performed with a reduced number of spikes.

At the level of dynamic processing of visual information, it has been shown that an encoding of the values of luminance imminence in the image instead of the retina [@doi:10.1126/science.1149639]. Notably one can appreciate in figure 1 that the response of ganglion cells to visual gratings that are flashed onto the retina. The authors showed that the neuronal response could be encoded in the latency of the response and not only in the frequency of discharge as is often assumed. In figure 4 of the same article, these results are extended to natural images and show a qualitatively similar behavior. The conclusion of the authors is that the discharge latency of the neurons allows to encode spatial characteristics of the image.

Similar results have been demonstrated through neurophysiological recordings in the primary visual cortex and show that different levels of visual activity will induce different levels of neuronal discharge latency in the primary visual area [@doi:10/dqt5cm]. Many models have used these properties in temporal coding to build fast image categorization networks. These models take the form of artificial spiking neural networks (SNNs) and have been able to demonstrate their practical applications for image categorization [@Perrinet2004]. This work has been extended to include unsupervised learning capabilities and we have recently developed a SNN architecture that allows to categorize images of different classes in only a few spikes [@Grimaldi2021, @Grimaldi2022]. This type of modeling is extremely important with respect to the development of a new generation of cameras called Silicon Cameras which, instead of using a basic frame-based representation, uses a representation similar to the one we have just described and which consists in representing the image by events [@arxiv:2201.12673]. This type of modeling often uses the classical architecture of image categorization developed in deep learning while adapting it to the specificity of the event-based representation [@arXiv:1912.11443]. Note also that timing is not entirely sensorial or internal but in [@doi:10.1073/pnas.1921226117], they found that "timing accuracy was improved when the environment afforded cues that rats can incorporate into motor routines. Timing, at least in animals, may thus be fundamentally embodied and situated."


### TODO: synfire chains

In [@Abeles1991] corticonics: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

M. Diesmann, M. O. Gewaltig, A. Aertsen, Nature402, 529 (1999).


#### synfire braids
sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.


 * [@Bienenstock1995] : from synfire chains to Synfire braids

 * recent theories of binding by synchrony : Fries 2005 trends cog neuro with spikes arriving at peak susceptibility (top of a cycle) or down, van Rullen, Laura Dugué


 * A notable exception is the polychronization model of Izhikevich [@Izhikevich2006], which combined the construction of a random recurrent model of spiking neurons including such delays and whose weights evolved with a Spike-Time Dependent Plasticity (STDP) learning rule. In this model, raster plot analysis showed repeated activation of Polychronous Groups (PGs), i.e., specific spike patterns with a specific sequence of activations.

#### link to traveling waves and synaptic delays

[@doi:10.1038/s41467-021-26175-1]



Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural [@doi:10.1007/s00422-014-0620-8] and behavioral [@doi:10.1371/journal.pcbi.1005068] levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network [@doi:10.1109/CBMI50038.2021.9461901,@doi:Grimaldi2022pami] will be crucial in the swift realization of this project.




### precise temporal patterns TODO read [@Luczak2015]


[@Luczak2015] Luczak A, McNaughton BL, Harris KD. Packet-based communication in the cortex. Nat Rev Neurosci. 2015;16(12):745–55.

In [@doi:10.1016/j.neuron.2020.12.013], it was shown that attentional information from V4 or arousal can change the timings of groups of events in V1. They develop a HMM model for quantifying the transitions. "In this study, van Kempen et al. show that fluctuations in neural excitability are coordinated between visual areas with retinotopic precision. Top-down attention drives interareal coordination along the reverse cortical hierarchy, predicting better behavioral performance with increased coordination."

### cortical songs [@Ikegaya2004]

* Ikegaya and colleagues worked on spontaneous activity in vitro and in vivo. They demonstated that in cortical activity, we can find a repetition of several motifs. In PSCs, but also in spike activity. These sequences repeat after minutes and have a precise spatio temporal structure with a ms precision. They can be specific of a particular layer or colomn, are synchronized with network activity oscillation and can involve several cells. They also demonstated that these sequences can form supersequences : the cortical songs. It consist of the assembly of several sequences which repeat in a specific order with a compressed timing.


* "We find precise repetitions of spontaneous patterns of synaptic inputs in neocortical neurons in vivo and in vitro. These patterns repeat after minutes, maintaining millisecond accuracy."
* Precisely repeating motifs of spontaneous synaptic activity in slices: duration around 1s +/- .5 s. Some events in motifs are of similar size but sometimes absent - better described by Bernouilli than SE (and covariance)
* *in vivo*  spontaneous activity also reveals repeating sequences. About 3000 sequences, each involving 3-10 cells out of about 900, and last up to 3 seconds
* topography: "Sequences had specific topographic structures, in some cases involving only a particular layer or a vertical column of cells or cells located in a cluster (Fig. 4, A and B, and fig. S3B). (...) Therefore, repeating temporal patterns of activation (...) were associated with a structured spatial organization of the neurons that formed them."
* "Cortical songs: modular assemblies of repeated sequences": hierarchical detection.
* in cotical songs, there is a "compressing timing" which may be taken into account by a similar mechanism as maxpooling in CNNs for space, but in time. Or there may be a mechanism for controlling the replay speed (pulvinar, ... ,  ?)

![Fig. 1. from  [@Ikegaya2004] Repeated motifs of spontaneous synaptic activity in vitro and in vivo. (A) Repeated motifs of intracellular activity from layer 5 pyramidal neurons in slices. Panels show segments (red) of the same voltage-clamp recording from the same cell repeating seconds or minutes after the initial occurrence (blue). Arrows indicate timings of repeated PSCs. (i) Upper trace: low–temporal resolution display of spontaneous activity of a neuron. Lower traces: higher resolution display of the repeated motif at indicated regions of the trace (a to c). (ii) Example of a longer motif. (B) Three repetitions of a motif. The top traces show the motifs superimposed on each other (blue, green, and red), the middle traces show these same traces individually, and the bottom traces show temporally magnified regions of the motifs (a to c). (C) Repeated sequences of intracellular current-clamp recordings in vivo. Two (i) and three (ii) repetitions of motifs are shown. Shuffle tests were performed on traces (i), a to c, yielding significantly fewer repeats (fig. S2, P < 0.02). In (i), the blue trace is shifted –2.75 mV; in (ii), the blue trace is shifted –1.58 mV, and the green +0.79 mV.](images/Ikegaya2004zse0150424620001.jpeg)


It is interesting to make a parallel with the "Rapid Formation of Robust Auditory Memories" reported in [@Agus2010] which uses noise patterns. They " used random waveforms to probe the formation of new memories for arbitrary complex sounds. A behavioral measure was designed, based on the detection of repetitions embedded in noises up to 4 s long." The  task is to detect the repetition of the same (frozen) noise within a trial. " Unbeknownst to listeners, some noise samples reoccurred randomly throughout an experimental block." they showed that the "repeated exposure induced learning for otherwise totally unpredictable and meaningless sounds" by showing that the sensitivity increases in that case. Note that "acoustical analyses failed to reveal any obvious differences between good and bad noises" and that "Time reversal had no significant effect on the RefRN advantage" (quite surprising). The Learning is unsupervised (statistical, automatic), fast-acting (phase transition, "insight"), and long-lasting (memorization).

### polychronization



### outline




The approach which is currently most prominent in the Spiking Neural Networks community is to use existing algorithms from machine learning and to adapt them to the specificity of spiking architectures. One such example is to adapt the successes of deep learning algorithms and to transfer the back-propagation algorithm to SNNs, for instance with a surrogate gradient. This approach is quite successful, and SNNs approach in some case the performance of Deep Learning algorithms, for instance on the N-MNIST dataset for categorizing digits in a stream of events. However, most biological neural systems use spikes and are obviously more efficient than current state-of-the-art vision systems, both in terms of efficiency (accuracy), in speed (latency), and energy consumption. There is therefore an immense gap in the way we understand biology to translate it to the efficiency of SNNs. Our approach will be to focus on the temporal representation of information directly. In particular, our objective is to fully exploit the capacity of spiking neurons to detect synchronous patterns.



This section has provided evidence that polychronous groups are an important apsect of information representation in biology with important application in data analysis and neuromorphic engineering. The rest of this review paper is organized as follows.

First, we will review models for the detection of polychronous groups:

* A crucial advantage of Spiking Neural Networks (SNNs) architectures lies in its processing of temporal information. Yet, most SNNs encode the temporal signal as an analog signal and try to “cross-compile” classical Neural Network to a spiking architecture. To go beyond the state-of-the-art, we will review here on one core computation of a spiking neuron, that is, is its ability to switch from the classical integrator mode (summing analog currents on its synapses) to a synchrony detector where it emits a spike whenever presynaptic spiking inputs are synchronized. To overcome the diversity of input presynaptic patterns, we will explore different existing architectures to learn to detect stable “polychronous“ events, that is, volleys of spikes which are stable up to certain synaptic delays. These models will be compared in light of neuroscientific and computational perspectives. We review theoretical and computational foundations of PG detection in models.

* Application to Image processing using sparse spiking representations: Using the core computational unit defined, extension of the computation to a topographic representation similar to that observed in the primary visual cortex of mammals. design of micro-circuits with specific lateral interactions will allow us to design efficient micro-circuits for the sparse representation of images.

Finally we will discuss future avenues for effective PG detection and learning in event streams.



## Models of polychronization detection in models



### Izhikevitch

* Reproducing Polychronization: A Guide to Maximizing the Reproducibility of Spiking Network Models <https://www.frontiersin.org/articles/10.3389/fninf.2018.00046/full>
  * comes with python code

* blog post by Paxon Frady <https://epaxon.blogspot.com/2012/07/izhikevich-2006-polychronization.html>

* dynamic networks & learning delays:
  * Huning H., Glunder H., and Palm G. (1998) Synaptic delay learning in pulse-coupled neurons. Neural Computation, 10:555–565. <https://www.deepdyve.com/lp/mit-press/synaptic-delay-learning-in-pulse-coupled-neurons-DGMiNHxp0A>
  * [Eurich C., Pawelzik K., Ernst U., Cowan J., and Milton J. (1999) Dynamics of self-organazed delay adaptation. Phys. Rev. Lett., 82:1594–1597.](https://www.researchgate.net/publication/37921636_Dynamics_of_Self-Organized_Delay_Adaptation)
  * The recent "multi-neuronal spike sequence detector" (MNSD) architecture integrates the weight- and delay-adjustment methods by combining heterosynaptic plasticity with the neurocomputational feature spike latency : <https://pubmed.ncbi.nlm.nih.gov/33679293/>
  * an extensive (graph-centric) review on [Synchronization in time-varying networks](https://arxiv.org/abs/2109.07618)
* related


### spike distances


J. D. Victor and K. P. Purpura, “Nature and precision of temporal coding in visual cortex: a metric-space analysis,” J. Neurophysiol., vol. 76, pp. 1310–1326, Aug. 1996.

M. C. W. van Rossum, “A novel spike distance,” Neural Comput., vol. 13, no. 4, pp. 751–763, 2001. [21] D. Aronov and J. D. Victor, “Non-Euclidean properties of spike train metric spaces,” Physical Rev. E (Statist., Nonlinear, Soft Matter Phys.), vol. 69, no. 6, 2004.

T. Kreuz, J. S. Haas, A. Morelli, H. D. I. Abarbanel, and A. Politi, “Measuring spike train synchrony,” J. Neurosci. Methods, vol. 165, no. 1, pp. 151–161, 2007. [23] H.

Paper by [@Moser2014] On Stability of Distance Measures for Event Sequences Induced by Level-Crossing Sampling

Weyl's discrepency measure [@doi:10.1007/BF01475864] which may lead to the definition of a cross-correlation.


Robust computation with rhythmic spike patterns. Proceedings of the National Academy of Sciences of the United States of America 116(36), 18050 - 18059. https://dx.doi.org/10.1073/pnas.1902653116


Memory traces in dynamical systems [@doi:10.1073pnas.0804451105] We address these issues by applying Fisher information theory to dynamical systems driven by time-dependent signals corrupted by noise.  Memory capacity is constrained by architecture: "This limit can be realized by feedforward structures with divergent fan out that distributes the signal across neurons, thereby avoiding saturation."


## Detecting patterns in biological raster plots

### decoding neural activity

In generic linear non linear lnl models, the output is assumed to be poisson. As such a simple decoding strategy is to asscume it is to b inferned for a given tuning curves (Jayazeri) or simply by a simple regression [@doi:10.1523/jneurosci.1335-12.2012]. This latter model assumes a Bernoulli model for the generation of spikes such that the decoding amounts to a single-layer logistic regression.


S. Grun, M. Diesmann, and A. Aertsen. Unitary event analysis. In Analysis of parallel spike trains, pages 191–220. Springer, 2010. + coincidence detection


### Rastermap : decoding large-scale data

[Rastermap](https://nbviewer.org/github/MouseLand/rastermap/blob/master/tutorial/tutorial.ipynb) re-arranges neurons in the raster plot based on similarity of activity

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


### detecting structured temporal patterns
#### Paper by Grossberger, 2018 [@Grossberger2018]

* Temporally ordered multi-neuron patterns likely encode information in the brain. We introduce an unsupervised method, SPOTDisClust (Spike Pattern Optimal Transport Dissimilarity Clustering), for their detection from high-dimensional neural ensembles. SPOTDisClust measures similarity between two ensemble spike patterns by determining the minimum transport cost of transforming their corresponding normalized cross-correlation matrices into each other (SPOTDis).
* Detecting these temporal patterns represents a major methodological challenge.
* Many approaches to this problem are supervised, that is, they take patterns occurring concurrently with a known event, such as the delivery of a stimulus for sensory neurons or the traversal of a running track for hippocampal place fields, as a “template” and then search for repetitions of the same template in spiking activity :
 * Nadasdy Z, Hirase H, Czurko A, Csicsvari J, Buzsaki G. Replay and time compression of recurring spike sequences in the hippocampus. J Neurosci. 1999;19(21):9497–507. pmid:10531452
 * Lee AK, Wilson MA. A combinatorial method for analyzing sequential firing patterns involving an arbitrary number of neurons based on relative time order. J Neurophysiol. 2004;92(4):2555–73. pmid:15212425
 * Davidson TJ, Kloosterman F, Wilson MA. Hippocampal replay of extended experience. Neuron. 2009;63(4):497–507. pmid:19709631
* only one spike per neuron: fig 1A = "For each pattern and each neuron, a random position was chosen for the activation pulse."
 * t-SNE projection with HDBSCAN labels shows that our clustering method can retrieve all patterns from the data.
* data available @ https://doi.org/10.1371/journal.pcbi.1006283.s013

![Fig 1 of @Grossberger2018: "Simulated example illustrating the steps in SPOTDisClust. A) Structure of five “ground-truth” patterns (...). For each pattern and each neuron, a random position was chosen for the activation pulse. B) Neuronal output is generated according to an inhomogeneous Poisson process, with rates dictated by the patterns in (A)." (© Authors under a [CC licence](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006283))](images/pcbi.1006283.g001.PNG_L.png){#fig:G2018-1 width="7in"}

* "However, SPOTDis has two principal weaknesses that we address here: (1) Its computational complexity, for comparing two time epochs, is O(N2), where N is the number of neurons. This becomes a major problem for computing an MM dissimilarity matrix (for M time epochs) for thousands of neurons. (2) It relies exclusively on pairwise spike-timing relationships (i.e 2nd order correlations), because it does not solve the optimal transport problem for the entire spike pattern, but only for neuron pairs separately. Hence, it may not be sensitive to higher-order correlations in spiking
patterns.
Here, we develop a novel dissimilarity measure for multi-neuron spiking patterns called SpikeShip, which has linear computational complexity of O(N). We achieve this by (1) computing the minimum transport cost of spikes for each spike train separately, and (2) discounting a global translation term in the transport flow across neurons."
https://doi.org/10.1101/2020.06.03.131573;

#### Paper by Russo et al 2017 [@Russo2017]

* "Here we present such a unifying methodological and conceptual framework which detects assembly structure at many different time scales, levels of precision, and with arbitrary internal organization. " by @Russo2017
* sliding window as in [@Grün2002] ("Numerous other statistical procedures for detecting assemblies or sequential patterns have been proposed previously") - extended to multiple lags [@Torre2016]
* based on a "non-stationarity-corrected parametric test statistic for assessing the independence of pairs" and "an agglomerative, heuristic clustering algorithm for fusing significant pairs into higher-order assemblies"


#### Neural Variability and Sampling-Based Probabilistic Representations in the Visual Cortex [@Orban2016]

 * Stochastic sampling links perceptual uncertainty to neural response variability
 * Model accounts for independent changes in strength and variability of responses
 * Model predicts relationship between noise, signal, and spontaneous correlations
 * Stimulus statistics dependence of response statistics is explained


#### FPGA

Dynamics of Delay-Coupled Excitable Neural Systems.

    February 2009International Journal of Bifurcation and Chaos 19(02):745-753

    DOI: 10.1142/S0218127409023111

V. Thanasoulis, B. Vogginger, J. Partzsch and C. Mayr, "Delay-Based Neural Computation: Pulse Routing Architecture and Benchmark Application in FPGA," 2021 28th IEEE International Conference on Electronics, Circuits, and Systems (ICECS), 2021, pp. 1-5, doi: 10.1109/ICECS53924.2021.9665468.



## Learning to detect polychronous groups

### Learning weights ... and delays

spike time coding in a neuron: We will describe the Spike-Time Dependent Plasticity (STDP) [@doi:10/ftvvd8] rule which implement an unsupervised learning aiming at optimizing the detection of polychronous patterns, that is volleys of spikes which are synchronized, up to some stable pattern of pre-synaptic delays. This STDP rule will be based by the inversion of the generative model for spike formation and will therefore be derived by a Bayesian approach. This will decouple the active synapses (similarly to a logistic regression) from the values of possible synaptic delays.


[@Perrinet2002] : coherence detection
[@Perrinet2001] : STDP


[@arxiv:2011.09380]

Bio-plausible Unsupervised Delay Learning for Extracting Temporal Features in Spiking Neural Networks
Alireza Nadafian, Mohammad Ganjtabesh

    The plasticity of the conduction delay between neurons plays a fundamental role in learning. However, the exact underlying mechanisms in the brain for this modulation is still an open problem. Understanding the precise adjustment of synaptic delays could help us in developing effective brain-inspired computational models in providing aligned insights with the experimental evidence. In this paper, we propose an unsupervised biologically plausible learning rule for adjusting the synaptic delays in spiking neural networks. Then, we provided some mathematical proofs to show that our learning rule gives a neuron the ability to learn repeating spatio-temporal patterns. Furthermore, the experimental results of applying an STDP-based spiking neural network equipped with our proposed delay learning rule on Random Dot Kinematogram indicate the efficacy of the proposed delay learning rule in extracting temporal features.

### Learning sequences

In [@doi:10.1073/pnas.1815910116], authors present a model to "show a way by which the nervous system maintains precise, stereotyped behavior in the face of environmental and neural changes". It is shown in bridsong generation that "A precise, temporally sparse sequence from the premotor nucleus HVC is crucial to the performance of song in songbirds" [@pmid:12490259,@pmid:8308169,@pmid:8791594] and this model shows how one could vary HVC activity using something similar to dropout in ML. Using such controlled variability, "behaviors are made more robust to environmental change by continually seeking subtly new ways of performing the same task". Not sure however how important it is that the HVC pattern should be sparse (and similar to PGs).

* in [@Agus2010], there are ‘‘good’’ and ‘‘bad’’ noises show that some patterns are more easy to disentangle - similar to bird songs and ecological niche.

* In Bellec [@arxiv:2106.10064], authors fit summary statistics of neural data with a differentiable spiking network simulator.
  * the loss function is the cross entropy (following Bernouilli hypothesis with a GLM where each unit is modelled with a SRM neuron [@doi:10/cwcn9d] with recurrent dynamics)
  * sample and measure method to include latent / hidden neurons
  * comes with code https://github.com/EPFL-LCN/pub-bellec-wang-2021-sample-and-measure
  * V1-dataset : The dataset we used was collected by Smith and Kohn [49] and is publicly available at:
http://crcns.org/data-sets/vc/pvc-11 - it is in a sense supervised with the input being the movie and the output the spikes recorded.

### TODO: more bib to read
Learning compositional sequences with multiple time scales through a hierarchical network of spiking neurons.
Maes A, Barahona M, Clopath C.PLoS Comput Biol. 2021

Characteristics of sequential activity in networks with temporally asymmetric Hebbian learning.
Gillett M, Pereira U, Brunel N.Proc Natl Acad Sci U S A. 2020

Unsupervised Learning of Persistent and Sequential Activity.
Pereira U, Brunel N.Front Comput Neurosci. 2020

From space to time: Spatial inhomogeneities lead to the emergence of spatiotemporal sequences in spiking neuronal networks.
Spreizer S, Aertsen A, Kumar A.PLoS Comput Biol. 2019

Fast and flexible sequence induction in spiking neural networks via rapid excitability changes.
Pang R, Fairhall AL.Elife. 2019 May [@doi:10.7554/eLife.44324.001]

Emergence of spontaneous assembly activity in developing neural networks without afferent input.
Triplett MA, Avitan L, Goodhill GJ.PLoS Comput Biol. 2018

Training and Spontaneous Reinforcement of Neuronal Assemblies by Spike Timing Plasticity.
Ocker GK, Doiron B.Cereb Cortex. 2019.



### learning pattern detection on natural images / event-based cameras


#### sparse coding on spatio-temporal data


#### HOTS


#### Grimaldi CBMI / PAMI



## Discussion



### dynamical models

Dumas and colleagues [@arxiv:2112.12147] : three levels / fourth paradigm [@doi:10.1109/JPROC.2011.2155130] i.e., data exploration in which the scientific models are fit to the data by learning algorithms.


### our model

Here, we develop a model for the efficient detection of such PGs based on the inversion of a probabilistic model defining the generation of the raster plot as a combination of such groups. We show that such an inference can be achieved by a neural-like computation that could itself be used as a spiking neuron, as can be implemented in a neuromorphic chip for instance. A first result is to show the efficiency of such a scheme in detecting different PGs occurring at specific times in synthetic data. The representational capacity of the PGs is particularly interesting compared to traditional models of neuronal encoding using spiking frequency. Our second result is to propose a novel learning method for learning PGs in raster plots in a self-supervised manner. Finally we demonstrate the use of this algorithm to the output of an event-based camera and how this may separate independent components from the stream of events. This end-to-end event-based computational brick could help improve the performance of current Spiking Neural Network solution currently used in neuromorphic chips.


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
