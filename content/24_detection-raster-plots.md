## Detecting precise heterosynaptic spiking motifs in biological raster plots
[#sec:detection]



### spike distances


<i class="fas fa-ban fa-lg"></i> **TODO**<br>
J. D. Victor and K. P. Purpura, “Nature and precision of temporal coding in visual cortex: a metric-space analysis,” J. Neurophysiol., vol. 76, pp. 1310–1326, Aug. 1996.

M. C. W. van Rossum, “A novel spike distance,” Neural Comput., vol. 13, no. 4, pp. 751–763, 2001. [21] D. Aronov and J. D. Victor, “Non-Euclidean properties of spike train metric spaces,” Physical Rev. E (Statist., Nonlinear, Soft Matter Phys.), vol. 69, no. 6, 2004.

T. Kreuz, J. S. Haas, A. Morelli, H. D. I. Abarbanel, and A. Politi, “Measuring spike train synchrony,” J. Neurosci. Methods, vol. 165, no. 1, pp. 151–161, 2007. [23] H.

Paper by [@Moser2014] On Stability of Distance Measures for Event Sequences Induced by Level-Crossing Sampling

Weyl's discrepency measure [@doi:10.1007/BF01475864] which may lead to the definition of a cross-correlation.


Robust computation with rhythmic spike patterns. Proceedings of the National Academy of Sciences of the United States of America 116(36), 18050 - 18059. https://dx.doi.org/10.1073/pnas.1902653116

]{.banner .lightred}


### decoding neural activity

In generic linear non linear lnl models, the output is assumed to be poisson. As such a simple decoding strategy is to asscume it is to b inferned for a given tuning curves (Jayazeri) or simply by a simple regression [@doi:10.1523/jneurosci.1335-12.2012]. This latter model assumes a Bernoulli model for the generation of spikes such that the decoding amounts to a single-layer logistic regression.


Unitary event analysis is performed by a statistical model of coincidence detection [@doi:10.1007/978-1-4419-5675-0_10]. This was extensively used in detecting above chance significant synchronous patterns, in particular in recordings of pairs of neurons (see [@doi:10.1126/science.278.5345.1950] for instance).

Statistical evaluation of synchronous spike patterns extracted by frequent item set mining -  a method to detect significant patterns of synchronous spiking in a subset of massively parallel spike trains in the presence of background activity  [@doi:10.3389/fncom.2013.00132]. By the same group the SPADE, CAD or ASSET algorithms are methods for identification of spike patterns in massively parallel spike trains (the spiking activity of tens to hundred(s) of neurons recorded in parallel) by identifying fine temporal correlations in the ms precision range [@doi:10.1007/s00422-018-0755-0].

This was recently extended in "3d-SPADE: Significance evaluation of spatio-temporal patterns of various temporal extents" [@doi:10.1016/j.biosystems.2019.104022] in order to find reoccurring spike patterns in parallel spike train data, and to determine their statistical significance. The extension improves the performance in the presence of patterns with different durations, as here demonstrated by application to various synthetic data.


A review of the methods for neuronal response latency estimation including bayesian binning [@doi:10.1016/j.biosystems.2015.04.008].

[@doi:]


TODO: summarize "Understanding Auditory Spectro-Temporal Receptive Fields and Their Changes with Input Statistics by Efficient Coding Principles" - Spectro-temporal receptive fields (STRFs) have been widely used as linear approximations to the signal transform from sound spectrograms to neural responses along the auditory pathway. Their dependence on statistical attributes of the stimuli, such as sound intensity, is usually explained by nonlinear mechanisms and models. Here, we apply an efficient coding principle which has been successfully used to understand receptive fields in early stages of visual processing, in order to provide a computational understanding of the STRFs. According to this principle, STRFs result from an optimal tradeoff between maximizing the sensory information the brain receives, and minimizing the cost of the neural activities required to represent and transmit this information. Both terms depend on the statistical properties of the sensory inputs and the noise that corrupts them. The STRFs should therefore depend on the input power spectrum and the signal-to-noise ratio, which is assumed to increase with input intensity. We analytically derive the optimal STRFs when signal and noise are approximated as Gaussians. Under the constraint that they should be spectro-temporally local, the STRFs are predicted to adapt from being band-pass to low-pass filters as the input intensity reduces, or the input correlation becomes longer range in sound frequency or time. These predictions qualitatively match physiological observations. Our prediction as to how the STRFs should be determined by the input power spectrum could readily be tested, since this spectrum depends on the stimulus ensemble. The potentials and limitations of the efficient coding principle are discussed.
[@doi:10.1371/journal.pcbi.1002123]

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


To overcome the limits of models which require spike times to be discretized, utilize a sub-optimal least-squares criterion, or do not provide uncertainty estimates for model predictions or estimated parameters, [@arXiv:2010.04875]  address each of these shortcomings by developing a point process model that characterizes fine-scale sequences at the level of individual spikes and represents sequence occurrences as a small number of marked events in continuous time. They also introduce learnable time warping parameters to model sequences of varying duration, which have been experimentally observed in neural circuits and demonstrate these advantages on experimental recordings from songbird higher vocal center and rodent hippocampus.

#### Dynamics of Delay-Coupled Excitable Neural Systems

uses a FPGA
[@doi:10.1142/S0218127409023111]


    February 2009International Journal of Bifurcation and Chaos 19(02):745-753

V. Thanasoulis, B. Vogginger, J. Partzsch and C. Mayr, "Delay-Based Neural Computation: Pulse Routing Architecture and Benchmark Application in FPGA," 2021 28th IEEE International Conference on Electronics, Circuits, and Systems (ICECS), 2021, pp. 1-5
[@doi:10.1109/ICECS53924.2021.9665468]

#### Cell assemblies at multiple time scales with arbitrary lag constellations

[@doi:10.7554/eLife.19428] starts from the relatively old notion of assessing the departure of the joint spike count distribution of two units (or sets) from independence. It is based on unitary events in multiple single-neuron spiking activity  [@doi:10.1162/089976602753284455] and the  reliable and efficient analysis of an excess or deficiency of joint-spike events  [@doi:10.1007/s10827-007-0065-3].  Having derived a fast, non-stationarity-corrected parametric test statistic for assessing the independence of pairs, they designed an agglomerative, heuristic clustering algorithm for fusing significant pairs into higher-order assemblies.
