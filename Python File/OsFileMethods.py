# Python Has A 'os' Package which We Have To Import And Then We Can Use All The Methods Of That Class.
import os

# renaming File Name 
# os.rename("MyFamilyInfo.txt","FamilyInfo.txt")

# New Directory
# os.mkdir("python")

# Change Name Of Current Directory
os.chdir("new")
# os.mkdir("python")

# Getting Current Directory
print(os.getcwd())

# Remove The Directory
os.rmdir("python")