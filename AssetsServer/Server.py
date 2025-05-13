from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import json
import os

class Server:
    @staticmethod
    def run():
        PORT = json.load(open("Settings.json"))["gameAssetsPort"]
        ADDR = json.load(open("Settings.json"))["gameAssetsAddress"]
        assets_dir = os.path.join(os.getcwd(), "AssetsServer/Update")

        class CustomHandler(SimpleHTTPRequestHandler):
            def translate_path(self, path):
                path = super().translate_path(path)
                relpath = os.path.relpath(path, os.getcwd())
                return os.path.join(assets_dir, relpath)

        httpd = HTTPServer(("", PORT), CustomHandler)
        print(f"[HTTPS] Assets server running on http://{ADDR}:{PORT}/")
        httpd.serve_forever()
