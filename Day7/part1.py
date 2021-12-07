def calculate_fuel_consumption(positions,pos):
    fuel_calcuation=[]
    for item in positions:
        fuel_calcuation.append(abs(item-positions[pos]))
    return {'pos': pos, 'sum': sum(fuel_calcuation)}

input_data = open("./sub_positions.txt").read().splitlines()

positions = [int(item) for item in input_data[0].split(',')]

fuel_matrix = []

i = 0
while i < len(positions):
    fuel_matrix.append(calculate_fuel_consumption(positions, i))
    i = i + 1

min_fuel = min([item['sum'] for item in fuel_matrix])
cheapest_pos = [item['pos'] for item in fuel_matrix if item['sum'] == min_fuel]

print(f"Minimum fuel: {min_fuel}")
print(f"Cheapest position: {cheapest_pos[0]}")