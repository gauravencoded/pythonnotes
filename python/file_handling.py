# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# you can specify if the file should be handled as binary or text mode
# "b" - Binary - Binary mode (e.g. images)
# "t" - Text - Default value. Text mode

# opening a file
f = open("demofile.txt")
print(f.read())
print(f.read(5))
print(f.readline())
f = open("demofile.txt", "rt")
for x in f:
  print(x)
  
  
appending to File

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()


import os
os.remove("demofile.txt")


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


os.rmdir("myfolder")