# virtual environment 
# a virtual environment is a tool used to isolate specific python environment on a single machine, allowing you to work
# on multiple projects with different dependencies and package without confilict. this can be especially useful when working
# on projects that have confilicting package version that are not compatible with each other 


# to create a virtual environment in python, you can use the venv module that come with python 

# create a virtual Environment
# python3 -m venv myenv  ----> this code run only mac and linux

# Activate the virtual Environment (linux/macos)
# source myenv/bin/activate

# Activate the virtual Environment (windows)
# myenv/scripts/activate.bat


# once the virtual Environment is activated , any package that you install using pip will be installed in the virtual Environment 
# rather than in the global python Environment . thios alllow you to have a sperate set of package foe each projects
# without affecting the packages installed in the global environment 


# deactivate the virtaul Environment
# using deactivate 


# the 'requirement.txt' File
# In addition to creating and activating a virtual Environment , it can be useful to create a requirement.txt file that lists
# he package and their version that your project depends on . this file can be used to easily install all the required
# package in a new environment 

# to create a requirement.txt file , you can use the pip freeze command,which output a list of installed packages and their version

# output the list of installed packages and their versions to a File 
# pip freeze > requirement.txt 


# installed the packages listed in the requirement.txt file 
# pip install -r requirement.txt