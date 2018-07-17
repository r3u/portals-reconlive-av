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
            console.log(destinationId);
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