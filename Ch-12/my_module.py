def myfun():
    print("Hello World!")

if __name__ == "__main__":
    myfun() 
# This will only run if the module is executed directly
print(__name__)  # This will print "__main__" if run directly, or "my_module" if imported
