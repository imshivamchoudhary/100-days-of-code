# if__name__=="__main__" in python
# this is if__name__=="__main__" idiom is a common pattern used in python script to determine whether
# the script is being run directly or being imported as  a module into another script

# In the python __name__ variable is a built-in variable that is automatically set to the name of the current Module 
# When a python script is run directly,,the __name__variable is set to the string __main__ when the script is imported 
# as a module into another script,the __name__ variable is set to the name of the module
import ishivam
ishivam.welcome()

# In this example , the main function contain the code that should be run when the script is run directly.
# The if statement at the bottom check whether the __name__ variable is equal to __main__. If it is the main function is called. 
