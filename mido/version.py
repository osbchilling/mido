# SPDX-FileCopyrightText: 2016 Ole Martin Bjorndalen <ombdalen@gmail.com>
#
# SPDX-License-Identifier: MIT

import packaging.version

try:import mido
from mido import MidiFile, MidiTrack, Message

# Create a new MIDI file and add a track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add some messages to the track
track.append(Message('program_change', program=12, time=0))

# Add some notes
notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=480))
    track.append(Message('note_off', note=note, velocity=64, time=480))

# Save the MIDI file
mid.save('output.mid')

print("MIDI file created successfully!")
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python 3.7 and lower
    import importlib_metadata

__version__ = "0.0.0.dev0"

try:
    __version__ = importlib_metadata.version("mido")
except importlib_metadata.PackageNotFoundError:
    # Package is not installed
    pass

version_info = packaging.version.Version(__version__)
