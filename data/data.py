"""
Worked together with Jatin Kapoor
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
# Read the CSV file using the pandas.read_csv method
league_data = pd.read_csv(league_data_file, index_col=0)
print(league_data.astype("string"))
print("----------")
print("Blue Team Kills Data")
print(league_data["blueKills"].describe())
print("According to this dataset, the average number of kills players on the blue side get on within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].mean())
print("According to this dataset, the minimum number of kills players on the blue side get within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].min())
print("According to this dataset, the maximum number of kills players on the blue side get within the first 10 minutes of a high diamond - masters game is: ")
print(league_data["blueKills"].max())
print("----------")
print("Red Team Kills Data")
print(league_data["redKills"].describe())

# Find the mean of the redKills column using the pandas.DataFrame.mean method
mean_red_kills = league_data["redKills"].mean()
# Find the mode of the redKills column using the pandas.DataFrame.mode method
mode_red_kills = league_data["redKills"].mode()
# Print the mean and mode of the redKills column
print("The mean number of red team kills is: ", mean_red_kills)
print("The mode number of red team kills is: ", mode_red_kills)


fig, (ax0, ax1) = plt.subplots(ncols= 2)

ax0.hist(league_data["blueKills"], bins= 22, density= False, histtype= "bar", color= "turquoise")
ax0.set_title("Number of Times each Kill Amount is Reported on the Blue Team Side Within 10 Minutes")
ax0.set_xlabel("Recorded Total Number of Kills within 10 Minutes")
ax0.set_ylabel("Recorded Amount of the Same Total Number of Kills")
ax1.hist(league_data["redKills"], bins= 22, density= False, histtype= "bar", color= "pink")
ax1.set_title("Number of Times each Kill Amount is Reported on the Red Team Side Within 10 Minutes")
ax1.set_xlabel("Recorded Total Number of Kills within 10 Minutes")
ax1.set_ylabel("Recorded Amount of the Same Total Number of Kills")
plt.show()

print("From these histograms, we can conclude that the kill amount frequencies on both teams are very similar.")

