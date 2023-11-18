# log_ingestor.py

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create SQLite database
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level TEXT,
        message TEXT,
        resourceID TEXT,
        timestamp TEXT,
        traceID TEXT,
        spanID TEXT,
        commit TEXT,
        parentResourceId TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/ingest_log', methods=['POST'])
def ingest_log():
    log_data = request.get_json()
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (level, message, resourceID, timestamp, traceID, spanID, commit, parentResourceId)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        log_data['level'],
        log_data['message'],
        log_data['resourceID'],
        log_data['timestamp'],
        log_data['traceID'],
        log_data['spanID'],
        log_data['commit'],
        log_data['metadata']['parentResourceId']
    ))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Log ingested successfully'})

if __name__ == '__main__':
    app.run(debug=True)
