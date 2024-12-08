import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def load_data(data1='data/data1.csv', data2='data/data2.csv'):
    df1 = pd.read_csv(data1)
    df2 = pd.read_csv(data2)
    return df1, df2

def exact_match(df1, df2):
    merged_df =pd.merge(df1, df2, on='TransactionID', how='outer', suffixes=['_df1', '_df2'])
    merged_df['Exact Match'] = (merged_df['Amount_df1'] == merged_df['Amount_df2']) & (merged_df['Date_df1'] == merged_df['Date_df2'])

    return merged_df[merged_df['Exact Match'] == True][['TransactionID', 'Amount_df1', 'Date_df1', 'Amount_df2', 'Date_df2']]

def partial_match(df1, df2, amount_tolerance=0.05, date_tolerance=2):
    merged = pd.merge(df1, df2, on="TransactionID", how="outer", suffixes=("_df1", "_df2"))

    merged["Amount Match"] = merged.apply(lambda row: abs(row["Amount_df1"] - row["Amount_df2"]) <= amount_tolerance * row["Amount_df1"], axis=1)

    merged["Date Match"] = merged.apply(lambda row: abs((pd.to_datetime(row["Date_df1"]) - pd.to_datetime(row["Date_df2"])).days) <= date_tolerance, axis=1)

    merged["Partial Match"] = merged["Amount Match"] & merged["Date Match"]
    # return merged[merged["Partial Match"] == True]
    return merged

def find_unmatched(df1, df2):
    unmatched_df1 = df1[~df1["TransactionID"].isin(df2["TransactionID"])]
    unmatched_df2 = df2[~df2["TransactionID"].isin(df1["TransactionID"])]
    return unmatched_df1, unmatched_df2

def reconcile_data():
    df1, df2 = load_data()
    exact_matches = exact_match(df1, df2)
    partial_matches = partial_match(df1, df2)
    unmatched_df1, unmatched_df2 = find_unmatched(df1, df2)
    
    # Generate reconciliation report
    report = {
        "Exact Matches": exact_matches,
        "Partial Matches": partial_matches,
        "Unmatched in DF1": unmatched_df1,
        "Unmatched in DF2": unmatched_df2
    }
    
    return report

def plot_amount_vs_date(df1, df2):
    merged_df = pd.merge(df1, df2, on="TransactionID", how="outer", suffixes=("_df1", "_df2"))
    
    # Plot scatter for matching amounts vs. dates
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['Amount_df1'], pd.to_datetime(merged_df['Date_df1']), color='blue', label='File 1 Matches')
    plt.scatter(merged_df['Amount_df2'], pd.to_datetime(merged_df['Date_df2']), color='red', label='File 2 Matches')

    plt.title('Amount vs Date Reconciliation')
    plt.xlabel('Amount')
    plt.ylabel('Date')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_reconciliation_pie_chart(report):
    categories = ["Exact Matches", "Partial Matches", "Unmatched in DF1", "Unmatched in DF2"]
    counts = [len(report[category]) for category in categories]

    fig = go.Figure(data=[go.Pie(labels=categories, values=counts, hole=0.3, textinfo="percent+label")])
    fig.update_layout(title="Reconciliation Breakdown")
    fig.show()

if __name__ == "__main__":
    df1, df2 = load_data()
    
    reconciliation_report = reconcile_data()
    
    plot_amount_vs_date(df1, df2)
    
    plot_reconciliation_pie_chart(reconciliation_report)
    
    print(f"Unmatched transactions in DF1:\n{reconciliation_report['Unmatched in DF1'].head()}")
    print(f"Unmatched transactions in DF2:\n{reconciliation_report['Unmatched in DF2'].head()}")