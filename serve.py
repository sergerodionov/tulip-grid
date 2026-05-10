#!/usr/bin/env python3
"""Minimal HTTP server for local development.
Resolves the serve directory from __file__ so it never calls os.getcwd().
Port is read from the PORT environment variable (set by Claude Code preview)."""
import os, http.server, socketserver

PORT = int(os.environ.get('PORT', 8080))
DIR  = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.js': 'application/javascript'})

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f'Serving {DIR} on http://localhost:{PORT}', flush=True)
    httpd.serve_forever()
