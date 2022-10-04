# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to exercise 2.3

time_now = input("What time is it now? (in hours)")
alarm_time = input("How long would you like to wait for? (in hours)")
final_time = (int(time_now) + int(alarm_time)) % (24)
print("The alarm will go off at", final_time)