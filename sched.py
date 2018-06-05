import csv

input_path = "input.csv"
output_path = "output.csv"

def write_out(path, result):
    out_file = open(path, 'wb')
    w_lines = csv.writer(out_file, delimiter=',')
    for i in iter(result):
        w_lines.writerow([i] + result[i])


subs = []
types = []
rec_slots = []
rooms = []

ass_slots_rooms = []

input_file = open(input_path, 'rb')
lines = csv.reader(input_file, delimiter=' ')
lines = list(lines)
for row in lines[:-1]:
    subs.append(row[0].strip(','))
    types.append(row[1].strip(','))
    slot = [j.strip(',') for j in row[2:]]
    rec_slots.append(slot)
rooms = [el.strip(',') for el in lines[-1]]

print subs
print types
print rec_slots
print rooms

# Code of backtracking

def is_safe():
    return 