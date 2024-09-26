#firstly install faker 
#pip install faker







from faker import Faker
import random
import csv
from datetime import datetime

fake = Faker()

# Generate synthetic data for the Location table
def generate_location_data(num_rows=100):
    locations = []
    for _ in range(num_rows):
        locations.append({
            'id': fake.unique.random_int(min=1, max=10000),
            'name': fake.company(),
            'menu': fake.word(),
            'state': fake.state()
        })
    return locations

# Generate synthetic data for the Customer table
def generate_customer_data(num_rows=100):
    customers = []
    for _ in range(num_rows):
        customers.append({
            'id': fake.unique.random_int(min=1, max=10000),
            'name': fake.name(),
            'state': fake.state()
        })
    return customers

# Generate synthetic data for the Transactions table
def generate_transaction_data(locations, customers, num_rows=100):
    transactions = []
    payment_types = ['Credit Card', 'Debit Card', 'Cash', 'Mobile Payment']
    dining_options = ['Dine In', 'Take Out', 'Delivery']

    for _ in range(num_rows):
        transactions.append({
            'id': fake.unique.random_int(min=1, max=10000),
            'menu': fake.word(),
            'paymentType': random.choice(payment_types),
            'CustomerId': random.choice(customers)['id'],
            'LocationId': random.choice(locations)['id'],
            'diningOptions': random.choice(dining_options),
            'TimeCreated': fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
        })
    return transactions

# Save the generated data to CSV files
def save_to_csv(filename, fieldnames, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Generate data
    locations_data = generate_location_data(100)
    customers_data = generate_customer_data(100)
    transactions_data = generate_transaction_data(locations_data, customers_data, 100)

    # Save data to CSV files
    save_to_csv('locations.csv', ['id', 'name', 'menu', 'state'], locations_data)
    save_to_csv('customers.csv', ['id', 'name', 'state'], customers_data)
    save_to_csv('transactions.csv', ['id', 'menu', 'paymentType', 'CustomerId', 'LocationId', 'diningOptions', 'TimeCreated'], transactions_data)

    print("Data generation complete and saved to CSV files.")
