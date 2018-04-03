SETUP

reccomended: download and install notepad++	LINK: https://notepad-plus-plus.org/download/v7.5.6.html

1. Download and install Python 3.6.5		LINK: https://www.python.org/downloads/

2. Download chromedriver_win32.zip, extract (right-click, Extract All...), run chromedriver.exe	LINK: https://chromedriver.storage.googleapis.com/index.html?path=2.37/ 

3. Run CreateAutoTasks.bat (if it doesn't set proper times, edit the tasks in Task Scheduler)
	-note: you'll likely see the tasks after clicking "Task Scheduler Library" in the top left

4. replace 'username' and 'password' in restrSign.bat with your CAS username and password
	-you'll have to right-click it and select edit

5. copy the text from this link into a file and save it as "get-pip.py" (no quotes) in the same folder: https://bootstrap.pypa.io/get-pip.py
	-this is where having Notepad++ may come in handy

6. copy your folder's adress

7. open a new command prompt

8. type "cd" followed by the folder's adress (hit Ctr+V), then hit enter

9. enter the command "python get-pip.py"

10. enter the command "pip install -U selenium"

11. enter the command "python autologin.py" to test that your program works


NOTE: THESE INSTRUCTIONS AND LINKS ONLY WORK FOR WINDOWS