(
~sounds = Dictionary.new;
~wysingSoundsDir = "/Users/henry/Desktop/WYSING";

~loadsound = {
	| basedir, filename, action |
	var buf;
	("INFO: Loading file " ++ filename).postln;
	Buffer.read(s, basedir +/+ filename, action: {
		|buf|
		~sounds.add(filename -> buf);
		action.value(buf);
	});
};

s.options.numInputBusChannels = 0;
s.options.sampleRate = 48000;
s.boot;
s.waitForBoot({
	"INFO: pOrtals init started".postln;

	p = ProxySpace.new(s);
	p.quant = 1;
	p.fadeTime = 10;

	p[\track1].play;
	p[\track2].play;
	p[\track3].play;

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

	"INFO: pOrtals init completed".postln;
});
)

(
p[\track1] = Pbind(
	\instrument, \sampler,
	\freq, Prand(#[110, 220, 440, 880], inf),
	\dur, Prand(#[1, 2, 3, 4, 6, 8, 16]/16, inf),
	\rate, Prand(#[0.25, 0.5, 1, 1.5, 2.0, -0.5, -1.0, -1.5], inf),
	\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
	\bufnum, ~sounds["Western.wav"],
	\numFrames, ~sounds["Western.wav"],
	\amp, 0.05,
	\release, 3,
	\hpf, 100
);
)

(
OSCdef(\playfileHandler, { | msg, time, addr, port |
	var track = msg[1].asSymbol;
	var filename = msg[2].asString;
	var buf, action;

	if (track == nil) {
		"Missing parameter 'track'".throw;
	};
	if (filename == nil) {
		"Missing parameter 'filename'".throw;
	};
	if (p.at(track).loaded == false) {
		("Invalid track: " ++ track).throw;
	};

	action = { |bufnum|
		("INFO: Track /" ++ track ++ " playing file: " ++ filename).postln;
		buf.postln;

		p[track] = Pbind(
			\instrument, \sampler,
			\freq, Prand([110, 220, 440, 880], inf),
			\dur, Prand(#[1, 2, 3, 4, 6, 8, 16]/4, inf),
			\rate, Pwrand(
				#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
				#[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
				inf),
			\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
			\bufnum, bufnum,
			\numFrames, bufnum.numFrames,
			\release, 5,
			\amp, 0.2,
			\hpf, 100
		);
	};

	buf = ~sounds[filename];
	if (buf == nil) {
		~loadsound.value(~wysingSoundsDir, filename, action);
	} {
		action.value(buf);
	};


}, '/playfile' );
)

(
OSCdef(\stop, { | msg, time, addr, port |
	var track = msg[1].asSymbol;

	if (track == nil) {
		"Missing parameter 'track'".throw;
	};
	if (p.at(track).loaded == false) {
		("Invalid track: " ++ track).throw;
	};

	p[track] = {};

	("INFO: Stopping track /" ++ track).postln;
}, '/stop' );
)


