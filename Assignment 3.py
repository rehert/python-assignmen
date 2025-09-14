def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    try:
        num = int(input("Enter an integer: "))
        print(classify_number(num))
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

#Question2
def calculate_average(*args):
    """
    Calculate the average of any number of values.

    Parameters:
        *args: numbers to average

    Returns:
        float: average of the numbers
    """
    return sum(args) / len(args) if args else 0

print(calculate_average(10, 20, 30))  # Example

#Question 3
while True:
    try:
        num = int(input("Enter a number: "))
        print(f"You entered {num}")
        break
    except ValueError:
        print("Invalid input! Please try again.")

#Question 4

names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())

#Question 5

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)

#Question 6

def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Inputs must be numbers.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))

#Question 7

class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number cannot be negative.")
    return "Number is positive"

try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print("Error:", e)

#Question 8
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Numbers:", numbers)
print("Average:", sum(numbers) / len(numbers))

#Question 9

import re

text = "Contact me at test@mail.com or info@example.org. Date: 2025-09-14"
date = "2025-09-14"
string = "Hello world, welcome to the world!"

# I. Extract emails
emails = re.findall(r'\b[\w.%+-]+@[\w.-]+\.\w+\b', text)
print("Emails:", emails)

# II. Validate date
print("Valid date?" , bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date)))

# III. Replace word
print(re.sub(r'world', 'Earth', string))

print(re.split(r'\W+', string))

#Question 10
import socket

with socket.socket() as s:
    s.bind(("localhost", 12345))
    s.listen(1)
    print("Server running on port 12345...")
    conn, addr = s.accept()
    with conn:
        print("Connection from", addr)
        conn.sendall(b"Hello from server!")

import socket

with socket.socket() as s:
    s.connect(("localhost", 12345))
    msg = s.recv(1024)
    print("Received:", msg.decode())

#Question 11

import requests
import sqlite3

# Step 1: GET request from API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:  # success
    data = response.json()
    print("API Data:", data)
else:
    print("API Request Failed:", response.status_code)
    exit()

# Step 2: Connect to SQLite (create file if it doesn't exist)
conn = sqlite3.connect("api_data.db")
cur = conn.cursor()

# Step 3: Create a table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT
)
""")

# Step 4: Insert API data into the table
cur.execute("""
INSERT OR REPLACE INTO posts (id, userId, title, body)
VALUES (?, ?, ?, ?)
""", (data["id"], data["userId"], data["title"], data["body"]))

# Step 5: Commit changes
conn.commit()

# Step 6: Fetch and display stored data
cur.execute("SELECT * FROM posts")
print("Data from database:", cur.fetchall())

# Step 7: Close connection
conn.close()

