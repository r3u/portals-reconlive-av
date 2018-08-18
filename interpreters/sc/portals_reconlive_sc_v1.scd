(
~soundsDir = "/Users/henry/Dropbox/reconlive/worlds/wysingtest";
~sounds = Dictionary.new;
~tracks = [\tonal1, \atonal1, \atonal2];

s.options.numInputBusChannels = 0;
s.options.sampleRate = 48000;
s.boot;
s.waitForBoot({
	var sounds, playFile, loadSound;

	"INFO: pOrtals init started".postln;

	StageLimiter.activate;

	loadSound = {
		| basedir, filename, action |
		var buf;
		("INFO: Loading file " ++ filename).postln;
		Buffer.read(s, basedir +/+ filename, action: {
			|buf|
			~sounds.add(filename -> buf);
			action.value(buf);
		});
	};

	p = ProxySpace.new(s);
	p.quant = 1;
	p.fadeTime = 8;

	~tracks.do({ arg track; p[track].play; });

	"INFO: Tracks initialized".postln;

	SynthDef(\sampler, { | dur=1, out=0, amp=1.0, rate=1.0,
		startPos=0, hpf=0, release=5.0, vol=1.0, bufnum, numFrames |
		var absStart = numFrames * startPos;
		var env = Env.linen(1, dur/2.0, release);
		var osc = PlayBuf.ar(2, bufnum, startPos: absStart, rate: rate * BufRateScale.kr(bufnum));
		var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * amp * vol;
		var filtered = HPF.ar(sig, hpf);
		Out.ar(out, filtered);
	}).add;

	"INFO: Instruments initialized".postln;

	Fdef(\loadSound, {
		| basedir, filename, action |
		("INFO: Loading file " ++ filename).postln;
		Buffer.read(s, basedir +/+ filename, action: {
			|buf|
			~sounds.add(filename -> buf);
			action.value(buf);
		});
	});

	Fdef(\playFile, {
		|track, filename, patternCtor|
		var buf, action;

		action = { |bufnum|
			var pattern = patternCtor.value(bufnum);
			if (pattern != nil) {
				("INFO: Track \\" ++ track ++ " playing file: " ++ filename).postln;
				p[track] = pattern;
			};
		};

		buf = ~sounds[filename];
		if (buf == nil) {
			Fdef(\loadSound).value(~soundsDir, filename, action);
		} {
			action.value(buf);
		};
	});

	Fdef(\playPad, {
		|track, filename|
		var createPattern = { arg bufnum;
			Pbind(
				\instrument, \sampler,
				\dur, Prand(#[1, 2, 3, 4, 6, 8]/4, inf),
				\rate, Pwrand(
					#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
					#[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
					inf),
				\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
				\bufnum, bufnum,
				\numFrames, bufnum.numFrames,
				\release, 5,
				\hpf, 50
			);
		};
		Fdef(\playFile).value(track, filename, createPattern);
	});

	Fdef(\playField, {
		|track, filename|
		var createPattern = { arg bufnum;
			Pbind(
				\instrument, \sampler,
				\dur, Prand([
					Prand(#[1, 2, 3, 4, 6, 8]/2, 8),
					Prand(#[1, 2, 3, 4, 6, 8]/4, 16),
					Prand(#[1, 2, 3, 4, 6, 8]/16, 16)
				], inf),
				\rate, Pwrand(
					#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
					#[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
					inf),
				\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
				\bufnum, bufnum,
				\numFrames, bufnum.numFrames,
				\release, 5,
				\hpf, 300,
				\vol, Pbrown(0.5, 2, 0.1)
			);
		};
		Fdef(\playFile).value(track, filename, createPattern);
	});

	Fdef(\stopTrack, {
		|track|
		("INFO: Stopping track \\" ++ track).postln;
		p[track] = {};
	});

	Fdef(\stopAll, {
		~tracks.do({ arg track; p[track] = {}; });
	});

	OSCdef(\oscNavigationHandler, { | msg, time, addr, port |
		var filename1 = msg[1].asString;
		filename1.postln;
		if (filename1 != nil) {
			Fdef(\playFile).value(\tonal1, filename1);
		}
	}, '/navigation');

	"INFO: pOrtals init completed".postln;
});

)

(
Fdef(\loadMetadata, {
	|filename|
	var path = ~soundsDir +/+ filename;
	var metadataFile = path ++ ".yaml";

	metadataFile.parseYAMLFile;
});

~metaDict = Dictionary.new;

~metaDict["TheKiln"] = Dictionary.new;
~metaDict["TreeKeep"] = Dictionary.new;
~metaDict["DoubleSpiral"] = Dictionary.new;

~metaDict["TheKiln"]["TheKiln_Gate_001.wav"] = Fdef(\loadMetadata).value("TheKiln_Gate_001.wav");
~metaDict["TheKiln"]["TheKiln_Tools_001.wav"] = Fdef(\loadMetadata).value("TheKiln_Tools_001.wav");

~metaDict["TreeKeep"]["TreeKeep_Pad_001.wav"] = Fdef(\loadMetadata).value("TreeKeep_Pad_001.wav");
~metaDict["TreeKeep"]["TreeKeep_Crackle_001.wav"] = Fdef(\loadMetadata).value("TreeKeep_Crackle_001.wav");
~metaDict["TreeKeep"]["TreeKeep_Stick_001.wav"] = Fdef(\loadMetadata).value("TreeKeep_Stick_001.wav");

~metaDict["DoubleSpiral"]["DoubleSpiral_Slate_001.wav"] = Fdef(\loadMetadata).value("DoubleSpiral_Slate_001.wav");
~metaDict["DoubleSpiral"]["DoubleSpiral_Crackle_001.wav"] = Fdef(\loadMetadata).value("DoubleSpiral_Crackle_001.wav");

Fdef(\assignFilesToTracks, {
	|metaDict|
	var droneOrMelody, fieldOrNoise1, fieldOrNoise2;
	var selectedKeys = [];

	droneOrMelody = metaDict.select({ arg m, f;
		((selectedKeys.select({ arg k; k == f; }).size == 0) &&
			(m["categories"].select({ arg cat; (cat == "drone") || (cat == "melody"); }).size > 0));
	}).keys.choose;
	if (droneOrMelody == nil) {
		Fdef(\stopTrack).value(\tonal1);
	} {
		selectedKeys = selectedKeys.add(droneOrMelody);
		Fdef(\playPad).value(\tonal1, droneOrMelody);
	};

	fieldOrNoise1 = metaDict.select({ arg m, f;
		((selectedKeys.select({ arg k; k == f; }).size == 0) &&
			(m["categories"].select({ arg cat; (cat == "field") || (cat == "noise"); }).size > 0));
	}).keys.choose;
	if (fieldOrNoise1 == nil) {
		Fdef(\stopTrack).value(\atonal1);
	} {
		selectedKeys = selectedKeys.add(fieldOrNoise1);
		Fdef(\playField).value(\atonal1, fieldOrNoise1);
	};

	fieldOrNoise2 = metaDict.select({ arg m, f;
		((selectedKeys.select({ arg k; k == f; }).size == 0) &&
			(m["categories"].select({ arg cat; (cat == "field") || (cat == "noise"); }).size > 0));
	}).keys.choose;
	if (fieldOrNoise2 == nil) {
		Fdef(\stopTrack).value(\atonal2);
	} {
		selectedKeys = selectedKeys.add(fieldOrNoise2);
		Fdef(\playField).value(\atonal2, fieldOrNoise2);
	};

	nil;
});
)

Fdef(\assignFilesToTracks).value(~metaDict["TheKiln"]);

Fdef(\assignFilesToTracks).value(~metaDict["TreeKeep"]);

Fdef(\assignFilesToTracks).value(~metaDict["DoubleSpiral"]);


// TODO: Implement test navigate
Fdef(\navigate).value("TheKiln")

Fdef(\stopAll).value;

~tracks.do({ arg track; p[track].play; });





