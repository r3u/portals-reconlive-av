#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import ChatlogEntry, Location
from services.asset_metadata_service import AssetMetadataDef


def rest_chat_msg(ent: ChatlogEntry):
    return {
        "event_type": "message",
        "session_id": ent.session_id,
        "id": ent.id,
        "message": ent.message,
        "actor": ent.actor.name
    }


def rest_navigation_msg(start_id: int, destination_id: int, session_id: int):
    return {
        "event_type": "navigation",
        "session_id": session_id,
        "start_id": start_id,
        "destination_id": destination_id
    }


def rest_location_msg(loc: Location):
    return {
        "id": loc.id,
        "name": loc.name
    }


def rest_asset_metadata_msg(metadata: AssetMetadataDef):
    return {
        "type": metadata.type,
        "asset": metadata.asset_filename,
        "locations": list(metadata.locations),
        "tags": list(metadata.tags)
    }
