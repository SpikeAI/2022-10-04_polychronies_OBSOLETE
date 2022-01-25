## introduction: precise temporal patterns in the brain

### ultra fast neural codes

Most importantly, it will provide with a detection ability requiring only a few spikes, and therefore in line with the performance observed in biological systems, like the ability for humans to detect the presence of an animal in an image in a few milliseconds (Thorpe et al (1996). Speed of processing in the human visual system. Nature, 381(6582), 520-522). Such biological observations would serve as benchmarks to compare our proposed architecture to conventional solutions.
(1] S Thorpe, D Fize, and C Marlot, Nature 381.6582 (1996), pp.520-522.

The approach which is currently most prominent in the Spiking Neural Networks community is to use existing algorithms from machine learning and to adapt them to the specificity of spiking architectures. One such example is to adapt the successes of deep learning algorithms and to transfer the back-propagation algorithm to SNNs, for instance with a surrogate gradient. This approach is quite successful, and SNNs approach in some case the performance of Deep Learning algorithms, for instance on the N-MNIST dataset for categorizing digits in a stream of events. However, most biological neural systems use spikes and are obviously more efficient than current state-of-the-art vision systems, both in terms of efficiency (accuracy), in speed (latency), and energy consumption. There is therefore an immense gap in the way we understand biology to translate it to the efficiency of SNNs. Our approach will be to focus on the temporal representation of information directly. In particular, our objective is to fully exploit the capacity of spiking neurons to detect synchronous patterns.

While my previous expertise was based on the modeling of how SNNs process information (Perrinet, Samuelides and Thorpe, 2004) and how these networks may be tuned in a unsupervised manner to their input (Perrinet, Samuelides and Thorpe, 2003), many different SNN architectures may provide robust solutions. Since that time, I have worked on exploring the space of all solutions which are the most efficient to solve a given problem using Bayesian methods. This culminated in defining a hierarchical model performing predictive coding (Boutin et al, 2020).  However, this network is analog and simulations perform too slowly, even on advanced GPU architectures, to be used for real life situation. We have recently developed a similar architecture but based on a SNN architecture.  In particular, this model is event-based from one end (sensory input from event-based cameras) to the other (classification) and its intermediate layers are learned in a self-supervised fashion (Grimaldi et al, 2021: a, b).


Lamme and Roelfsemma, 2000

Nowak and Bullier, 1997

RSVP - 17ms per image


### how timing encodes analogous profile

[@doi:10.1126/science.1149639] T Gollisch and M Meister, Science 319.5866 (2008), pp. 1108-1111.
Fig. 1. Ganglion cell responses to flashed gratings with different spatial phases.
Gollisch and colaborators demonstrated that depending on the shifted of a square-wave grating, the OFF ganglion cells of the retina modify their activity. They encode structural information not by the number of spikes, but by the latency of appearance of the first spikes.

Fig. 4. Responses of a fast OFF ganglion cell to a flashed natural image. (For results from other cell types, see fig. S9.)
The projection of a natural image on the retina leads to an encoding of the spatial information by the OFF ganglion cells in a rather faithful way. Depending on the luminosity, the ganglion cells respond with different latencies. If we make a gray-scale plot of the
differential spike latency according to the location of the receptor field of the ganglion cells, we obtain a representation of the presented image that is much more faithful than by doing a gray-scale plot of spike count.


Celebrini [@doi:10/dqt5cm]


Used in models like [@arXiv:1912.11443] : Fast and energy-efficient neuromorphic deep learning with first-spike times


#### timing in natural images

in  [@natural],  we generate raster plots from natural images

Note also that timing is not entirely sensorial or internal but in [@doi:10.1073/pnas.1921226117], they found that "timing accuracy was improved when the environment afforded cues that rats can incorporate into motor routines. Timing, at least in animals, may thus be fundamentally embodied and situated."

####  delays

Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural [@doi:10.1007/s00422-014-0620-8] and behavioral [@doi:10.1371/journal.pcbi.1005068] levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network [@doi:10.1109/CBMI50038.2021.9461901,@doi:Grimaldi2022pami] will be crucial in the swift realization of this project.



#### synfire chains

In [@Abeles1991] corticonics: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.

M. Diesmann, M. O. Gewaltig, A. Aertsen, Nature402, 529 (1999).


 * [@Bienenstock1995] : from synfire chains to Synfire braids

 * recent theories of binding by synchrony : Fries 2005 trends cog neuro with spikes arriving at peak susceptibility (top of a cycle) or down, van Rullen, Laura Dugué


 * A notable exception is the polychronization model of Izhikevich (2006), which combined the construction of a random recurrent model of spiking neurons including such delays and whose weights evolved with a Spike-Time Dependent Plasticity (STDP) learning rule. In this model, raster plot analysis showed repeated activation of Polychronous Groups (PGs), i.e., specific spike patterns with a specific sequence of activations.

#### traveling waves

[@doi:10.1038/s41467-021-26175-1]
