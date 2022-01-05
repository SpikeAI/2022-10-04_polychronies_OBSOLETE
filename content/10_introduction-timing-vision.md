## introduction

### ultra fast neural codes

Most importantly, it will provide with a detection ability requiring only a few spikes, and therefore in line with the performance observed in biological systems, like the ability for humans to detect the presence of an animal in an image in a few milliseconds (Thorpe et al (1996). Speed of processing in the human visual system. Nature, 381(6582), 520-522). Such biological observations would serve as benchmarks to compare our proposed architecture  to conventional solutions.
(1] S Thorpe, D Fize, and C Marlot, Nature 381.6582 (1996), pp.520-522.



The approach which is currently most prominent in the Spiking Neural Networks community is to use existing algorithms from machine learning and to adapt them to the specificity of spiking architectures. One such example is to adapt the successes of deep learning algorithms and to transfer the back-propagation algorithm to SNNs, for instance with a surrogate gradient. This approach is quite successful, and SNNs approach in some case the performance of Deep Learning algorithms, for instance on the N-MNIST dataset for categorizing digits in a stream of events. However, most biological neural systems use spikes and are obviously more efficient than current state-of-the-art vision systems, both in terms of efficiency (accuracy), in speed (latency), and energy consumption. There is therefore an immense gap in the way we understand biology to translate it to the efficiency of SNNs. Our approach will be to focus on the temporal representation of information directly. In particular, our objective is to fully exploit the capacity of spiking neurons to detect synchronous patterns.

While my previous expertise was based on the modeling of how SNNs process information (Perrinet, Samuelides and Thorpe, 2004) and how these networks may be tuned in a unsupervised manner to their input (Perrinet, Samuelides and Thorpe, 2003), many different SNN architectures may provide robust solutions. Since that time, I have worked on exploring the space of all solutions which are the most efficient to solve a given problem using Bayesian methods. This culminated in defining a hierarchical model performing predictive coding (Boutin et al, 2020).  However, this network is analog and simulations perform too slowly, even on advanced GPU architectures, to be used for real life situation. We have recently developed a similar architecture but based on a SNN architecture.  In particular, this model is event-based from one end (sensory input from event-based cameras) to the other (classification) and its intermediate layers are learned in a self-supervised fashion (Grimaldi et al, 2021: a, b).

### dynamical models

Dumas and colleagues [@arxiv:2112.12147] : three levels


### timing encodes profile


#### timing in natural images

in  [@natural],  we generate raster plots from natural images

A natural documentary, Planet Earth with David Attenborough

```
filename = './nat_inputs/PlanetEarth.mp4'  # filename of the movie
```

Note also that timing is not entirely sensorial or internal but in [@doi:10.1073/pnas.1921226117], they found that "timing accuracy was improved when the environment afforded cues that rats can incorporate into motor routines. Timing, at least in animals, may thus be fundamentally embodied and situated."

####  delays

Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural (Perrinet, Adams, Friston, 2012) and behavioral (Khoei et al, 2017) levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network (Grimaldi et al, 2021: a, b) will be crucial in the swift realization of this project.


Celebrini

[4] T Gollisch and M Meister, Science 319.5866 (2008), pp. 1108-1111.


### synfire chains

In [@Abeles1991] corticonics: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.

M. Diesmann, M. O. Gewaltig, A. Aertsen, Nature402, 529 (1999).


 * [@Bienenstock1995] : from synfire chains to Synfire braids

 * recent theories of binding by synchrony : Fries 2005 trends cog neuro with spikes arriving at peak susceptibility (top of a cycle) or down, van Rullen, Laura Dugué
