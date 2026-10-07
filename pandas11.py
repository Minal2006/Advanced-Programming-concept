import pandas as pd

patients = {
    "P101": 65,
    "P102": 45,
    "P103": 70,
    "P104": 35,
    "P105": 62
}

series = pd.Series(patients)

print("Average Age:")
print(series.mean())

print("\nOldest Patient:")
print(series.idxmax(), series.max())

print("\nYoungest Patient:")
print(series.idxmin(), series.min())

print("\nPatients above 60:")
print(series[series > 60])