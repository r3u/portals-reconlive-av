const io = require('socket.io-client')
const osc = require('osc');
const request = require('request');
const _ = require('lodash');

const serverAddr = "192.168.1.68";
const serverProto = "http://";
const socketPort = 8080;

const udpPort = new osc.UDPPort({
    localAddress: "127.0.0.1",
    localPort: 57121,
    metadata: true
});

udpPort.open();

function locationAssets(location_id, callback) {
    const url = serverProto + serverAddr + "/media_asset?location_id=" + location_id;
    console.log(url);
    request(url, { json: true }, (err, res, body) => {
        if (err) {
            return console.log(err);
        }
        callback(body);
    });
}

socket = io.connect('http://' + serverAddr + ':' + socketPort + '/chat');

socket.on('connect', function() {
    socket.emit('joined', {});
});

socket.on('messages', function(messages) {
    new_location_id = null;
    messages.forEach(function(entry) {
        if (entry.event_type === 'navigation') {
            new_location_id = entry.destination_id;
        }
    });
    if (new_location_id !== null) {
        locationAssets(new_location_id, playfiles);
    }
});

socket.on('disconnect', function(){
});

function oscSend(msg) {
    udpPort.send(msg, "127.0.0.1", 57120);
}

function playfiles(assets) {
    var selection = _.filter(assets, a => a.mime_type.indexOf("audio/") !== -1);
    selection = _.sampleSize(selection, 10);
    selection = _.map(selection, a => {
        return {
            type: "s",
            value: a.filename
        };
    });
    console.log(selection);
    oscSend({
        address: "/navigation",
        args: selection
    });
}
