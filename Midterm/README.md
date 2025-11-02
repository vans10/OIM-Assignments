![Python](https://img.shields.io/badge/Python-3.10-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-brightgreen)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

### Overview
This project demonstrates how **data scientists** can use **SQLAlchemy** to manage, query, and analyze large datasets — using a real-world example: Spotify song analytics.

It includes:
1. A Jupyter Notebook (`SQLAlchemy_Spotify_Tutorial.ipynb`) for live teaching or self-paced learning.
2. CSV data (`dataset.csv` or `dataset.csv.zip`).
3. Tutorial
4. Slides

## Table of Contents
1. [Introduction](#introduction)
2. [Why SQLAlchemy?](#why-sqlalchemy)
3. [Project Overview](#project-overview)
4. [Key Learning Objectives](#key-learning-objectives)
5. [Quick Start](#quick-start)
6. [Code Walkthrough](#code-walkthrough)
7. [Spotify Business Questions](#spotify-business-questions)
8. [Advanced Topics](#advanced-topics)
9. [Results & Insights](#results--insights)
10. [Project Structure](#project-structure)
11. [How to Run](#how-to-run)
12. [References](#references)

## Introduction

Databases are essential for managing, querying, and analyzing structured data.  
While pandas excels at in-memory data manipulation, **SQLAlchemy** acts as a bridge, letting Python users access databases efficiently **without writing complex SQL syntax by hand**.

In this project, I'll explore how data scientists use SQLAlchemy and pandas to:
- Connect to a database
- Create, read, and update tables
- Run analytical SQL queries
- Combine SQL logic with pandas visualization

I demonstrate this workflow on a **Spotify dataset** containing thousands of tracks, artists, and popularity scores.

## Why SQLAlchemy?

SQLAlchemy is a **Python SQL toolkit** and **Object-Relational Mapper (ORM)**.  
It helps:
- **Connect** to many databases (SQLite, MySQL, PostgreSQL, etc.)
- **Run SQL commands** directly in Python
- **Store and retrieve data** seamlessly with pandas
- **Avoid repetitive SQL code** through automation

> In short: SQLAlchemy lets Python speak SQL fluently.

## Project Overview

- **Goal:** Teach how to use SQLAlchemy with pandas through simple, realistic data examples.  
- **Dataset:** Spotify songs (includes `track_name`, `artists`, `genre`, `popularity`, `danceability`, etc.)
- **Database used:** SQLite (`.db` file)
- **Key concepts demonstrated:**
  - Database connection setup
  - Table creation and insertion
  - Running queries (filtering, sorting, grouping)
  - Simple visualizations with matplotlib
  - Basic JOINs and rollback transactions
  
## Key Learning Objectives

1. Understand **how SQLAlchemy connects Python and SQL**  
2. Use `pandas.to_sql()` and `pandas.read_sql()` effectively  
3. Write simple SQL queries inside Python  
4. Clean and subset a real dataset using SQL logic  
5. Create quick visual insights directly from SQL outputs  
6. Learn safe database operations (transactions, rollbacks)

├── data/
│   ├── dataset.csv.zip           # Spotify dataset
│   ├── dataset.csv               # Extracted data
│   └── spotify.db                # Auto-generated SQLite DB
│
├── SQLAlchemy_Simplified_Tutorial.ipynb   # Main notebook
└── README.md                               # Project documentation


## How It Works
1️. Connect to the Database
Uses SQLAlchemy’s create_engine() to connect to a SQLite database (demo.db or spotify.db).

2️. Store and Query Data
Loads data into tables using pandas.to_sql().
Reads results back using pandas.read_sql().

3️. Run Business Queries
Simple SQL queries inside Python:
Top 10 most popular genres
Most consistent artists (5+ songs)
Effect of danceability on popularity
Popularity comparison between explicit/non-explicit songs
Tempo ranges associated with top-performing tracks

4️. Visualize Results
Quick bar chart using matplotlib to show top genres by popularity.

5️. Advanced Topics
JOIN example: Creates an artists_dim table and joins with top_songs to calculate artist averages.
Transactions & Rollback: Demonstrates database safety by handling duplicate inserts gracefully.

| Question                                   | Description                                          |
| ------------------------------------------ | ---------------------------------------------------- |
|  Which genres are most popular?            | Calculates average popularity by genre               |
|  Who are the most consistent artists?      | Finds artists with 5+ songs and high avg. popularity |
|  Does danceability affect popularity?      | Groups songs by danceability score                   |
|  Are explicit songs more popular?          | Compares popularity between explicit/non-explicit    |
|  What tempo ranges perform best?           | Analyzes popularity by tempo group (in BPM)          |


## Results Summary
Pop and Dance Pop are the highest-performing genres.
Artists like Dua Lipa, Ed Sheeran, and The Weeknd consistently score high.
Tracks with higher danceability (0.7–0.9) correlate with better popularity.
Explicit songs are slightly more popular overall.
The 100–120 BPM range performs best in listener engagement.

## Why SQLAlchemy?
Works across multiple database systems (SQLite, MySQL, PostgreSQL, etc.)
Enables both Core (SQL) and ORM (Object) approaches
Makes data pipelines reproducible and PEP-8 compliant
Easy to integrate with analytics libraries like pandas and matplotlib

## Author
Vanshika Gupta
MS in Business Analytics, Babson College
