#!/usr/bin/env python3

from seed import connect_to_prodev
def stream_users_in_batches(batch_size):
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows 

    cursor.close()
    conn.close()

# --- Process batches: filter users over 25 ---
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):     # loop 1
        for user in batch:                                # loop 2
            if int(user["age"]) > 25:
                print(user)
