import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# load images
with open('data.json') as fp:
    data_images = json.load(fp)

# Get Images
@app.route('/images', methods=['GET'])
def getImages():
    return jsonify(data_images)

# Filter images
@app.route('/images/<string:explanation>')
def getImage(explanation):
    imageFound = [image for image in data_images if explanation.lower() in image['explanation'].lower()]
    if len(imageFound) > 0:
        return jsonify(imageFound)
    return jsonify({'ERROR Message': 'Image not found'})

# Post Images
@app.route('/images', methods=['POST'])
def postImage():
    try:
        new_image = {
            'title': request.json['title'],
            'explanation': request.json['explanation'],
            'url': request.json['url'],
            'hdurl': request.json['hdurl']
            }
        data_images.append(new_image)
        return jsonify({'message': 'Image posted succesfully'})
    except:
        return jsonify({'ERROR': 'Image not posted'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
