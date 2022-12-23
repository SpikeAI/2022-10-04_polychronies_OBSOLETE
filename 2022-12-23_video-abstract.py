# 2022-12-23_video-abstract

"""
 Using the template @ https://laurentperrinet.github.io/sciblog/posts/2019-09-11_video-abstract-vision.html
and using that @ https://github.com/chloepasturel/AnticipatorySPEM/blob/master/2020-03_video-abstract/2020-03-24_video-abstract.ipynb
"""
# Creating the movie using the (*excellent*) [MoviePy](http://zulko.github.io/moviepy/index.html) library:

videoname = "2022-12-23_polychrony-review_video-abstract"
gifname = videoname + ".gif"
gifname = None
fps = 30
from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip

H, W = 500, 800
H_fig, W_fig = int(H-H/(1.618*3)), int(W-W/(1.618*3))


opt_t = dict(font="Arial", size=(W,H), method='caption')
opt_st = dict(font="Arial", size=(W,H), method='caption')
# opt_t = dict(size=(W,H), method='caption')
# opt_st = dict(size=(W,H), method='caption')

clip = []
t = 0 

# TITRE
texts = ["""Precise spiking motifs in neurobiological and neuromorphic data





""", """Precise spiking motifs in neurobiological and neuromorphic data

   Grimaldi, Gruel, Besnainou, 
   Jérémie, Martinet, and Perrinet


""", """Precise spiking motifs in neurobiological and neuromorphic data

   Grimaldi, Gruel, Besnainou, 
   Jérémie, Martinet, and Perrinet

Brain Sciences (2022)
"""]
txt_opts = dict(align='center', color='white', **opt_t) #stroke_color='gray', stroke_width=.5
duration = 1.5
for text in texts:
    txt = TextClip(text, fontsize=35, **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clip.append(txt)

# INTRO
sub_opts = dict(fontsize=28, align='West', color='white', **opt_t)
sub_duration = 1.5
intro_subs = ["""
The majority of information passing 
in the brain is mediated by all-or-none 
events, 



""", """
The majority of information passing 
in the brain is mediated by all-or-none 
events, *spikes*.



""", """
The majority of information passing 
in the brain is mediated by all-or-none 
events, *spikes*.
We present here novel evidence for the 
role of their precise timing from 
neurobiological and neuromorphic data.
""",
               ]

for i_sub, subtitle in enumerate(intro_subs):
    sub = TextClip(subtitle, **sub_opts).set_start(t).set_duration(sub_duration)
    t += sub_duration
    clip.append(sub)
clip.append(sub) # another bit on the last bit

chapters = [dict(title="Visual system", color='black',
            content=[dict(figure='figures/visual-latency.jpg', duration=5, subtitle=[
                            "The visual system is very efficient to generate a...", 
                            "...decision from the raw image to the different ...", 
                            "...stages of the visual pathways here a reaction...", 
                            "...of finger muscles in about 300 milliseconds."]),
                     dict(figure='../AG_figures/animated_neurons/LIF.mp4', duration=5, subtitle=[
                            "This efficiency is thought to be mediated by spikes...", 
                            "...that is brief all-or-none events which are passed...", 
                            "...from assemblies of neurons to others, in the...", 
                            "...very large network which forms the brain."])]), 
           dict(title="Polychrony", color='orange',
            content=[dict(figure='figures/replicating_MainenSejnowski1995.png', duration=5, subtitle=[
                            "This shows that different individuals have different...", 
                            "...compromise between exploration and the exploitation...", 
                            "...a hallmark of their inter-individual differences."]),
                    dict(figure='figures/THC_1a_k.png', duration=5, subtitle=[
                            "This shows that different individuals have different...", 
                            "...compromise between exploration and the exploitation...", 
                            "...a hallmark of their inter-individual differences."]),
                    dict(figure='figures/THC_1a.png', duration=5, subtitle=[
                            "This shows that different individuals have different...", 
                            "...compromise between exploration and the exploitation...", 
                            "...a hallmark of their inter-individual differences."])]), 
           dict(title="Neurobiology", color='red',
            content=[dict(figure='figures/Ikegaya2004zse0150424620001.jpeg', duration=5, subtitle=[
                            "This shows that different individuals have different...", 
                            "...compromise between exploration and the exploitation...", 
                            "...a hallmark of their inter-individual differences."])]), 
           dict(title="Neuromorphic", color='blue',
            content=[dict(figure='figures/event_driven_computations.png', duration=5, subtitle=[
                            "This shows that different individuals have different...", 
                            "...compromise between exploration and the exploitation...", 
                            "...a hallmark of their inter-individual differences."])]), 
           ]


# http://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=compositevideoclip#textclip
txt_opts = dict(fontsize=65, bg_color='white', align='center', **opt_st)
sub_opts = dict(fontsize=28, align='South', color='white', **opt_st)

for chapter in chapters:
    duration = 1
    txt = TextClip(chapter['title'], color=chapter['color'], **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clip.append(txt)

    for content in chapter['content']:
        # set the figure
        figname = content['figure']
        if figname[-4:]=='.mp4' :
            img = VideoFileClip(figname, audio=False)
            print(figname, '--> duration:', img.duration, ', fps:', img.fps)
            duration = img.duration
        else :
            duration = content['duration']
            img = ImageClip(figname).set_duration(duration)

        H_clip, W_clip, three = img.get_frame(0).shape
        if H_clip/W_clip > H_fig/W_fig: # portrait-like
            img = img.resize(height=H_fig)
        else: # landscape-like
            img = img.resize(width=W_fig)

        img = img.set_start(t).set_pos('center')#.resize(height=H_fig, width=W_fig)

        t += duration
        clip.append(img)

        # write the subtitles
        t_sub = t - duration
        sub_duration = duration / len(content['subtitle'])
        for subtitle in content['subtitle']:
            sub = TextClip(subtitle, **sub_opts).set_start(t_sub).set_duration(sub_duration)
            t_sub += sub_duration
            clip.append(sub)

# OUTRO
texts = ["""
Overall, this manuscript reviews the potential
of using the precise spiking motifs for a
building more efficient 




""",
"""
Overall, this manuscript reviews the potential
of using the precise spiking motifs for a
building more efficient machine learning 
algorithms, faster and more frugal,
but also to better understand 


""",
"""
Overall, this manuscript reviews the potential
of using the precise spiking motifs for a
building more efficient machine learning 
algorithms, faster and more frugal,
but also to better understand 
neurobiological functioning and their 
disorders...
"""]

txt_opts = dict(fontsize=30, align='center', **opt_t)
duration = 3
for text in texts:
    txt = TextClip(text, color='white', **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clip.append(txt)
    
# FIN
texts = ["""
For more info, and the full, open-sourced code... visit



""", """
For more info, and the full, open-sourced code... visit

https://laurentperrinet.github.io/           
             /publication/grimaldi-22-polychronies/
""",
]

txt_opts = dict(align='center', **opt_t)
duration = 2.5
for text, fontsize in zip(texts, [28, 28]):
    txt = TextClip(text, color='orange', fontsize=fontsize, **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clip.append(txt)    


# COMPOSITING
video = CompositeVideoClip(clip)
video.write_videofile(videoname + '.mp4', fps=fps)

if not(gifname is None):
    video.write_gif(gifname, fps=fps)
    from pygifsicle import optimize
    optimize(gifname)