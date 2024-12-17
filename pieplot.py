import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Region': ['North', 'South', 'East', 'West'],
        'Revenue': [300, 400, 200, 100]}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the 'Region' column as the index and plot the 'Revenue' column as a pie chart
df.set_index('Region')['Revenue'].plot(kind='pie', autopct='%1.1f%%', title='Revenue Share')

# Remove the y-axis label (it won't be needed in a pie chart)
plt.ylabel('')

# Display the plot
plt.show()
