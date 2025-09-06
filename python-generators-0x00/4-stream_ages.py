#!/usr/bin/env/python3

from seed import connect_to_prodev

def stream_user_ages():
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:   # loop 1 (streaming)
        yield int(age)

    cursor.close()
    conn.close()

# --- Compute average using generator ---
def average_age():
    total, count = 0, 0
    for age in stream_user_ages():   # loop 2 (aggregation)
        total += age
        count += 1
    avg = total / count if count else 0
    print(f"Average age of users: {avg:.2f}")
