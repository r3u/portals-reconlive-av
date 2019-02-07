(
~assetDir = "/Users/henry/Dropbox/reconlive/worlds/PV3/assets";

~macroTracks = [\track1, \track2, \track3, \track4];

~midiHooks = Dictionary.new;
~midiDebug = true;

~bufferCache = Dictionary.new;
Fdef(\loadSoundFile, {
	| filename, action |
	var fullPath, cached;

	("INFO: Loading file " ++ filename).postln;
	fullPath = thisProcess.nowExecutingPath.dirname +/+ filename;
	cached = ~bufferCache.at(fullPath);
	if (cached != nil) {
		"Buffer cache HIT".postln;
		action.value(cached);
	} {
		"Buffer cache MISS".postln;
		Buffer.read(s, fullPath, action: {
			|buf|
			~bufferCache.add(fullPath -> buf);
			action.value(buf);
		});
	};
});

Fdef(\loadMacro, {
	|filename|
	~macroTracks.do({ arg track; p[track] = {}; }); // Clear tracks
	this.executeFile(~assetDir +/+ filename);
});

Fdef(\loadSimple, {
	|filename|
	p[\track5] = {};
	this.executeFile(~assetDir +/+ filename);
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

	p[\track5mix] = 1.0;
	p[\track5mix].fadeTime = 4;
	p[\track5mix].quant = 0;

	p[\track5].fadeTime = 0.1;

	p[\mix] = {
		var sig = (
			(p[\track1].ar(2) * p[\track1mix].kr) +
			(p[\track2].ar(2) * p[\track2mix].kr) +
			(p[\track3].ar(2) * p[\track3mix].kr) +
			(p[\track4].ar(2) * p[\track4mix].kr) +
			(p[\track5].ar(2) * p[\track5mix].kr)
		);
		HPF.ar(FreeVerb.ar(sig, p[\distance].kr, 1.0), (50 + (p[\distance].kr * 200))) * 2;
	};

	p[\mix].play;
	//~macroTracks.do({ arg track; p[track].play; });

	OSCdef(\loadMacroHandler, {
		|msg, time, addr, recvPort|

		var macro = msg[1];

		macro.postln;
		if (macro != nil) {
			Fdef(\loadMacro).value(macro);
		};
	}, '/load_macro');

	OSCdef(\loadSimpleHandler, {
		|msg, time, addr, recvPort|

		var simple = msg[1];

		simple.postln;
		if (simple != nil) {
			Fdef(\loadSimple).value(simple);
		};
	}, '/load_simple');

	OSCdef(\endHandler, {
		"End handler called".postln;
		~macroTracks.do({ arg track; p[track] = {}; });
		p[\track5] = {};
	}, '/end');

	~remixFactor = 0.0;
	Fdef(\remixFactor, {
		arg value;
		var param = max(0.0, min(1.0, 1.0 - value));
		~remixFactor = value;
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

~macroTracks.do({ arg track; p[track].play; });

p.fadeTime = 1;

p[\distance] = 0.0

m = NetAddr("127.0.0.1", 57120);
m.sendMsg("/end");

s.volume.mute;
s.volume.unmute;

Fdef(\loadMacro).value("Audio/Location Macros/Isolated Beach/Isolated Beach.scd");
Fdef(\loadSimple).value("Audio/Tagged/Thunder 1/Thunder 1.scd");

Fdef(\remixFactor).value(0.0)

~bufferCache.size


// Open GUI ctrls
(
{
	var window = Window("pOrtals SI ctrl", Rect(100, 500, 300, 100), resizable: false, scroll: false).front;
	var hLayout = HLayout();
	var vLayout = VLayout(hLayout);
	var distanceSlider = Slider().value_(p[\distance].source).action_({
		arg it;
		p[\distance] = it.value;
	});
	var remixSlider = Slider().value_(~remixFactor).action_({
		arg it;
		Fdef(\remixFactor).value(it.value);
	});
	distanceSlider.orientation = \horizontal;
	remixSlider.orientation = \horizontal;
	vLayout.add(StaticText().string_("Distance"));
	vLayout.add(distanceSlider);
	vLayout.add(StaticText().string_("Remix"));
	vLayout.add(remixSlider);
	window.layout = vLayout;
	window.front;
	window.alwaysOnTop = true;
}.value

);
)