(
~tracks = [\track1, \track2, \track3, \track4];

~midiHooks = Dictionary.new;
~midiDebug = true;

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
	this.executeFile("/Users/henry/Dropbox/reconlive/worlds/PV3/assets" +/+ filename);
});

s.options.numInputBusChannels = 0;
s.options.sampleRate = 48000;
s.boot;

s.waitForBoot({
	var uid;

	SynthDef(\sampler1, { | dur=1, out=0, amp=1.0, rate=1.0, startPos=0, hpf=0, release=5.0, vol=1.0, bufnum, numFrames |
		var absStart = numFrames * startPos;
		var env = Env.linen(1, dur/2.0, release);
		var expAmp = max(0.0, min(1.0, (amp.exp - 1.0) / (1.0.exp - 1.0)));
		var osc = PlayBuf.ar(numChannels: 2, bufnum: bufnum, startPos: absStart, rate: rate * BufRateScale.kr(bufnum));
		var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * expAmp * vol;
		var filtered = HPF.ar(sig, hpf);
		Out.ar(out, filtered);
	}).add;

	SynthDef(\sampler1mono, { | dur=1, out=0, amp=1.0, rate=1.0, startPos=0, hpf=0, release=5.0, vol=1.0, bufnum, numFrames |
		var absStart = numFrames * startPos;
		var env = Env.linen(1, dur/2.0, release);
		var expAmp = max(0.0, min(1.0, (amp.exp - 1.0) / (1.0.exp - 1.0)));
		var osc = PlayBuf.ar(numChannels: 1, bufnum: bufnum, startPos: absStart, rate: rate * BufRateScale.kr(bufnum));
		var sig = osc * EnvGen.ar(env, doneAction: Done.freeSelf) * expAmp * vol;
		var filtered = HPF.ar(sig, hpf);
		Out.ar(out, Pan2.ar(filtered));
	}).add;

/*	MIDIClient.init;
	uid = MIDIIn.findPort("Launch Control", "Launch Control").uid;
	MIDIIn.connectAll();
	MIDIIn.control = {
		arg thisUid, chan, ctrl, value;
		var hook;

		if (~midiDebug == true) {
			("MIDI: ctrl " ++ ctrl ++ " = " ++ value).postln;
		};

		if (thisUid == uid && chan == 0) {
			hook = ~midiHooks.at(ctrl);
			if (hook != nil) {
				hook.value(value);
			};
		};
	};*/

	StageLimiter.activate;

	p = ProxySpace.new(s);

	// For performance
	p.quant = 1;
	p.fadeTime = 20;

	// Session paramters
	p[\typingSpeed] = 1.0;

	p[\distance] = 0.1;
	p[\distance].fadeTime = 4;
	p[\distance].quant = 0;

	p[\track1mix] = 1.0;
	p[\track1mix].fadeTime = 4;
	p[\track1mix].quant = 0;

	p[\track2mix] = 1.0;
	p[\track2mix].fadeTime = 4;
	p[\track2mix].quant = 0;

	p[\track3mix] = 1.0;
	p[\track3mix].fadeTime = 4;
	p[\track3mix].quant = 0;

	p[\track4mix] = 1.0;
	p[\track4mix].fadeTime = 4;
	p[\track4mix].quant = 0;

	p[\mix] = {
		var sig = (
			(p[\track1].ar(2) * p[\track1mix].kr) +
			(p[\track2].ar(2) * p[\track2mix].kr) +
			(p[\track3].ar(2) * p[\track3mix].kr) +
			(p[\track4].ar(2) * p[\track4mix].kr)
		);
		HPF.ar(FreeVerb.ar(sig, p[\distance].kr, 1.0), (50 + (p[\distance].kr * 200))) * 2;
	};

	p[\mix].play;
	//~tracks.do({ arg track; p[track].play; });

	OSCdef(\loadMacroHandler, {
		|msg, time, addr, recvPort|

		var macro = msg[1];

		macro.postln;
		if (macro != nil) {
			Fdef(\loadMacro).value(macro);
		};
	}, '/load_macro');

	OSCdef(\endHandler, {
		"End handler called".postln;
		~tracks.do({ arg track; p[track] = {}; });
	}, '/end');

	~midiHooks.put(21, {
		arg value;
		p[\distance] = value / 127.0;
	});

	~midiHooks.put(41, {
		arg value;
		var param = 1.0 - (value / 127.0);
		p[\track2mix] = param;
		p[\track3mix] = param;
	});
});
)

(
m = ProxyMixer(p, 8);
n.parent.alwaysOnTop_(true);
)


// DEBUG HELPERS

~tracks.do({ arg track; p[track].play; });



p.fadeTime = 1;

p[\distance] = 0


m = NetAddr("127.0.0.1", 57120);
m.sendMsg("/end");
m.sendMsg("/load_macro", "Base of the Tower/Base of the Tower.scd");
