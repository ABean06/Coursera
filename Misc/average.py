count = 0
total = 0
while True:
    inp = raw_input("Enter a number ")
    #Don't count here as it could be off if break

    #Handle Cases
    if inp == 'done' : break
    if len(inp) < 1 : break #Check for empty line

    #Do Work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue #done with iteration and goes back to the while bc do not want to run rest or will be innacurate
    count = count + 1
    total = total + num
    print num, total, count

print "Average = " , total/count


