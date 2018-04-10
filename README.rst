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
        print("frames: {}".format(sample.frames))
        print("format: major={0[0]}, minor={0[1]}".format(sample.format))
        print("samplerate: {}".format(sample.samplerate))
        print("channels: {}".format(sample.channels))
        print("sections: {}".format(sample.sections))

        print(sample.read_frames("l"))
