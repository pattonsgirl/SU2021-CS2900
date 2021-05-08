# CS 2900 - Summer 2021
Content for Data Analysis with Python

- [Software](#Software)
- [Resources](#Resources)

## Software

- [Anaconda](#Anaconda)
- [Git](#Git)
- [VSCode](#Visual-Studio-Code)

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
        - Use "Move Up" button to place above any other python installs
        - Open a terminal, and type `python` - you should see notes that state you are using anaconda python 3.8
        - If you see this warning: 
        ```
        Warning:
        This Python interpreter is in a conda environment, but the environment has not been activated.  Libraries may fail to load.  To activate this environment please see https://conda.io/activation
        ```
        - Run this command: `C:\ProgramData\Anaconda3\Scripts\activate base`
        - The next line may now start with `(base)`
    - Linux:
        - Close and open new terminal or type `source .profile`
        - The next line may now start with `(base)`.
    - Mac:
        - First volunteer will help me fill this section out! 

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

3. SSH Key Authorization (Optional) - likely for Linux and Mac
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

## Resources

### Markdown for `.md` Files
- [markdown-demo.md](markdown-demo.md)
    - [Direct link to raw file](https://raw.githubusercontent.com/pattonsgirl/SU2021-CS2900/main/markdown-demo.md)
- [Basic Writing and Formatting Syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)