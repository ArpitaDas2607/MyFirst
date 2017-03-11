def Cheese_and_crackers(Cheese_count,Crackers_count):
    print "we have %r cheese!" % Cheese_count
    print "we have %r crackers" % Crackers_count
    print "Man, that's enough for a party!!"
    print "Go, get a blanket\n\n\n"



print "We can just give the fuction numbers directly"
Cheese_and_crackers(20,30)



print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 20

Cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can aldo do some math inside the function arguments"
Cheese_and_crackers(10+20,5+55)

print "you can also use varablies in the math function within"
Cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+200)
