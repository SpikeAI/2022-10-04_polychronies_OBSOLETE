
## Learning to detect polychronous groups


### Learning weights ... and delays

spike time coding in a neuron: We will describe the Spike-Time Dependent Plasticity (STDP) [@doi:10/ftvvd8] rule which implement an unsupervised learning aiming at optimizing the detection of polychronous patterns, that is volleys of spikes which are synchronized, up to some stable pattern of pre-synaptic delays. This STDP rule will be based by the inversion of the generative model for spike formation and will therefore be derived by a Bayesian approach. This will decouple the active synapses (similarly to a logistic regression) from the values of possible synaptic delays.


* [@Perrinet2002] : coherence detection
* [@Perrinet2001] : STDP
* Masquelier, Gilson et al. - 2010 - STDP in Recurrent Neuronal Networks [@doi:10.3389/fncom.2010.00023] or Delay Selection by Spike-Timing-Dependent Plasticity in Recurrent Networks of Spiking Neurons Receiving Oscillatory Inputs. PLoS Comput Biol 9(2): e1002897. [@doi:10.1371/journal.pcbi.1002897] which targets at the selective potentiation of recurrent connections with different axonal and dendritic delays during oscillatory activity.

 Our ability to track and respond to rapidly changing visual stimuli, such as a fast-moving tennis ball, indicates that the brain is capable of extrapolating the trajectory of a moving object to predict its current position, despite the delays that result from neural transmission. Here, we show how the neural circuits underlying this ability can be learned through spike-timing-dependent synaptic plasticity and that these circuits emerge spontaneously and without supervision. This demonstrates how the neural transmission delays can, in part, be compensated to implement the extrapolation mechanisms required to predict where a moving object is at the present moment. [@doi:10.1523/JNEUROSCI.2017-20.2021]

<i class="fas fa-ban fa-lg"></i>
**TODO amelie** section sur l'apprentissage des délais dans la biologie<br>

[@arxiv:2011.09380]

]{.banner .lightred}

Bio-plausible Unsupervised Delay Learning for Extracting Temporal Features in Spiking Neural Networks
Alireza Nadafian, Mohammad Ganjtabesh

    The plasticity of the conduction delay between neurons plays a fundamental role in learning. However, the exact underlying mechanisms in the brain for this modulation is still an open problem. Understanding the precise adjustment of synaptic delays could help us in developing effective brain-inspired computational models in providing aligned insights with the experimental evidence. In this paper, we propose an unsupervised biologically plausible learning rule for adjusting the synaptic delays in spiking neural networks. Then, we provided some mathematical proofs to show that our learning rule gives a neuron the ability to learn repeating spatio-temporal patterns. Furthermore, the experimental results of applying an STDP-based spiking neural network equipped with our proposed delay learning rule on Random Dot Kinematogram indicate the efficacy of the proposed delay learning rule in extracting temporal features.


Integrating synaptic delay plasticity into supervised learning and proposes a novel learning method that adjusts both the synaptic delays and weights of the learning neurons to make them fire precisely timed spikes, that is referred to as synaptic delay-weight plasticity [@doi:10.1016/j.neucom.2020.03.079]. Uses synthetic data to extend the existing Remote Supervised Method (ReSuMe) method.

In a recent paper [@doi:10.1109/TNNLS.2022.3164930], authors propose a gradient descent-based learning algorithm for synaptic delays to enhance the sequential learning performance of single spiking neuron. In this algorithm, information is encoded in the relative timing of individual neuronal spikes, and learning is performed based on the exact derivatives of the postsynaptic spike times with respect to presynaptic spike times.

In a computational model, authors show that the frequently activated polychronous neuronal groups can be learned by readout neurons with joint weight-delay spike-timing-dependent plasticity [@doi:10.1162/NECO_a_00879]. This uses a joint Weight-Delay Spike-Timing-Dependent Plasticity and show aan efficient learning of polychronous groups.

### Learning sequences

In [@doi:10.1073/pnas.1815910116], authors present a model to "show a way by which the nervous system maintains precise, stereotyped behavior in the face of environmental and neural changes". It is shown in bridsong generation that "A precise, temporally sparse sequence from the premotor nucleus HVC is crucial to the performance of song in songbirds" [@pmid:12490259; @pmid:8308169; @pmid:8791594] and this model shows how one could vary HVC activity using something similar to dropout in ML. Using such controlled variability, "behaviors are made more robust to environmental change by continually seeking subtly new ways of performing the same task". Not sure however how important it is that the HVC pattern should be sparse (and similar to PGs).

* in [@Agus2010], there are ‘‘good’’ and ‘‘bad’’ noises show that some patterns are more easy to disentangle - similar to bird songs and ecological niche.

* In Bellec [@arxiv:2106.10064], authors fit summary statistics of neural data with a differentiable spiking network simulator.
  * the loss function is the cross entropy (following Bernouilli hypothesis with a GLM where each unit is modelled with a SRM neuron [@doi:10/cwcn9d] with recurrent dynamics)
  * sample and measure method to include latent / hidden neurons
  * comes with code https://github.com/EPFL-LCN/pub-bellec-wang-2021-sample-and-measure
  * V1-dataset : The dataset we used was collected by Smith and Kohn [49] and is publicly available at:
http://crcns.org/data-sets/vc/pvc-11 - it is in a sense supervised with the input being the movie and the output the spikes recorded.

A recent work [@doi:10.48550/arXiv.1903.07067] proposes a two-stage unsupervised-supervised system for the categorization of spatiotemporal actions from an event-based stream. The first stage learns spatiotemporal convolutional filters targeted to minimize event-removal related changes to a local spatiotemporal spike-event pattern. The second stage takes the output of the spatiotemporal filters as an input example containing multiple feature channels, and proceeds to train a classifier for recognition of spatiotemporal activity. For testing the system, two datasets are considered: DVS Gesture and a new action recognition dataset recorded for this work. Results demonstrate the ability of the system to outperform the state-of-the-art in event-based gesture recognition, along with demonstrating superior performance to other alternative ways of obtaining the first stage filters. Showing the potential of such representation

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
]{.banner .lightred}
