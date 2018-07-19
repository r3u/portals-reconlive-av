/*
 * pOrtals::reconLIVE:AV
 *
 * Copyright (C) 2018  Rachael Melanson
 * Copyright (C) 2018  Henry Rodrick
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

function portalsConnect(onMessage) {
    var currentSession = null;
    var socketAddr = "192.168.50.42";
    var socketPort = 8080;

    socket = io.connect('http://' + socketAddr + ':' + socketPort + '/chat');

    socket.on('connect', function() {
        socket.emit('joined', {});
    });

    socket.on('messages', function(messages) {
        messages.forEach(function(entry) {
            onMessage(entry);
        });
    });

    socket.on('disconnect', function(){
    });
}
