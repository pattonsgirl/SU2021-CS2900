# CS 2900 - Summer 2021
Content for Data Analysis with Python

- [Software](#Software)
- [Resources](#Resources)

## Software

- [Anaconda](#Anaconda)
- [Git](#Git)
- [VSCode](#Visual-Studio-Code)
- [Test Workflow](#Test-Workflow)
- [Troubleshooting](#Troubleshooting)

### Anaconda
1. Install Anaconda
    - [Installer for Windows](https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe)
        - Install for all users (personal preference)
        - By default, installs to `C:\ProgramData\Anaconda3`
        - Select `Register Anaconda as System Python 3.8`
    - [Installation script for Linux](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh)
        - If using terminal, download with: `wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh`
        - Change permissions so script is executable: `chmod u+x Anaconda3-2020.11-Linux-x86_64.sh`
        - Execute script: `./Anaconda3-2020.11-Linux-x86_64.sh`
            - Install to either `/home/your_username/anaconda3` or `/opt/anaconda3` (opt is more of an all users location, may need `sudo`)
        - Type `yes` to initialize Anaconda3
    - Macs:
        - [Graphical Installer for Mac](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg)
        - [Command line install for Mac](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.sh)
        - What's the diff?  Graphical will have a wizard (and install some additional program baggage), command line will be more Linux-like
        - Anticipated CLI instructions (message me if untrue):
            - download with: `wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh`
            - Change permissions so script is executable: `chmod u+x Anaconda3-2020.11-Linux-x86_64.sh`
            - Execute script: `./Anaconda3-2020.11-Linux-x86_64.sh`
                - Install to either `/home/your_username/anaconda3` or `/opt/anaconda3` (opt is more of an all users location, may need `sudo`)
            - Type `yes` to initialize Anaconda3

2. Add to `PATH`
    - Windows: 
        - Start menu, "Environment Variables", look for "Path" entry under **"System variables"**
        - Add new entry: `C:\ProgramData\Anaconda3`
        - Add new entry: `C:\ProgramData\Anaconda3\Scripts`
        - Use "Move Up" button to place above any other python installs
        - Open a terminal, and type `python` - you should see notes that state you are using anaconda python 3.8
        - If you see this warning: 
        ```
        Warning:
        This Python interpreter is in a conda environment, but the environment has not been activated.  
        Libraries may fail to load.  To activate this environment please see https://conda.io/activation
        ```
        - Run this command: `C:\ProgramData\Anaconda3\Scripts\activate base`
        - The next line may now start with `(base)`
        - Going forward, I recommend using the tools installed with Anaconda if you need a terminal only - otherwise you have to remember to activate every time.
    - Linux:
        - Close and open new terminal or type `source .profile`
        - The next line may now start with `(base)`.
    - Mac:
        - First volunteer will help me fill this section out! 

3. [Windows] Powershell changes
    - Allow 'conda' to work on your computer:
        - (Running Powershell): `conda init powershell`
        - (In cmd - optional): `conda init cmd.exe`
    - Allow Powershell to run scripts:
        - Running Powershell as Admin: `Set-ExecutionPolicy RemoteSigned`
            - Recommend selecting A, Yes to All

### Git
1. Install:
    - [For Windows](https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe)
        - Accept defaults until you get to the Choosing the default editor used by Git screen, on this I would recommend selecting Visual Studio Code (not insider build) from the dropdown.
        - Accept all other defaults
        - After installation, run the Git Bash program and execute the following commands:
        - `git config --global user.name "Your Name"`
        - `git config --global user.email "youremail@yourdomain.com"`
        - Note: substitute your name and email in the above commands inside the quote (keep the quotation marks)
    - For Linux: 
        - `sudo apt install git-all`
        - [Other install instructions](https://git-scm.com/download/linux)
        - After installation, run the following commands:
        - `git config --global user.name "Your Name"`
        - `git config --global user.email "youremail@yourdomain.com"`
        - Note: substitute your name and email in the above commands inside the quote (keep the quotation marks)
    - For Mac: 
        - Type `git` on command line.  Should prompt to install
        - [Other install instructions](https://git-scm.com/download/mac)
        - After installation, run the following commands:
        - `git config --global user.name "Your Name"`
        - `git config --global user.email "youremail@yourdomain.com"`
        - Note: substitute your name and email in the above commands inside the quote (keep the quotation marks)

2. GitHub Desktop (Optional) - likely for Windows & Mac users
    - The advantage here is purely in authentication.  I literally don't open it after I've cloned a project, VSCode then uses the Desktop apps credentials, and I am happy.
    - [GitHub Desktop](https://desktop.github.com/)
 
3. SSH Key Authorization (Optional) - likely for Linux and Mac (this may work in Windows using Git Bash)
    - Generate a key pair: `ssh-keygen -t ed25519 -C "your_email@example.com"`
        - I would keep the default name & location for the file, and I would **not** enter a passphrase
    - Open your GitHub profile, go to Settings, then select "SSH & GPG Keys"
    - Copy the contents of `.ssh\id_ed25519.pub` to a new key entry - I usually name them with my system name to remember
    - In your repository, click the green "Code" button, select "SSH", copy the URL provided
    - In your terminal, type `git clone insert-URL-here`
    - [If you cloned with HTTPS, how to change your repo to authenticate with SSH (not HTTPS)](https://haydar-ai.medium.com/learning-how-to-git-using-ssh-instead-of-https-91f09cff72de)
    - [If you have errors, poke around here](https://docs.github.com/en/github/authenticating-to-github/error-permission-denied-publickey)

### Visual Studio Code
1. Install:
    - [For Windows](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)
    - [For Linux (Ubuntu/Debian)](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64)
    - [For Mac](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)
    - [Setup Guide (includes any OS)](https://code.visualstudio.com/docs/setup/setup-overview)

2. Recommended Plugins / Extensions
    - Python

3. Open your folder that you cloned in VS Code
    - File -> Open Folder, use explorer to browse to folder
    - In GitHub Desktop, Repository -> Open in Visual Studio Code

4. Make sure in the bottom left corner that it states something similar to `Python 3.8.5 64-bit ('base':conda)`
    - If not, click on it, and in the dropdown select the Anaconda version of python
    - This may add a `.vscode` folder with this special selection.  Leave it.

### Test Workflow
1. In your Demos folder, create a `.py` file with the following contents:
```
import numpy
print("Hello World")
a = numpy.arange(10)
print(a)
```
2. Hit the "Play" button in the upper right.  The expected output is below.  If you see something different, check [Troubleshooting](#Troubleshooting) or post to the Discord chat if you see something not documented.
```
Hello World
[0 1 2 3 4 5 6 7 8 9]
```
![visual model to compare](Images/working-output.png)
3. In the "Source Control" menu, there should be a note that files in your folder have had changes (or been added)
4. Click the "Commit" checkmark".  This may prompt asking if you want files to be auto added.  Go ahead and say "Yes"
5. Click the three dots (...) for a dropdown, and select "Push"
    - If you cloned with HTTPS, you'll be prompted for a username / password to authenticate with GitHub here.
    - If you cloned with SSH, you should not be prompted.  If you have an error, post to the Discord chat and I'll help you through
    - If you installed GitHub for Desktop and signed in to your GitHub account, you should not be prompted.  If you have an error, post to the Discord chat and I'll help you through
6. In the browser, refresh your GitHub page for this course. You should see your new file in the Demos folder.

### Troubleshooting
Problem: Hit "Play", see "& was unexpected at this time"

Solution: Need to change VSCode to use Powershell by default.  This is due to VSCode getting a tighter integration with Powershell.
- In VSCode, type: Ctrl + Shift + P
- Search for Preferences: Open User Settings and select to open
- Search for Terminal › Integrated › Default Profile: Windows
- Click to open `Edit in settings.json`
- There should be a line: `"terminal.integrated.defaultProfile.windows": "Command Prompt",`
- Change `Command Prompt` to `Powershell` and Ctrl + S to Save
- Close your terminal / reload VSCode.  Hit "Play".  Output should now be as advertised.


## Resources

This lists are by no means exhuastive.  Also, please share links to communities you enjoy and I'll add them to the list!

- [Python for Data Analysis Companion Repository](#Companion-Repo)
- [Understanding git](#Understanding-git)
- [Python Tutorials](#Python-Basics)
- [Immersion](#Immersion)

### Companion Repo
- [Python for Data Analysis Companion Repository](https://github.com/wesm/pydata-book)

### Understanding git
- [Pro Git Book](https://git-scm.com/book/en/v2)

#### Markdown for `.md` Files
- [markdown-demo.md](markdown-demo.md)
    - [Direct link to raw file](https://raw.githubusercontent.com/pattonsgirl/SU2021-CS2900/main/markdown-demo.md)
- [Basic Writing and Formatting Syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

### Python Basics
- Note: I recommend picking one of these and treating it as your textbook.  Google searches of what you're trying to do are also effective, but can feel overwhelming if you don't quite know what you're looking for.
- [Official Python Docs](https://docs.python.org/3/tutorial/index.html)
- [learnpython.org](https://www.learnpython.org/)
- [Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
    - [Companion Jupyter Notebooks](https://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/tree/master/)
- [W3 Schools - Python](https://www.w3schools.com/python/python_intro.asp)
- [Python Tutorial](https://pythonbasics.org/)

### Immersion
- [Towards Data Science](https://towardsdatascience.com/)
    - Frequent blogs about problem solving.  Community is python focused.
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [r/Python](https://www.reddit.com/r/Python/)
- [r/datasets](https://www.reddit.com/r/datasets/)
- [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/)