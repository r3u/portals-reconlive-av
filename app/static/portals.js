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

$(function() {
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
    setConnectionStatus("connecting");

    socket.on('connect', function() {
        setConnectionStatus("connected");
        socket.emit('joined', {});
    });
    socket.on('status', function(data) {
        $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('message', function(data) {
        $('#chat').val($('#chat').val() + data.msg + '\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('disconnect', function(){
        setConnectionStatus("disconnected");
    });
    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code === 13) {
            text = $('#text').val().trim();
            $('#text').val('');
            if (text !== '') {
                socket.emit('text', {msg: text});
            }
        }
    });
});
