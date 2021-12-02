measurements = []

input_data = open("./measures.txt").read().splitlines()

for x in input_data:
    if int(x):
        measurements.append(int(x))

sliding_windows = []

index = 0

while index < len(measurements) - 2:
    sliding_windows.append(measurements[index] + measurements[index+1] + measurements[index+2])
    index = index + 1

previous_depth = sliding_windows[0]
depth_count = 0

for measure in sliding_windows:
    if measure > previous_depth:
        depth_count = depth_count + 1
    previous_depth = measure

print(depth_count)