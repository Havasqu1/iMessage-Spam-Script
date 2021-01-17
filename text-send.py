import os

word ='Hey'
##for word in beeMovieWords:
for i in range(0,100000):
        applescript = "'" + "on run\n" + "\ttell application " + '"Messages"\n' +'\t\tsend "' + word + '" to buddy "ENTER PHONE NUMBER HERE" of service "SMS"\n\tend tell\nend run'+"'"

        os.system('osascript -e ' +applescript)

