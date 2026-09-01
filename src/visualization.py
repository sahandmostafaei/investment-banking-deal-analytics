import matplotlib.pyplot as plt


def plot_revenue_forecast(
    historical,
    forecast,
    output_path,
):
    plt.figure(figsize=(10, 6))

    plt.plot(
        historical["year"],
        historical["revenue"],
        marker="o",
        label="Historical Revenue",
    )

    plt.plot(
        forecast["year"],
        forecast["revenue"],
        marker="o",
        linestyle="--",
        label="Forecast Revenue",
    )

    plt.title("Revenue Forecast")
    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def plot_dcf_sensitivity(
    sensitivity,
    output_path,
):
    plt.figure(figsize=(10, 6))

    plt.imshow(
        sensitivity,
        aspect="auto",
    )

    plt.colorbar(
        label="Enterprise Value"
    )

    plt.xticks(
        range(len(sensitivity.columns)),
        [
            f"{x:.1%}"
            for x in sensitivity.columns
        ],
    )

    plt.yticks(
        range(len(sensitivity.index)),
        [
            f"{x:.1%}"
            for x in sensitivity.index
        ],
    )

    plt.xlabel("Terminal Growth Rate")
    plt.ylabel("WACC")
    plt.title("DCF Sensitivity Analysis")

    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
