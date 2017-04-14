#exp 44

class Parent(object):

    def implicit(self):
        print "This is the parent"

class Child(Parent):
    def implicit(self):
        print "This is the Child"
        super(Child,self).implicit()
        print "This is altered child"

dad = Parent()
kid = Child()

dad.implicit()
kid.implicit()
