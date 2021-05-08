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
    - For Linux: 
        - `sudo apt install git-all`
        - [Other install instructions](https://git-scm.com/download/linux)
    - For Mac: 
        - Type `git` on command line.  Should prompt to install
        - [Other install instructions](https://git-scm.com/download/mac)

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