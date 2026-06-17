# 🧬 Protein Stability & Mutation Explorer

> Exploring the impact of protein mutations through data engineering, machine learning, and interactive visualization.

⚠️ **This project is still a work in progress (WIP).**  
The goal is to progressively build an end-to-end platform combining:
- biological data processing,
- protein structure exploration,
- machine learning,
- modern data tooling,
- and interactive scientific visualization.

---

# 🎯 Project Goal

Protein mutations can significantly impact protein stability and function.  
This project aims to build a small platform capable of:

- ingesting and transforming protein mutation datasets,
- engineering biologically relevant features,
- training ML models to predict mutation impact,
- visualizing proteins and mutations in 3D,
- and providing an interactive interface to explore predictions.

The project is intentionally designed as a full-stack scientific AI project rather than a simple notebook experiment.

---

# 🧪 Scientific Context

Proteins are highly structured biological molecules whose stability depends on complex physical and chemical interactions.

Even a single amino acid mutation may:
- destabilize a protein,
- alter its folding,
- impact enzymatic activity,
- or modify interactions with other molecules.

Predicting mutation impact is therefore an important challenge in:
- drug discovery,
- protein engineering,
- biotechnology,
- and computational biology.

# Database schema

The project uses a PostgreSQL version of FireProtDB. (https://loschmidt.chemi.muni.cz/fireprotdb/download/)

Main relational structure:
![Schema](doc/fireprotdb_public.png)


