"""
Random Forest Regression - Praktikum 11 Kelompok 04
Wahyu Anisa Efriati (2924002)

Input:
  Model_Data_Superstore_P10_Kelompok04.xlsx
  Sheet: Fact_OrderLines
  Header berada pada baris Excel ke-3.

Method:
  Target: Profit
  Model A: Sales + Discount
  Model B: Sales only
  Train: Order Date < 2026-04-03
  Test : Order Date >= 2026-04-03
  RandomForestRegressor(n_estimators=300, min_samples_leaf=2)
  Seeds: 42, 7, 21
"""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to Model_Data_Superstore_P10_Kelompok04.xlsx")
    parser.add_argument("--output", default="P11_RandomForest_Results.xlsx")
    args = parser.parse_args()

    df = pd.read_excel(args.input, sheet_name="Fact_OrderLines", header=2)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df = df.dropna(subset=["Order Date", "Sales", "Discount", "Profit"]).copy()

    cutoff = pd.Timestamp("2026-04-03")
    train = df[df["Order Date"] < cutoff]
    test = df[df["Order Date"] >= cutoff]
    if train.empty or test.empty:
        raise ValueError("Train/test kosong. Periksa tanggal pada kolom Order Date.")

    seeds = [42, 7, 21]
    rows = []
    importances = []

    baseline_pred = np.full(len(test), train["Profit"].mean())
    baseline = {
        "Model": "Baseline",
        "Features": "Rata-rata Profit train",
        "MAE": mean_absolute_error(test["Profit"], baseline_pred),
        "RMSE": mean_squared_error(test["Profit"], baseline_pred) ** 0.5,
        "R2": r2_score(test["Profit"], baseline_pred),
        "Seed": None,
    }
    rows.append(baseline)

    for seed in seeds:
        for model_name, features in [
            ("Model A", ["Sales", "Discount"]),
            ("Model B", ["Sales"]),
        ]:
            model = RandomForestRegressor(
                n_estimators=300,
                min_samples_leaf=2,
                random_state=seed,
                n_jobs=-1,
            )
            model.fit(train[features], train["Profit"])
            pred = model.predict(test[features])
            rows.append({
                "Model": model_name,
                "Features": " + ".join(features),
                "MAE": mean_absolute_error(test["Profit"], pred),
                "RMSE": mean_squared_error(test["Profit"], pred) ** 0.5,
                "R2": r2_score(test["Profit"], pred),
                "Seed": seed,
            })
            if model_name == "Model A":
                importances.append(dict(zip(features, model.feature_importances_)))

    result = pd.DataFrame(rows)
    rf_only = result[result["Model"].isin(["Model A", "Model B"])]
    summary = rf_only.groupby(["Model", "Features"])[["MAE", "RMSE", "R2"]].agg(["mean", "std"])
    importance = (pd.DataFrame(importances).mean().rename("Mean Importance")
                  .rename_axis("Feature").reset_index())
    split = pd.DataFrame([
        ["Cutoff", str(cutoff.date())],
        ["Train rows", len(train)],
        ["Test rows", len(test)],
        ["Trees", 300],
        ["min_samples_leaf", 2],
        ["Seeds", ", ".join(map(str, seeds))],
    ], columns=["Parameter", "Value"])

    with pd.ExcelWriter(args.output, engine="openpyxl") as writer:
        result.to_excel(writer, sheet_name="Metrics_By_Seed", index=False)
        summary.to_excel(writer, sheet_name="Summary")
        importance.to_excel(writer, sheet_name="Feature_Importance", index=False)
        split.to_excel(writer, sheet_name="Configuration", index=False)

    print("Train rows:", len(train))
    print("Test rows:", len(test))
    print(summary)
    print(importance)
    print("Saved:", args.output)

if __name__ == "__main__":
    main()
