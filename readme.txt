helloGEMSEC.

This is a tutorial repository intended to teach the very basics of working in a Python development environment: Git, Python, Virtualenvs, and Packages. (We'll be using Numpy as an example.)

Please undertake these steps:

1. Get Git
In a terminal type:
git

If nothing happens, download Git from:
https://git-scm.com/

2. Get Python 3.x
In a terminal, type:
> python --version
or
> py -3

If nothing happens, download Python 3 from here:
https://www.python.org/

3. Get this repository:
In a terminal, go to a safe directory, and type:
git clone 'https://github.com/onakanob/helloGEMSEC'


4. Get the virtualenvs library. You don't always have to do this if you don't want to, but today we're doing things the hard way.
In a terminal:
> pip3 install --upgrade virtualenv
> pip3 install --upgrade virtualenvwrapper-win


5. Set up a virtual environment:
This is an isolated Python playground where we can install packages and mess with the environment for one specific project.
I'm asuming you're still in the directory where you cloned the project...
In a terminal:
> mkvirtualenv helloGEMSEC
> setprojectdir ./helloGEMSEC
> deactivate
> workon helloGEMSEC


6. Install a package in the virtual environment:
Numpy is a standard matrix computing package that is generally good to have!
In a terminal:
> pip3 install --upgrade numpy


7. Say hello:
Run the sample Python code by issuing these terminal commands:
> python helloPython.py
> python helloNumpy.py
> python helloFunction.py
> python helloClass.py



8. Now the easy way - all this can happen in the cloud:

Go to https://notebooks.azure.com/onakanob/libraries/hello

Everything works! Also, let's talk about tensorflow.
