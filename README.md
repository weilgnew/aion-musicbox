# aion-musicbox
# Procedural music generator

#Progress
1. Harmony to generate the music melody in list form [array]
  - Simple harmony rule to generate melody embedded in the main .py file
  - Normal distribution is used to determine the probability of note's generation
  - Limited in the same octave (expansion to multiple octave, how?)

2. Divide the melody into 'bar', with relationship between bars (repetition, alteration)
  - Define the time signature
  - Define the tempo

2. Melody list contain: frequency (pitch), duration, position
3. Note's duration, position
4. Tone's texture
  - Texture for different sounds (different instruments) by mixing frequencies
  - chords?
  
5. Generate wav file with the list of melody?

6. Play the music?
  - Use a media player, no plan to integrate the music player into the project

# Standard for waveform_gen
# waveform_gen is a function that generates the waveform for wav file exporter using the melody list

melody = [note1, duration1, note2, duration2, note3, duration3, ...]
-multiple layers add to one track by having note1, note 2, note3 with respective duration
