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
		\rate, Pwrand(
			#[0.25, 0.50, 1.00, 1.50, -0.50, -1.00, -1.50],
			#[1.00, 3.00, 3.00, 3.00,  1.00,  1.00,  1.00].normalizeSum,
			inf),
		\startPos, 0,
		\bufnum, buf,
		\numFrames, buf.numFrames,
		\release, 5,
		\hpf, 100,
		\vol, Pbrown(2, 4, 0.1)
	);
});

)