class Fish:

    def __init__(self, timer=8):
        self.timer = timer

    def get_timer(self):
        return self.timer

    def decrease_timer(self):
        self.timer = self.timer - 1

    def reset_timer(self):
        self.timer = 6

    def spawn(self):
        return Fish()

def progress_one_day(fishes):
    new_fishes = []
    for fish in fishes:
        if fish.get_timer() == 0:
            new_fishes.append(fish.spawn())
            fish.reset_timer()
        else:
            fish.decrease_timer()
    return new_fishes
    
input_data = open("./fish_input.txt").read().splitlines()

inital_timers = input_data[0].split(',')

fishes = []
days = 80

for timer in inital_timers:
    timer_val = int(timer)
    fishes.append(Fish(timer_val))

curr_day = 0
while curr_day < days:
    fishes = fishes + progress_one_day(fishes)
    curr_day = curr_day + 1

total_fishes = len(fishes)

print(total_fishes)
