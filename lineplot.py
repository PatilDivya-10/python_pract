import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019]
sales = [200, 300, 400, 500, 600]

plt.plot(years, sales, marker='o', linestyle='--', color='b')
plt.title('Yearly Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
