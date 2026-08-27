import pytest

from src.etl_load_sqlite import load_csv_to_sqlite
from src.kpi_city import city_kpi


@pytest.fixture(autouse=True)
def loaded_database() -> None:
    load_csv_to_sqlite()


def test_city_kpi_returns_mumbai_metrics() -> None:
    result = city_kpi("Mumbai")

    assert result == {
        "city": "Mumbai",
        "customer_count": 3,
        "total_monthly_spend": 3551.25,
        "churn_rate_percent": 33.33,
    }


def test_city_kpi_does_not_allow_sql_injection() -> None:
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result["customer_count"] == 0
    assert result["total_monthly_spend"] == 0.0
    assert result["churn_rate_percent"] == 0.0