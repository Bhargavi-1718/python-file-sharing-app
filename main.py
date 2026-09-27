import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

PORT = 8010

# Project folder
project_folder = os.path.dirname(os.path.abspath(__file__))

# Folder that will be shared
share_folder = os.path.join(project_folder, "shared_files")
os.makedirs(share_folder, exist_ok=True)

# Serve only the shared_files folder
os.chdir(share_folder)

# Handler for browser requests
Handler = http.server.SimpleHTTPRequestHandler

# Find local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

IP = "http://" + s.getsockname()[0] + ":" + str(PORT)

# Generate QR code
qr_path = "myqr.png"
url = pyqrcode.create(IP)
url.png(qr_path, scale=8)

# Open QR code
webbrowser.open(qr_path)

# Start HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your Browser:", IP)
    print("Scan the QR code to access the files")
    print("Press Ctrl+C to stop the server")

    httpd.serve_forever()