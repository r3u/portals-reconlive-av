const io = require('socket.io-client')
const osc = require('osc');
const request = require('request');
const _ = require('lodash');

const serverAddr = "127.0.0.1";
const serverProto = "http://";
const serverPort = 8080;

const udpPort = new osc.UDPPort({
    localAddress: "127.0.0.1",
    localPort: 57121,
    metadata: true
});

udpPort.open();

socket = io.connect('http://' + serverAddr + ':' + serverPort + '/chat');

socket.on('connect', function() {
    console.log('Connected to server');
    socket.emit('joined', {});

    sendEnd(); // Let's clean up to be safe
    console.log('Getting current location');
    getCurrentLocation();
});

socket.on('messages', function(messages) {
    var navDestinationId = null;

    _.each(messages, (message) => {
        if (message.event_type === "message") {
            console.log('Received message: "' + message.message + '"');
        } else if (message.event_type === "navigation") {
            console.log('Received navigation event: destination_id=' + message.destination_id);
            navDestinationId = message.destination_id;
        }
    });

    if (navDestinationId !== null) {
        updateLocation(navDestinationId);
    }
});

socket.on('disconnect', function(){
    console.log("Disconnected from server")
});

function getCurrentLocation() {
    request.get(serverProto + serverAddr + ":" + serverPort + '/current_location.json', (err, res, body) => {
        if (err) {
            console.log("Failed to get current location: " + err);
            return
        }

        updateLocation(JSON.parse(body).id);
    });
}

function updateLocation(locationId) {
    var path = '/metadata.json?location_id=' + locationId
    request.get(serverProto + serverAddr + ":" + serverPort + path, (err, res, body) => {
        if (err || res.statusCode != 200) {
            var msg = err ? err : "Status code: " + res.statusCode
            console.log("Failed to get location metadata: " + msg);
            return
        }

        var metadataDefs = JSON.parse(body);
        var metadata = _.find(metadataDefs, (m) => m.type === 'supercollider');

        if (metadata) {
            var macro = metadata.asset;
            sendLoadMacro(macro);
        } else {
            console.log("Warning: No metadata definition with type 'supercollider' found for location " + locationId);
        }
    });
}

function oscSend(msg) {
    udpPort.send(msg, "127.0.0.1", 57120);
}

function sendLoadMacro(macroFilename) {
    console.log('Sending /load_macro event with argument "' + macroFilename + '"');
    oscSend({
        address: "/load_macro",
        args: [{type: 's', value: macroFilename}]
    });
}

function sendEnd() {
    oscSend({
        address: "/end",
        args: []
    });
}
