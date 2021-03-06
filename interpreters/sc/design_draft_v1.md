# pOrtals::reconLIVE::AV

*Sonic Interpreter* (design draft 1)

*2018-08-16*

## Intro

The *Sonic Interpreter* (SI) is the subsystem responsible for all real-time audio aspects of the pOrtals::reconLIVE::AV performance system. Implementation-wise, the SuperCollider programming language is used for the implementation of the Sonic Interpreter, but we avoid using the term *SuperCollider Interpreter* since it has a different meaning (the SuperCollider Interpreter is the program, part of the SuperCollider software package, that reads and executes SuperCollider source code).

The Sonic Interpreter relies heavily on interactive programming techniques provided by the [JITLib](http://doc.sccode.org/Overviews/JITLib.html) class library.

A good practical introduction to the most commonly used JITLib classes can be found [here](https://theseanco.github.io/howto_co34pt_liveCode/).

## Requirements

This section aims to summarise the most important functional requirements of SI in order to motivate the following design decisions.

- **Sonic environments** - As sessions progress, guides and scouts will typically move around in the world and interact with various entities (i.e WorldObjects). SI should support the implementation of different sonic environments (locations) in a generative and extensible way, and be able to sonically respond to events such as interactions with WorldObjects.

- **Network communication** - reconLIVE is a network based (typically LAN) performance system, and SI must be able to receive updates, e.g location changes, from the "master server" (the server where chat sessions and updates of the "world state" are coordinated).

- **Transitions** - SI should have a way to transition between different sonic environments smoothly, for example using crossfades.

- **Session/World parameters** - There should be a way to define global parameters that aren't specific to a location or WorldObject, e.g _**typing speed**_ (average words or characters per second in the current session chat), _**zoom level**_ (possibly a parameter directly controlled by the guide from the UI using a slider), etc. Concrete examples of how this is useful:
   - Typing speed could affect density of a granular synth, the tempo of a rhythmic pattern, etc.
   - Zoom level could affect the placement of certain sounds in the 3d sound field (i.e spatialisation).

## Basic design

### portals_boot.scd
The portals_boot.scd file (aka the *boot file*) contains the startup sequence of the SI system. Preparing SI for a performance should be as simple as executing this file in the SuperCollider interpreter. The boot file will rely heavily on the JITLib ProxySpace class, which provides a way to replace sounds or entire patterns on the fly, optionally with a crossfade applied to the transition.

Using ProxySpace mechanics, the boot file defines a number of _stereo_ audio tracks, named ```\track1```, ```\track2```, and so forth, a number of parameter tracks, and possibly also a couple of send-return loops for common effects (reverb, delay, etc.)

#### Sonic environments and transitions

The boot file also defines a function, ```\loadMacro``` which loads SI *macros*. A macro is simply a SuperCollider document that defines what to play on each track. One could thing of this as being similar to the *scenes* in Ableton Live. In addition, macros will be treated like any other asset in pOrtals, meaning that they can be tagged as belonging to locations, WorldObjects and so forth (using .yaml metadata files).

The following snippet is an example of a very simple SI macro, which plays a sine wave at 440 Hz on track 1 (L+R channel), and a sine wave at 660 Hz on track 2 (L+R channel):

```
(

p[\track1] = { SinOsc.ar(440 ! 2); };
p[\track2] = { SinOsc.ar(660 ! 2); };

)
```

Now let's assume this file is saved in the pOrtals asset directly as ```my-macro.scd```. Then loading this into SI is done by executing the ```\loadMacro``` function as follows:

```
Fdef(\loadMacro).value("my-macro")
```

Now the sine waves will fade in (based on a master fadeTime parameter set in portals_boot). If another macro (let's call it *my-macro-2*) is loaded using the ```\loadMacro```, function, then a crossfade will happen transitioning *my-macro-1* into *my-macro-2*.

#### Network communication

Running ```\loadMacro``` manually in SuperCollider is useful for testing out macros and transitions between different macros, but is obviously not good enough for a fully automated performance system. During performances, location changes, world parameter changes, and other types of events will be received via OSC (music-oriented network protocol) from the chat client, so for example a *location change* OSC event responder will call the ```\loadMacro``` function to load a macro mapped to that location.

*Exactly how macros will be chosen based on location is something we can work out later, but as mentioned above it's useful to think of macros as just being another form of pOrtals asset, which could be mapped to locations, WorldObjects, etc.*

The OSC responders will be configured automatically when running the boot file.

#### Session/World parameters

World parameters will be defined in the boot file and are available to all macros. These parameters will typically be updated by OSC responders (see *Network communication*) but can also be set manually when testing macros.

For example, assume a session parameter called ```\typingSpeed``` is defined. Then it can be used in a macro as follows:

**TODO**: Add code example here.

## Audio Demo

An example of two generative macros, with a macro transition happening around 1:15:
 [reconLIVE-SI-demo-2018-08-18.mp3](https://www.dropbox.com/s/ilhnvlgv5necmx0/reconLIVE-SI-demo-2018-08-18.mp3?dl=0)


#### Source code of first demo macro:
```
(

Fdef(\loadSoundFile).value("DoubleSpiral_Crackle_001.wav", {
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
		\startPos, Pbrown(0.3, 0.7, step: 0.1, length: inf),
		\bufnum, buf,
		\numFrames, buf.numFrames,
		\release, 5,
		\hpf, 300,
		\vol, Pbrown(2, 4, 0.1)
	);
});

)
```

#### Source code of second demo macro:
```
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

```
