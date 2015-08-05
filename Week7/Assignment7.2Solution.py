#Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#
#X-DSPAM-Confidence:    0.8475
#
#Count these lines and extract the floating point values from each of the lines and compute the average of those
#values and produce an output as shown below.
#Average spam confidence: 0.750718518519
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below
#enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
#I added line 15 so that if a file name is entered and there is any whitespace before or after the file name it gets
# removed to help avoid errors.
name = fname.strip()
#Could also add a try/except before line 10 to handle any errors due to invalid file names.
fh = open(name)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        #wOULD BE BETTER TO USE REGEX HERE IN CASE WHITESPACE TO NUMBER IS DIFFERENT AND FOR SCALABILITY
        continue
    position = line.find(":")
    line = float(line[position+1:])
    #COUNT = COUNT +1 IS SAME AS COUNT += 1
    count = count + 1
    total = total + line
    average = total/count
    #print line, count, total, average

print "Average spam confidence: ", average