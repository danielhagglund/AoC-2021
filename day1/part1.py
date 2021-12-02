measurements = []

input_data = open("./measures.txt").read().splitlines()

for x in input_data:
    if int(x):
        measurements.append(int(x))

previous_depth = measurements[0]
depth_count = 0

for measure in measurements:
    if measure > previous_depth:
        depth_count = depth_count + 1
    previous_depth = measure

print(depth_count)