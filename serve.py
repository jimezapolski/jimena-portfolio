import os, http.server, socketserver

os.chdir('/Users/jimezapolski/Documents/PORTFOLIO/.claude/worktrees/unruffled-davinci')

PORT = 3333
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
