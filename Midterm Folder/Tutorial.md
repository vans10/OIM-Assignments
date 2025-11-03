# SQLAlchemy + Spotify Data Tutorial (Quick Guide)

This short tutorial explains how to explore the Spotify dataset using **SQLAlchemy** and **pandas** in Python.  
It walks through how data scientists connect databases, run SQL queries, and visualize real insights — all inside Jupyter.

## What This Project Teaches

- How to **connect Python to a database** using SQLAlchemy  
- How to **create, read, and query** tables with pandas  
- How to answer **real business questions** using SQL inside Python  
- How to **visualize results** using matplotlib  
- How to perform safe **transactions and rollbacks**

## Quick Setup

1. Install required libraries:
   ```bash
   pip install pandas sqlalchemy matplotlib
2. Place the Spotify dataset (dataset.csv or dataset.csv.zip) in the /data folder.

3. Open and run the notebook: SQLAlchemy_Simplified_Tutorial.ipynb


4. The notebook automatically:
-Creates a SQLite database
-Loads the dataset
-Runs SQL queries through pandas
-Displays analysis and charts

## Key Steps in the Notebook

| Step             | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **1️ Connect**    | Use `create_engine()` to connect to a local SQLite database |
| **2️ Load Data**  | Import the Spotify dataset and save it as a SQL table       |
| **3️ Query Data** | Run SQL queries using `pd.read_sql()`                       |
| **4️ Analyze**    | Explore top genres, artists, danceability, and popularity   |
| **5️ Visualize**  | Plot graphs for key insights                                |
| **6️ Advanced**   | Demonstrate simple JOINs and transaction rollbacks          |

## Why It Matters

SQLAlchemy bridges Python and databases —
it helps data scientists query structured data without switching tools.
By combining it with pandas and visualization, you can create a complete data workflow inside one environment.

### Run the notebook, explore, and modify the queries to test your own ideas.
