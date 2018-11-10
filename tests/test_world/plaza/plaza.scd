(

Fdef(\loadSoundFile).value("clap.wav", {
	|buf|

	p[\track1] = Pbind(
		\instrument, \sampler1,
		\dur, Prand([
			Prand(#[1, 2, 3, 4, 6, 8]/2, 8),
			Prand(#[1, 2, 3, 4, 6, 8]/4, 16),
			Prand(#[1, 2, 3, 4, 6, 8]/16, 16)
		], inf),
		\rate, 1/16,
		\startPos, 0,
		\bufnum, buf,
		\numFrames, buf.numFrames,
		\release, 5,
		\hpf, 100,
		\vol, Pbrown(2, 4, 0.1)
	);
});

)