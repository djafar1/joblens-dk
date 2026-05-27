# JobLens DK

JobLens DK is a learning and portfolio project focused on NLP, ML evaluation, SQL, Docker, CI/CD, and deployment.

The goal is to build a primarily Danish, but also English, job intelligence tool that compares a CV with a job posting. The tool should identify matched and missing skills, retrieve supporting evidence from the CV, and later use RAG to explain the matches found.

The project is designed as a decision-support tool for job seekers, not as an automated hiring or candidate-ranking system.

## Current Status

Current version: `v0.1 - Classical NLP Baseline`

The first version focuses on classical NLP methods without LLMs.

Planned v0.1 features:

- Parse CV text and job posting text
- Clean and tokenize text
- Extract skills with a simple skill dictionary
- Split CV and job posting into chunks
- Compute TF-IDF vectors
- Rank CV chunks using cosine similarity
- Show matched and missing skills
- Return a simple analysis report

## Why This Project Exists

I am building this project to rebuild my coding fundamentals while connecting theory and practice.

The project is meant to strengthen skills in:

- Python
- NLP
- ML evaluation
- SQL
- Docker
- CI/CD
- Deployment
- Cost-aware AI system design

The project also gives me a practical way to revisit topics from machine learning and NLP courses through a real system instead of isolated notebooks.

## Core Idea

Input:

- CV text or PDF
- Job posting text

Output:

- Extracted skills
- Matched skills
- Missing skills
- Similarity score
- Relevant CV evidence for each job requirement
- Suggestions for honest CV improvement
- Later: RAG-based explanation

## Planned Versions

### v0.1 - Classical NLP Baseline

Classical NLP baseline using text cleaning, tokenization, TF-IDF, cosine similarity, and skill extraction.

### v0.2 - Streamlit Interface

Simple UI where a user can upload or paste a CV and job posting, then view the analysis results.

### v0.3 - SQL and Analysis History

Store documents, chunks, skills, matches, and analysis runs in a database.

### v0.4 - Embeddings and Semantic Search

Use embeddings to compare CV chunks and job requirements semantically.

### v0.5 - ML Relevance Model

Train a logistic regression or linear SVM model to predict whether a CV chunk is relevant to a job requirement.

### v0.6 - RAG Explanation

Use retrieved evidence from the CV and job posting to generate grounded explanations with an LLM.

### v0.7 - Engineering Polish

Add tests, Docker, CI/CD, VPS deployment, screenshots, and improved documentation.

## Planned Tech Stack

Early version:

- Python
- scikit-learn
- Streamlit
- SQLite
- pytest

Later versions:

- FastAPI
- PostgreSQL
- pgvector
- sentence-transformers
- Docker
- GitHub Actions
- VPS deployment

## Project Structure

```text
joblens-dk/
  README.md
  docs/
    PROJECT_PLAN.md
    ARCHITECTURE.md
    COST_ANALYSIS.md
    PRIVACY_AND_SAFETY.md
    LEARNING_LOG.md
    THEORY_MAP.md
    DECISIONS.md

  app/
    streamlit_app.py

  src/
    parsing/
    nlp/
    retrieval/
    ml/
    database/
    services/

  tests/
  docker-compose.yml
  pyproject.toml
```

## Documentation

More detailed documentation is available in:

- `docs/PROJECT_PLAN.md`
- `docs/ARCHITECTURE.md`
- `docs/LEARNING_LOG.md`
- `docs/THEORY_MAP.md`
- `docs/DECISIONS.md`

## First Milestone

The first milestone is to build a working classical NLP baseline.

The focus is not on design yet. The focus is on getting the core logic right:

- clean text
- extract skills
- chunk documents
- compute TF-IDF
- rank chunks with cosine similarity
- return a readable report

## Notes

This project is built for learning, experimentation, and portfolio development.