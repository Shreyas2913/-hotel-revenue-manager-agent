# Hotel Reservation ETL Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for hotel reservation data.

## Extract
- Reads reservation data from CSV file.
- Loads data into a Pandas DataFrame.

## Transform
- Removes duplicate records.
- Handles missing values.
- Prepares clean data for loading.

## Load
- Loads cleaned data into PostgreSQL database.

## Technologies Used
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- pgAdmin

## Project Structure

hotel-agent/
├── Data/
│ ├── raw/
│ └── processed/
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py

## Execution

```bash
python etl/main.py