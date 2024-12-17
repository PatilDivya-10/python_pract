import pandas as pd



print("Hello World")
name = "Divya" #string
age = 20
price = 20.34
print(age)
print("my name is :", name)
print("my age is :", age)
print(type(name))
print(type(age))
print(type(price))

a = 1000
b = 500
sum = a + b
print(sum)


s = pd.Series([1, 2, 3, 4])
print(s)

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('industry.csv')
df.to_csv('output.csv', index=False)
df = pd.read_excel('FSI-2023.xlsx')

