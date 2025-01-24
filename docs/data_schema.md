# Data Schema

This document describes the columns present in the `transactions.csv` dataset.

| Column Name      | Type        | Description                                                                            |
|------------------|-------------|----------------------------------------------------------------------------------------|
| `transaction_id` | string      | Unique identifier for the transaction (e.g., "tx_1").                                  |
| `user_id`        | int         | Identifier for the user who made the transaction.                                      |
| `amount`         | float       | Transaction amount, generated with a lognormal distribution to emulate real-world data. |
| `timestamp`      | datetime    | Date and time when the transaction occurred.                                           |
| `location`       | string      | City or region name where the transaction originated.                                  |
| `is_fraud`       | int (0 or 1)| Binary label indicating if the transaction was fraudulent (`1`) or legitimate (`0`).  |

## Fraud Rate
By default, the script generates a dataset where approximately 3% of transactions are labeled as fraudulent.
