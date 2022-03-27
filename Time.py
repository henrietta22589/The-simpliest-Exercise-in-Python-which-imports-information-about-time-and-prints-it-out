'''
This programm will ask from the user, to import the time(hours,minutes,seconds in order this time to be printed in the form--> hour:minutes:seconds)
'''
hour=int(input("Give me the hour\n"))
minutes=int(input("Give me the minutes\n"))
seconds=int(input("Give me the seconds\n"))
''' We cannot print an integer, so the values which are integers have to convert them to strings in order to be printed, to to that, we use the function str'''
print("The hour is\n"+str(hour)+":"+str(minutes)+":"+str(seconds))