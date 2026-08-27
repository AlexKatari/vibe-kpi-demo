from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).resolve().parents[1] / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> dict[str, float | int | str]:
    """Return customer count, spend, and churn rate for one city."""
    query = """
        SELECT
            COUNT(*) AS customer_count,
            COALESCE(SUM(monthly_spend), 0.0) AS total_monthly_spend,
            COALESCE(AVG(churned) * 100.0, 0.0) AS churn_rate_percent
        FROM customers_raw
        WHERE city = ?
    """

    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute(query, (city,)).fetchone()

    return {
        "city": city,
        "customer_count": row[0],
        "total_monthly_spend": round(row[1], 2),
        "churn_rate_percent": round(row[2], 2),
    }


if __name__ == "__main__":
    print(city_kpi("Mumbai"))
    print(city_kpi("Mumbai' OR 1=1 --"))