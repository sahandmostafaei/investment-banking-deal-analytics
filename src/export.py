import pandas as pd


def export_valuation_workbook(
    financials,
    forecast,
    comparables,
    precedents,
    sensitivity,
    output_path,
):
    with pd.ExcelWriter(
        output_path,
        engine="openpyxl",
    ) as writer:

        financials.to_excel(
            writer,
            sheet_name="Financials",
            index=False,
        )

        forecast.to_excel(
            writer,
            sheet_name="Forecast",
            index=False,
        )

        comparables.to_excel(
            writer,
            sheet_name="Comparables",
            index=False,
        )

        precedents.to_excel(
            writer,
            sheet_name="Precedents",
            index=False,
        )

        sensitivity.to_excel(
            writer,
            sheet_name="DCF Sensitivity",
        )
