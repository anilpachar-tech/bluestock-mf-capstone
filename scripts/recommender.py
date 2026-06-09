def recommend_funds(risk_appetite):

    mapping = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"]
    }

    selected_grades = mapping.get(
        risk_appetite,
        ["Moderate"]
    )

    recommendations = (

        scheme_perf[
            scheme_perf["risk_grade"]
            .isin(selected_grades)
        ]

        .sort_values(
            by="sharpe_ratio",
            ascending=False
        )

        .head(3)

        [
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ]

    )

    return recommendations