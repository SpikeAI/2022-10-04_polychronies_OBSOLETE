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

In [@Abeles1991], Abeles asked if the role of cortical neurons is whether to integrate synaptic inputs or rather to detect coincidences in temporal spiking patterns. corticonics: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

While the first role favors the rate coding theory, the second possibility highlights the need for temporal precision in the neural code. Since, numerous studies demonstrated the emergence of synchronicity in neuron population activity [@doi:10.1126/science.278.5345.1950, @doi:10/gm79hh], efficient encoding thanks to the use of spike latencies [@Perrinet2004, @doi:10.1126/science.1149639] or precise timing in the auditory system [@url:https://repository.cshl.edu/id/eprint/30941, @doi:10.1523/JNEUROSCI.10-10-03227.1990]. All these findings, and more [@doi:10.1023/B:NACO.0000027755.02868.60], highlight the importance of the temporal aspect of the neural code and suggest the existence of repeated spatio-temporal patterns in the spike train.

In neuronal models, an efficient use or detection of these spatio-temporal patterns embedded in the spike train comes with the integration of heterogeneous delays [@doi:10/ch29r4, @doi:10/f6chbq, @doi:10.1016/j.neucom.2020.03.079]. Notably, Izhikevich [@Izhikevich2006] introduced the notion of polychronous groups (PGs) as a repetitive motif of spikes defined by a subset of neurons with different, yet precise,  spiking delays. This representation has a much greater information capacity in comparison to other neural coding approaches through their connectivity and the possible coexistence of numerous superposed PGs.

It was shown that a simple model may allow the propagation of such synfire chains [@pmid:11665761].

![Simulation [using Brian](https://brian2.readthedocs.io/en/stable/examples/frompapers.Diesmann_et_al_1999.html) ](https://brian2.readthedocs.io/en/stable/_images/frompapers.Diesmann_et_al_1999.1.png)

#### synfire braids
sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.


 * [@Bienenstock1995] : from synfire chains to Synfire braids

 * recent theories of binding by synchrony : Fries 2005 trends cog neuro with spikes arriving at peak susceptibility (top of a cycle) or down, van Rullen, Laura Dugué


 * A notable exception is the polychronization model of Izhikevich [@Izhikevich2006], which combined the construction of a random recurrent model of spiking neurons including such delays and whose weights evolved with a Spike-Time Dependent Plasticity (STDP) learning rule. In this model, raster plot analysis showed repeated activation of Polychronous Groups (PGs), i.e., specific spike patterns with a specific sequence of activations.

#### link to traveling waves and synaptic delays

[@doi:10.1038/s41467-021-26175-1]



Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural [@doi:10.1007/s00422-014-0620-8] and behavioral [@doi:10.1371/journal.pcbi.1005068] levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network [@doi:10.1109/CBMI50038.2021.9461901,@doi:Grimaldi2022pami] will be crucial in the swift realization of this project.
