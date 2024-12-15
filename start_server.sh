#!/bin/bash
# Kill any process using port 8000
lsof -t -i:8000 | xargs kill -9
# Start the server
uvicorn server:app --reload
