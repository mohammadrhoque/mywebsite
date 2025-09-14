#!/usr/bin/env python3
"""
Simple HTTP server to test sql.js-httpvfs functionality
This server serves the database file with proper headers for range requests
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Range, Content-Type')
        
        # Add headers for sql.js-httpvfs
        if self.path.endswith('.db'):
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Type', 'application/octet-stream')
        
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSHTTPRequestHandler)
    print(f"🌐 Test server running on http://localhost:{port}")
    print("📊 Serving files with proper headers for sql.js-httpvfs")
    print("🗄️ Database file: bangladesh_map.db")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
