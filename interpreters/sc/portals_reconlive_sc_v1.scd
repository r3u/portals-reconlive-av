(
~soundsDir = "/Users/henry/Dropbox/reconlive/worlds/wysing";
~sounds = Dictionary.new;
~tracks = [\track1, \track2, \track3];

s.options.numInputBusChannels = 0;
s.options.sampleRate = 48000;
s.boot;
s.waitForBoot({
	var sounds, playFile, loadSound;

	"INFO: pOrtals init started".postln;

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
	p.fadeTime = 5;

	~tracks.do({ arg track; p[track].play; });

	"INFO: Tracks initialized".postln;

	SynthDef(\sampler, { | dur=1, out=0, amp=1.0, rate=1.0,
		startPos=0, hpf=0, release=5.0, bufnum, numFrames |
		var absStart = numFrames * startPos;
		var env = Env.linen(1, dur/2.0, release);
		var osc = PlayBuf.ar(2, bufnum, startPos: absStart, rate: rate * BufRateScale.kr(bufnum));
		var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * amp;
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
		|track, filename|
		var buf, action;

		action = { |bufnum|
			("INFO: Track /" ++ track ++ " playing file: " ++ filename).postln;
			buf.postln;

			p[track] = Pbind(
				\instrument, \sampler,
				\dur, Prand(#[1, 2, 3, 4, 6, 8]/8, inf),
				\rate, Pwrand(
					#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
					#[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
					inf),
				\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
				\bufnum, bufnum,
				\numFrames, bufnum.numFrames,
				\release, 5,
				\hpf, 100
			);
		};

		buf = ~sounds[filename];
		if (buf == nil) {
			Fdef(\loadSound).value(~soundsDir, filename, action);
		} {
			action.value(buf);
		};
	});

	Fdef(\stopAll, {
		~tracks.do({ arg track; p[track] = {}; });
	});

	OSCdef(\oscNavigationHandler, { | msg, time, addr, port |
		var filename1 = msg[1].asString;
		filename1.postln;
		if (filename1 != nil) {
			Fdef(\playFile).value(\track1, filename1);
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

~filename1 = "TheKiln_Tools_001.wav";
~filename2 = "TheKiln_Gate_001.wav";
~filename3 = "TheKiln_Pad_001.wav";

~metaDict[~filename1] = Fdef(\loadMetadata).value(~filename1);
~metaDict[~filename2] = Fdef(\loadMetadata).value(~filename2);
~metaDict[~filename3] = Fdef(\loadMetadata).value(~filename3);

Fdef(\assignFilesToTracks, {
	|metaDict|
	var droneOrMelody, fieldOrNoise;
	var selectedKeys = [];

	droneOrMelody = metaDict.select({ arg m, f;
		((selectedKeys.select({ arg k; k == f; }).size == 0) &&
			(m["categories"].select({ arg cat; (cat == "drone") || (cat == "melody"); }).size > 0));
	}).keys.choose;
	selectedKeys = selectedKeys.add(droneOrMelody);

	fieldOrNoise = metaDict.select({ arg m, f;
		((selectedKeys.select({ arg k; k == f; }).size == 0) &&
			(m["categories"].select({ arg cat; (cat == "field") || (cat == "noise"); }).size > 0));
	}).keys.choose;
	selectedKeys = selectedKeys.add(fieldOrNoise);

	~tracks.do({ arg track, index;
		var filename = selectedKeys[index];
		if (filename != nil) {
			Fdef(\playFile).value(track, filename);
		};
	});

	nil;
});
)

Fdef(\assignFilesToTracks).value(~metaDict);


// TODO: Implement test navigate
Fdef(\navigate).value("TheKiln")

Fdef(\stopAll).value;

~tracks.do({ arg track; p[track].play; });



