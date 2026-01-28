#writing to a file
with open('new_config.txt','w') as file:
    file.write('Key Features of Linux. \n')
    file.write('Open source. anyone can view, modify, and share its source code. \n')
    file.write('Free to use. no licensing cost. \n')

with open('new_config.txt','at') as file:
    file.write('Secure. strong permission and user-based security. \n')
    file.write('Stable & reliable. often runs for long periods without crashing. \n')
    file.write('Multiuser & multitasking . many users and programs can run at the same time')