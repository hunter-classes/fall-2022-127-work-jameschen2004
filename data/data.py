"""
pandas was installed through 'pip install pandas'
matplotlib was installed through 'pip install matplotlib'
Extras done: 2
- Use Matplotlib or another Python graphing/plotting library to
  visualize part or all of your analysis.
- Use multiple aspects of a single data source in your analysis
"""
import pandas as pd
import matplotlib as m
import numpy as n
import csv

league_data_file = open("league.csv")
league_data = pd.read_csv(league_data_file)
print(league_data.astype("string"))
print(league_data["blueKills"].describe())
print("According to the above data, the average number of kills players on the blue side get on within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].mean())

xpoints = league_data.array([0, 6])
ypoints = league_data.array([0, 250])

league_data.plot(xpoints, ypoints)
league_data.show()