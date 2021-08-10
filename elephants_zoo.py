import argparse
import os


def elephants(data_file):
    with open(data_file, 'r') as f:
        data_store = []
        lines = f.readlines()
        for line in lines:
            data_store.append([int(x) for x in line.split()])
    elephant_number = data_store[0][0]
    check_c_list = [False for _x in range(elephant_number + 1)]
    weight = data_store[1]
    min_weight = min(weight)
    start_positions = [0 for _x in range(elephant_number)]
    end_positions = [0 for _x in range(elephant_number)]
    for a in range(elephant_number):
        start_positions[a] = data_store[2][a] - 1  # start_positions[0] = 3 -1
    for a in range(elephant_number):
        end_positions[data_store[3][a] - 1] = start_positions[a]
    weight_sum = 0
    for x in range(elephant_number):
        if not check_c_list[x]:
            min_cycle_wg = max(weight) + 1
            cycle_weight = 0
            cycle_length = 0
            cycle_x = x
            while True:
                min_cycle_wg = min(min_cycle_wg, weight[cycle_x])
                cycle_weight += weight[cycle_x]
                cycle_x = end_positions[cycle_x]
                check_c_list[cycle_x] = True
                cycle_length += 1
                if cycle_x == x:
                    break
            weight_sum += min((cycle_weight + (cycle_length - 2) * min_cycle_wg),
                              (cycle_weight + min_cycle_wg + (cycle_length + 1) * min_weight))
    print(weight_sum)


parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='Please put file name after program name')
args = parser.parse_args()
if not os.path.exists(args.file_name):
    print("file doesn't exist")
else:
    elephants(args.file_name)

