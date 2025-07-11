ft_package
A simple Python package demonstrating package creation.
Installation
bashCopypip install .
Usage
pythonCopyfrom ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
License
MIT License