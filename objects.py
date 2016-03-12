class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."

myobjectx = MyClass()

print myobjectx.variable

myobjecty = MyClass()
myobjecty.variable = "yackity"
print myobjecty.variable   # This would print "yackity".

myobjectx.function()

# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1, car2 = Vehicle(), Vehicle()
car1.name, car1.color, car1.kind, car1.value= "Fer", "red", "convertible", 60000.00
car2.name, car2.color, car2.kind, car2.value= "Jump", "blue", "van", 10000.00
# test code
print car1.description()
print car2.description()
