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
        email = f'test_email_{i}@example.com'  # Example email format
        db.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    db.commit()
    print(f'{num_contacts} test contacts added to the database.')
    db.close()

if __name__ == '__main__':
    generate_test_data(10)  # Generate 10 test contacts.

