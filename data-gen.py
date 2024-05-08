import sqlite3
import os

DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def generate_test_data(num_contacts):
    """Generate test data for the contacts table."""
    db = connect_db()
    for i in range(num_contacts):
        name = f'Test Name {i}'
        phone = f'123-456-789{i}'
        address = f'Test Address {i}'  # Replace with actual test addresses
        zipcode = f'12345{i}'  # Replace with actual test zip codes
        db.execute('INSERT INTO contacts (name, phone, address, zipcode) VALUES (?, ?, ?, ?)',
                   (name, phone, address, zipcode))
    db.commit()
    print(f'{num_contacts} test contacts added to the database.')
    db.close()

if __name__ == '__main__':
    generate_test_data(10)  # Generate 10 test contacts.

