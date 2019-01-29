#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import ChatlogEntry, Session, Actor
from typing import Iterator, List
from db import db


def load_chat_log(session_id, limit=100) -> Iterator[ChatlogEntry]:
    results = ChatlogEntry \
        .query \
        .filter(ChatlogEntry.session_id == session_id) \
        .order_by(ChatlogEntry.id.desc()) \
        .limit(limit) \
        .all()
    return reversed(results)


def save_log_entry(session: Session, actor: Actor, message: str) -> ChatlogEntry:
    log_entry = ChatlogEntry(session_id=session.id,
                             actor_id=actor.id,
                             message=message)
    db.session.add(log_entry)
    db.session.commit()
    return log_entry


def get_log_entry(log_entry_id: int) -> ChatlogEntry:
    return ChatlogEntry.query.get(log_entry_id)


def get_log_entries(log_entry_ids: List[int]) -> List[ChatlogEntry]:
    return ChatlogEntry.query.filter(ChatlogEntry.id.in_(log_entry_ids))