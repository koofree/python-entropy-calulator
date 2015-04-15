__author__ = 'koo'

import math

is_normalize = True


def cal(value, total):
    p = float(value) / float(total)

    return (math.log(p) * p) * -1

# settings info
open_file_name = 'data.txt'
# open_file_name = 'high_data.txt'
#open_file_name = 'perfect_data.txt'
open_file_name = 'bad_data.txt'
is_initial = True
k = 1
zero_entropy = 0

open_file = open(open_file_name)

for line in open_file:
    if line.startswith("#") or len(line.strip()) is 0:
        continue

    initial_count = int(line)
    data_count = list()
    category_data_count = list()
    for num in xrange(0, initial_count):
        data_count.append(int(open_file.next()))
        category_data_count.append(0)

    is_initial = False
    break

num = 0
category_data_size = list()
each_size = 0
for line in open_file:
    if line.startswith("#") or len(line.strip()) is 0:
        continue

    value = int(line)
    category_data_count[num % initial_count] += value
    each_size += value

    num += 1

    if num % initial_count is 0:
        category_data_size.append(each_size)
        each_size = 0

open_file.seek(0)
for num in xrange(0, initial_count + 1):
    line = open_file.next()
    while line.startswith("#") or len(line.strip()) is 0:
        line = open_file.next()

num = 0
category_total_count = 0
total_count = 0

category_entropy = 0
real_entropy = 0
size_entropy = 0

total_category_entropy = 0
total_real_entropy = 0
total_size_entropy = 0

for line in open_file:
    if line.startswith("#") or len(line.strip()) is 0:
        continue

    value = int(line)

    if value is 0:
        category_entropy += zero_entropy
    else:
        category_total_count += value

        # real_data_count
        real_entropy += cal(value, data_count[num % initial_count])
        # category_data_count
        category_entropy += cal(value, category_data_count[num % initial_count])
        # category_data_size
        size_entropy += cal(value, category_data_size[num / initial_count])

    num += 1

    if num % initial_count is 0:
        total_real_entropy += real_entropy
        total_category_entropy += category_entropy
        total_size_entropy += size_entropy
        print real_entropy, category_entropy, size_entropy
        total_count += category_total_count
        category_entropy = 0
        real_entropy = 0
        size_entropy = 0
        category_total_count = 0

print
print 'real entropy :', total_real_entropy
print 'category entropy :', total_category_entropy
print 'size entropy :', total_size_entropy

print total_count
print data_count
print category_data_count
print category_data_size