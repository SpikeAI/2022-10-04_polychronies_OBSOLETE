
## Learning to detect polychronous groups

### Learning weights ... and delays

spike time coding in a neuron: We will describe the Spike-Time Dependent Plasticity (STDP) [@doi:10/ftvvd8] rule which implement an unsupervised learning aiming at optimizing the detection of polychronous patterns, that is volleys of spikes which are synchronized, up to some stable pattern of pre-synaptic delays. This STDP rule will be based by the inversion of the generative model for spike formation and will therefore be derived by a Bayesian approach. This will decouple the active synapses (similarly to a logistic regression) from the values of possible synaptic delays.


[@Perrinet2002] : coherence detection
[@Perrinet2001] : STDP


### Learning sequences


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
Pang R, Fairhall AL.Elife. 2019 May

Emergence of spontaneous assembly activity in developing neural networks without afferent input.
Triplett MA, Avitan L, Goodhill GJ.PLoS Comput Biol. 2018

Training and Spontaneous Reinforcement of Neuronal Assemblies by Spike Timing Plasticity.
Ocker GK, Doiron B.Cereb Cortex. 2019.
