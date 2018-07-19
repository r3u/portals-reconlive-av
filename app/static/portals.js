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

function setConnectionStatus(status) {
    var el = $('#connection-status');
    el.removeClass('disconnected').removeClass('connected')
    if (status === 'connected') {
        el.addClass('connected');
    } else if (status == 'disconnected') {
        el.addClass('disconnected');
    }
    el.html(status);
}

function clearChat() {
    $('#chat-messages').val("");
}

function appendToChat(message) {
    if($('#chat-messages').val()) {
        message = "\n" + message;
    }
    $('#chat-messages').val($('#chat-messages').val() + message);
    $('#chat-messages').scrollTop($('#chat-messages')[0].scrollHeight);
}

function chatFormat(actor, message) {
    return actor + "> " + message;
}

$(function() {
    var currentSession = null;
    var socket_port = 8080;
    socket = io.connect('http://' + document.domain + ':' + socket_port + '/chat');
    setConnectionStatus("connecting");

    socket.on('connect', function() {
        $('#chat-messages').val('');
        setConnectionStatus("connected");
        socket.emit('joined', {});
    });

    socket.on('messages', function(messages) {
        messages.forEach(function(entry) {
            if (entry.event_type !== 'message') {
                return;
            }
            if (currentSession === null) {
                currentSession = entry.session_id;
            } else if (currentSession !== entry.session_id) {
                location.reload(true);
                return;
            }
            appendToChat(chatFormat(entry.actor, entry.message))
        });
    });

    socket.on('disconnect', function(){
        setConnectionStatus("disconnected");
    });

    $('#chat-input').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code === 13) {
            text = $('#chat-input').val().trim();
            $('#chat-input').val('');
            if (text !== '') {
                socket.emit('text', {message: text});
            }
        }
    });
});
