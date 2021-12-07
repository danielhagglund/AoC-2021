def progress_one_day(fishes):
    fishes[1][8] = fishes[0][0] # Spawn new fishes
    fishes[1][7] = fishes[0][8] 
    fishes[1][6] = fishes[0][0] + fishes[0][7]
    fishes[1][5] = fishes[0][6]
    fishes[1][4] = fishes[0][5]
    fishes[1][3] = fishes[0][4]
    fishes[1][2] = fishes[0][3]
    fishes[1][1] = fishes[0][2]
    fishes[1][0] = fishes[0][1]
    fishes.pop(0)
    fishes.append([0,0,0,0,0,0,0,0,0])
    return fishes

input_data = open("./fish_input.txt").read().splitlines()

inital_timers = input_data[0].split(',')

fishes = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
days = 256

for timer in inital_timers:
    timer_val = int(timer)
    fishes[0][timer_val] = fishes[0][timer_val] + 1

curr_day = 0
while curr_day < days:
    fishes = progress_one_day(fishes)
    curr_day = curr_day + 1

total_fishes = sum(fishes[0])

print(total_fishes)
