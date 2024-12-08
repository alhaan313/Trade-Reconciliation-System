import pandas as pd
import random
from faker import Faker
import os

fake = Faker()

def generate_random_data(num_count=100):
    data = []
    
    for _ in range(num_count):
        transaction_id = random.randint(1000, 9999)
        amount = round(random.uniform(100, 1000), 2)
        date = fake.date_this_decade()
        status = random.choice(["Completed", "Pending", "Failed"])
        data.append([transaction_id, amount, date, status])

    return pd.DataFrame(data, columns=["TransactionID", "Amount", "Date", "Status"])

def generate_data_with_overlap():
    df1 = generate_random_data()
    df2 = df1.copy()  # Start with the same data

    num_discrepancies = 20  # Number of records to modify in df2
    rows_to_modify = random.sample(range(df1.shape[0]), num_discrepancies)


    for idx in rows_to_modify:
            # Randomly decide which column(s) to modify for this row
            columns_to_modify = random.sample(df1.columns.tolist(), random.randint(1, len(df1.columns)))

            for col in columns_to_modify:
                if col == 'Amount':
                    # Modify Amount by introducing random error
                    df2.at[idx, 'Amount'] = round(random.uniform(100, 1000), 2)
                elif col == 'Date':
                    # Modify Date by introducing random date (within this decade)
                    df2.at[idx, 'Date'] = fake.date_this_decade()
                elif col == 'TransactionID':
                    # Modify TransactionID (random new ID)
                    df2.at[idx, 'TransactionID'] = random.randint(1000, 9999)
                elif col == 'Status':
                    # Modify Status (random status)
                    df2.at[idx, 'Status'] = random.choice(["Completed", "Pending", "Failed"])
                
                # You can add other types of errors (e.g., introducing NaN or out-of-range values)
                if random.random() < 0.1:  # 10% chance to introduce NaN error
                    df2.at[idx, col] = None

    return df1, df2

file_loc = 'data/'
if not os.path.exists(file_loc):
    os.mkdir(file_loc)

if __name__ == "__main__":

    df1, df2 = generate_data_with_overlap()
    df1.to_csv(file_loc + "data1.csv", index=False)
    df2.to_csv(file_loc + "data2.csv", index=False)