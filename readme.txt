helloGEMSEC.

This is a tutorial repository intended to teach the very basics of working in a Python development environment: Git, Python, Virtualenvs, and Packages. (We'll be using Numpy as an example.)

Please undertake these steps:

1. Get Git
Open a terminal (or bash, cmd, command-prompt, etc.). Type:
git

If nothing happens, download Git from:
https://git-scm.com/



2. Get Python
Open a terminal. Type:
> python --version
or
> py

If nothing happens, download Python 3 from here:
https://www.python.org/

IMPORTANT: It will be useful to have your python directory on PATH. When installing Python, select the option to add Python to Path. (If you have multiple versions of Python installed and know what you are doing, do this at your discretion.) If you are unfamiliar with your system path, take a moment to Google "What is system path?"



3. Go get the helloGEMSEC repository:
Open a terminal. Use the 'cd' command to navigate to a directory where you keep projects:
Type:
> git clone "https://github.com/onakanob/helloGEMSEC"

Now cd into the directory that GIT just created:

> cd helloGEMSEC

Let's make sure we're in the right place. Ask the terminal to display the current directory:

> ls

You should see a readme.txt, a bunch of hello____.py files, and some additional directories.



4. Install a Python package:
Numpy is a standard matrix computing package that is generally good to have!
In a terminal:
> pip install --upgrade numpy

Other packages that we will likely use include:
scipy, matplotlib, pandas, jupyter

To install them all
> pip install --upgrade numpy scipy pandas jupyter matplotlib



5. Say hello:
Run the sample Python code snippets by issuing these terminal commands:
> python helloPython.py
> python helloNumpy.py
> python helloFunction.py
> python helloClass.py



6. Now the easy way - all this can happen in the cloud:

Go to https://notebooks.azure.com/onakanob/libraries/hello

Clone this library into your own account.

Everything works on Microsoft's computers - magic!




7. [OPTIONAL] Get the virtualenvs library. You don't always have to do this if you don't want to, but today we're doing things the hard way.
In a terminal:
> pip3 install --upgrade virtualenv

Then, if you are on Windows:
> pip3 install --upgrade virtualenvwrapper-win

Or, if you are on Mac or Linux:
> pip3 install --upgrade virtualenvwrapper


8. [OPTIONAL] Set up a virtual environment:
This is an isolated Python playground where we can install packages and mess with the environment for one specific project.
In a terminal, use the "CD" command to navigate to a directory where you would like to make a Python program:
This command will create a new virtual environment called helloGEMSEC with its own Python installation and packages:
> mkvirtualenv helloGEMSEC

This will make your new project remember this directory as its home directory:
> setprojectdir .

This will exit the virtual environment:
> deactivate

And this will bring back the virtual environment:
> workon helloGEMSEC
