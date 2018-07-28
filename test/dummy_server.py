from flask import Flask, jsonify, send_file, Response, request, abort
import io
import os
from pathlib import Path
from collections import namedtuple

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
Asset = namedtuple("Asset", "content, mime_type, filename")


def read_file(path):
    with Path(path).resolve().open(mode="rb") as binary_file:
        data = binary_file.read()
        return data


def create_asset(path):
    _, ext = os.path.splitext(path)
    if ext == ".jpg" or ext == ".jpeg":
        mime_type = "image/jpeg"
    elif ext == ".wav":
        mime_type = "audio/x-wav"
    elif ext == ".mp4":
        mime_type = "video/mp4"
    else:
        print("Unexpected file ext {0}".format(path))
        mime_type = None
    return Asset(read_file(path), mime_type, path)


dl_media_assets = {
    1: create_asset("spider.jpg"),
    2: create_asset("synbass.wav"),
    3: create_asset("cat.mp4")
}

ls_media_assets = {
    1: [{"filename": "Bistro - voix ponctuelle avec effets.wav",
         "id": 1,
         "mime_type": "audio/x-wav"},
        {"filename": "DAT - Porte grinc\u0327ante du "
                     "garage a\u0300 Montreuil.wav",
         "id": 2,
         "mime_type": "audio/x-wav"}],
    2: [{"filename": "Dimanche.jpg",
         "id": 1,
         "mime_type": "image/jpeg"},
        {"filename": "A toute a l'heure.jpg",
         "id": 2,
         "mime_type": "image/jpeg"},
        {"filename": "A toute a l'heure.jpg",
         "id": 3,
         "mime_type": "video/mp4"}]
}

app = Flask(__name__)


@app.route('/')
def index():
    return Response(status=200)


@app.route('/media_asset/<int:asset_id>')
def download_media_asset(asset_id):
    asset = dl_media_assets.get(int(asset_id), None)
    if not asset:
        return abort(404)
    return send_file(
        io.BytesIO(asset.content),
        mimetype=asset.mime_type,
        as_attachment=True,
        attachment_filename=asset.filename)


@app.route('/media_asset')
def list_media_asset():
    location_id = request.args.get('location_id')

    if location_id:
        assets = ls_media_assets[int(location_id)]
    else:
        assets = ls_media_assets
    return jsonify(assets)


if __name__ == '__main__':
    app.debug = True
    app.run(HOST_NAME, PORT_NUMBER)
