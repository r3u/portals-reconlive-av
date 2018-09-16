(
~tracks = [\track1, \track2, \track3, \track4];

Fdef(\loadSoundFile, {
	| filename, action |
	("INFO: Loading file " ++ filename).postln;
	Buffer.read(s, thisProcess.nowExecutingPath.dirname +/+ filename, action: {
		|buf|
		action.value(buf);
	});
});

Fdef(\loadMacro, {
	|filename|
	~tracks.do({ arg track; p[track] = {}; }); // Clear tracks
	this.executeFile("/Users/henry/Documents/workspace/portals-reconlive-av/tests/test_world" +/+ filename);
});

s.options.numInputBusChannels = 0;
s.options.sampleRate = 48000;
s.boot;

s.waitForBoot({
	SynthDef(\sampler1, { | dur=1, out=0, amp=1.0, rate=1.0,
		startPos=0, hpf=0, release=5.0, vol=1.0, bufnum, numFrames |
		var absStart = numFrames * startPos;
		var env = Env.linen(1, dur/2.0, release);
		var osc = PlayBuf.ar(2, bufnum, startPos: absStart, rate: rate * BufRateScale.kr(bufnum));
		var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * amp * vol;
		var filtered = HPF.ar(sig, hpf);
		Out.ar(out, filtered);
	}).add;

	StageLimiter.activate;

	p = ProxySpace.new(s);
	p.quant = 1;
	p.fadeTime = 10;

	// Session paramters
	p[\typingSpeed] = 1.0;

	~tracks.do({ arg track; p[track].play; });

	OSCdef(\loadMacroHandler, {
		|msg, time, addr, recvPort|

		var macro = msg[1];

		macro.postln;
		if (macro != nil) {
			Fdef(\loadMacro).value(macro);
		};
	}, '/load_macro');
});
)

(
m = ProxyMixer(p, 8);
n.parent.alwaysOnTop_(true);
)

~tracks.do({ arg track; p[track].play; });
~tracks.do({ arg track; p[track] = {}; }); // Clear tracks

// Fdef(\loadMacro).value("hotel_basement/hotel_basement.scd")
