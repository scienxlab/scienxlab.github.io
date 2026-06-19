---
title: "What happens next to software development?"
author: "Matt Hall"
date: "2026-06-19"
description: "The economics of re-usable code will shape the future profession of software development"
categories:
  - ai
  - programming
---

The question "What happens next to open source?" came up several times at [the EAGE open source workshop](./open-for-energy/) last week. And in various guises: funding stability, maintainer fatigue, supply chain security, and so on. But the biggest concern was the effect of AI on software development — under the assumption that agentic coding actually works in the medium and long term, which I think is not a given.

So, if coding agents produce useful code and their role grows, what happens? It's a good question, but I think it can be broadened: _What happens next to software development?_

My take: **token price is everything**.

If coding agents work and tokens are cheap then everything we know changes. It becomes a manifestation of [Rich Sutton's bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html): human ideas and patterns can and will be beaten with compute. No need to store code: just generate what you need, when you need it. No more repos! Forget JIT compiling — JIT everything!

In the recent past, in the world of nearly-free tokens, an agent in need of a wavelet (say) will likely prefer to implement the algorithm from scratch in preference to using a library. If code is free and programming is solved, then why bother looking for a library? (Wait, then why use Python? Why not generate C? Wait, why not assembly? Or machine code? Or just generate the binary bitstream straight into memory?)

OK, let's calm down — if agentic coding works then for sure tokens will not be cheap.

So tokens will be expensive and "synthetic labour" will cost real money — if you follow the news, you know the AI revenue maximization function [is already running](https://www.investing.com/analysis/the-ai-token-pricing-crisis-behind-openai-and-anthropics-revenue-race-200680777). Now we will have to motivate agents to re-use code (and languages!), because repos and libraries serve to 'freeze' invested labour. With a Scrooge criterion, agents and their human minders will re-discover DRY, the advantages of open source, long-lived teams, and so on. And yeah, it will be pretty annoying because we know all this, remember?

Today I think there's reasonable evidence to suggest that, far from being inclined to economise, large language models use more tokens than they need. They tend to produce a lot of code, often repeat themselves, and always [seek to prolong interaction](https://www.library.hbs.edu/working-knowledge/how-ai-chatbots-try-to-keep-you-from-walking-away): LLMs are Scrooge on Christmas Day, except you're paying for all of it!

**Without a strong compulsion to minimize cost — a frugality function or re-use requirement that will of course drive token prices further up — I don't know how this changes.**
