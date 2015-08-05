# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
# Use words.txt as the file name
fname = raw_input('Enter file name: ')
#I added line 8 so that if a file name is entered and there is any whitespace before or after the file name it gets
# removed to help avoid errors.
name = fname.strip()
#Could also add a try/except before line 10 to handle any errors due to invalid file names.
fh = open(name)
for line in fh:
    #Timming white space at end of line (new lines) since print will already add a new line.
    #Also converting to Uppercase.
    line = line.rstrip().upper()
    #Can convert to uppercase on separate line as show on line 16 and leave off the .upper() on line 14.
    #line = line.upper()
    print line