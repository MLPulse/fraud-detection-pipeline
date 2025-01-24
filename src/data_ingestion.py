# File: src/data_ingestion.py

import os
import sys
import argparse
import pandas as pd

def load_data(path, fraud_column='is_fraud'):
    """
    Load data from a CSV file or multiple CSV files in a directory. 
    Returns a pandas DataFrame.
    
    Parameters:
    -----------
    path : str
        Path to a CSV file or directory containing CSV files.
    fraud_column : str
        Name of the column that indicates fraud cases (default 'is_fraud').
    
    Returns:
    --------
    df : pandas DataFrame
    """
    if os.path.isdir(path):
        # Read all CSV files in the directory
        all_files = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith('.csv')
        ]
        if not all_files:
            raise ValueError(f"No CSV files found in directory: {path}")
        df_list = [pd.read_csv(csv_file) for csv_file in all_files]
        df = pd.concat(df_list, ignore_index=True)
    else:
        # Assume the path is a single file
        if path.lower().endswith('.csv'):
            df = pd.read_csv(path)
        elif path.lower().endswith('.parquet'):
            df = pd.read_parquet(path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Parquet.")
    return df

def print_summary(df, fraud_column='is_fraud'):
    """
    Print summary statistics about the DataFrame: row count, column count,
    and fraction of fraud if the specified fraud column exists.
    """
    row_count, col_count = df.shape
    print(f"Rows: {row_count}")
    print(f"Columns: {col_count}")
    
    if fraud_column in df.columns:
        # Compute fraction of fraudulent rows
        frac_fraud = df[fraud_column].mean()
        print(f"Fraction of fraud cases (column: '{fraud_column}'): {frac_fraud:.4f}")
    else:
        print(f"Fraud column '{fraud_column}' not found in the dataset.")

def main():
    parser = argparse.ArgumentParser(
        description="Ingest transaction data from a CSV or directory of CSVs."
    )
    parser.add_argument(
        "data_path",
        help="Path to a CSV file, Parquet file, or directory containing CSV files."
    )
    parser.add_argument(
        "--fraud_column",
        default="is_fraud",
        help="Name of the fraud indicator column. Default is 'is_fraud'."
    )
    args = parser.parse_args()

    df = load_data(args.data_path, args.fraud_column)
    print_summary(df, args.fraud_column)

if __name__ == "__main__":
    main()