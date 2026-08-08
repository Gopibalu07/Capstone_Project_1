import pandas as pd


def recommend_funds(risk_appetite):

    # -----------------------------
    # 1. Load datasets
    # -----------------------------
    fund = pd.read_csv(
        "data/raw/01_fund_master.csv"
    )

    performance = pd.read_csv(
        "data/processed/clean_performance.csv"
    )

    # -----------------------------
    # 2. Clean column names
    # -----------------------------
    fund.columns = fund.columns.str.strip()
    performance.columns = performance.columns.str.strip()

    # -----------------------------
    # 3. Identify required columns
    # -----------------------------

    # Scheme name
    possible_scheme_columns = [
        "scheme_name",
        "scheme",
        "fund_name",
        "name"
    ]

    scheme_column = next(
        (
            col for col in possible_scheme_columns
            if col in fund.columns
        ),
        None
    )

    if scheme_column is None:
        raise ValueError(
            "Could not find scheme name column in fund master.\n"
            f"Available columns: {fund.columns.tolist()}"
        )

    # Risk column
    possible_risk_columns = [
        "risk_category",
        "risk_grade",
        "risk",
        "risk_level"
    ]

    risk_column = next(
        (
            col for col in possible_risk_columns
            if col in fund.columns
        ),
        None
    )

    if risk_column is None:
        raise ValueError(
            "Could not find risk column in fund master.\n"
            f"Available columns: {fund.columns.tolist()}"
        )

    # Sharpe ratio column
    possible_sharpe_columns = [
        "sharpe_ratio",
        "sharpe",
        "sharpe_90d"
    ]

    sharpe_column = next(
        (
            col for col in possible_sharpe_columns
            if col in performance.columns
        ),
        None
    )

    if sharpe_column is None:
        raise ValueError(
            "Could not find Sharpe ratio column in performance data.\n"
            f"Available columns: {performance.columns.tolist()}"
        )

    # -----------------------------
    # 4. Select only required columns
    # -----------------------------
    fund_data = fund[
        [
            "amfi_code",
            scheme_column,
            risk_column
        ]
    ].copy()

    performance_data = performance[
        [
            "amfi_code",
            sharpe_column
        ]
    ].copy()

    # -----------------------------
    # 5. Rename columns
    # -----------------------------
    fund_data = fund_data.rename(
        columns={
            scheme_column: "scheme_name",
            risk_column: "risk_grade"
        }
    )

    performance_data = performance_data.rename(
        columns={
            sharpe_column: "sharpe_ratio"
        }
    )

    # -----------------------------
    # 6. Merge fund + performance
    # -----------------------------
    data = fund_data.merge(
        performance_data,
        on="amfi_code",
        how="inner"
    )

    # -----------------------------
    # 7. Clean risk appetite input
    # -----------------------------
    risk_appetite = risk_appetite.strip().lower()

    valid_risks = [
        "low",
        "moderate",
        "high"
    ]

    if risk_appetite not in valid_risks:
        print(
            "\nInvalid risk appetite."
        )
        print(
            "Please enter: Low, Moderate, or High"
        )
        return pd.DataFrame()

    # -----------------------------
    # 8. Filter by risk
    # -----------------------------
    recommendations = data[
        data["risk_grade"]
        .astype(str)
        .str.strip()
        .str.lower()
        == risk_appetite
    ].copy()

    # -----------------------------
    # 9. Convert Sharpe to numeric
    # -----------------------------
    recommendations["sharpe_ratio"] = pd.to_numeric(
        recommendations["sharpe_ratio"],
        errors="coerce"
    )

    recommendations = recommendations.dropna(
        subset=["sharpe_ratio"]
    )

    # -----------------------------
    # 10. Sort by Sharpe Ratio
    # -----------------------------
    recommendations = recommendations.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    # -----------------------------
    # 11. Select top 3
    # -----------------------------
    recommendations = recommendations.head(3)

    # -----------------------------
    # 12. Return result
    # -----------------------------
    return recommendations[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]


# =====================================================
# Main Program
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print(" Bluestock Mutual Fund Recommendation System")
    print("=" * 50)

    risk = input(
        "\nEnter risk appetite (Low/Moderate/High): "
    )

    result = recommend_funds(risk)

    if result.empty:

        print(
            "\nNo matching funds found."
        )

    else:

        print(
            "\nTop 3 Recommended Funds:"
        )

        print("-" * 50)

        print(
            result.to_string(index=False)
        )