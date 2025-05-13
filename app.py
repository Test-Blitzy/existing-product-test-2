#!/usr/bin/env python3

"""
Simple HTTP server implementation using Flask.

This is a direct replacement for the original Node.js implementation,
maintaining identical functionality and behavior while leveraging Python and Flask.
"""

from flask import Flask

# Initialize Flask application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """
    Route handler for the root endpoint.
    Returns 'Hello, World!' with appropriate headers and status code.
    
    Returns:
        tuple: Response body, status code, and headers dictionary
    """
    return "Hello, World!\n", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    # Server configuration - matches original Node.js implementation
    host = '127.0.0.1'
    port = 3000
    
    # Log server startup information - matches format of Node.js implementation
    print(f"Server running at http://{host}:{port}/")
    
    # Start the Flask development server
    app.run(host=host, port=port)