# Log Ingestor and Query Interface

## Overview

This project demonstrates a simple log ingestor system and a query interface implemented in Python using Flask for handling log data efficiently.

The system consists of two components:

1. **Log Ingestor**: Accepts log data in a specified format and stores it in an SQLite database.
2. **Query Interface**: Provides a Flask web server that allows users to search logs based on specific criteria.

## Prerequisites

- Python (version 3.x recommended)
- Flask
- SQLite

## Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

   Replace `<repository_url>` with the URL of the repository and `<repository_directory>` with the name of the directory you created.

2. Install dependencies:

    ```bash
    pip install Flask
    ```

3. Run the Log Ingestor:

    ```bash
    python log_ingestor.py
    ```

4. Run the Query Interface:

    ```bash
    python query_interface.py
    ```

## Usage

### Log Ingestor

The Log Ingestor exposes an endpoint for ingesting log data. Send a POST request to `http://127.0.0.1:5000/ingest_log` with log data in the request body.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"level": "error", "message": "Failed to connect to DB", "resourceID": "server-1234", "timestamp": "2023-09-15T08:00:00Z", "traceID": "abc-xyz-123", "spanID": "span-456", "commit": "5e5342f", "metadata": {"parentResourceId": "server-0987"}}' http://127.0.0.1:5000/ingest_log
```

### Query Interface

The Query Interface exposes an endpoint for searching logs based on specified filters. Send a POST request to `http://127.0.0.1:5000/search_logs` with the desired filters in the request body.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"level": "error", "resourceID": "server-1234"}' http://127.0.0.1:5000/search_logs
```

## Testing

To test the functionality, you can use the provided `test.py` script. Run:

```bash
python test.py
```
