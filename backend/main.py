"""
Hockey Stream Assistant - Main Application File
This file serves as the entry point for our FastAPI application.
Created on: [today's date]
"""

from fastapi import FastAPI

# Create our FastAPI application instance
# The title will appear in the automatic API documentation
app = FastAPI(title="Hockey Stream Assistant")

# Define our first endpoint (like a door into our application)
# When someone visits the root URL ("/"), this function will run
@app.get("/")
async def root():
    """
    Test endpoint to verify our server is running correctly.
    Returns a simple status message and welcome text.
    """
    return {
        "status": "ok",
        "message": "Hockey Stream Assistant is running!",
        "environment": "development"
    }