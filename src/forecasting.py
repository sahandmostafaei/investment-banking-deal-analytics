import pandas as pd


def forecast_revenue(
    df,
    years=5,
    growth_rate=0.08,
):
    last_year = int(df["year"].max())
    last_revenue = float(
        df.loc[df["year"] == last_year, "revenue"].iloc[0]
    )

    forecasts = []

    for i in range(1, years + 1):
        year = last_year + i
        revenue = last_revenue * (
            1 + growth_rate
        ) ** i

        forecasts.append(
            {
                "year": year,
                "revenue": revenue,
            }
        )

    return pd.DataFrame(forecasts)


if __name__ == "__main__":

    financials = pd.read_csv(
        "data/company_financials.csv"
    )

    forecast = forecast_revenue(
        financials
    )

    print(forecast)
