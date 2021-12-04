def transpose(list1, list2):
    list2 =[[row[i] for row in list1] for i in range(len(list1[0]))]
    return list2

input_data = open("./diagnostic_report.txt").read().splitlines()

gamma_rate = ''
epsilon_rate = ''

report = []
report_transposed = []
for item in input_data:
    entry = []
    for bit in item:
        entry.append(int(bit))
    report.append(entry)

report_transposed = transpose(report, report_transposed)

for line in report_transposed:
    nr_of_ones = line.count(1)
    nr_of_zero = line.count(0)
    if nr_of_ones > nr_of_zero:
        most_signigicant = 1
        least_significant = 0
    else:
        most_signigicant = 0
        least_significant = 1
    gamma_rate = gamma_rate + str(most_signigicant)
    epsilon_rate = epsilon_rate + str(least_significant)

print(int(gamma_rate,2))
print(int(epsilon_rate,2))
print(int(gamma_rate,2) * int(epsilon_rate,2))