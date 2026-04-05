from flask import Flask, render_template, url_for
import os

# Current directory
current_path = os.path.dirname(os.path.abspath(__file__))

# Flask setup (everything in same folder)
server = Flask(
    __name__,
    template_folder=current_path,
    static_folder=current_path
)

@server.route("/")
def home():
    # Get all images in same directory
    image_files = [
        f for f in os.listdir(current_path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]

    image_urls = [url_for('static', filename=f) for f in image_files]

    return render_template("index.html", images=image_urls)

server.run()