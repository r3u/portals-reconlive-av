(

SynthDef(\test_macro_2_imp, {
	arg out=0, freq = 440, amp = 1.0, pan = 0;
	var pluck = Pluck.ar(WhiteNoise.ar(0.1), Impulse.kr(0),
		    freq.reciprocal, freq.reciprocal, 15,
            coef: 0.25);
	var env = Env.perc(0.01, 3);
	var envGen = EnvGen.ar(env, doneAction: Done.freeSelf);
	var sig = pluck * envGen * amp * 3;
	OffsetOut.ar(out, Pan2.ar(sig, pos: pan));
}).add;

SynthDef(\test_macro_2_bass, {
	arg out=0, freq = 440, amp = 1.0, pan = 0;
	var osc = SinOsc.ar(freq);
	var env = Env.perc(0.01, 4);
	var envGen = EnvGen.ar(env, doneAction: Done.freeSelf);
	var sig = osc * envGen * amp;
	OffsetOut.ar(out, Pan2.ar(sig, pos: pan));
}).add;

p[\track1] = Pbind(
	\instrument, \test_macro_2_imp,
	\dur, Pbrown(1/16, 1/2, 1/16, inf),
	\note, Pwrand([0, 2, 3, 5, 7, 12, 15], [4, 3, 3, 2, 2, 2, 1].normalizeSum, inf),
	\pan, -0.7
);

p[\track2] = Pbind(
	\instrument, \test_macro_2_imp,
	\dur, Pbrown(1/16, 1/2, 1/16, inf),
	\note, Pwrand([0, 2, 3, 5, 7, 12, 15] - 7, [4, 3, 3, 2, 2, 2, 1].normalizeSum, inf),
	\pan, 0.7
);

p[\track3] = Pbind(
	\instrument, \test_macro_2_bass,
	\dur, Pseq([8 * 4, Pbrown(1/2, 2, 1/2, inf)]),
	\note, Pseq([\rest, Prand([-24, -36] + 5, inf)]),
	\pan, 0
);

p[\track4] = {
	var carrier = 48;
	var osc = DFM1.ar(
		SinOsc.ar([carrier, carrier * 1.01], 0, 0.1),
		carrier * 2,
		SinOsc.kr(0.05).range(0.9, 1.6),
		1,
		0,
		0.0003,
		0.2
	);

	osc * 0.1;
};

)
