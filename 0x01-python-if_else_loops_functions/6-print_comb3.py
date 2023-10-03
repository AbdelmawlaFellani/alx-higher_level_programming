#!/usr/bin/python3
output = []
for i in range(0, 10):
    for j in range(i + 1, 10):
        output.append("{:d}{:d}".format(i, j))

output = ", ".join(output)
print(output)
