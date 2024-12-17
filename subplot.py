import matplotlib.pyplot as plt

# Sample data
years = [2015, 2016, 2017, 2018, 2019]
sales = [200, 300, 400, 500, 600]
regions = ['North', 'South', 'East', 'West']
revenue = [300, 400, 200, 100]
x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 6, 10]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]

# Create a 2x2 grid of subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First subplot (Line plot)
axs[0, 0].plot(years, sales, color='blue')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Sales')

# Second subplot (Bar plot)
axs[0, 1].bar(regions, revenue, color='green')
axs[0, 1].set_title('Bar Plot')
axs[0, 1].set_xlabel('Region')
axs[0, 1].set_ylabel('Revenue')

# Third subplot (Scatter plot)
axs[1, 0].scatter(x, y, color='red')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')

# Fourth subplot (Histogram)
axs[1, 1].hist(data, bins=5, color='orange')
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout to prevent overlap of subplots
plt.tight_layout()

# Display the figure
plt.show()
