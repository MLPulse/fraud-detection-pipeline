#!/usr/bin/env python3

"""
generate_synthetic_data.py
Generates a synthetic transactions dataset for fraud detection tasks.
Outputs the dataset to data/transactions.csv
"""

import os
import numpy as np
import pandas as pd
from faker import Faker

def generate_synthetic_transactions(
    n_transactions=10000,
    fraud_rate=0.03,
    output_path="data/transactions.csv"
):
    """
    Generates a synthetic transaction dataset and saves it to CSV.
    
    Parameters:
    -----------
    n_transactions : int
        Number of transaction records to generate.
    fraud_rate : float
        Fraction of fraudulent transactions (0 < fraud_rate < 1).
    output_path : str
        File path where to save the resulting CSV.
    """
    fake = Faker()
    
    # For reproducibility (optional)
    Faker.seed(42)
    np.random.seed(42)
    
    # Generate transaction IDs
    transaction_ids = [f"tx_{i+1}" for i in range(n_transactions)]
    
    # Generate user IDs
    user_ids = np.random.randint(1, 1001, size=n_transactions)
    
    # Generate amounts
    amounts = np.random.lognormal(mean=3.0, sigma=1.0, size=n_transactions)
    
    # Generate timestamps
    timestamps = [
        fake.date_time_between(start_date='-365d', end_date='now')
        for _ in range(n_transactions)
    ]
    
    # Generate random locations
    locations = [fake.city() for _ in range(n_transactions)]
    
    # Generate is_fraud
    is_fraud_array = np.random.choice([0, 1],
                                      size=n_transactions,
                                      p=[1 - fraud_rate, fraud_rate])
    
    # Build the dataframe
    df = pd.DataFrame({
        "transaction_id": transaction_ids,
        "user_id": user_ids,
        "amount": amounts,
        "timestamp": timestamps,
        "location": locations,
        "is_fraud": is_fraud_array
    })
    
    # Shuffle rows
    df = df.sample(frac=1).reset_index(drop=True)

    # Create data folder if not exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    
    print(f"Generated synthetic dataset with {n_transactions} transactions.")
    print(f"File saved at: {output_path}")

if __name__ == "__main__":
    generate_synthetic_transactions()