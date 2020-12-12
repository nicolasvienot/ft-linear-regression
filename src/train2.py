def predict(x):
    return slope * x + intercept


def variance(values, mean):
    return sum([(val - mean)**2 for val in values])


def covariance(yearsexperience, mean_yoe, salary, mean_salary):
    covariance = 0.0
    for r in range(len(yearsexperience)):
        covariance = covariance + (yearsexperience[r] -
                                   mean_yoe) * (salary[r] - mean_salary)
    return covariance


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

mean_km = sum(df['km']) / float(len(df['km']))
mean_price = sum(df['price']) / float(len(df['price']))

variance_km = variance(df['km'], mean_km)
variance_price = variance(df['price'], mean_price)

covariance_km_price = covariance(df['km'], mean_km, df['price'], mean_price)

m = covariance_km_price / variance_km
c = mean_price - m * mean_km

price = m * 240000 + c
print(price)
