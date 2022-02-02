## introduction: precise temporal patterns in the brain

### Ultra fast neural codes for ultra fast vision

Nous pouvons commencer notre revue de l'état de l'art sur le rôle de la dynamique dans la vision en présentant tout d'abord des résultats surprenants qui ont été obtenus en neuroscience. En effet, le groupe de Simon Thorpe a montré que les humains peuvent catégoriser en une fraction de seconde des images présentées brièvement.
Cette  expérience consistait à demander à des sujets de catégoriser catégoriser des images qui contiennent ou ne contiennent pas des animaux [@Thorpe1996]. Les résultats ont montré que les humains arrive à très bien réaliser cette tâche (avec un taux de réussite supérieur à 95 %) mais surtout que l'on pouvait enregistrer par électroencéphalographie une activité différentielle pour les deux catégories d'images qui montrer que cette différenciation émerge à une latence très précoce dans l'activité neuronale. Ces résultats ont été étendu à plusieurs espaces espèces notamment le primates n'en humain mais aussi étendu à différentes protocoles d'expérience et ont montré par exemple que la réponse pouvait être extrêmement rapide de l'ordre deux cents 20 000 secondes lorsque la tâche consistait à effectuer une saccade [@doi:10/d8gpjq].

Ce traitement rapide  aussi d'expliquer des expériences surprenantes de rapide serial détection qui consiste à présenter une  successions rapide d'images différentes et de décoder par l'EEG si l'observateur peut détecter par exemple la présence d'un animal. Les performances vont alors diminuer progressivement quand la fréquence de présentation des images augmente. Toutefois il a été montré chez le macaque que l'on pouvait garder une performance significative avec un temps de présentation d'images de seulement 14 milli secondes par image [@doi:10.1162/089892901564199].

Cette rapidité du cortex visuel bien que surprenante, est tout à fait compatible avec les latence qui sont enregistrés au niveau neuro-physiologique. En effet, à la présentation d'une image sur la rétine, l'information visuelle est rapidement propagé vers le thème Adamus puis vers le thalamus puis le cortex visuel en environ 50. Pour atteindre le cortex visuel primaire ans environ 55 milli-secondes chez le macaque [@doi:10.1007/978-1-4757-9625-4_5]. Ce fonctionnement du traitement visuel comme une passe en avant et sûrement majoritaire dans le traitement rapide et peut se complémenter avec des boucles en retour des R supérieur vers les aires sensorielles [@doi:10.1016/S0166-2236(00)01657-X].


### how timing encodes analogous profile

Une caractéristique importante de l'information neuronale et que celle-ci consiste principalement dans le transfert de potentiels d'action, ou Spike, qui consiste en de brève impulsion qui se propage sur les axones des neurones. Ceux-ci ont la particularité d'être binaire dans leur amplitude (C'est-à-dire d'être prototypiques, tout ou rien). Une conséquence importante de la rapidité de traitement et qu'elle implique que celui-ci est effectué en seulement en utilisant très peu de Spikes. En effet, si on considère qu'une réponse comportementale en seulement 120 ms consiste en une dizaine d'étapes de traitement en suivant les voies "en avant" du système visuel, alors cela impose que le traitement dans seule aire est effectué avec un nombre réduit de Spike.

Au niveau du traitement dynamique de l'information visuelle, il a été montré qu'un encodage des valeurs de l'imminence de luminance dans l'image au lieu de la rétine [@doi:10.1126/science.1149639]. Notamment apprécié sur la figure à la réponse de cellules ganglionnaire à des réseaux visuels de ligne qui sont flashé sur la rétine. Les auteurs ont montré que la réponse neuronale pouvait être encodé dans la latence de la réponse et pas seulement dans la fréquence de décharge comme cela est sous le lit souvent assumé. Dans la figure quatre de ce même article, c'est résultats sont étendues pour des images naturelles et montre un comportement qualitativement similaire. La conclusion des auteurs et que la latence de décharge des neurones permet d'encoder des caractéristiques spatiales de l'image.

Des résultats similaires ont été mises en évidence grâce a des enregistrements neurophysiologiques dans le cortex visuel primaire et montre que différents niveaux d'activité visuelle vont induire différents niveaux de différentes latence de décharge des neurones dans l'air visuel primaire [@doi:10/dqt5cm]. De nombreux modèles ont utilisé ces propriétés dans le codage temporelle pour réaliser des réseaux de catégorisation rapide d'image. Ces modèle prennent la forme de réseau de neurones artificiels à Spike et ont pu mettre en évidence leurs applications pratiques pour la catégorisation d'images [@Perrinet2004]. De travaux ont été étendu en incluant des capacités d'apprentissage non viens superviser et nous avons récemment développé des architecture de type Staking n'aura le network qui permet de catégoriser des images de différentes classes en seulement quelques Spike [@Grimaldi2021, @Grimaldi2022]. Ce type de modélisation est extrêmement importante vis-à-vis du développement d'une nouvelle génération de caméra dit silicone caméras qui, au lieu d'utiliser une représentation friend base, utilise une représentation similaire à celle que nous venons de voir et qui consiste à cause de l'image par des événements. Ce type de modélisation reprend souvent les architecture classique de catégorisation d'image développé dans l'apprentissage profond tout en l'adaptant à la spécificité de la représentation événementielle [@arXiv:1912.11443].

Note also that timing is not entirely sensorial or internal but in [@doi:10.1073/pnas.1921226117], they found that "timing accuracy was improved when the environment afforded cues that rats can incorporate into motor routines. Timing, at least in animals, may thus be fundamentally embodied and situated."


### synfire chains

In [@Abeles1991] corticonics: The book gradually leads the reader from the macroscopic cortical anatomy and standard electrophysiological properties of single neurons to neural network models and synfire chains

M. Diesmann, M. O. Gewaltig, A. Aertsen, Nature402, 529 (1999).


### synfire braids
sparse in time and space [2] AL Barth and JF Poulet Trends in Neurosciences 35.6 (2012), pp. 345-355. [3] CC Petersen and S Crochet, Neuron 78.1 (2013), pp. 28-48.


 * [@Bienenstock1995] : from synfire chains to Synfire braids

 * recent theories of binding by synchrony : Fries 2005 trends cog neuro with spikes arriving at peak susceptibility (top of a cycle) or down, van Rullen, Laura Dugué


 * A notable exception is the polychronization model of Izhikevich [@Izhikevich2006], which combined the construction of a random recurrent model of spiking neurons including such delays and whose weights evolved with a Spike-Time Dependent Plasticity (STDP) learning rule. In this model, raster plot analysis showed repeated activation of Polychronous Groups (PGs), i.e., specific spike patterns with a specific sequence of activations.

#### traveling waves

[@doi:10.1038/s41467-021-26175-1]



####  delays

Our approach would be distinct than these approaches from us and colleagues as we will directly deal with delays in the system at the presynaptic level. I have an extensive expertise in the domain of temporal delays in the nervous system, both at the neural [@doi:10.1007/s00422-014-0620-8] and behavioral [@doi:10.1371/journal.pcbi.1005068] levels. Extending this knowledge to the optimization of delays in a SNN will provide a breakthrough in the efficiency of these networks. Our expertise in reproducing the HOTS network [@doi:10.1109/CBMI50038.2021.9461901,@doi:Grimaldi2022pami] will be crucial in the swift realization of this project.
