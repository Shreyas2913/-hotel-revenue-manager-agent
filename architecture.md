# Hotel Revenue Manager Agent Architecture

## System Flow

Playwright Scraper

↓

ETL Pipeline

↓

Clean Reservation Dataset

↓

Neon PostgreSQL

↓

Semantic Tools Layer

* Cancellation Analysis
* ADR Analysis
* Booking Source Analysis
* Guest Country Analysis

↓

Revenue Manager Agent

* Memory
* Skill Routing
* Business Explanations

↓

OpenRouter (DeepSeek)

↓

Streamlit Dashboard

↓

Hotel Revenue Manager

---

## Agent Workflow

User Question

↓

Memory Module

↓

Skill Router

↓

OpenRouter LLM

↓

SQL Generation

↓

PostgreSQL

↓

Business Explanation

↓

Final Answer

---

## Dashboard Components

* KPI Cards
* Booking Source Analysis
* Guest Country Analysis
* AI Revenue Assistant
* Conversation Memory

---

## Technologies

* Python
* Streamlit
* PostgreSQL (Neon)
* OpenRouter
* DeepSeek
* LangChain
* DeepAgents
* SQLAlchemy
* Plotly
* Pandas
