import csv

#----------------------------------------------------------------#
#       Defining input and output read/write functions           #
#----------------------------------------------------------------#

inputpath = "input.csv"
outputpath = "output.csv"

def get_in(input_path, inps):
    input_file = open(input_path, 'rb')
    lines = csv.reader(input_file, delimiter=' ')
    for row in lines:
        inps.append(row)
    return inps

def write_out(output_path, result):
    output_file = open(output_path, 'wb')
    lines = csv.writer(output_file, delimiter=',')
    for i in iter(result):
        lines.writerow([i] + result[i])

#----------------------------------------------------------------#
#                Creating arrays from the data                   #
#----------------------------------------------------------------#

inps = []
subs = []
types = []
rec_slots = []
rooms = []

ass_slots_rooms = []

inps = get_in(inputpath,[])

for i in range(len(inps)-1):
    subs.append(inps[i][0].strip(','))
    types.append(inps[i][1].strip(','))
    slot = [j.strip(',') for j in inps[i][2:]]
    rec_slots.append(slot)
rooms = [i.strip(',') for i in inps[-1]]

print subs
print types
print rec_slots
print rooms

#----------------------------------------------------------------#
#                     Main Code                                  #
#----------------------------------------------------------------#

