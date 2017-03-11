def add(a,b):
    print "Adding %r and %r"%(a,b)
    return a+b

Age = add(30,5)

print "His age is %r" %Age

print "Now please enter as many apples you have each day and your age"
k=int(raw_input(">>>"))
l=int(raw_input(">>>"))
Pred_age = add(k,l)

print "Your age can be predicted as %r"% Pred_age
