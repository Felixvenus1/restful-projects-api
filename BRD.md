# Portfolio Development Business Requirements Document

**Document Title:** Developer Portfolio — GitHub Project BRD
**Version:** 1.0

**Author:** $$
Your Name
$$

**Date:** March 2026
**Status:** Draft
**Audience:** Personal Reference / Technical Planning

***

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Document Purpose \& Scope](#2-document-purpose--scope)
3. [Portfolio Strategy \& Guiding Principles](#3-portfolio-strategy--guiding-principles)
4. [Project Inventory \& Skill Matrix](#4-project-inventory--skill-matrix)
5. [Project 01 — SQLite Game Stats Tracker](#5-project-01--sqlite-game-stats-tracker)
6. [Project 02 — RESTful CRUD API with FastAPI + SQLite](#6-project-02--restful-crud-api-with-fastapi--sqlite)
7. [Project 03 — Supabase Real-Time Leaderboard](#7-project-03--supabase-real-time-leaderboard)
8. [Project 04 — UK Open Data Explorer](#8-project-04--uk-open-data-explorer)
9. [Project 05 — Steam Gaming Trends Analyser](#9-project-05--steam-gaming-trends-analyser)
10. [Project 06 — Premier League Performance Analytics](#10-project-06--premier-league-performance-analytics)
11. [Project 07 — Customer Churn Prediction Model](#11-project-07--customer-churn-prediction-model)
12. [Project 08 — Time Series Forecasting Engine](#12-project-08--time-series-forecasting-engine)
13. [Project 09 — Customer Segmentation Dashboard](#13-project-09--customer-segmentation-dashboard)
14. [Project 10 — Streamlit Interactive Dashboard](#14-project-10--streamlit-interactive-dashboard)
15. [Project 11 — Plotly/Dash Exploration App](#15-project-11--plotlydash-exploration-app)
16. [Project 12 — Geographic Choropleth Map Viewer](#16-project-12--geographic-choropleth-map-viewer)
17. [Project 13 — CLI File Intelligence Tool](#17-project-13--cli-file-intelligence-tool)
18. [Project 14 — GitHub Actions Data Pipeline](#18-project-14--github-actions-data-pipeline)
19. [Project 15 — Python Package: datakit](#19-project-15--python-package-datakit)
20. [Project 16 — Local Dev MCP Server](#20-project-16--local-dev-mcp-server)
21. [Project 17 — Game Review Sentiment Classifier (PyTorch)](#21-project-17--game-review-sentiment-classifier-pytorch)
22. [GitHub Profile Standards](#22-github-profile-standards)
23. [Cross-Project Dependency Map](#23-cross-project-dependency-map)
24. [Global Tools \& Technologies Reference](#24-global-tools--technologies-reference)
25. [Appendix A — Milestone Summary Table](#25-appendix-a--milestone-summary-table)

***

## 1. Executive Summary

This Business Requirements Document (BRD) defines the scope, requirements, tooling, artefacts, and delivery milestones for a structured GitHub portfolio comprising **17 individual software projects**. The portfolio is designed to demonstrate technical breadth and depth to prospective employers in software engineering, data engineering, data science, machine learning, and AI tooling roles.

Each project is intentionally scoped to be **completable as a solo developer** using entirely **free, open-source tools** with no paid subscriptions or API access fees required. Projects are designed to be independently valuable but also **thematically connected**, allowing the portfolio to tell a coherent story about an engineer who can move fluidly across a modern data and software stack.

The portfolio covers seven technical domains:

- **Relational Databases** — schema design, CRUD operations, cloud-backed persistence
- **Data Analytics** — exploratory data analysis, statistical reasoning, public datasets
- **Data Science \& Classical ML** — supervised learning, time series, clustering, model evaluation
- **Deep Learning / NLP** — PyTorch training loops, transformer fine-tuning, sentiment analysis
- **Data Visualisation** — interactive dashboards, geographic maps, charting libraries
- **Software Engineering** — clean architecture, CLI tooling, packaging, testing, CI/CD
- **AI Tooling (MCP)** — Model Context Protocol server development, AI assistant integration

The PyTorch project (Project 17) is purposefully designed as an **extension of the Steam Gaming Trends Analyser** (Project 05), creating a narrative arc where analytics work informs and feeds into a deep learning pipeline — demonstrating mature, connected engineering thinking.

***

## 2. Document Purpose \& Scope

### 2.1 Purpose

This BRD exists to:

- Define clear, unambiguous requirements for each portfolio project before development begins
- Prevent scope creep by establishing what is and is not in scope for each project
- Serve as a reference document during development and as retrospective documentation for README files
- Ensure the portfolio as a whole tells a coherent, employer-facing story


### 2.2 Scope

**In scope:**

- All 17 projects listed in the Table of Contents
- GitHub repository structures for each project
- Artefact placeholders (diagrams, schemas, notebooks) with descriptions
- Milestone definitions for each project
- A global standards section governing how all repos are presented

**Out of scope:**

- Actual code or implementation
- Deployment to paid cloud services
- Projects requiring proprietary data or APIs behind a paywall


### 2.3 Assumptions

- Developer has Python 3.11+ installed
- VS Code with GitHub Copilot is the primary IDE
- Git and GitHub CLI are configured
- All public repos will be on GitHub under a single account
- No budget is allocated — all tools must be free or open-source

***

## 3. Portfolio Strategy \& Guiding Principles

### 3.1 Employer-First Thinking

Every project must answer the question: *"What does this show a hiring manager in 30 seconds?"* Each repository's README, folder structure, and live demo link (where applicable) should make this immediately obvious.

### 3.2 Depth Over Breadth Within Each Domain

Rather than producing shallow demos, each project should demonstrate one or two skills with genuine depth. A churn model with proper cross-validation, a ROC curve, and feature importance analysis is worth far more than ten trivial notebooks.

### 3.3 Connected Narrative

Several projects share data or themes (Steam games, UK public data). This is intentional — it allows the portfolio to function as a connected body of work rather than a disconnected list of tutorials.

### 3.4 Engineering Discipline

Every project, regardless of its primary focus, must meet baseline software engineering standards: clear README, requirements file, at least basic tests, and a `.gitignore`. This signals production-code habits.

### 3.5 Suggested Build Order

Build projects roughly in this sequence to leverage learning and reuse artefacts:

```
DB Projects (1→2→3) → Analytics (4→5→6) → Visualisation (10→11→12)
→ Data Science (7→8→9) → PyTorch (17) → SE (13→14→15) → MCP (16)
```


***

## 4. Project Inventory \& Skill Matrix

| \# | Project Name | Primary Domain | Secondary Domain | Live Demo | Complexity |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 01 | SQLite Game Stats Tracker | Databases | Software Engineering | No | Low |
| 02 | RESTful CRUD API | Databases | Software Engineering | Swagger UI | Low–Med |
| 03 | Supabase Leaderboard | Databases | Cloud / Real-Time | Yes (Supabase) | Medium |
| 04 | UK Open Data Explorer | Data Analytics | Data Visualisation | Jupyter | Low |
| 05 | Steam Gaming Trends | Data Analytics | Data Science | Jupyter | Medium |
| 06 | Premier League Analytics | Data Analytics | Data Visualisation | Jupyter | Medium |
| 07 | Churn Prediction Model | Data Science | ML Engineering | No | Medium |
| 08 | Time Series Forecasting | Data Science | ML Engineering | No | Medium |
| 09 | Segmentation Dashboard | Data Science | Data Visualisation | Streamlit | Medium |
| 10 | Streamlit Dashboard | Data Visualisation | Data Analytics | Streamlit Cloud | Low–Med |
| 11 | Plotly/Dash App | Data Visualisation | Software Engineering | Render | Medium |
| 12 | Geographic Choropleth | Data Visualisation | Data Analytics | HTML export | Low |
| 13 | CLI File Intelligence Tool | Software Engineering | Data Analytics | CLI | Medium |
| 14 | GitHub Actions Pipeline | DevOps / SE | Data Analytics | GitHub | Low–Med |
| 15 | Python Package: datakit | Software Engineering | PyPI | pip install | Medium |
| 16 | Local Dev MCP Server | AI Tooling | Software Engineering | Claude/VS Code | Medium–High |
| 17 | Game Review Classifier | Deep Learning / NLP | Data Science | Jupyter + Model | High |


***

## 5. Project 01 — SQLite Game Stats Tracker

### 5.1 Overview

A command-line Python application that records, stores, and queries game session data using a local SQLite database. Designed to demonstrate relational database fundamentals (schema design, normalisation, CRUD), Python's native `sqlite3` module, and clean CLI architecture.

### 5.2 Business Objectives

- Demonstrate proficiency in relational schema design without an ORM
- Show raw SQL query writing (no abstraction layer)
- Produce a functional, documented CLI tool as a deliverable


### 5.3 Functional Requirements

- **FR-01:** The user shall be able to log a new game session with: game name, score, level reached, duration (minutes), and timestamp
- **FR-02:** The user shall be able to query all sessions for a specific game
- **FR-03:** The user shall be able to retrieve aggregate stats (total sessions, average score, highest score, most played game)
- **FR-04:** The user shall be able to delete sessions by session ID
- **FR-05:** The database shall be created automatically on first run if it does not exist
- **FR-06:** All commands shall be accessible via a CLI interface


### 5.4 Non-Functional Requirements

- **NFR-01:** Written in Python 3.11+ using only the standard library (`sqlite3`, `argparse`) — no pip dependencies required
- **NFR-02:** Database file shall be stored locally as `stats.db`
- **NFR-03:** Unit tests shall cover all query functions using an in-memory SQLite database
- **NFR-04:** Code shall comply with PEP 8 style conventions


### 5.5 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Language | Python 3.11+ | Free |
| Database | SQLite (stdlib `sqlite3`) | Free |
| CLI | `argparse` (stdlib) | Free |
| Testing | `pytest` | Free |
| Style | `ruff` (linter) | Free |

### 5.6 Artefacts

> **[ARTEFACT 01-A] Entity-Relationship Diagram**
> *Should include: `sessions` table (session_id PK, game_name, score, level, duration_minutes, created_at), `games` lookup table (game_id PK, game_name, genre), foreign key relationship. Tool: dbdiagram.io (free) or hand-drawn and photographed.*

> **[ARTEFACT 01-B] CLI Command Reference Table**
> *Should include: each command, its flags, example usage, and expected output. Format: Markdown table in README.*

> **[ARTEFACT 01-C] Database Schema SQL Script**
> *Should include: `CREATE TABLE` statements with appropriate constraints (NOT NULL, DEFAULT, FOREIGN KEY). Located at `/sql/schema.sql`.*

### 5.7 GitHub Repository Structure

```
sqlite-game-stats/
├── README.md                  # Project overview, usage, screenshots
├── .gitignore                 # Ignore stats.db, __pycache__, .env
├── requirements.txt           # Empty or pytest only
├── pyproject.toml             # Project metadata
├── src/
│   └── game_stats/
│       ├── __init__.py
│       ├── db.py              # Connection and schema initialisation
│       ├── queries.py         # All SQL query functions
│       └── cli.py             # argparse command definitions
├── sql/
│   └── schema.sql             # Raw schema DDL script
├── tests/
│   ├── __init__.py
│   ├── test_db.py             # Tests using in-memory SQLite
│   └── test_queries.py
└── docs/
    └── erd.png                # [ARTEFACT 01-A] ERD image
```


### 5.8 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Schema Design | Define tables, relationships, and constraints; write `schema.sql` |
| M2 | Database Layer | Implement `db.py` — connection management and schema initialisation |
| M3 | Query Layer | Implement all CRUD functions in `queries.py` with docstrings |
| M4 | CLI Layer | Wire all commands via `argparse` in `cli.py` |
| M5 | Testing | Write `pytest` tests using in-memory DB; achieve >80% coverage |
| M6 | Documentation | Complete README with demo GIF and CLI reference table |


***

## 6. Project 02 — RESTful CRUD API with FastAPI + SQLite

### 6.1 Overview

A production-structured REST API built with FastAPI, using SQLite as its persistence layer and SQLAlchemy as the ORM. This project demonstrates HTTP API design (endpoints, status codes, validation), ORM usage, Pydantic schema validation, and auto-generated API documentation.[^1]

### 6.2 Business Objectives

- Demonstrate REST API design principles (proper HTTP verbs, response codes, error handling)
- Show ORM proficiency with SQLAlchemy
- Produce a live Swagger UI that acts as a visual portfolio showcase


### 6.3 Functional Requirements

- **FR-01:** The API shall expose full CRUD endpoints for a `Project` resource (project management domain)
- **FR-02:** `GET /projects` — retrieve all projects with optional filtering by status
- **FR-03:** `GET /projects/{id}` — retrieve a single project by ID; return 404 if not found
- **FR-04:** `POST /projects` — create a new project; validate input with Pydantic
- **FR-05:** `PUT /projects/{id}` — update a project; return 404 if not found
- **FR-06:** `DELETE /projects/{id}` — delete a project; return 204 on success
- **FR-07:** Swagger UI (`/docs`) and ReDoc (`/redoc`) shall be accessible
- **FR-08:** All endpoints shall return structured JSON responses with consistent error envelopes


### 6.4 Non-Functional Requirements

- **NFR-01:** Follow layered architecture: routers → services → repositories → models[^2]
- **NFR-02:** Input validation errors shall return HTTP 422 with field-level detail
- **NFR-03:** The API shall be runnable with a single `uvicorn` command
- **NFR-04:** Integration tests shall cover all endpoints using `TestClient`


### 6.5 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Framework | FastAPI | Free |
| ASGI Server | Uvicorn | Free |
| ORM | SQLAlchemy 2.0 | Free |
| Database | SQLite | Free |
| Validation | Pydantic v2 | Free |
| Testing | pytest + httpx | Free |
| Docs | Built-in Swagger UI | Free |

### 6.6 Artefacts

> **[ARTEFACT 02-A] API Endpoint Specification Table**
> *Should include: Method, Path, Request Body schema, Response schema, HTTP status codes, and description. Format: Markdown table in README.*

> **[ARTEFACT 02-B] Architecture Layer Diagram**
> *Should include: Client → Router → Service → Repository → SQLAlchemy Model → SQLite. Show data flow direction and what each layer is responsible for. Tool: draw.io or Mermaid diagram in README.*

> **[ARTEFACT 02-C] Pydantic Schema Definitions**
> *Should include: `ProjectCreate`, `ProjectUpdate`, `ProjectResponse` schemas with field names, types, and validation rules. Located in `/src/schemas.py`.*

> **[ARTEFACT 02-D] Swagger UI Screenshot**
> *Should include: A screenshot of the `/docs` page showing all endpoints expanded. Embed in README as a visual demo.*

### 6.7 GitHub Repository Structure

```
fastapi-project-api/
├── README.md
├── .gitignore
├── requirements.txt           # fastapi, uvicorn, sqlalchemy, pydantic, pytest, httpx
├── pyproject.toml
├── .env.example               # Template for environment variables
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py            # FastAPI app instance, startup events
│       ├── database.py        # SQLAlchemy engine and session factory
│       ├── models.py          # SQLAlchemy ORM models
│       ├── schemas.py         # Pydantic request/response schemas
│       ├── routers/
│       │   ├── __init__.py
│       │   └── projects.py    # Route definitions
│       ├── services/
│       │   ├── __init__.py
│       │   └── project_service.py  # Business logic
│       └── repositories/
│           ├── __init__.py
│           └── project_repo.py     # DB queries via SQLAlchemy
├── tests/
│   ├── conftest.py            # TestClient fixture, test DB setup
│   ├── test_projects_crud.py
│   └── test_validation.py
└── docs/
    └── swagger_screenshot.png # [ARTEFACT 02-D]
```


### 6.8 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Schema \& Models | Define SQLAlchemy models and Pydantic schemas |
| M2 | Database Layer | Set up SQLite engine, session factory, and table creation |
| M3 | Repository Layer | Implement all CRUD database operations |
| M4 | Service Layer | Add business logic; decouple from DB layer |
| M5 | Router Layer | Define all FastAPI routes; wire to services |
| M6 | Testing | Full integration test suite using `TestClient` |
| M7 | Documentation | README with Swagger screenshot, architecture diagram |


***

## 7. Project 03 — Supabase Real-Time Leaderboard

### 7.1 Overview

A web-based game leaderboard backed by Supabase's free-tier PostgreSQL database. This project demonstrates cloud database integration, real-time data subscriptions, and a lightweight web frontend — bridging database skills with web delivery. Supabase's free tier provides a full hosted PostgreSQL instance, REST API, and real-time subscriptions at no cost.

### 7.2 Business Objectives

- Demonstrate cloud database integration skills (managed PostgreSQL)
- Show real-time data capability via Supabase Realtime
- Produce a live, accessible URL that can be linked from a CV


### 7.3 Functional Requirements

- **FR-01:** The system shall display a ranked leaderboard of players sorted by score (descending)
- **FR-02:** The system shall allow a new score submission via a form (player name + score)
- **FR-03:** The leaderboard shall update in real time when a new score is submitted (using Supabase Realtime)
- **FR-04:** The frontend shall display rank, player name, score, and submission timestamp
- **FR-05:** The system shall cap the leaderboard display at the top 20 entries
- **FR-06:** Scores shall be validated server-side (must be a positive integer)


### 7.4 Non-Functional Requirements

- **NFR-01:** Frontend shall be pure HTML/CSS/JavaScript (no paid frameworks) or a lightweight Python framework (Streamlit/Flask)
- **NFR-02:** All Supabase credentials shall be stored in environment variables, never committed to Git
- **NFR-03:** The deployed app shall be accessible via a public URL (Streamlit Cloud or Vercel free tier)


### 7.5 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Cloud Database | Supabase (free tier — 500MB, 2 projects) | Free |
| DB Engine | PostgreSQL (via Supabase) | Free |
| Backend SDK | `supabase-py` | Free |
| Frontend | Streamlit or Vanilla JS | Free |
| Deployment | Streamlit Community Cloud | Free |
| Environment Mgmt | `python-dotenv` | Free |

### 7.6 Artefacts

> **[ARTEFACT 03-A] Supabase Table Schema**
> *Should include: `leaderboard` table definition — `id` (UUID PK), `player_name` (VARCHAR), `score` (INTEGER), `game_name` (VARCHAR), `created_at` (TIMESTAMPTZ DEFAULT now()). Include the SQL used to create the table.*

> **[ARTEFACT 03-B] Data Flow Diagram**
> *Should include: User submits form → Python backend → Supabase REST API → PostgreSQL → Supabase Realtime pushes update → Frontend rerenders. Tool: Mermaid sequence diagram.*

> **[ARTEFACT 03-C] Live App Screenshot**
> *Should include: Screenshot of the running leaderboard with ranked entries, embedded in README.*

### 7.7 GitHub Repository Structure

```
supabase-leaderboard/
├── README.md                  # Live URL link, setup guide, screenshots
├── .gitignore                 # Ignore .env
├── requirements.txt           # supabase, streamlit, python-dotenv
├── .env.example               # SUPABASE_URL=, SUPABASE_KEY=
├── app.py                     # Streamlit frontend and Supabase integration
├── src/
│   ├── db.py                  # Supabase client setup
│   └── leaderboard.py         # Score fetching, insertion, validation logic
├── sql/
│   └── schema.sql             # [ARTEFACT 03-A] PostgreSQL DDL
└── docs/
    └── dataflow.md            # [ARTEFACT 03-B] Mermaid diagram
```


### 7.8 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Supabase Setup | Create Supabase project, define schema, configure RLS policies |
| M2 | Backend Integration | Implement `db.py` and score insert/fetch logic using `supabase-py` |
| M3 | Frontend (Static) | Build leaderboard display and submission form in Streamlit |
| M4 | Real-Time | Integrate Supabase Realtime for live updates |
| M5 | Deployment | Deploy to Streamlit Community Cloud; configure environment secrets |
| M6 | Documentation | README with live URL, architecture notes, setup instructions |


***

## 8. Project 04 — UK Open Data Explorer

### 8.1 Overview

A Jupyter notebook-based exploratory data analysis (EDA) project using publicly available datasets from [data.gov.uk](https://data.gov.uk). The goal is to demonstrate statistical reasoning, data cleaning, and narrative-driven analysis on real-world messy data. This project prioritises documentation quality — the notebook itself is the portfolio deliverable.

### 8.2 Business Objectives

- Demonstrate EDA methodology with real-world, imperfect public data
- Show proficiency in data cleaning, descriptive statistics, and visual storytelling
- Produce a well-narrated, publication-quality Jupyter notebook


### 8.3 Dataset Options (choose one)

- **Road Safety / Accidents** — rich, well-structured; shows geospatial and temporal analysis
- **NHS Waiting Times** — demonstrates time series and regional comparison
- **UK Local Authority Deprivation Indices** — allows correlation and geographic analysis

*Recommended: Road Safety dataset — most visually rich and technically interesting.*

### 8.4 Functional Requirements

- **FR-01:** The notebook shall load and describe the raw dataset (shape, dtypes, null counts)
- **FR-02:** The notebook shall clean the data (handle nulls, fix dtypes, remove duplicates) with explanations in markdown cells
- **FR-03:** The notebook shall produce at least 6 distinct visualisations (trend over time, regional breakdown, correlation heatmap, distribution histogram, bar chart, scatter plot)
- **FR-04:** Each visualisation shall be accompanied by a written interpretation in markdown
- **FR-05:** The notebook shall conclude with a written summary of 3–5 key findings
- **FR-06:** A `data/` directory shall contain a data download script rather than the raw data file (if file is large)


### 8.5 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Language | Python 3.11+ | Free |
| Data Manipulation | Pandas, NumPy | Free |
| Visualisation | Matplotlib, Seaborn | Free |
| Notebooks | Jupyter Lab | Free |
| Data Source | data.gov.uk (open licence) | Free |
| Linting | `nbqa` + `ruff` | Free |

### 8.6 Artefacts

> **[ARTEFACT 04-A] Data Dictionary**
> *Should include: Each column name, data type, description, and notes on quality issues encountered. Format: Markdown table at the top of the notebook or in a separate `docs/data_dictionary.md`.*

> **[ARTEFACT 04-B] Data Cleaning Log**
> *Should include: For each cleaning action taken (e.g., dropping nulls in column X, recasting column Y to datetime), the before/after row counts and justification. Format: Markdown cells within the notebook.*

> **[ARTEFACT 04-C] Key Findings Section**
> *Should include: 3–5 bullet-point insights drawn from the analysis, written in plain English for a non-technical reader. Located at the bottom of the notebook.*

### 8.7 GitHub Repository Structure

```
uk-open-data-explorer/
├── README.md                  # What dataset, key findings summary, notebook preview
├── .gitignore                 # Ignore large data files, .ipynb_checkpoints
├── requirements.txt           # pandas, numpy, matplotlib, seaborn, jupyter
├── notebooks/
│   └── eda_road_safety.ipynb  # Main analysis notebook
├── data/
│   ├── download_data.py       # Script to fetch data from data.gov.uk
│   └── README.md              # Instructions for data acquisition
├── docs/
│   └── data_dictionary.md     # [ARTEFACT 04-A]
└── outputs/
    └── figures/               # Exported chart PNGs for README embedding
```


### 8.8 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Acquisition | Write `download_data.py`; verify dataset licence and structure |
| M2 | Data Profiling | Load and describe data; produce data dictionary |
| M3 | Data Cleaning | Handle nulls, fix dtypes, document all decisions |
| M4 | Exploratory Analysis | Produce all 6+ visualisations with interpretations |
| M5 | Key Findings | Write conclusion section |
| M6 | Polish | Clean notebook output, ensure runs top-to-bottom cleanly, update README |


***

## 9. Project 05 — Steam Gaming Trends Analyser

### 9.1 Overview

An analytical notebook exploring trends in the PC gaming market using Steam platform datasets (sourced freely from Kaggle or the Steam public API). This project demonstrates applied EDA with domain knowledge, feature engineering, and sentiment analysis groundwork — and crucially **feeds data into Project 17 (PyTorch Classifier)**, making it a cornerstone of the portfolio narrative.

### 9.2 Business Objectives

- Demonstrate EDA on a large, real-world commercial dataset
- Show feature engineering and multi-dataset joining skills
- Establish the dataset and preprocessing pipeline that Project 17 will use


### 9.3 Functional Requirements

- **FR-01:** The analysis shall cover at least three dimensions: pricing trends, review volume over time, and genre popularity
- **FR-02:** The notebook shall engineer at least 3 derived features (e.g., review positivity ratio, price-per-hour-of-playtime, release-year lag)
- **FR-03:** The notebook shall produce a cleaned, serialised dataset (`processed_reviews.parquet`) for use in Project 17
- **FR-04:** Sentiment polarity of review text shall be estimated using VADER (lightweight, rule-based — as a baseline for Project 17's deep learning model)
- **FR-05:** Visualisations shall include: genre distribution bar chart, price vs. review score scatter plot, release volume over time, top 10 games by review count


### 9.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Data Source | Kaggle Steam datasets (free account) | Free |
| Data Manipulation | Pandas, NumPy | Free |
| NLP (baseline) | VADER (`vaderSentiment`) | Free |
| Visualisation | Matplotlib, Seaborn, Plotly Express | Free |
| Serialisation | Parquet via `pyarrow` | Free |
| Notebooks | Jupyter Lab | Free |

### 9.5 Artefacts

> **[ARTEFACT 05-A] Dataset Provenance Note**
> *Should include: Source URL, licence type, download date, original column definitions, and any known data quality issues. Format: Markdown in `data/README.md`.*

> **[ARTEFACT 05-B] Feature Engineering Log**
> *Should include: Name of each derived feature, the formula or logic used to compute it, and its intended analytical purpose. Format: Markdown table in the notebook.*

> **[ARTEFACT 05-C] VADER vs. Ground Truth Comparison**
> *Should include: A sample of 20 reviews with VADER scores and their actual Steam recommendation label (recommended/not recommended), as a baseline accuracy sanity check. This sets up the motivation for Project 17's deep learning approach.*

> **[ARTEFACT 05-D] Processed Output Schema**
> *Should include: Schema of `processed_reviews.parquet` — column names, types, and description. This is the contract between Project 05 and Project 17.*

### 9.6 GitHub Repository Structure

```
steam-gaming-trends/
├── README.md
├── .gitignore                 # Ignore large data files, parquet outputs
├── requirements.txt
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_eda_trends.ipynb
│   └── 03_baseline_sentiment.ipynb
├── data/
│   ├── download_data.py
│   └── README.md              # [ARTEFACT 05-A]
├── src/
│   ├── features.py            # Feature engineering functions
│   └── sentiment.py           # VADER sentiment wrapper
├── outputs/
│   ├── figures/
│   └── processed_reviews.parquet  # Contract output for Project 17
└── docs/
    └── feature_log.md         # [ARTEFACT 05-B]
```


### 9.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Acquisition | Kaggle API download; verify columns and row counts |
| M2 | Profiling \& Cleaning | Profile nulls, fix types, document in data dictionary |
| M3 | EDA — Trends | Produce all required trend visualisations |
| M4 | Feature Engineering | Compute and document all derived features |
| M5 | Baseline Sentiment | Run VADER; produce [ARTEFACT 05-C] baseline comparison |
| M6 | Output Contract | Serialise `processed_reviews.parquet` with documented schema |
| M7 | Documentation | Update README; cross-reference Project 17 |


***

## 10. Project 06 — Premier League Performance Analytics

### 10.1 Overview

A data analytics notebook focused on Premier League football statistics sourced from FBref or a Kaggle football dataset. This project demonstrates multi-table joins, correlation analysis, statistical hypothesis testing, and domain-specific feature interpretation — all using free, publicly available data.

### 10.2 Business Objectives

- Demonstrate statistical analysis beyond simple EDA (correlation, hypothesis testing)
- Show multi-dataset joining and entity resolution (matching player names across tables)
- Produce a visually compelling notebook with sports domain context


### 10.3 Functional Requirements

- **FR-01:** The analysis shall cover at least two seasons of data
- **FR-02:** Player-level and team-level statistics shall be joined and analysed separately
- **FR-03:** The notebook shall include a correlation matrix across at least 10 performance metrics
- **FR-04:** The notebook shall perform at least one statistical significance test (e.g., t-test comparing two groups of players or teams)
- **FR-05:** Visualisations shall include: radar chart (player profile comparison), scatter plot with regression line (e.g., xG vs. actual goals), ranked bar chart, correlation heatmap
- **FR-06:** A "player similarity" function shall return the N most statistically similar players to a given input using Euclidean or cosine distance


### 10.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Data Source | FBref (scrape via `soccerdata` library) or Kaggle | Free |
| Data Manipulation | Pandas, NumPy | Free |
| Statistics | SciPy | Free |
| Visualisation | Matplotlib, Seaborn, Plotly | Free |
| Notebooks | Jupyter Lab | Free |

### 10.5 Artefacts

> **[ARTEFACT 06-A] Correlation Heatmap**
> *Should include: Pearson correlation matrix across 10+ performance metrics rendered as a Seaborn heatmap with annotated values. Export to `/outputs/figures/correlation_heatmap.png`.*

> **[ARTEFACT 06-B] Player Radar Chart**
> *Should include: A Plotly polar/radar chart comparing two selected players across 6 normalised metrics (goals, assists, key passes, dribbles, defensive actions, xG). Export to `/outputs/figures/radar_chart.png`.*

> **[ARTEFACT 06-C] Statistical Test Write-Up**
> *Should include: Hypothesis, test type, p-value, interpretation in plain English. Format: Markdown cell in the notebook immediately following the test code.*

### 10.6 GitHub Repository Structure

```
premier-league-analytics/
├── README.md
├── .gitignore
├── requirements.txt           # pandas, numpy, scipy, matplotlib, seaborn, plotly
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_team_analysis.ipynb
│   └── 03_player_analysis.ipynb
├── data/
│   ├── fetch_data.py
│   └── README.md
├── src/
│   ├── similarity.py          # Player similarity function
│   └── charts.py              # Reusable chart functions
├── outputs/
│   └── figures/               # [ARTEFACTS 06-A, 06-B]
└── tests/
    └── test_similarity.py     # Unit tests for similarity function
```


### 10.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Acquisition | Fetch data; handle multi-season joins |
| M2 | Cleaning \& Joining | Entity resolution; produce clean player and team tables |
| M3 | Team Analysis | Team-level trends and comparison |
| M4 | Player Analysis | Correlation matrix, radar chart, regression analysis |
| M5 | Statistical Testing | Formulate and run at least one hypothesis test |
| M6 | Similarity Function | Implement and test `find_similar_players()` |
| M7 | Documentation | README with key findings, chart exports embedded |


***

## 11. Project 07 — Customer Churn Prediction Model

### 11.1 Overview

A supervised machine learning project that predicts customer churn using a free Kaggle telecom dataset. This project demonstrates a complete, rigorous ML pipeline: data preprocessing, feature engineering, model training, cross-validation, hyperparameter tuning, and evaluation — with clear documentation of every decision.

### 11.2 Business Objectives

- Demonstrate a full, disciplined ML pipeline from raw data to evaluated model
- Show model comparison methodology (not just "I ran Random Forest")
- Produce interpretable results (feature importance, confusion matrix, ROC curve)


### 11.3 Functional Requirements

- **FR-01:** The pipeline shall support at least 3 model types: Logistic Regression, Random Forest, and XGBoost
- **FR-02:** All models shall be evaluated using stratified k-fold cross-validation (k=5)
- **FR-03:** Evaluation metrics shall include: accuracy, precision, recall, F1, AUC-ROC
- **FR-04:** Feature importance shall be extracted and visualised for the best-performing model
- **FR-05:** A SHAP (SHapley Additive exPlanations) analysis shall be included for interpretability
- **FR-06:** The best model shall be serialised to disk using `joblib`
- **FR-07:** A `predict.py` script shall load the serialised model and return predictions for a given input CSV


### 11.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Data Source | Kaggle Telco Customer Churn dataset | Free |
| ML Framework | Scikit-learn | Free |
| Boosting | XGBoost | Free |
| Interpretability | SHAP | Free |
| Model Serialisation | joblib | Free |
| Notebooks | Jupyter Lab | Free |
| Testing | pytest | Free |

### 11.5 Artefacts

> **[ARTEFACT 07-A] Model Comparison Table**
> *Should include: For each of the 3 models — CV mean accuracy, CV mean F1, CV mean AUC-ROC, training time. Format: Markdown table in README and notebook.*

> **[ARTEFACT 07-B] ROC Curve Plot**
> *Should include: Multi-model ROC curves on a single plot with AUC scores in the legend. Export to `/outputs/figures/roc_curves.png`.*

> **[ARTEFACT 07-C] SHAP Summary Plot**
> *Should include: SHAP beeswarm or bar chart showing top 10 most influential features for the best model. Export to `/outputs/figures/shap_summary.png`.*

> **[ARTEFACT 07-D] ML Pipeline Diagram**
> *Should include: Raw Data → Cleaning → Feature Engineering → Train/Test Split → Cross-Validation → Model Training → Evaluation → Serialisation. Tool: Mermaid flowchart in README.*

### 11.6 GitHub Repository Structure

```
churn-prediction/
├── README.md                  # Problem statement, results, model comparison table
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modelling.ipynb
├── src/
│   ├── preprocess.py          # Cleaning and encoding functions
│   ├── train.py               # Model training and evaluation logic
│   └── predict.py             # Load model; run inference on input CSV
├── models/
│   └── best_model.joblib      # Serialised trained model
├── data/
│   └── README.md              # Dataset source and download instructions
├── outputs/
│   └── figures/               # [ARTEFACTS 07-B, 07-C]
└── tests/
    ├── test_preprocess.py
    └── test_predict.py
```


### 11.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | EDA | Explore class imbalance, feature distributions, correlations |
| M2 | Preprocessing | Encode categoricals, scale numerics, handle nulls |
| M3 | Baseline Model | Train Logistic Regression; establish baseline metrics |
| M4 | Advanced Models | Train Random Forest and XGBoost with cross-validation |
| M5 | Evaluation | Produce ROC curves, confusion matrices, metric comparison table |
| M6 | Interpretability | SHAP analysis on best model |
| M7 | Inference Script | Write and test `predict.py` |
| M8 | Documentation | README with results, artefacts, and methodology explanation |


***

## 12. Project 08 — Time Series Forecasting Engine

### 12.1 Overview

A time series analysis and forecasting project using publicly available energy consumption or weather data. This project demonstrates classical time series concepts (stationarity, decomposition, autocorrelation) alongside modern forecasting approaches (Prophet), producing a structured, reproducible forecasting pipeline.

### 12.2 Business Objectives

- Demonstrate time series-specific techniques that differ from standard ML
- Show understanding of train/test splitting for sequential data
- Produce a reusable forecasting module, not just a notebook


### 12.3 Functional Requirements

- **FR-01:** The system shall support at least two datasets: a short-term (daily) and a long-term (monthly) time series
- **FR-02:** The notebook shall perform: decomposition (trend, seasonality, residuals), ADF stationarity test, ACF/PACF plots
- **FR-03:** At least two forecasting models shall be implemented and compared: Prophet and an ARIMA/SARIMA baseline
- **FR-04:** Train/test split shall respect temporal ordering (no data leakage)
- **FR-05:** Evaluation metrics shall include: MAE, RMSE, and MAPE
- **FR-06:** A reusable `Forecaster` class in `/src/forecaster.py` shall wrap model training and prediction
- **FR-07:** Forecast output shall include confidence intervals


### 12.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Data Source | UK National Grid ESO open data or Open-Meteo API (free) | Free |
| Time Series | Pandas, NumPy | Free |
| Statistics | Statsmodels (ARIMA, ADF, ACF/PACF) | Free |
| Forecasting | Prophet (by Meta, open source) | Free |
| Visualisation | Matplotlib, Plotly | Free |

### 12.5 Artefacts

> **[ARTEFACT 08-A] Time Series Decomposition Plot**
> *Should include: Four-panel plot — original series, trend component, seasonal component, residuals. Export to `/outputs/figures/decomposition.png`.*

> **[ARTEFACT 08-B] ACF / PACF Plot**
> *Should include: Side-by-side ACF and PACF plots with lag values annotated. Used to justify ARIMA parameter selection. Export to `/outputs/figures/acf_pacf.png`.*

> **[ARTEFACT 08-C] Forecast Comparison Chart**
> *Should include: Actual vs. Prophet forecast vs. ARIMA forecast on the test set, with confidence intervals shaded. Export to `/outputs/figures/forecast_comparison.png`.*

> **[ARTEFACT 08-D] Model Performance Table**
> *Should include: MAE, RMSE, MAPE for each model on the test set. Format: Markdown table in README.*

### 12.6 GitHub Repository Structure

```
time-series-forecasting/
├── README.md
├── .gitignore
├── requirements.txt           # pandas, prophet, statsmodels, plotly, matplotlib
├── notebooks/
│   ├── 01_decomposition.ipynb
│   ├── 02_arima_model.ipynb
│   └── 03_prophet_model.ipynb
├── src/
│   └── forecaster.py          # Reusable Forecaster class
├── data/
│   └── fetch_data.py          # Download script for chosen dataset
├── outputs/
│   └── figures/               # [ARTEFACTS 08-A, 08-B, 08-C]
└── tests/
    └── test_forecaster.py
```


### 12.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Acquisition | Fetch data; verify temporal resolution and continuity |
| M2 | Decomposition | Perform and visualise decomposition; run ADF test |
| M3 | ARIMA Baseline | Select p/d/q using ACF/PACF; train and evaluate |
| M4 | Prophet Model | Configure and train Prophet with seasonality modes |
| M5 | Comparison | Produce [ARTEFACT 08-C] and metric table |
| M6 | Forecaster Class | Wrap logic into reusable class; write tests |
| M7 | Documentation | README with methodology and results |


***

## 13. Project 09 — Customer Segmentation Dashboard

### 13.1 Overview

An unsupervised machine learning project applying clustering techniques to a retail or e-commerce dataset to produce customer segments. Results are visualised in an interactive Streamlit dashboard. This project demonstrates ML model selection, dimensionality reduction, and the ability to communicate cluster insights to a non-technical audience.

### 13.2 Business Objectives

- Demonstrate unsupervised ML (K-Means, DBSCAN) and cluster evaluation
- Show dimensionality reduction (PCA, t-SNE) for visualisation
- Produce an interactive live dashboard that non-technical stakeholders can explore


### 13.3 Functional Requirements

- **FR-01:** The system shall apply at least two clustering algorithms: K-Means and DBSCAN
- **FR-02:** Optimal K for K-Means shall be determined using the Elbow Method and Silhouette Score
- **FR-03:** Clusters shall be visualised in 2D using PCA-reduced components
- **FR-04:** The Streamlit dashboard shall allow users to: select number of clusters, filter by cluster, view cluster statistics
- **FR-05:** Each cluster shall have a human-readable label with a written interpretation (e.g., "High-Value Loyalists", "At-Risk Occasional Buyers")
- **FR-06:** The dashboard shall display a cluster profile table (mean values per feature per cluster)


### 13.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Data Source | UCI Online Retail dataset or Kaggle (free) | Free |
| ML | Scikit-learn (KMeans, DBSCAN, PCA, t-SNE) | Free |
| Dashboard | Streamlit | Free |
| Deployment | Streamlit Community Cloud | Free |
| Visualisation | Plotly Express | Free |

### 13.5 Artefacts

> **[ARTEFACT 09-A] Elbow / Silhouette Plot**
> *Should include: Line plot of inertia vs. K (Elbow) and Silhouette Score vs. K on the same or adjacent axes, with the chosen K annotated. Export to `/outputs/figures/elbow_silhouette.png`.*

> **[ARTEFACT 09-B] PCA Scatter Plot with Cluster Colours**
> *Should include: 2D scatter plot of all data points projected onto the first two principal components, coloured by cluster assignment. Export to `/outputs/figures/pca_clusters.png`.*

> **[ARTEFACT 09-C] Cluster Profile Table**
> *Should include: Mean value of each feature for each cluster, formatted as a heatmap-styled table. Displayed in Streamlit dashboard and exported as `/outputs/cluster_profiles.csv`.*

### 13.6 GitHub Repository Structure

```
customer-segmentation/
├── README.md                  # Live link, cluster descriptions, methodology
├── .gitignore
├── requirements.txt
├── app.py                     # Streamlit dashboard entry point
├── src/
│   ├── preprocess.py
│   ├── cluster.py             # KMeans, DBSCAN, elbow/silhouette logic
│   └── reduce.py              # PCA and t-SNE wrappers
├── data/
│   └── download_data.py
├── outputs/
│   ├── figures/               # [ARTEFACTS 09-A, 09-B]
│   └── cluster_profiles.csv   # [ARTEFACT 09-C]
└── tests/
    └── test_cluster.py
```


### 13.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Acquisition \& Cleaning | Load retail data; handle returns, outliers, currency |
| M2 | Feature Engineering | RFM (Recency, Frequency, Monetary) feature construction |
| M3 | Cluster Optimisation | Elbow method, Silhouette scores; choose K |
| M4 | Clustering | Apply K-Means and DBSCAN; evaluate and compare |
| M5 | Dimensionality Reduction | PCA visualisation; optionally t-SNE |
| M6 | Cluster Interpretation | Write human-readable cluster labels |
| M7 | Dashboard | Build Streamlit app with interactive filters |
| M8 | Deployment | Deploy to Streamlit Cloud; add live link to README |


***

## 14. Project 10 — Streamlit Interactive Dashboard

### 14.1 Overview

A multi-page Streamlit dashboard that aggregates visualisations and insights from Projects 04, 05, and 06 into a single, cohesive, navigable application. This project demonstrates frontend data application skills, Streamlit multipage architecture, and the ability to package analytical work into a polished, user-facing product.

### 14.2 Business Objectives

- Demonstrate Streamlit app architecture (multipage, session state, caching)
- Show ability to convert notebook work into a deployable application
- Produce a portfolio centrepiece with a live public URL


### 14.3 Functional Requirements

- **FR-01:** The app shall contain at least 3 pages: UK Open Data, Steam Trends, Football Analytics
- **FR-02:** Each page shall include interactive filters (date range, category selector, metric selector)
- **FR-03:** All charts shall use Plotly for interactivity (hover, zoom, pan)
- **FR-04:** Data loading shall use `@st.cache_data` to prevent redundant reloads
- **FR-05:** The sidebar shall provide navigation and global filters where applicable
- **FR-06:** The app shall include a "About This Portfolio" page explaining each data source and methodology


### 14.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Framework | Streamlit | Free |
| Charts | Plotly Express | Free |
| Deployment | Streamlit Community Cloud | Free |
| Data Sources | Outputs from Projects 04, 05, 06 | Free |
| Caching | `@st.cache_data` decorator | Free |

### 14.5 Artefacts

> **[ARTEFACT 10-A] App Wireframe**
> *Should include: Low-fidelity wireframe of each page layout — sidebar, filter panel, chart areas, table area. Tool: Excalidraw (free) or hand-drawn. Located at `docs/wireframe.png`.*

> **[ARTEFACT 10-B] Live App URL**
> *Should include: Public Streamlit Community Cloud URL embedded at the top of the README as a badge.*

> **[ARTEFACT 10-C] Page Navigation Diagram**
> *Should include: Mermaid diagram showing all pages and the data sources each page draws from.*

### 14.6 GitHub Repository Structure

```
streamlit-portfolio-dashboard/
├── README.md                  # Live URL badge, page descriptions, screenshots
├── .gitignore
├── requirements.txt
├── app.py                     # Entry point; navigation logic
├── pages/
│   ├── 1_uk_open_data.py
│   ├── 2_steam_trends.py
│   ├── 3_football_analytics.py
│   └── 4_about.py
├── src/
│   ├── data_loaders.py        # Cached data loading functions
│   └── chart_builders.py      # Reusable Plotly chart functions
├── data/
│   └── [cached outputs from Projects 04, 05, 06]
└── docs/
    └── wireframe.png          # [ARTEFACT 10-A]
```


### 14.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Data Consolidation | Prepare cached data outputs from Projects 04, 05, 06 |
| M2 | App Skeleton | Multipage structure; sidebar navigation working |
| M3 | Page 1 — UK Open Data | Migrate and enhance EDA charts to Plotly |
| M4 | Page 2 — Steam Trends | Migrate Steam charts; add interactive filters |
| M5 | Page 3 — Football | Migrate football charts; add player comparison selector |
| M6 | About Page | Write methodology and data source explanations |
| M7 | Polish \& Deploy | Performance tuning, caching, deploy to Streamlit Cloud |


***

## 15. Project 11 — Plotly/Dash Exploration App

### 15.1 Overview

A multi-tab Dash application built on Plotly's Dash framework, allowing users to upload a CSV and explore it interactively. This project demonstrates Dash callback architecture, component layout design, and software engineering discipline in a frontend-adjacent context. It is a general-purpose tool, making it broadly appealing on a portfolio.

### 15.2 Business Objectives

- Demonstrate Dash's callback system (reactive programming pattern)
- Produce a general-purpose data exploration tool (not domain-specific)
- Show frontend-adjacent Python skills (layout, components, interactivity)


### 15.3 Functional Requirements

- **FR-01:** The user shall be able to upload any CSV file via a drag-and-drop component
- **FR-02:** Tab 1 — Overview: display row count, column count, dtypes, null counts, and a sample table
- **FR-03:** Tab 2 — Distribution: select any column and view histogram or box plot
- **FR-04:** Tab 3 — Correlation: generate a Pearson correlation heatmap for numeric columns
- **FR-05:** Tab 4 — Scatter: select X axis, Y axis, and optional colour-by column for a scatter plot
- **FR-06:** All charts shall update reactively via Dash callbacks when filters or selections change


### 15.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Framework | Dash (by Plotly) | Free |
| Charts | Plotly Express | Free |
| Data | User-uploaded CSV (any) | Free |
| Deployment | Render.com free tier | Free |
| Testing | Dash testing utilities + pytest | Free |

### 15.5 Artefacts

> **[ARTEFACT 11-A] Callback Graph Diagram**
> *Should include: Visual representation of Dash Input/Output/State relationships between components. Tool: Manually drawn or auto-generated via `dash.get_app().server`. Located at `docs/callback_graph.png`.*

> **[ARTEFACT 11-B] App Screenshot (all 4 tabs)**
> *Should include: One screenshot per tab showing the app with a sample dataset loaded. Embed in README.*

### 15.6 GitHub Repository Structure

```
dash-data-explorer/
├── README.md                  # Live link, feature list, screenshots
├── .gitignore
├── requirements.txt           # dash, plotly, pandas, gunicorn
├── app.py                     # App entry point and layout
├── src/
│   ├── layout.py              # Component layout definitions
│   ├── callbacks.py           # All Dash callback functions
│   └── utils.py               # Data parsing and validation helpers
├── assets/
│   └── style.css              # Custom CSS overrides
├── tests/
│   └── test_callbacks.py
└── docs/
    └── callback_graph.png     # [ARTEFACT 11-A]
```


### 15.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | App Skeleton | Layout structure; tab navigation working |
| M2 | CSV Upload | File upload component; parse to DataFrame |
| M3 | Tab 1 — Overview | Data profile display |
| M4 | Tabs 2 \& 3 | Distribution and correlation charts with callbacks |
| M5 | Tab 4 | Scatter plot with axis selectors |
| M6 | Deployment | Configure Gunicorn; deploy to Render free tier |
| M7 | Polish | Error handling for malformed CSVs; loading states |


***

## 16. Project 12 — Geographic Choropleth Map Viewer

### 16.1 Overview

A geographic data visualisation project producing interactive and static choropleth maps of UK local authority statistics using Folium and Plotly. This project demonstrates geospatial data handling (GeoJSON, shapefiles), geographic joins, and the creation of publication-quality map outputs.

### 16.2 Business Objectives

- Demonstrate geospatial data skills (GeoJSON merging, coordinate systems)
- Produce immediately impressive visuals that communicate data at a glance
- Show ability to export to self-contained HTML (shareable without a server)


### 16.3 Functional Requirements

- **FR-01:** The system shall produce at least 3 choropleth maps of different UK metrics (e.g., deprivation index, median income, unemployment rate) using Local Authority boundary GeoJSON
- **FR-02:** Folium maps shall be interactive (hover tooltips, zoom, click-to-highlight)
- **FR-03:** Each map shall export as a self-contained `.html` file
- **FR-04:** A Plotly Express choropleth shall also be produced for comparison
- **FR-05:** A reusable `ChoroplethBuilder` class shall accept a GeoJSON path, a metric DataFrame, and a join key, returning a rendered Folium map


### 16.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Maps | Folium, Plotly Express | Free |
| Geospatial | GeoPandas | Free |
| GeoJSON | ONS Open Geography Portal (free) | Free |
| Data | data.gov.uk or ONS (free) | Free |

### 16.5 Artefacts

> **[ARTEFACT 12-A] GeoJSON Source Reference**
> *Should include: URL to ONS boundary files used, the coordinate reference system (CRS), and the join key field name. Format: Markdown in `data/README.md`.*

> **[ARTEFACT 12-B] Sample Map HTML Exports**
> *Should include: At least 2 exported `.html` map files committed to `outputs/maps/`. Add a note in README that users can download and open locally.*

> **[ARTEFACT 12-C] Class API Documentation**
> *Should include: Docstring-based documentation for `ChoroplethBuilder` showing constructor parameters, method signatures, and example usage. Auto-generate with `pdoc` (free).*

### 16.6 GitHub Repository Structure

```
uk-choropleth-maps/
├── README.md                  # Map previews (screenshots), usage examples
├── .gitignore
├── requirements.txt           # folium, geopandas, plotly, pandas
├── notebooks/
│   └── map_exploration.ipynb
├── src/
│   └── choropleth_builder.py  # ChoroplethBuilder class
├── data/
│   ├── geojson/               # UK boundary files
│   └── README.md              # [ARTEFACT 12-A]
├── outputs/
│   └── maps/                  # [ARTEFACT 12-B] HTML exports
└── tests/
    └── test_builder.py
```


### 16.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | GeoJSON Acquisition | Download ONS boundary files; verify CRS |
| M2 | Data Joining | Merge metric data with GeoJSON on Local Authority code |
| M3 | First Map | Produce one Folium choropleth; verify tooltips and zoom |
| M4 | Remaining Maps | Produce 2 additional maps with different metrics |
| M5 | Plotly Equivalent | Produce Plotly Express version of one map |
| M6 | ChoroplethBuilder | Refactor into reusable class; write tests |
| M7 | Exports \& README | Export HTML files; embed screenshots in README |


***

## 17. Project 13 — CLI File Intelligence Tool

### 17.1 Overview

A command-line tool built with Typer and Rich that analyses a directory of files and produces a structured report: file type distribution, total sizes, newest/oldest files, duplicate detection, and optional CSV export. This project demonstrates clean CLI design, real software engineering discipline (tests, packaging, CI), and practical utility.

### 17.2 Business Objectives

- Demonstrate production-quality CLI tool design using modern Python tooling
- Show testing discipline with `pytest` and CI via GitHub Actions
- Produce a tool that is genuinely useful, not a toy demo


### 17.3 Functional Requirements

- **FR-01:** `scandir <path>` — recursively scan a directory and report: total files, file type distribution (by extension), total size, largest 5 files, oldest and newest files
- **FR-02:** `duplicates <path>` — detect duplicate files by MD5 hash; display grouped duplicates with sizes
- **FR-03:** `export <path> --output report.csv` — export the directory scan to a CSV file
- **FR-04:** All output shall be formatted using Rich (tables, progress bars, coloured text)
- **FR-05:** `--help` shall produce clear, formatted documentation for every command
- **FR-06:** The tool shall handle permission errors and inaccessible paths gracefully without crashing


### 17.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| CLI Framework | Typer | Free |
| Terminal UI | Rich | Free |
| Hashing | `hashlib` (stdlib) | Free |
| Testing | pytest | Free |
| CI | GitHub Actions | Free |
| Packaging | `pyproject.toml` + pip | Free |

### 17.5 Artefacts

> **[ARTEFACT 13-A] CLI Help Output Screenshot**
> *Should include: Screenshot of `python -m fileintel --help` and each subcommand's `--help` output, demonstrating clean command documentation. Embed in README.*

> **[ARTEFACT 13-B] GitHub Actions CI Badge**
> *Should include: A GitHub Actions badge in the README header showing the test suite passing status.*

> **[ARTEFACT 13-C] Example Report Output Screenshot**
> *Should include: Screenshot of Rich-formatted terminal output when `scandir` is run on a sample directory, showing the table layout and colours.*

### 17.6 GitHub Repository Structure

```
fileintel-cli/
├── README.md                  # CI badge, install instructions, usage examples, screenshots
├── .gitignore
├── pyproject.toml             # Package metadata, dependencies
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions: lint + test on push
├── src/
│   └── fileintel/
│       ├── __init__.py
│       ├── __main__.py        # Entry point
│       ├── cli.py             # Typer app and command definitions
│       ├── scanner.py         # Directory scanning logic
│       ├── duplicates.py      # MD5-based duplicate detection
│       └── exporter.py        # CSV export logic
└── tests/
    ├── conftest.py            # Temp directory fixtures
    ├── test_scanner.py
    ├── test_duplicates.py
    └── test_exporter.py
```


### 17.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | Project Setup | `pyproject.toml`, virtual environment, `__main__.py` entry point |
| M2 | Scanner Module | Recursive directory walk; file metadata extraction |
| M3 | CLI — scandir | Typer command with Rich table output |
| M4 | Duplicates Module | MD5 hashing; grouping logic |
| M5 | CLI — duplicates | Typer command; Rich grouped display |
| M6 | Export | CSV export via `csv` stdlib |
| M7 | Testing | Full test suite with temp directory fixtures |
| M8 | CI Pipeline | GitHub Actions workflow running lint + tests on every push |
| M9 | Documentation | README with screenshots and install instructions |


***

## 18. Project 14 — GitHub Actions Data Pipeline

### 18.1 Overview

A repository that demonstrates GitHub Actions as an automation and data engineering tool. The pipeline fetches data from a free public API daily, processes it, generates a summary report (Markdown + chart), and commits the results back to the repository — creating a live, auto-updating data feed visible on GitHub.

### 18.2 Business Objectives

- Demonstrate CI/CD and DevOps awareness using GitHub Actions
- Show scheduled automation, environment secret handling, and file-commit workflows
- Produce a repo whose README updates automatically — a visually compelling portfolio signal


### 18.3 Functional Requirements

- **FR-01:** A GitHub Actions workflow shall run on a schedule (daily via `cron`) and on manual trigger
- **FR-02:** The pipeline shall fetch data from a free API (e.g., Open-Meteo weather API, UK Met Office open data, or a financial market open API)
- **FR-03:** The pipeline shall process the fetched data and append it to a running `data/history.csv`
- **FR-04:** The pipeline shall generate an updated chart (`outputs/latest_chart.png`)
- **FR-05:** The pipeline shall commit and push the updated files back to the repository
- **FR-06:** The README shall display the latest chart as an embedded image, appearing to auto-update
- **FR-07:** All secrets (if any API keys are needed) shall be stored as GitHub Actions secrets


### 18.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Automation | GitHub Actions | Free (public repos) |
| API | Open-Meteo (no key required) | Free |
| Data Processing | Pandas | Free |
| Charting | Matplotlib | Free |
| Git Ops | GitHub Actions `git commit` step | Free |

### 18.5 Artefacts

> **[ARTEFACT 14-A] Workflow YAML Diagram**
> *Should include: Visual representation of the GitHub Actions workflow — trigger → checkout → setup Python → install deps → fetch data → process → chart → commit → push. Tool: Mermaid flowchart in README.*

> **[ARTEFACT 14-B] Auto-Updated Chart**
> *Should include: The chart committed to the repo by the pipeline (`outputs/latest_chart.png`), embedded in the README. This is a live artefact — it updates itself.*

### 18.6 GitHub Repository Structure

```
github-actions-data-pipeline/
├── README.md                  # Embedded [ARTEFACT 14-B], workflow explanation
├── .gitignore
├── requirements.txt
├── .github/
│   └── workflows/
│       └── daily_pipeline.yml # Scheduled workflow definition
├── src/
│   ├── fetch.py               # API data fetching
│   ├── process.py             # Data cleaning and aggregation
│   └── chart.py               # Chart generation
├── data/
│   └── history.csv            # Append-only historical data (committed by pipeline)
└── outputs/
    └── latest_chart.png       # [ARTEFACT 14-B] Auto-updated by pipeline
```


### 18.7 Milestones

| \# | Milestone | Description |
| :-- | :-- | :-- |
| M1 | API Selection | Confirm free API; test data fetch locally |
| M2 | Processing Scripts | Write fetch, process, and chart scripts |
| M3 | Workflow YAML | Write `daily_pipeline.yml`; test with manual trigger |
| M4 | Git Commit Step | Configure bot commit with `GITHUB_TOKEN` |
| M5 | Scheduling | Enable `cron` trigger; verify first automated run |
| M6 | README Integration | Embed auto-updating chart in README |


***

## 19. Project 15 — Python Package: `datakit`

### 19.1 Overview

A published, installable Python package on PyPI that provides utility functions reused across this portfolio (e.g., data loading helpers, chart templates, evaluation metric calculators). This project demonstrates software delivery skills: package architecture, versioning, documentation, and publication — the hallmarks of a professional-grade engineer.

### 19.2 Business Objectives

- Demonstrate understanding of Python packaging (pyproject.toml, build tools, PyPI)
- Show reusable library design (not just scripts)
- Produce a `pip install datakit-[yourname]` command that works — a compelling CV talking point


### 19.3 Functional Requirements

- **FR-01:** The package shall expose at least 3 utility modules: `datakit.io` (data loading), `datakit.viz` (chart helpers), `datakit.metrics` (ML evaluation utilities)
- **FR-02:** All public functions shall have complete docstrings (Google or NumPy style)
- **FR-03:** The package shall be published to PyPI and installable via `pip install`
- **FR-04:** A `CHANGELOG.md` shall track version history
- **FR-05:** Documentation shall be auto-generated using `pdoc` and hosted on GitHub Pages (free)
- **FR-06:** GitHub Actions shall publish a new version to PyPI on tagged release automatically


### 19.4 Technical Stack

| Component | Tool | Cost |
| :-- | :-- | :-- |
| Packaging | `pyproject.toml` + `hatchling` | Free |
| Publication | PyPI (free account) | Free |
| Documentation | `pdoc` + GitHub Pages | Free |
| CI/CD | GitHub Actions | Free |
| Versioning | `bump-my-version` or manual | Free |

### 19.5 Artefacts

> **[ARTEFACT 15-A] PyPI Package Page**
> *Should include: A live PyPI.org package page with description
<span style="display:none">[^10][^11][^12][^13][^14][^15][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://auth0.com/blog/fastapi-best-practices/

[^2]: https://dev.to/mohammad222pr/structuring-a-fastapi-project-best-practices-53l6

[^3]: https://github.com/zhanymkanov/fastapi-best-practices

[^4]: https://dev.to/zestminds_technologies_c1/fastapi-setup-guide-for-2025-requirements-structure-deployment-1gd

[^5]: https://www.reddit.com/r/FastAPI/comments/1je4dsv/scalable_fastapi_project_structure/

[^6]: https://github.com/elayer/Steam-Elden-Ring-Reviews-Project

[^7]: https://machinelearningmastery.com/building-a-simple-mcp-server-in-python/

[^8]: https://www.linkedin.com/pulse/fastapi-project-structure-best-practices-manikandan-parasuraman-fx4pc

[^9]: https://www.geeksforgeeks.org/deep-learning/how-to-use-pytorch-for-sentiment-analysis-on-textual-data/

[^10]: https://mcpshowcase.com/blog/create-mcp-server-with-python

[^11]: https://www.youtube.com/watch?v=Af6Zr0tNNdE

[^12]: https://dev.to/gruhesh_kurra_6eb933146da/building-a-sentiment-analysis-model-with-lstms-in-pytorch-468p

[^13]: https://www.firecrawl.dev/blog/fastmcp-tutorial-building-mcp-servers-python

[^14]: https://fastlaunchapi.dev/blog/how-to-structure-fastapi

[^15]: https://docs.pytorch.org/text/main/tutorials/t5_demo.html

