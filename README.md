# Hotel Revenue Manager Agent

## Overview

Hotel Revenue Manager Agent is an AI-powered business intelligence platform designed for hotel revenue management.

The system combines:

* ETL data pipeline
* PostgreSQL database
* OpenRouter LLM
* Skill-based agent routing
* Conversation memory
* Business semantic tools
* Interactive Streamlit dashboard

The goal is to allow hotel managers to ask natural language questions and receive actionable revenue insights.

---

## Features

### ETL Pipeline

* Extract reservation data
* Transform and clean records
* Load data into PostgreSQL (Neon)

### AI Agent

* Natural language to SQL generation
* OpenRouter DeepSeek integration
* Skill routing
* Conversation memory
* Business explanations

### Revenue Analytics

* Cancellation rate analysis
* ADR analysis
* Booking source analysis
* Guest country analysis
* Reservation metrics

### Dashboard

* KPI cards
* Interactive charts
* AI assistant
* Memory tracking

---

## Architecture

User

↓

Streamlit Dashboard

↓

Memory Layer

↓

Skill Router

↓

Revenue Manager Agent

↓

OpenRouter (DeepSeek)

↓

Semantic Tool Layer

↓

PostgreSQL (Neon)

↓

Business Insights

---

## Project Structure

hotel-agent/

├── app.py

├── main.py

├── requirements.txt

├── README.md

│

├── agent/

│   ├── agent.py

│   ├── config.py

│   ├── prompts.py

│   ├── tools.py

│   ├── router.py

│   ├── skills.py

│   ├── memory.py

│   ├── semantic_tools.py

│   └── explainer.py

│

├── skills/

│   ├── cancellation_skill.md

│   ├── revenue_skill.md

│   └── market_mix_skill.md

│

├── etl/

│   ├── extract.py

│   ├── transform.py

│   └── load.py

│

└── Data/

---

## Example Questions

* What is the cancellation rate?
* What is the average ADR?
* How many cancelled reservations?
* Which booking source has the most reservations?
* Show top guest countries by reservations.
* What is the average lead time?

---

## Tech Stack

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

---

## Running the Application

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

Run terminal agent:

python main.py
