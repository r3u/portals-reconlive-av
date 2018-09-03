/*
 * This file is part of pOrtals:reconLIVE:AV which is released
 * under version 3 of the GNU General Public License (GPLv3).
 * See the LICENSE file in the project root for more information.
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