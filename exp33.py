i = 0
numbers = []

while i<6:
    print "At the tope i is %d"%i
    numbers.append(i)

    i += 1
#check how a list (in this case numbers) appear without havaving to specify it's location and nothing like %r etc.
    print "Numbers now: ",numbers
    print "At the bottom i is %d" %i

print "The numbers: "

#num is already defined in python? No, any word will do- like mosambi too
for mosambi in numbers:
    print mosambi
