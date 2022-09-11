import os


dir = os.path.abspath(os.path.dirname(__file__))
print(dir)
file = os.path.join(dir, "file.txt")
print(file)
print(os.name)
print(f"{os.getcwd()}\\file.txt")
print(os.path.dirname(__file__))
print(__file__)