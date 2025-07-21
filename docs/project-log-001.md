**Project Log: Topological Music**

**Start Date**: July 2025  
**Participants**: [User], Hugo Angulo  
**Platform**: GitHub (public), MuseScore, Python (planned), possible use of MusicXML and sound rendering tools

---

### **Entry 1: Project Initialization**

**Date**: July 17, 2025

- Created a GitHub repository for the project with an MIT license.
- Confirmed with Hugo that the project could move forward publicly.
- A short project description was written: *"Exploring music from number sequences using topology, code, and perception to reveal hidden structures through sound."*
- Intention stated to respect Hugo's conceptual ownership, especially if earlier work was to be kept private.

---

### **Entry 2: Tooling and Software**

**Date**: July 17, 2025

- Chose **MuseScore** as the free, open-source notation and playback tool. It replaces the need for Dorico and NotePerformer, which are paid.
- Created a local folder structure compatible with GitHub:
  - `code/` for scripts
  - `docs/` for writeups and theory
  - `sound_tests/` for exported audio

---

### **Entry 3: Conceptual Grounding**

**Date**: July 17, 2025

- Discussed with Hugo how increasing numerical values in sequences might be perceived sonically as a change in spatial experience:
  - Smaller numbers = "dry," "infant-like," muted audio.
  - Larger numbers = more spacious, echo-rich, expanded sound field.
  - Idea: audio lives in a virtual room whose size changes with the data.
- This inspired the idea to map number sequences to **reverb**, **timbre**, and **spatialization** — not just pitch and rhythm.

---

### **Entry 4: Research Into Auditory Perception**

**Date**: July 17, 2025

- Investigated how the human brain perceives musical structure:
  - **Gestalt principles**: grouping, symmetry, repetition.
  - **Auditory Scene Analysis**: layering of sounds.
  - **1/f rhythm patterns**: preferred by the brain.
  - **Emotional response** to musical expectation and resolution.
- Conclusions:
  - Structure in number sequences must be made perceptible through auditory features that the brain naturally responds to.
  - This validates the project's core idea: number-based structures can be "heard" if thoughtfully rendered.

---

### **Planned Next Steps**

- Write a Python script that converts OEIS sequences to MusicXML.
- Use MuseScore to import, visualize, and play these sequences.
- Experiment with mapping number properties (size, gaps, modularity) to musical parameters (pitch, rhythm, space, timbre).
- Log further conceptual conversations and findings in `docs/` folder of the repo.

- ---

### **Entry 5: Local Environment Setup**
**Date**: July 18, 2025

- Installed **Python 3.x** from python.org.
- Chose **Visual Studio Code** as the code editor for development.
- Verified Python installation using `python --version`.
- Installed the **music21** library via `pip install music21` to handle MusicXML creation.
- Confirmed `music21` works on the local machine for generating `.musicxml` files.
- Created and tested a script `sequence_to_musicxml.py` in the `code/` folder to convert sequences into pitch-mapped MusicXML scores.
- Defined the pitch-mapping logic using a **local context** window of 3 previous and 3 following values.
- Applied normalization to map local values into a range of MIDI pitches (21–108 for full piano).

---

### **Planned Next Steps**

- Use the `sequence_to_musicxml.py` script with OEIS sequences.
- Open and review generated `.musicxml` scores in MuseScore.
- Expand the script to support variable durations, dynamics, or instrument mappings.
- Begin exploring mappings beyond pitch: spatialization, reverb, timbral variation.
- Document ideas and discussions in `docs/` folder of the GitHub project.

### **Entry 6: Two-Note Chords with Local Context**

**Date**: July 21, 2025\\

- Developed script to render a series of 2-note chords from a number sequence.\\
- Each chord is formed by taking two consecutive values, mapped to pitch using local min/max normalization.\\
- Duration of each chord is proportional to the pitch difference between the two notes, then snapped to valid rhythmic values.\\
- Result: flowing harmony with evolving texture and rhythm.

---

### **Entry 7: Three-Note Chords with Spread-Based Rhythm**

**Date**: July 21, 2025\\

- Updated script to render 3-note chords based on triplets of consecutive numbers.\\
- Pitch mapping retains local context logic.\\
- Duration determined by spread (max - min) of the three pitches, emphasizing wider harmonic jumps with longer durations.\\
- Output generated and tested successfully in MuseScore — dense but structured result.

---

### **Playback and Listening Techniques**

**Date**: July 21, 2025\\

- To slow down the music in MuseScore:\\
  - Used the Play Panel (F8) and reduced tempo to 50% for better perception.\\
  - Optionally used “Halve Note Durations” in MuseScore to make the change permanent.\\
- Future consideration: embed tempo metadata directly in MusicXML if needed.

---

### **Next Steps**

- Extend script functionality with optional tempo scaling.\\
- Begin testing with real OEIS sequences.\\
- Start experimenting with spatial markers, dynamic layers, and timbral changes to simulate "room size" or topological wrapping.\\
- Log and document each script version with consistent naming for reproducibility.
