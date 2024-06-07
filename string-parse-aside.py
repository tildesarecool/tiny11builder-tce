import subprocess, os

sample_input = """Index : 1
Name : Windows 11 Home
Description : Windows 11 Home
Size : 18,638,210,474 bytes

Index : 2
Name : Windows 11 Home N
Description : Windows 11 Home N
Size : 17,934,598,356 bytes"""

first_index = sample_input.split("\n\n")

#print(sample_input)
print(first_index[0])
print(f"type of varialbe first index is is {type(first_index)}")

entry_one = first_index[0]

print(f"before split line, entry one is \n{entry_one}")

entry_one = entry_one.splitlines()

entry_one.pop()
entry_one[0] = entry_one[0].replace("Index", "Enter")

print(f"after split line, entry one is \n{entry_one[0]}")

