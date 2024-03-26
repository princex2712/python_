def count_notes(amount):
    notes = {10: 0, 20: 0, 50: 0, 100: 0, 500: 0}
    note_values = [10, 20, 50, 100, 500]
    curr = len(note_values) - 1
    while curr >= 0 and amount > 0:
        if note_values[curr]<=amount:
            temp = amount//note_values[curr]
            notes[note_values[curr]] = temp
            amount -= temp*note_values[curr]
        curr-=1
    return notes
note =count_notes(4680)
for k,v in note.items():
    if v > 0:
        print('Notes of',k,':',v)

