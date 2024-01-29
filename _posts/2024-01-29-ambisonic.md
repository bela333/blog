---
layout: post
author: bela333
title: Surround sound using the Replay Mod
toc: true
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">

<iframe width="560" height="315" src="https://www.youtube.com/embed/tgI0obs8GDE?si=1eANunMTy9lZUo2Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

As many of you know, the [Replay Mod](https://www.replaymod.com/) itself has no built-in way to record audio. In most cases this is alright, since you can just record your computer's audio using [Audacity](https://www.audacityteam.org/) or (despite being pretty overkill for this purpose) [OBS](https://obsproject.com/).

Yes, these methods work *pretty well* for *most* use cases. 360° videos for example don't work really well with conventional stereo audio recording. Thankfully YouTube and some other platforms (for example Facebook) let you use a different format, that can efficiently encode spatial audio: Ambisonics.

## What are ambisonics?

Ambisonics is, as previously mentioned, a spatial audio format. They can be quite different from the well known stereo, 4.1, 5.1, 7.1 etc systems. What makes it so different, is that while these methods record what sounds should come out of some speakers, ambisonics records sound differences.

Probably the best way to demonstrate how ambisonics works, is to use a lower complexity equivalent.

Let me introduce you to: M/S stereo.

M/S stereo records onto two channels, similarly to normal stereo, but what it records is completely different: 

- A **Mid** channel, recording everything from every side, equally
- A **Side** channel, that records the difference between the sounds of the left and the right side of the microphone.

<!-- One might imagine it the following way:

{% katex display %}
\begin{aligned}
M = L + R \\
S = L - R
\end{aligned}
{% endkatex %}

From this you can really easily recover the original Left and Right audio channels.

{% katex display %}
\begin{aligned}
L = \frac{M + S}2 \\
R = \frac{M - S}2
\end{aligned}
{% endkatex %} -->

With [just](https://www.todepond.com/wikiblogarden/better-computing/just/) a bit of mathematics you can turn these signals back into our usual **Left** and **Right** channels.

But what if, instead of only recording the difference between the Left and the Right side, we also record the difference for all 3 axis?

This way, we get 4 audio channels:

- {%katex%}W{%endkatex%}, which is the same as the M in M/S
- {%katex%}X{%endkatex%}, which is the difference between the sounds in-front and the sounds behind the microphone
- {%katex%}Y{%endkatex%}, which is the difference between the left and the right sides
- {%katex%}Z{%endkatex%}, which is the difference between the sounds above and the sounds below the microphone

We call this recording method **first-order ambisonics**.

First-order ambisonics captures directionality of sounds *reasonably well*. If you need more accuracy, you would need higher-order ambisonics, that use more channels, for more accuracy.

YouTube only supports first-order ambisonics, while Facebook supports some higher-order ones as well.

## What do I need?

This guide is made for Windows.

- [Minecraft](https://www.minecraft.net/) (duh)
- [Replay Mod](https://www.replaymod.com/) (DUH)
- [Fabric Mod Loader](https://fabricmc.net/) (DUH????)
- [OpenAL Soft Configuration](https://www.openal-soft.org/openal-binaries/openal-soft-1.23.1-bin.zip) (oh....)
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) or any video editor that can handle multiple audio channels
- [IEM Plug-in Suite](https://plugins.iem.at/)

## Setting up OpenAL



## Recording audio



## Editing ambisonics



## How about on Facebook?