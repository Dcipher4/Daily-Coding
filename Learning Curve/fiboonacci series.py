import pandas as pd
from sklearn.datasets import load_iris

# def fibonacci(n):
#     fib_series = [0, 1]
#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series

# # Example usage:
# n = 10  # Change this value to generate more or fewer Fibonacci numbers
# print(fibonacci(n))

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=' ')
# Load iris dataset
from urllib.request import urlretrieve

# URL of the iris.csv file
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Local path where the file should be saved
local_file_path = 'C:\\Users\\Admin\\OneDrive\\Desktop\\python programs\\iris.csv'

# Download the file
urlretrieve(file_url, local_file_path)

print("Download completed!")