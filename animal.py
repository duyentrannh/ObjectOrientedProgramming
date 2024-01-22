# This model define a class that models the hierarchy of animals


class Animal: 
    """
        Create a superclass Animal for different types of animals
    """

    def __init__(self,name,age):
        """
            Construct an Animal class with a name and an age
            Parameters:
            name(str) : The name of animal
            age(int)  : The age of animal 
        """
        self._name = name
        self._age = age

    def greets(self):
        """
            Define this abstract method but there is no implementation
            If the user of the class attempts to invoke, the exception will be raised
            to flag the missing implementation. Hence we need to create subclasses with the
            method to override this abstract "greets".
        """
        raise NotImplementedError
    
    def getName(self):
        """
            Define method getName to get name of the animal
            return the name of the animal
        """
        return self._name
    
    def getAge(self):
        """
            Define method getAge to get age of the animal
            return the age of animal
        """
        return self._age
    
    def eat(self):
        """
            Define method eat and print statement that {the animal} is eating.
        """
        return "{} is eating.".format(self._name)
    
    def getDescription(self):
        """
            Get the description of the animal
            return a string containing the description
        """
        return "This is a {}. And it is {} years old.".format(self._name, self._age)
    
class Cat(Animal):
    """
        Subclass of Animal that represent a Cat
    """
    def __init__(self,name,age):
             
        """
            Call superclass constructor to define its instance variables
        """
        super().__init__(name,age)

    def greets(self):
        """
        Override Animal.greets() and print out the greet
        """
        print("meow")

    def run(self):
        """
        Define a method run and print out the statement
        """
        print("The cat runs very fast")
        
class Dog(Animal):

    """
        Subclass of Animal that represent a Dog
    """

    def __init__(self,name,age):
        """
            Call superclass constructor to define its instance variables
        """
        super().__init__(name,age)

    def greets(self):
        """
        Override Animal.greets() and print out the greet
        """
        print("woof")
    
    def run(self):
        """
        Define a method run and print out the statement
        """
        print("The dog runs faster than the cat")

class BigDog(Dog):
    """
        Subclass of Dog that represent a BigDog
    """

    def __init__(self,name,age):
        """
            Call superclass constructor to define its instance variables
        """
        super().__init__(name,age)

    def greets(self):
        
        """
        Override Dog.greets() and print out the greet
        This will print out"woof" ( the greeting from Dog class)
        And add additional beahvior which is extend from Dog class("woooof")
        
        """
        super().greets()
        
        print("woooof")
    
    def swim(self):
        """
            Define a method swim and print out the statemenr
        """
        print("A big dog swims faster than a small dog.")





