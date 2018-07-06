from db import db
from model import MediaAsset
from magic import Magic

import pathlib
import hashlib


def save_asset(filename, data):
    mime = Magic(mime=True)
    asset = MediaAsset()
    asset.filename = pathlib.Path(filename).name
    asset.hash_sha256 = hashlib.sha256(data).hexdigest()
    asset.content = data
    asset.mime_type = mime.from_buffer(data)
    db.session.add(asset)
    db.session.commit()

