### outline

A natural candidate to use these precise temporal patterns in the brain is to use Spiking Neural Networks (SNNs) [@Maass97]. The approach which is at present most prominent in the SNNs community is to use existing algorithms from machine learning and to adapt them to the specificity of spiking architectures. One such example is to adapt the successes of deep learning algorithms and to transfer the back-propagation algorithm to SNNs, for instance with a surrogate gradient. This approach is quite successful, and SNNs approach in some case the performance of Deep Learning algorithms, for instance on the N-MNIST dataset for categorizing digits in a stream of events. However, most biological neural systems use spikes and are obviously more efficient than current state-of-the-art vision systems, both in terms of efficiency (accuracy), in speed (latency), and energy consumption. There is therefore an immense gap in the way we understand biology to translate it to the efficiency of SNNs. Our approach will be to focus on the temporal representation of information directly. In particular, our objective is to fully exploit the capacity of spiking neurons to detect synchronous patterns.

[
<i class="fas fa-ban fa-lg"></i> **TODO: a paragraph on our existing work**<br>
Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level.

there are temporal delays in the nervous system, both at the neural [@doi:10.1007/s00422-014-0620-8] and behavioral [@doi:10.1371/journal.pcbi.1005068] levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks.

may be used for motion detection and interpolation [@Kaplan13] [@KhoeiMassonPerrinet17]

]{.banner .lightred}


Remarkably, novel neuromorphic chips use a representation similar to that of real neurons [@arxiv:2201.12673]. For example, event-based cameras provide a stream of binary asynchronous events signaling detectable changes in luminance, and information is represented by these spike-based temporal motifs, hence their name "silicon retinas" (see Figure @fig:silicon_retina). For such devices, it is crucial to better understand the potential of using such event-based representations in order to devise novel algorithms.

![A miniature, event-based ATIS sensor. Contrary to a classical frame-based camera for which a full dense image representation is given at discrete, regularly spaced timings, the event-based camera provides with events at the micro-second resolution. These are sparse as they represent luminance increments or decrements (ON and OFF events, respectively).](https://laurentperrinet.github.io/grant/anr-anr/event_driven_computations.png){#fig:silicon_retina}

This section has provided evidence that polychronous groups are an important apsect of information representation in biology with important application in data analysis and neuromorphic engineering. The rest of this review paper is organized as follows.

First, we will review models for the detection of polychronous groups:

* A crucial advantage of Spiking Neural Networks (SNNs) architectures lies in its processing of temporal information. Yet, most SNNs encode the temporal signal as an analog signal and try to “cross-compile” classical Neural Network to a spiking architecture. To go beyond the state-of-the-art, we will review here on one core computation of a spiking neuron, that is, is its ability to switch from the classical integrator mode (summing analog currents on its synapses) to a synchrony detector where it emits a spike whenever presynaptic spiking inputs are synchronized. To overcome the diversity of input presynaptic patterns, we will explore different existing architectures to learn to detect stable “polychronous“ events, that is, volleys of spikes which are stable up to certain synaptic delays. These models will be compared in light of neuroscientific and computational perspectives. We review theoretical and computational foundations of PG detection in models.

* Application to Image processing using sparse spiking representations: Using the core computational unit defined, extension of the computation to a topographic representation similar to that observed in the primary visual cortex of mammals. design of micro-circuits with specific lateral interactions will allow us to design efficient micro-circuits for the sparse representation of images.

Finally we will discuss future avenues for effective PG detection and learning in event streams.
