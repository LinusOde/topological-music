from music21 import stream, chord

def normalize_to_range(value, min_val, max_val, target_min, target_max):
    if max_val == min_val:
        return target_min
    norm = (value - min_val) / (max_val - min_val)
    return norm * (target_max - target_min) + target_min

def get_local_pitch(seq, index, window=3, pitch_range=(36, 96)):
    context = seq[max(0, index - window):index] + seq[index + 1:index + 1 + window]
    center_val = seq[index]
    local_min = min(context) if context else center_val
    local_max = max(context) if context else center_val
    return int(normalize_to_range(center_val, local_min, local_max, *pitch_range))

def snap_to_note_length(value):
    allowed_durations = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]
    return min(allowed_durations, key=lambda x: abs(x - value))

def sequence_to_local_3note_chords_musicxml(seq, filename="sequence_chords_3note_local_dynamic.musicxml", window=3):
    score = stream.Score()
    part = stream.Part()
    max_interval = 60

    for i in range(len(seq) - 2):
        pitch1 = get_local_pitch(seq, i, window)
        pitch2 = get_local_pitch(seq, i + 1, window)
        pitch3 = get_local_pitch(seq, i + 2, window)
        pitches = [pitch1, pitch2, pitch3]

        spread = max(pitches) - min(pitches)
        raw_duration = normalize_to_range(spread, 0, max_interval, 0.5, 2.0)
        snapped_duration = snap_to_note_length(raw_duration)

        c = chord.Chord(pitches)
        c.quarterLength = snapped_duration
        part.append(c)

    score.append(part)
    score.write("musicxml", fp=filename)

# Example usage
if __name__ == "__main__":
    # sequence = [3, 5, 8, 2, 10, 7, 12, 6, 1, 9]
    sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]
    # sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
    
    sequence_to_local_3note_chords_musicxml(sequence)
