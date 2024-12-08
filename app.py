import os
import pandas as pd
from flask import Flask, render_template, send_file, request, jsonify
from reconciliation import load_data, exact_match, partial_match, find_unmatched, reconcile_data
from data_gen import generate_data_with_overlap

app = Flask(__name__)

# Directory to store data files
file_loc = 'data/'

# Route to render the home page with project name and Generate Data button
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate data and present it to the user in an iframe
@app.route('/generate_data', methods=['POST'])
def generate_data():
    # Generate the data using your existing function
    df1, df2 = generate_data_with_overlap()

    # Save generated data to CSV files
    df1.to_csv(os.path.join(file_loc, 'data1.csv'), index=False)
    df2.to_csv(os.path.join(file_loc, 'data2.csv'), index=False)

    # Convert DataFrames to HTML (to be rendered in iframe)
    df1_html = df1.to_html(classes='data', index=False)
    df2_html = df2.to_html(classes='data', index=False)

    return render_template('index.html', df1_html=df1_html, df2_html=df2_html)

@app.route('/start_analysis', methods=['POST'])
def start_analysis():
    # Load the data
    df1, df2 = load_data()

    # Perform reconciliation
    reconciliation_report = reconcile_data()

    # Extract necessary results to display
    exact_matches = reconciliation_report["Exact Matches"]
    partial_matches = reconciliation_report["Partial Matches"]
    unmatched_df1 = reconciliation_report["Unmatched in DF1"]
    unmatched_df2 = reconciliation_report["Unmatched in DF2"]

    # Debug: Print the reconciliation results to see if data is being passed correctly
    print("Exact Matches:", exact_matches.shape)
    print("Partial Matches:", partial_matches.shape)
    print("Unmatched in DF1:", unmatched_df1.shape)
    print("Unmatched in DF2:", unmatched_df2.shape)

    # Render results in the results page
    return render_template('analysis.html', exact_matches=exact_matches, 
                           unmatched_df1=unmatched_df1, 
                           unmatched_df2=unmatched_df2)

if __name__ == "__main__":
    app.run(debug=True)
