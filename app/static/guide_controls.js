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
        var destinationName = el.data('destination-name');
        var url = '/path_description.json?start_id=' + startId + '&destination_id=' + destinationId;
        $('#next-location').html(destinationName);
        $.get(url, function(data) {
            var updateAndGoEl = $('#update-and-go');
            updateAndGoEl.css('visibility', 'visible');
            updateAndGoEl.data('destination-id', destinationId);
            var editorEl = $('.guide-description-editor');
            editorEl.removeAttr("readonly");
            loadedDescription = data.description;
            editorEl.html(loadedDescription);
        }).fail(function(xhr) {
            loadedDescription = null;
            var updateAndGoEl = $('#update-and-go');
            var editorEl = $('.guide-description-editor');
            editorEl.html('');
            if (xhr.status === 404) {
                updateAndGoEl.css('visibility', 'visible');
                updateAndGoEl.data('destination-id', destinationId);
                editorEl.removeAttr("readonly");
            } else {
                updateAndGoEl.css('visibility', 'false');
                updateAndGoEl.data('destination-id', '');
                editorEl.attr("readonly", "readonly");
            }
        });
    });

    $('#update-and-go').click(function(e) {
        e.preventDefault();
        var el = $(e.target);
        var newDescription = $('.guide-description-editor').val().trim().toUpperCase();
        var startId = el.data('start-id');
        var destinationId = el.data('destination-id');

        if (newDescription !== "") {
            $.ajax({
                type: "POST",
                url: '/move.json',
                contentType: 'application/json; charset=utf-8',
                dataType: "json",
                data: JSON.stringify({
                    newDescription: newDescription,
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
    });
});