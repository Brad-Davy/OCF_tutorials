import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["figure.autolayout"] = True
cm = 1/2.54  # centimeters in inches

raw_data = [] 
processed_data = []
exponent = 3

with open('input.txt', 'r') as input_file:
    data = input_file.read().split('\n')
    for i in data:
        raw_data.append(float(i))

def process_data(data: list, exponent: int) -> list:
    if data > 50:
        return data
    else:
        return data**exponent

for i in raw_data:
    processed_data.append(process_data(i, exponent))

fig=plt.figure(figsize=(12*cm, 12*cm))
plt.plot(raw_data, processed_data, label=f'y = x^{exponent}', color='black', linestyle='--')
plt.legend(ncol=1, frameon=False)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(f'img/figure_1_exponent_{exponent}.svg', dpi=500)
plt.show()