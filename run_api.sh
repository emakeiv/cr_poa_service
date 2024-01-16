#!/bin/bash

# this entry start the application using uvicorn server
uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload