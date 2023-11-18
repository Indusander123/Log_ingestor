# query_interface.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/search_logs', methods=['POST'])
def search_logs():
    filters = request.get_json()
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM logs WHERE '
    conditions = []
    for key, value in filters.items():
        conditions.append(f"{key}='{value}'")
    query += ' AND '.join(conditions)
    result = cursor.execute(query).fetchall()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
