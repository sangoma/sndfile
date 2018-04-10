=======
sndfile
=======

Work in progress simple CFFI wrapper around the C ``libsndfile`` API.

Currently only implements a simple interface for reading frames from
supported audio files into Python's ``array.array``.

Example
-------

A simple example that loads an audio file, prints some statistics, and
dumps out all the frames as 32bit integers.

.. code:: python

    SAMPLES = pathlib.Path("my-audio-sample-dir")

    with sndfile.open(SAMPLES / "my-sample.flac", "r") as sample:
        print(sample)
        print("frames:", sample.frames)
        print("format:", sample.format)
        print("samplerate:", sample.samplerate)
        print("channels:", sample.channels)
        print("sections:", sample.sections)

        print(sample.read_frames("l"))
