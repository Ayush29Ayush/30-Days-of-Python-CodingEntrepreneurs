def some_function():
    print("\n","This function can be used as a module","\n")

if __name__ == "__main__":
    print("This code will only run if the script is executed directly.")

some_function()


# In this example, if you import my_module into another Python script, some_function() can be used, but the code under if __name__ == "__main__": will not run. However, if you run my_module.py as a standalone script, both the function and the code under if __name__ == "__main__": will execute.

# This allows you to create modules that can be used in various contexts, and you can include test code or examples within the module that won't run when the module is imported by other scripts.