# JobLens DK - Project Plan

## Goal

The goal of this project is to build a primarily Danish, but also English, job intelligence tool that compares a user-uploaded CV with a job posting.

The tool should identify matched and missing skills, retrieve supporting evidence from the CV, and later use RAG to explain the matches found.

The project is mainly a learning and portfolio project. The goal is to rebuild coding fundamentals while learning NLP, ML evaluation, SQL, Docker, CI/CD, and deployment.

JobLens DK should be a decision-support tool for job seekers. It should help a user understand how well their CV matches a specific job posting and how they can improve their profile honestly.

It should not be built as an automated hiring or candidate-ranking system for employers.

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

## Version Plan

### v0.1 - Classical NLP Baseline

Goal: Build the first working version using classical NLP methods without LLMs.

Features:

- Parse plain text CV and job posting
- Clean and tokenize text
- Extract skills with a simple skill dictionary
- Split CV and job posting into smaller chunks
- Compute TF-IDF vectors
- Rank CV chunks using cosine similarity
- Show matched and missing skills
- Show top relevant CV sections for the job posting

Learning focus:

- Python fundamentals
- Text preprocessing
- Tokenization
- TF-IDF
- Cosine similarity
- Basic ranking
- Clean project structure

### v0.2 - Streamlit Interface

Goal: Add a simple user interface for testing and demonstrating the project.

Features:

- Add a simple upload/paste interface
- Allow the user to paste a job posting
- Allow the user to upload or paste a CV
- Show extracted skills as tables
- Show matched and missing skills
- Show ranked CV evidence
- Keep UI code separate from the core logic

Learning focus:

- Streamlit
- Separating UI logic from core logic
- Presenting model outputs clearly
- Making a demo that is easy to understand

### v0.3 - SQL and Analysis History

Goal: Add persistent storage and learn basic database design.

Features:

- Store documents
- Store analysis runs
- Store extracted skills
- Store matches between job requirements and CV chunks
- Add a simple history page
- Allow comparison between previous analysis runs

Possible database tables:

- `documents`
- `document_chunks`
- `skills`
- `analysis_runs`
- `matches`
- `feedback_labels`

Learning focus:

- SQL
- Database schema design
- SQLite first, PostgreSQL later
- Joins
- Basic queries
- Data persistence
- Analysis history

### v0.4 - Embeddings and Semantic Search

Goal: Move beyond keyword matching and support semantic matching.

Features:

- Split CV and job postings into chunks
- Generate embeddings for CV chunks and job requirements
- Compare semantic similarity between chunks
- Rank CV evidence using embedding similarity
- Compare embedding-based search against TF-IDF
- Later store vectors with PostgreSQL and pgvector

Example:

A job requirement like:

> Experience deploying machine learning models

Should be able to match a CV sentence like:

> Built a FastAPI model service, containerized it with Docker, and deployed it on a VPS

Learning focus:

- Embeddings
- Sentence transformers
- Semantic search
- Vector similarity
- Retrieval
- pgvector later
- Comparing classical NLP with modern NLP

### v0.5 - ML Relevance Model

Goal: Add a supervised ML component for predicting whether a CV chunk is relevant to a job requirement.

Features:

- Create labeled examples of job requirement and CV chunk pairs
- Label examples as relevant or not relevant
- Train a logistic regression or linear SVM classifier
- Use features such as:
  - TF-IDF cosine similarity
  - Embedding similarity
  - Keyword overlap
  - Skill category match
  - Section type
- Evaluate the model using:
  - Train/test split
  - Precision
  - Recall
  - F1-score
- Compare the ML model against TF-IDF and embedding baselines

Learning focus:

- Supervised learning
- Ranking
- Classification
- Logistic regression
- Linear SVM
- Train/test split
- Precision and recall
- Model evaluation
- Generalization

### v0.6 - RAG Explanation

Goal: Use an LLM as an explanation layer, not as the whole matching system.

Features:

- Retrieve relevant evidence from the CV and job posting
- Send only retrieved evidence to the LLM
- Generate an explanation of:
  - Why the job matches the CV
  - Which requirements are covered
  - Which requirements are missing
  - How the CV can be improved honestly
- Avoid hallucinated skills or fake experience
- Clearly separate retrieved evidence from generated explanation

Learning focus:

- RAG
- Prompt design
- Grounded generation
- Evidence-based explanation
- LLM limitations
- Hallucination control
- Token cost awareness

### v0.7 - Engineering Polish

Goal: Make the project look and feel like a serious portfolio project.

Features:

- Add tests for core logic
- Add type hints
- Add linting and formatting
- Add Docker
- Add GitHub Actions
- Deploy on VPS
- Add screenshots to README
- Add an architecture diagram
- Add clear setup instructions
- Add version tags or GitHub releases

Learning focus:

- Production-grade Python
- Testing
- Docker
- CI/CD
- Deployment
- Documentation
- GitHub project presentation

## Learning Goals

### Programming

- Write clean Python modules
- Use type hints
- Write tests
- Structure a real project
- Separate core logic from UI code
- Debug and refactor code independently

### NLP

- Tokenization
- Text normalization
- TF-IDF
- Skill extraction
- Chunking
- Embeddings
- Semantic search
- RAG

### ML

- Ranking
- Similarity scoring
- Logistic regression baseline
- Linear SVM baseline
- Train/test split
- Precision, recall, and F1-score
- Generalization
- Model comparison

### MLB Theory

The project should connect naturally to theory from Machine Learning B, especially when the system moves from simple matching to learned ranking.

Relevant theory topics:

- Convexity in logistic regression
- Cross-entropy loss
- Gradient-based optimization
- Regularization
- Overfitting and generalization
- Model complexity
- Evaluation and train/test splits
- Precision and recall tradeoffs
- Linear classifiers and margins

The theory connection will mainly appear in the ML relevance model, the evaluation setup, and the technical documentation. The goal is to understand why the models behave the way they do, not only to use them as black-box tools.

### Engineering

- SQL
- SQLite first, PostgreSQL later
- PostgreSQL with pgvector later
- Docker
- CI/CD
- VPS deployment
- Basic cost control
- Privacy-aware design

## Deployment and Cost Analysis

The project should include a realistic cost analysis for deploying the system publicly.

The goal is to understand what it would cost to run JobLens DK outside a local development environment, especially if the app later uses embeddings, vector search, and LLM-based explanations.

### Deployment Scenarios

#### Scenario 1 - Local Demo

The project runs locally on a laptop.

Expected cost:

- Server: $0
- Database: $0
- LLM usage: $0 if disabled
- Best use case: development, testing, screenshots, and portfolio documentation

#### Scenario 2 - Small Public Demo

The project is deployed on a small VPS.

Expected cost:

- VPS: around $5/month
- Database: SQLite or PostgreSQL on the same VPS
- Storage: low, as long as raw CV files are not stored permanently
- LLM usage: optional and controlled
- Best use case: portfolio demo for recruiters, friends, and small-scale testing

#### Scenario 3 - Public App With LLM Explanations

The project is publicly available and users can generate RAG-based explanations.

Expected cost drivers:

- Number of analyses per day
- Average CV length
- Average job posting length
- Number of retrieved chunks sent to the LLM
- Input tokens
- Output tokens
- Embedding generation
- Database storage
- Server CPU/RAM usage

This version needs stricter limits because LLM calls can create variable cost.

### Cost-Control Decisions

To keep the project cheap and safe to run:

- No GPU hosting
- No large file uploads in the first public version
- Limit CV and job posting length
- Limit number of analyses per user/IP
- Cache repeated analyses when possible
- Use classical NLP and embeddings before calling an LLM
- Use the LLM only for explanation, not for the entire matching pipeline
- Keep raw CV storage disabled by default
- Add a maximum token budget per analysis
- Add a daily or monthly usage cap for LLM calls
- Keep a local/offline mode without LLM calls

### Example Cost Model

A simple cost estimate should be added before public deployment.

Example variables:

- Analyses per day
- Average input tokens per analysis
- Average output tokens per analysis
- Embedding cost per document
- LLM cost per 1 million input tokens
- LLM cost per 1 million output tokens
- Monthly VPS cost
- Monthly database/storage cost

Example formula:

```text
Monthly LLM cost =
number of analyses per month × average tokens per analysis × model price per token
```

A more detailed version should separate:

```text
Embedding cost
+ LLM input token cost
+ LLM output token cost
+ VPS cost
+ database/storage cost
= estimated monthly cost
```

### Why This Matters

The project should not only show that the system works technically. It should also show that the deployment is realistic.

A useful AI feature is not only about model quality. It also has to be affordable, predictable, and safe to expose publicly.

## Privacy and Safety

CVs may contain personal information, so privacy should be considered from the beginning.

Design decisions:

- Do not store raw CVs by default in early versions
- Avoid sending CV text to an LLM unless explicitly enabled
- Use local processing for classical NLP and embeddings when possible
- Clearly separate raw documents from extracted features and analysis results
- Allow users to delete analysis history if storage is added
- Do not rank candidates for employers
- Do not present the tool as an automated hiring system
- Focus on helping the job seeker understand skill gaps and improve their CV honestly

## Success Criteria

The project is successful if it can:

- Take a CV and a job posting as input
- Extract relevant technical skills
- Show matched and missing skills
- Rank CV sections against job requirements
- Compare at least two matching methods
- Store analysis history in a database
- Include tests for core logic
- Run locally with clear setup instructions
- Be deployed on a VPS with Docker
- Include a realistic deployment and cost analysis
- Include limits that prevent expensive or abusive usage
- Explain the technical choices in the README

## Suggested Repository Structure

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
      pdf_parser.py
      text_cleaner.py

    nlp/
      tokenizer.py
      skill_extractor.py
      tfidf_matcher.py
      embedding_matcher.py

    retrieval/
      chunker.py
      ranker.py

    ml/
      relevance_model.py
      evaluation.py
      metrics.py

    database/
      models.py
      repository.py

    services/
      analyze_service.py

  tests/
    test_text_cleaner.py
    test_skill_extractor.py
    test_ranker.py
    test_metrics.py

  docker-compose.yml
  pyproject.toml
```

## Documentation Files

### README.md

The public-facing explanation of the project.

Should include:

- What the project does
- Why it exists
- How to run it
- Screenshots
- Current version
- Roadmap
- Architecture overview

### docs/PROJECT_PLAN.md

The full project plan and version roadmap.

### docs/ARCHITECTURE.md

Explains how the system is structured.

Should include:

- Data flow
- Core modules
- UI layer
- Database layer
- Later FastAPI architecture

### docs/COST_ANALYSIS.md

Explains expected cost, token usage, VPS cost, and scaling considerations.

### docs/PRIVACY_AND_SAFETY.md

Explains how the project handles CV data and avoids becoming an automated hiring system.

### docs/LEARNING_LOG.md

Short daily or weekly notes.

Each entry should include:

- What was done
- What was learned
- What was difficult
- Next step

### docs/THEORY_MAP.md

Connects the project to theory.

Examples:

- TF-IDF and vector spaces
- Cosine similarity
- Logistic regression
- Convexity
- Regularization
- Train/test split
- Precision and recall
- Generalization

### docs/DECISIONS.md

Records important technical decisions.

Examples:

- Why Streamlit is used first
- Why SQLite is used before PostgreSQL
- Why LLMs are not used in early versions
- Why the project focuses on job seekers instead of employers

## First Milestone

The first milestone is v0.1.

The goal is to build a classical NLP baseline that works without a database, without an LLM, and without deployment.

v0.1 should be able to:

- Accept CV text
- Accept job posting text
- Clean both texts
- Extract skills from both texts
- Split the CV into chunks
- Compute TF-IDF vectors
- Rank CV chunks against the job posting
- Show matched and missing skills
- Return a simple analysis report

This first milestone should focus on correctness, understanding, and clean code rather than design.