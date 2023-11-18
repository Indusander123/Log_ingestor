# test.py

import requests

# Ingest a log
ingest_url = 'http://127.0.0.1:5000/ingest_log'
log_data = {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceID": "server-1234",
    "timestamp": "2023-09-15T08:00:00Z",
    "traceID": "abc-xyz-123",
    "spanID": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
response = requests.post(ingest_url, json=log_data)
print(response.json())

# Search logs
search_url = 'http://127.0.0.1:5000/search_logs'
filters = {"level": "error", "resourceID": "server-1234"}
response = requests.post(search_url, json=filters)
print(response.json())
