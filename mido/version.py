# SPDX-FileCopyrightText: 2016 Ole Martin Bjorndalen <ombdalen@gmail.com>
#
# SPDX-License-Identifier: MIT

import packaging.version

try:import mido
from mido import MidiFile, MidiTrack, Message

import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()

# Add tracks
drums = MidiTrack()
bass = MidiTrack()
keys = MidiTrack()
sax = MidiTrack()

mid.tracks.append(drums)
mid.tracks.append(bass)
mid.tracks.append(keys)
mid.tracks.append(sax)

# Drum pattern (Boom-bap shuffle: Kick, Snare, Hi-hat)
drum_pattern = [
    (36, 100, 0),   # Kick on beat 1
    (42, 70, 120),  # Hi-hat shuffle
    (38, 100, 240), # Snare on beat 2
    (42, 60, 360),  # Hi-hat
    (36, 90, 480),  # Kick on beat 3
    (42, 70, 600),  # Hi-hat shuffle
    (38, 100, 720), # Snare on beat 4
]

for note, velocity, time in drum_pattern:
    drums.append(Message('note_on', note=note, velocity=velocity, time=time))
    drums.append(Message('note_off', note=note, velocity=0, time=time+120))

# Bassline (Warm, rolling jazz feel)
bassline = [
    (48, 80, 0),   # C
    (50, 80, 240), # D
    (52, 80, 480), # E
    (53, 80, 720), # F
]

for note, velocity, time in bassline:
    bass.append(Message('note_on', note=note, velocity=velocity, time=time))
    bass.append(Message('note_off', note=note, velocity=0, time=time+240))

# Rhodes Chords (Cmaj7 - A7 - Dm7 - G7)
chords = [
    ([48, 52, 55, 59], 0),    # Cmaj7
    ([45, 49, 52, 56], 960),  # A7
    ([50, 53, 57, 60], 1920), # Dm7
    ([43, 47, 50, 54], 2880)  # G7
]

for chord, time in chords:
    for note in chord:
        keys.append(Message('note_on', note=note, velocity=70, time=time))
    for note in chord:
        keys.append(Message('note_off', note=note, velocity=0, time=time+960))

# Saxophone Melody (Simple nostalgic melody)
sax_melody = [
    (60, 80, 0),    # Middle C
    (62, 85, 480),  # D
    (64, 90, 960),  # E
    (67, 95, 1440), # G
]

for note, velocity, time in sax_melody:
    sax.append(Message('note_on', note=note, velocity=velocity, time=time))
    sax.append(Message('note_off', note=note, velocity=0, time=time+480))

# Save MIDI file
midi_filename = "boom_bap_lofi_70bpm.mid"
mid.save(midi_filename)

print(f"MIDI file saved as {midi_filename}")# Create a new MIDI file and add a track
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
