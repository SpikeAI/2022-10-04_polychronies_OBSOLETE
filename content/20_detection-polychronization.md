
## Models of polychronization detection in models

A model for the detection of latency patterns is the tempotron
[@doi:10/ch29r4]. This model is in particular reviewed in [@doi:10.1016/j.conb.2014.01.004]. The Tempotron is a supervised synaptic learning algorithm which classifies a distractor from a target motif. This aims at extending the perceptron which does not incorporate a spike timing framework. The tempotron learning rule is derived by an optimization process and takes the form of a STDP rule.  It is general consensus that spike timing (STDP) plays a crucial role in the development of synaptic efficacy for many different kinds of neurons [@doi:10.1146/annurev.neuro.31.060407.125639]. The limits of this model is that it's output is only binary and that it's staorage capacity are limited.

Some other models of latency motifs detection using STDP learning rules. For instance, [@10.1016/j.neunet.2017.12.005] implements a STDP-based spiking deep convolutional neural networks for object recognition;  [@doi:10.1016/j.neunet.2018.05.018] develops a form of spike-based, competitive learning applied for unsupervised learning.

In [@10.7554/eLife.19428], authors developed novel machine learning tools and statistical tests for unsupervised spatio-temporal pattern detection in non-stationary environments, which was applied to simultaneous electrophysiological recordings from tens to hundreds of neurons for decoding cognitive processes from neural activity.

### polychronization Izhikevitch

Considering the number of spikes required to exceed a voltage threshold, asynchronous signals are less efficient than synchronous signals. However, taking axonal propagation times into account, synchronous signals may not coincide significantly at the post-synaptic neuron contrary to asynchronous or polychronous signals. The term polychronous was first introduced in 2006, by E. Izhichevitch in [@doi: 10.1162/089976606775093882]. He defines this term after pointing out a particular organization of the neurons of his spiking artificial neural network. The network is characterized by a timing-dependant learning rule for weights (STDP) and by fixed conduction delays between neurons. Due to the interplay between the delays and STDP, the spiking neurons spontaneously self-organize into groups and generate patterns of stereotypical polychronous activity, i.e. exhibit reproducible time-locked but not synchronous firing patterns. The neurons composing a group discharge at different times, but due to delays, the spikes reach the postsynaptic neuron at the same time. This synchrony leads to the summation of the excitatory post-synaptic potentials evoked by each spike and thus to the crossing of the voltage threshold and to the discharge of a spike. According to the STDP rule, the neurons involved in this activity will see their weight of synaptic connection increase and thus, constitute a polychronous group. Interestingly, thanks to the fact that a neuron can be involved in different polychronous groups,  the number of coexisting polychronous groups far exceeds the number of neurons in the network, resulting in an unprecedented memory capacity of the system.

[
<i class="fas fa-ban fa-lg"></i> **TODO**<br>

-> insert fig 2 of [@doi: 10.1162/089976606775093882]

Thus, the learning of delays allowing this polychronous group organization may be useful to detect temporal sequences of interest.

* Reproducing Polychronization: A Guide to Maximizing the Reproducibility of Spiking Network Models <https://www.frontiersin.org/articles/10.3389/fninf.2018.00046/full>
  * comes with python code

* blog post by Paxon Frady <https://epaxon.blogspot.com/2012/07/izhikevich-2006-polychronization.html>

* dynamic networks & learning delays:
  * Huning H., Glunder H., and Palm G. (1998) Synaptic delay learning in pulse-coupled neurons. Neural Computation, 10:555–565. <https://www.deepdyve.com/lp/mit-press/synaptic-delay-learning-in-pulse-coupled-neurons-DGMiNHxp0A>

  * [Eurich C., Pawelzik K., Ernst U., Cowan J., and Milton J. (1999) Dynamics of self-organazed delay adaptation. Phys. Rev. Lett., 82:1594–1597.](https://www.researchgate.net/publication/37921636_Dynamics_of_Self-Organized_Delay_Adaptation)

  * The recent "multi-neuronal spike sequence detector" (MNSD) architecture integrates the weight- and delay-adjustment methods by combining heterosynaptic plasticity with the neurocomputational feature spike latency : <https://pubmed.ncbi.nlm.nih.gov/33679293/>

  * an extensive (graph-centric) review on [Synchronization in time-varying networks](https://arxiv.org/abs/2109.07618)

]{.banner .lightred}


A Bayesian account: "Previous methods for studying the PNG activation response to stimuli have been limited by the template-based methods used to identify PNG activation. In this letter, we outline a new method that overcomes these difficulties by establishing for the first time a probabilistic interpretation of PNG activation. We then demonstrate the use of this method by investigating the claim that PNGs might provide the foundation of a representational system." [@10.1162/NECO_a_00620].  Stimulation of a trained network produces the activation of a PNG, ie the propagation of firing activity through multiple layers due to convergent patterns of firing.

### spike distances




<i class="fas fa-ban fa-lg"></i> **TODO**<br>
J. D. Victor and K. P. Purpura, “Nature and precision of temporal coding in visual cortex: a metric-space analysis,” J. Neurophysiol., vol. 76, pp. 1310–1326, Aug. 1996.

M. C. W. van Rossum, “A novel spike distance,” Neural Comput., vol. 13, no. 4, pp. 751–763, 2001. [21] D. Aronov and J. D. Victor, “Non-Euclidean properties of spike train metric spaces,” Physical Rev. E (Statist., Nonlinear, Soft Matter Phys.), vol. 69, no. 6, 2004.

T. Kreuz, J. S. Haas, A. Morelli, H. D. I. Abarbanel, and A. Politi, “Measuring spike train synchrony,” J. Neurosci. Methods, vol. 165, no. 1, pp. 151–161, 2007. [23] H.

Paper by [@Moser2014] On Stability of Distance Measures for Event Sequences Induced by Level-Crossing Sampling

Weyl's discrepency measure [@doi:10.1007/BF01475864] which may lead to the definition of a cross-correlation.


Robust computation with rhythmic spike patterns. Proceedings of the National Academy of Sciences of the United States of America 116(36), 18050 - 18059. https://dx.doi.org/10.1073/pnas.1902653116

]{.banner .lightred}


Memory traces in dynamical systems [@doi:10.1073/pnas.0804451105] : "To perform nontrivial, real-time computations on a sensory input stream, biological systems must retain a short-term memory trace of their recent inputs. It has been proposed that generic high-dimensional dynamical systems could retain a memory trace for past inputs in their current state. This raises important questions about the fundamental limits of such memory traces and the properties required of dynamical systems to achieve these limits. We address these issues by applying Fisher information theory to dynamical systems driven by time-dependent signals corrupted by noise. We introduce the Fisher Memory Curve (FMC) as a measure of the signal-to-noise ratio (SNR) embedded in the dynamical state relative to the input SNR. The integrated FMC indicates the total memory capacity. We apply this theory to linear neuronal networks and show that the capacity of networks with normal connectivity matrices is exactly 1 and that of any network of N neurons is, at most, N. A nonnormal network achieving this bound is subject to stringent design constraints: It must have a hidden feedforward architecture that superlinearly amplifies its input for a time of order N, and the input connectivity must optimally match this architecture. The memory capacity of networks subject to saturating nonlinearities is further limited, and cannot exceed √𝑁. This limit can be realized by feedforward structures with divergent fan out that distributes the signal across neurons, thereby avoiding saturation. We illustrate the generality of the theory by showing that memory in fluid systems can be sustained by transient nonnormal amplification due to convective instability or the onset of turbulence."

We address these issues by applying Fisher information theory to dynamical systems driven by time-dependent signals corrupted by noise.  Memory capacity is constrained by architecture: "This limit can be realized by feedforward structures with divergent fan out that distributes the signal across neurons, thereby avoiding saturation."
