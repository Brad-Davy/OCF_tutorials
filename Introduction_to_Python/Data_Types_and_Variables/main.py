import matplotlib.pyplot as plt


arr = []

data = open("test.txt", "r")
read_data = data.read().split('\n')
print(read_data)

for lines in read_data:
    arr.append(float(lines))
data.close()

print(arr)

plt.plot(arr)
plt.show()  