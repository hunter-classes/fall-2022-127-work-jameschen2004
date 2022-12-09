"""
pandas was installed through 'pip install pandas'
matplotlib was installed through 'pip install matplotlib'
graphs displayed through 'sudo apt-get install python3-tk' on Ubuntu terminal

Extras done: 2
- Use Matplotlib or another Python graphing/plotting library to
  visualize part or all of your analysis.
- Use multiple aspects of a single data source in your analysis
"""
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 
import csv

league_data_file = open("league.csv")
league_data = pd.read_csv(league_data_file)
print(league_data.astype("string"))
print(league_data["blueKills"].describe())
print("According to this dataset, the average number of kills players on the blue side get on within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].mean())
print("According to this dataset, the minimum number of kills players on the blue side get within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].min())
print("According to this dataset, the maximum number of kills players on the blue side get within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].max())

pdBlueSeries = pd.Series(league_data["blueKills"], name = "Blue Team Kills")
pdBlueSeries.plot(legend= True)
pdRedSeries = pd.Series(league_data["redKills"], name = "Red Team Kills")
pdRedSeries.plot(legend= True)
plt.show()