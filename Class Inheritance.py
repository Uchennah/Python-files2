class Parent:
    ParentAttr = 100
    def __init__(self):
        print('Calling Parent Constructor')
    def ParentMethod(self):
        print('Calling Parent Method')
    def setAttr(self, Attr):
        Parent.ParentAttr = Attr
    def getAttr(self):
        print('Parent Attribute: ' ,Parent.ParentAttr)

class Child(Parent):
    def __init__(self):
        print('Calling Child Constructor')
    def ChildMethod(self):
        print('Calling Child Method')

c = Child()
c.ChildMethod()
c.ParentMethod()
c.getAttr()
c.setAttr(200)
c.getAttr()
        
