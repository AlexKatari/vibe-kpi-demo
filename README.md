# Applied Analytics KPI Demo

## Run commands

```powershell
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
python -m pytest
```

## Files

- `data/raw/customers_raw.csv`: Sample customer data for the analysis.
- `data/db/analytics.db`: SQLite database created by the ETL script.
- `src/etl_load_sqlite.py`: Loads the CSV into the SQLite `customers_raw` table.
- `src/kpi_city.py`: Calculates city-level customer, spend, and churn KPIs.
- `tests/test_kpi_city.py`: Checks the KPI result and SQL injection protection.
- `requirements.txt`: Lists the two Python packages needed by the project.
- `.gitignore`: Keeps local environments, secrets, caches, and the database out of Git.
