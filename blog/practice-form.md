---
title: "Practice your form"
author: "Matt Hall"
date: "2024-02-26"
description: "Coding challenges for scientists and engineers"
---

**Years ago, I learned karate.** I never really got into the sparring side of the sport and eventually stopped, but I loved the mindful practice involved in one aspect of it: **kata**, or 形. The word means 'form', and the focus is on quality, not speed, power, or quantity. I spent hours in a squash court at the YMCA in Calgary, learning the elements of karate, one move at a time, very slowly.

Later, teaching Python classes and enjoying the [Advent of Code](https://adventofcode.com/) challenges every December, I made some 'mindful practice' exercises for my students, mostly geoscientists and engineers. I called them **kata**.

<div style="text-align: center">[**形 Check out the kata.**](https://kata.scienxlab.org/)</div>


## Lots to choose from

Today there are 13 challenges, some of them more 'geo' than others. Here are some of them:

- `sequence` — Analyse a sequence of rocks to find patterns. Good first problem.
- `wireline` — Automatically detect bed boundaries in a density log.
- `sample-names` — Ah, the realities of data-loading!
- `prospecting` — Combine information from several map layers.
- `photomicrograph` — An introduction to image processing and analysis.
- `regression` — A single-variable machine learning regression problem.

One slightly funky aspect of the challenges is that you have to interact with a web API to play, making HTTP GET requests to read your data and submit your answers. The server will tell you if you got the question right or not.

💡 **If you want to try one, [this Google Colab notebook](https://colab.research.google.com/drive/1eP68NTV-GA3R-BYUh-CUxcgYDQ5IuetS) will help you get started. Or read on for some tips...**


## Getting started

To get started, you don't need an account or anything, the server doesn't know who you are. Just think up a random-ish key and use that to identify yourself (so the server can match your answer to the data you received).

As a quick example, here's how you can get the data for the first challenge, called `sequence`:

```python
import requests

uri = 'https://kata.scienxlab.org/challenge/sequence'

params = {
    'key': 'honey badger'  # Choose a unique-ish key.
}

r = requests.get(url, params)
print(r.text)
```

Now `r.text` holds a long text string with your input data.

To send an answer, update the `params` dictionary with the question number and your answer:

```python
params.update({'question': 1, 'answer': 42})
r = requests.get(url, params)
print(r.text)
```

The server will tell you how you did. In this case: `Incorrect. Your answer is too low.`

If you get stuck on a question, you can ask the server for a clue by sending a question number but no answer:

```python
params = {
    'key': 'honey badger',
    'question': 1,
}
r = requests.get(url, params)
print(r.text)
```

**If you decide to give it a go, then good luck and have fun! And if you fancy trying to _write_ a challenge &mdash; a challenge in itself! &mdash; then check out the [`kata-dev` repo](https://github.com/scienxlab/kata-dev).**
