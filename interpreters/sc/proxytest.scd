(
s.options.numInputBusChannels = 0;
s.boot;

p = ProxySpace.new(s);
p.quant = 1;
p.fadeTime = 10;

p[\track1].play;
p[\track2].play;
p[\track3].play;

)

(
~sounds = Dictionary.new;
~testSoundsDir = thisProcess.nowExecutingPath.dirname +/+ "testsounds";
~wysingSoundsDir = "/Users/henry/Desktop/WYSING";

~loadsound = {
	| basedir, filename |
	var buf = Buffer.read(s, basedir +/+ filename);
	~sounds.add(filename -> buf);
};
)

(
~loadsound.value(~wysingSoundsDir, "TreeKeep/TreeKeep_Crackle_001.wav");
~loadsound.value(~wysingSoundsDir, "TreeKeep/TreeKeep_Stick_001.wav");
~loadsound.value(~wysingSoundsDir, "TreeKeep/TreeKeep_BugAndLeaf_001.wav");
~loadsound.value(~wysingSoundsDir, "TheKiln/TheKiln_Gate_001.wav");
~loadsound.value(~wysingSoundsDir, "TheKiln/TheKiln_Tools_001.wav");

~loadsound.value(~testSoundsDir, "Western.wav");
~loadsound.value(~testSoundsDir, "YourSound.wav");
)


(
//m = ProxyMixer(p, numItems: 8)

SynthDef(\sampler, { | dur=1, out=0, amp=1.0, rate=1.0,
	                   startPos=0, hpf=0, release=5.0, bufnum, numFrames |
	var absStart = numFrames * startPos;
	var env = Env.linen(1, dur/2.0, release);
	var osc = PlayBuf.ar(2, bufnum, startPos: absStart, rate: rate);
	var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * amp;
	var filtered = HPF.ar(sig, hpf);
	Out.ar(out, filtered);
}).add;
);

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
	var buf;

	if (track == nil) {
		"Missing parameter 'track'".throw;
	};
	if (filename == nil) {
		"Missing parameter 'filename'".throw;
	};
	if (p.at(track).loaded == false) {
		("Invalid track: " ++ track).throw;
	};

	buf = ~sounds[filename];
	if (buf == nil) {
		("Could not load buffer for file: " ++ filename).throw;
	};

	"LOADED BUFFER".postln;
	buf.postln;

	p[track] = Pbind(
		\instrument, \sampler,
		\freq, Prand([110, 220, 440, 880], inf),
		\dur, Prand(#[1, 2, 3, 4, 6, 8, 16]/1, inf),
		\rate, Pwrand(#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
			          #[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
			          inf),
		\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
		\bufnum, buf,
		\numFrames, buf.numFrames,
		\release, 3,
		\amp, 0.2,
		\hpf, 100
	);

}, '/playfile' );
)



(
OSCdef(\playfileHandler, { | msg, time, addr, port |
	var filename = msg[2].asString;
	~sounds[filename].postln;

}, '/playfile' );
)


