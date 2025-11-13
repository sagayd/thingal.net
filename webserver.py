#from livereload import Server
#import os

#root_dir = 'housewarming'
#default_file = 'welcome.html'

#def serve_default():
#    index_path = os.path.join(root_dir, default_file)
#    with open(index_path, 'r', encoding='utf-8') as f:
#        return f.read()

#server = Server()

## Serve the custom default page at "/"
#server.app.add_url_rule('/', 'root', serve_default)

## Watch for changes
#server.watch(root_dir, delay=1)

## Serve static files from housewarming/
#server.serve(root=root_dir, port=8080, host='0.0.0.0')

from livereload import Server, shell
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

root_dir = 'docs'
default_file = 'welcome.html'

@app.route('/')
def root():
    return send_from_directory(root_dir, default_file)

# Serve all static files normally
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(root_dir, path)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch(root_dir, delay=1)
    server.serve(port=8080, host='0.0.0.0')

