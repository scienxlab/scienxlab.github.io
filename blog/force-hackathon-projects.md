---
title: "FORCE hackathon project round-up"
author: "Matt Hall"
date: "2023-12-04"
description: "All the projects at the FORCE LLM hackathon in Stavanger"
---

🤖 **Yesterday, I summed up last week's FORCE large language model hackathon, which took place last week in Stavanger, Norway. Today, let's look more closely at the projects our hackers worked on...**

### Anonymizers

**Lynn Vogel** (EBN), **Odd Kolbjørnsen** (AkerBP), **Zana Pepaj** (Equinor), **Petter Dischington** (NPD), **Jari Kunnas** (Vår Energi).

This dataset, and others like it, contains a lot of names — of people (Knut Hansen), fields (Johan Sverdrup), equipment (Billy Pugh), and report authors (J. Doe et al). Some uses of some names might be considered personally identifiable information; there are also emails, phone numbers, and other data. The team tried applying a combination of NER models (e.g. with [Spacy](https://spacy.io)), specialist anonymization pipelines like [Microsoft Presidio](https://microsoft.github.io/presidio/), and the [Azure OpenAI API](https://azure.microsoft.com/en-us/products/ai-services/openai-service) to the problem, achieving some success. The team crafted some serious ChatGPT prompts to elicit structured NER labeling, and it was very interesting to see how good the model is at this task.

⭐ The jury understood the task right away, and appreciated the difficulty of completing it. They also liked the relatable way in which the story was told.

### Embedding enthusiasts

**Ryan Cole** (Capgemini), **Benjamin Kofoed** (Equinor), **Kristian de Figueiredo Kollsgård** (NPD), **George Ghon** (Capgemini), **Bartek Florczyk Vik**.

Embeddings of words, sentences, and documents are useful resources in natural language processing. The idea is to cast the corpus into a vector space in which semantically similar entities are close to each other. The team set about creating a clean dataset using various methods from plain regex to [transformer-based denoising (TSDAE) in SBERT](https://www.sbert.net/examples/unsupervised_learning/TSDAE/README.html), then comparing how GPT and SBERT, and a real human geologist, rated the sentences. They were then able to compare sentence similarity using various methods, and score the performance of multiple models, both off-the-shelf and self-trained.

🌟 **Special mention** Everyone was impressed with this end-to-end data science project, with a pipeline that included data cleaning, and quantitative comparisons between several models.

### Zero-shot chatbots

**Jörg Peisker** (OMV), **Doris Winkler** (OMV), **Dennis Schmidt** (OMV), **Daan Petri** (EBN), **Dylan Loss** (ConocoPhillips).

The dream many people have when they first meet a smart chatbot is to be able to ask simple questions with ordinary language, and get back exactly what you wanted. Achieving this dream on a custom dataset is, however, challenging; even mundane things like typos ('wel', 'welll', 'weel', 'wlel') gave all the teams headaches. This team experimented with various manifestations of the NPD dataset, [the LangChain toolkit](https://www.langchain.com), cleaning the vector database in various ways, Facebook's [FAISS](https://github.com/facebookresearch/faiss) project for storing vectors, and extensive prompt engineering — which Jörg pointed out, "is definitely a thing".

⭐ The jury appreciated the sharp focus on real business questions, and the subsequent story of what did not work — and why. The team put a solid, scientific project together.

### Knowledge-graphers

**Hammad Ali**, **Catherine Adams**, **Henrik Busengdal**, **Anil Dhiman** (all Sopra Steria), **Thomas Crabie**, **Adam Hammoumi**, **Aziz Ben Ammar**, **Ilyas Tib** (all IFPEN), **Lars Lukerstuen** (Bouvet), **Erich Suter** (Equinor), and **Johannes Åsheim** (Fabriq).

The team applied a deep technology stack to exploring the usefulness of graph theory and semantic _subject-predicate-object_ triples in querying large language models. They also explored ways to extract both knowledge graphs and sample questions that would exploit knowledge from multiple documents from datasets like the one we had. With this foundation, the query response pipeline had several elements including:

- Use the Azure OpenAI API to convert a user query to a Cypher query ([Cypher](https://neo4j.com/developer/cypher/) is [Neo4J's](https://neo4j.com) graph query language).
- Apply the query to the Neo4j graph database, and retrieve the result.
- Simultaneously convert the user query to embeddings and fetch the nearest neighbours from the vector database.
- Use ChatGPT to synthesize a response based on the graph and embedding responses, and providing references for its answers.

[Check out the team's GitHub repo here.](https://github.com/ilyas-ifp/Stavanger_hackathon)

🌟 **Special mention** The jury was impressed by the project management skills of this large team, all of whom contributed to the end result. Their graph-based approach has clear value and utility in these problems.

### Q&A generators

**Nolwenn Bernard** (UiS), **Henri Blondelle** (Agile DD), **Eirik Morken** (Bouvet), **Aleksander Jakobsen** (Bouvet), **Akram Ourir** (Sval Energy).

Recognizing that the long-term goal of a domain-specific chatbot will take a lot of work and collaboration, the team set about creating a large database of question-answer pairs. Apart from being a great hackathon project in itself, such an collection would be a valuable asset to the community, for both training and benchmarking models. Drawing inspriation from  [Stanford's SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/), the team used ChatGPT-4 Turbo with a highly customized prompt to generate 11 200 JSON-formatted candidate pairs from a clean subset of the NPD data. Here's a simplifed example:

```
    {
        "Q": "What type of sandstone lies in the 15/12-Beta-
              West reservoir of wellbore 15/12-4?", 
        "A": "Late Jurassic (Oxfordian) sandstone."
    }
```

Based on a sample of 550 questions, the team estimated that about 80% of the pairs were of sufficient quality to meet their needs. In a nod to accessibility and sustainability, the team estimated the compute cost of generating the collection at USD 36 — plus about 75 person-hours of labour!

[Check out the team's GitHub repo here.](https://github.com/NoB0/NorthSeaPQA-force-npd-hackathon)

🌟 **Special mention** The team did a terrific job of explaining and justifying their goal, and the jury were impressed by this impactful contribution to the community.

### Metadata extractors

**Enrico Riccardi**, **Wiktor Weibull**, **Aksel Hiorth** (all UiS), **Mads Lorentzen** (Geo), **Sanjay Kamath**, **Dorra Nouira** (both TotalEnergies).

All of the teams faced a noise problem and needed to reduce the training dataset to something models might learn from. This team chose to focus on well entities, focusing on about 10 wells out of more than 4000. The team used the pretrained [KeyBERT](https://github.com/MaartenGr/KeyBERT) model to extract keywords/phrases from documents pertaining to a known well, then selected the 18 most relevant and interesting, including things like `drilling risk`, `equipment failure` and `medical issues`. These were combined into custom prompts for ChatGPT-4, which returned structured JSON containing documents from the entire dataset. Once again, the orchestration of an elaborate toolchain being hidden behind deceptively simple outputs — perhaps that sums up all of transformer-based NLP!

⭐ The team presented a nice story, grounded in the perspective of a subsurface professional. This teams work promises to be useful to anyone picking up an NLP project in our domain.

---

**That's it for this event!** Many thanks to all the participants, who worked so hard to learn new things, put them into action, then share what they learned with everyone else. It was, as always, inspiring to see. I'm sure there will be more events like this in the future, so stay tuned and look forward to the next one 🚀

---

### Changelog

- **2023-12-04** — corrected record of exactly what the knowledge graph team did
