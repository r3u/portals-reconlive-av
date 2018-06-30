#
# pOrtals::reconLIVE:AV
#
# Copyright (C) 2018  Rachael Melanson
# Copyright (C) 2018  Henry Rodrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from model import ChatlogEntry, Session, Actor
from typing import Iterator
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
