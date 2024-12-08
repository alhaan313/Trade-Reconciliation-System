
###Project Overview
This project is a data reconciliation application built with Flask. It allows users to generate two sets of overlapping financial transaction data, compare them, and perform reconciliation to identify exact matches, partial matches, and unmatched entries between the two datasets.

The reconciliation process includes:
- **Exact Matches**: Transactions that match exactly in both datasets.
- **Partial Matches**: Transactions that match within certain tolerances (e.g., amount and date).
- **Unmatched Entries**: Transactions that appear only in one dataset.

#### Features
1. **Generate Data**: Generates random transaction data with overlap and discrepancies between two datasets.
2. **Reconciliation Analysis**: Performs reconciliation on the datasets and identifies exact, partial matches, and unmatched entries.
3. **Data Visualization**:
   - Scatter plot for amounts vs. dates.
   - Pie chart displaying the reconciliation breakdown.

#### Core Functions
- **Data Generation**: The `generate_data_with_overlap()` function creates two dataframes, `df1` and `df2`, with random discrepancies in the transaction data.
- **Exact Match**: The `exact_match()` function identifies records with exact matching values for amount and date.
- **Partial Match**: The `partial_match()` function identifies records where the amount and date are within a specified tolerance.
- **Unmatched Transactions**: The `find_unmatched()` function identifies transactions present in one dataset but not the other.
- **Reconciliation Report**: The `reconcile_data()` function produces a summary report with exact matches, partial matches, and unmatched entries.
- **Data Visualization**: Functions to plot a scatter chart and pie chart to visualize the reconciliation results.

#### Web Interface
- **Home Page**: Displays project name and provides an option to generate data.
- **Generate Data**: Allows users to generate two data files with transaction data and display them in an iframe.
- **Start Analysis**: After generating the data, users can run reconciliation analysis, and the results are displayed on a separate page, including exact matches, partial matches, and unmatched records.

#### Key Files
- **`app.py`**: The main Flask application file that handles routing, data generation, and analysis.
- **`data_gen.py`**: Contains functions to generate random financial transaction data with overlap and discrepancies.
- **`reconciliation.py`**: Contains functions to perform data reconciliation (exact match, partial match, unmatched entries).
- **`templates/index.html`**: The home page template.
- **`templates/analysis.html`**: The results page template displaying reconciliation outcomes.

#### Data Flow
1. **Data Generation**: Users generate two datasets (`data1.csv` and `data2.csv`) via the web interface.
2. **Data Reconciliation**: After generating the data, users can start the reconciliation process, which produces a detailed analysis of exact and partial matches and unmatched records.
3. **Visualization**: The system plots reconciliation results using charts to help visualize data discrepancies.

This application provides a simple and effective way to compare two datasets, identify differences, and visualize reconciliation results for financial or transaction-related data.
