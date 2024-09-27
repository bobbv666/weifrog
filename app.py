from flask import Flask, send_file
import os, random

app = Flask(__name__)

# Directory where images are stored
IMAGE_FOLDER = 'images'

@app.route('/random-image')
def random_image():
    # List all files in the image folder
    image_files = os.listdir(IMAGE_FOLDER)
    
    # Randomly select an image from the directory
    random_image = random.choice(image_files)
    
    # Serve the selected image
    return send_file(os.path.join(IMAGE_FOLDER, random_image), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)