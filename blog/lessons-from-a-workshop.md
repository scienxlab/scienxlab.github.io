---
title: "Lessons from a workshop"
author:
  - Matt Hall
  - Guillermo Vargas
date: "2026-06-11"
description: "Reflections on the EAGE open source workshop"
---

[Earlier this week](./open-for-energy/) we summarized the goings-on at the EAGE open source workshop. Turns out Sunday workshops are on the small side — but on the plus side, this did make for plenty of open discussion that everyone could participate in. (Next time I'll ask for a Monday session!)

I started the day by reflecting on Joe Dellinger's words from his summary of the 2006 open source workshop in Vienna:

> The economic benefits of a collaborative open-source exploration and production processing and research software environment would be enormous. Skilled geophysicists could spend more of their time doing innovative geophysics instead of mediocre computer science. Technical advances could be quickly shared and reproduced instead of laboriously re-invented and reverse-engineered. Oil companies, contractors, academics, and individuals would all benefit. — Joe Dellinger, 2006, Vienna

Joe's words and this spirit support my own belief that **software is knowledge sharing**. Concrete, fully specified, executable text files beat hand-wavy best-practice PDFs every day of the week. Especially open source text files!

## The fourth edition

This was the fourth EAGE open source workshop. Here's the timeline:

- 2006 — EAGE, Vienna
- 2012 — EAGE, Copenhagen — [blog post](https://agilescientific.com/blog/2012/6/12/two-decades-of-geophysics-freedom.html)
- 2016 — EAGE, Vienna — [blog post](https://agilescientific.com/blog/2016/5/31/open-source-fwi-i-mean-geoscience)
- 2026 — EAGE, Aberdeen — [blog post](https://scienxlab.org/blog/open-for-energy/)

To my knowledge, there have been two other events in a similar vein: one PTTC meeting, and an Agile event that was effectively the Software Underground's first conference:

- 2011 — [PTTC, Houston](https://ahay.org/wiki/Houston_2011) — [blog post](https://agilescientific.com/blog/2011/6/16/open-seismic-processing-and-dolphins.html)
- 2019 — TRANSFORM #1, Rouen — [blog post](https://agilescientific.com/blog/2019/5/18/transform-happened)

## Coding agents as users? Contributors? Maintainers?

One of the patterns I learned from [Leo Uieda and his group](https://www.fatiando.org/) is "tutorial driven development". This firmly orients the product around _users_ (who are, for much scientific software, also _learners_). Matteo (Shearwater) offered expanded advice for starting an open project: focus on documention, tests, and automated project management. This seems especially sensible in the AI era, as it becomes clear that documentation & automation are essential for agents, just as for human collaborators. (And by the way, please can we stop treating them separately?)

Andrea (RWTH Aachen) mentioned that the volume of incomplete or ambiguous issues is a challenge. This presaged Guillermo's presentation on using agents to manage and maintain open-source projects with a prototype assistant called _Steward_. Later, Guillermo and Andrea did a quick proof of concept for finding and closing stale issues.

If AI feels more like a threat than an opportunity, Julien's talk on hardware development was perhaps comforting. It seems that some aspects of software development are easier now, but the impact on (and threat to!) hardware development seems less obvious, to us anyway. Creating, iterating, and modifying hardware solutions is necessarily quite messy, with bits of wire, solder spots, and occasional puffs of blue smoke. Designing PCBs and programming FPGAs is objectively much harder than writing web apps. If you're worried about your future as a coder, maybe [now is the time to try hardware hacking](https://blog.oscars.dev/posts/rip-softwarehackathons-long-live-the-hardware-hackathon)?

## The simple lesson

It was striking to hear several people highlight "simplicity by design". Take Julien: he built a sensitive detector that can be driven across Djibouti, chucked in a boat, dragged up a mountain, and shoved in a volcanic fumarole at 95&deg;. It must be simultaneously robust and hackable with minimal equipment. Every design decision had consequences that, as a field geologist, he understood intuitively. Hence standard industrial tubing, few moving parts, seawater cooling — and running Python on a microcontroller.

Echoing the sentiment, but in software, Collin (USGS) described building composable UNIX-style command-line tools around plain text data files — and users were grateful for the lack of functionality. Nanna (dGB) said early design decisions in [OpendTect](https://dgbes.com/software/opendtect/) paid off in allowing the fast addition of tooling for new seismic data formats. Mark (TGS) attributed their success with MDIO to leaning on existing formats and libraries. And in my own experience, I find people are much more likely to understand and therefore use simple projects. That goes for features too — those that were complex to implement are often the least used.

## Myths of open source

Clearly the greatest myth of all is that "open source is free", or (relatedly) that you cannot build a business around open source. Open source may be free of charge to you, but someone is paying.

Gerard Gorman ([Devito Codes](https://www.devitocodes.com/)) runs the Devito project with [an _open-core_ model](https://en.wikipedia.org/wiki/Open-core_model): the Devito framework is open source, and Devito Codes Ltd runs around this core. Researchers can do fantastic things with the core 'out of the box', while the DevitoPRO offering adds software and services. TerraNigma does the same around GemPy, and dGB uses a similar strategy for OpendTect — and has done this for 20 years.

It's a smart model. The organization does not seek 'charity' for the open core, rather it chooses to fund the core itself. This helps separate the concerns, for example when talking to customers and investors, who may be unconvinced about open strategies; it is not their concern.

All this said, one thing about even the small group of maintainers at the workshop was clear: the range of motivations is broad. Openness may be a requirement (as for the USGS), a moral imperative, a commitment to education, expedient for collaboration, or a strategic differentiator. And the range of funding models is correspondingly diverse.

---

**The day was super fun and I think everyone present felt some cameraderie around the drive to collaborate in scientific software. I only hope that when we do it again, we can attract some people and perspectives from outside our cosy clique. One thing I know about doing hard science, nurturing communities, fundraising, and dealing with a lot of uncertainty is that all of it is easier with more humans.**
