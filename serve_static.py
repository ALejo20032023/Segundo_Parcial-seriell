"""
Sirve la carpeta del proyecto (index.html en la raíz) en http://localhost:3000
(sin dependencias; útil si aún no tienes Node.js en el PATH)
"""
import http.server
import socketserver
import os

PORT = 3000
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Abre http://localhost:{PORT} (solo archivos estáticos)")
    print("Para usar Express (Node.js): npm install && npm start")
    httpd.serve_forever()
