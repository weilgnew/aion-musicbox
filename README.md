# aion-musicbox
# Procedural music generator

#Progress
1. Harmony to generate the music melody in list form [array]  - done, but need more complex mechanism, in future
  - Simple harmony rule to generate melody embedded in the main .py  
  - Normal distribution is used to determine the probability of note's generation
  - Limited in the same octave (expansion to multiple octave, how?) - will be done in chords

2. Divide the melody into 'bar', with relationship between bars (repetition, alteration) 
  - Define the time signature
  - Define the tempo
  # Beat generator is there, but might need to create a library for various tempo

3. Melody list contain: frequency (pitch), duration, position
  - It is there, so far. consist of: melody[], beat[]
  
4. Tone's texture
  - Texture for different sounds (different instruments) by mixing frequencies
  - chords?
  
5. Generate wav file with the list of melody? - done

6. Play the music?
  - Use a media player, no plan to integrate the music player into the project

THE NEXT BIG THING!
CHORD CHORD CHORD CHORD CHORD CHORD
- build the melody movement with existing melody generator, then fill the melody with chord
- using chord library?
- format should be
melody = [note1, note2, note3, ...]
beat = [duration1, duration2, duration3, ...]
-multiple layers add to one track by having note1, note 2, note3 with respective duration
