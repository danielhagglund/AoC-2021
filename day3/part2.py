def find_signicant_bit(report, pos, most_significant):
    count_ones = 0
    count_zero = 0
    for line in report:
        if line[pos] == 1:
            count_ones = count_ones + 1
        else:
            count_zero = count_zero + 1
    
    if most_significant:
        if count_ones >= count_zero:
            return 1
        else:
            return 0
    else:
        if count_zero <= count_ones:
            return 0
        else:
            return 1

def reduce_report(report, pos, keep):
    if len(report) == 1:
        return report

    reduced_report = []
    for line in report:
        if line[pos] == keep:
            reduced_report.append(line)

    return reduced_report


# main
input_data = open("./diagnostic_report.txt").read().splitlines()

report = []

for item in input_data:
    entry = [int(bit) for bit in item]
    report.append(entry)

most_significant_bits = []
least_significant_bits = []
pos_length = len(report[0])
oxygen_report = report.copy()
co2_report = report.copy()
pos = 0
while pos < pos_length:
    significant_bit = find_signicant_bit(oxygen_report, pos, True)
    most_significant_bits.append(significant_bit)
    oxygen_report = reduce_report(oxygen_report, pos, significant_bit)
    least_significant_bit = find_signicant_bit(co2_report, pos, False)
    least_significant_bits.append(least_significant_bit)
    co2_report = reduce_report(co2_report, pos, least_significant_bits[pos])
    pos = pos + 1

co2_scrubber_value = ''.join([str(val) for val in co2_report[0]])
oxygen_generator_rating = ''.join([str(val) for val in oxygen_report[0]])

print(f"CO2 scrubber rating: {int(co2_scrubber_value, 2)}")
print(f"Oxygen generator rating: {int(oxygen_generator_rating, 2)}")
print(f"Lif support rating: {(int(co2_scrubber_value, 2)) * (int(oxygen_generator_rating, 2))}")