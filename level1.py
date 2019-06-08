import time
import webbrowser
import subprocess
import os
option='''
press 0 for displaying current system date and time
press 1 for opening player
'''
print("enter your choice")
choice=input();
if choice=='0':
	current_time=time.ctime()
	print(current_time) 
elif choice =='1':
	data=input("type what you want to search")
	webbrowser.open_new_tab('http:/www.google.com/search?q='+data)
elif choice=='2':
	subprocess.getoutput('firefox')
elif choice=='3':
	os.system('reboot')


