print(f"You just imported {__name__}!")

def function1_from_module1():
	print("Hello from package1!")

def get_last(myList):
    return myList[-1]

if __name__ == "__main__":

	print("====================")
	print("This won't be printed, unless run directly.")
	print(f"If we run it directly, the name is going to be {__name__}")
	print("====================")
	