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

$(function() {
    var loadedDescription = null;

    $('.navigation-link').click(function(e) {
        e.preventDefault();
        var el = $(e.target);
        var startId = el.data('start-id');
        var destinationId = el.data('destination-id');
        move(startId, destinationId);
    });

    $('.send-to-chat-link').click(function(e) {
        e.preventDefault();
        var description = $('#path-description').html();
        sendToChat(description);
        $(e.target).css('visibility', 'hidden');
    });
});

function sendToChat(message) {
    $.ajax({
        type: "POST",
        url: '/chatlog_entry.json',
        contentType: 'application/json; charset=utf-8',
        dataType: "json",
        data: JSON.stringify({
            message: message
        }),
        success: function() {
        },
        failure: function() {
        }
    });
}

function move(startId, destinationId) {
    $.ajax({
        type: "POST",
        url: '/move.json',
        contentType: 'application/json; charset=utf-8',
        dataType: "json",
        data: JSON.stringify({
            startId: startId,
            destinationId: destinationId
        }),
        success: function() {
            location.reload(true);
        },
        failure: function() {
            location.reload(true);
        }
    });
}