

# This program is to test the Animal hierarchy

def demo():
    import argparse
    import textwrap
    from animal import Animal, Cat, Dog, BigDog


    parser = argparse.ArgumentParser(prog='My test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                        An animal hierarchy
                                    ----------------------------------------------------
                                    A simulated superclass  Animal with subclasses of Cat, Dog, BigDog
                                
                                    
                                    Methods:
                                    1) getName : Gets the name of the animal
                                    @return the animal name

                                    2) getAge : Gets the age of the animal.
                                    @return the animal age                                                         
                                                                 
                                    3) eat: Method that print out the animal is eating
                                    @return the name of animal is eating
                                    
                                    4) getDescription : a method to get description of the animal 
                                    @return the name and age of the animal
                                                                
                                    5) run : Method that print out how the animal run                       
                                    @return statemnent of how the animal run  
                                    
                                    6) swim : Method that print out how the animal swim                       
                                    @return statemnent of how the animal swim
                                    
                                    7) greets : Method that print out how the animal greets                     
                                    @return the greeting from the animal
                                    
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                        Usage
                                    --------------------------------------
                                    my_cat = Cat("") the cat name and age
                                    my_dog = Dog ("") the dog name and age
                                    my_big_dog = BigDog("") the big dog name and age
                                    
                                    my_cat.getName() get the name of the cat
                                    my_cat.getAge() get the age of the cat
                                    my_cat.eat() Get name of the cat is eating 
                                    my_cat.greets() get the greeting of the cat
                                    my_cat.run() print out how the cat run
                                    my_cat.getDescription() get both the name and age of the cat
                                    
                                    my_dog.getName() get the name of the dog
                                    my_dog.getAge() get the age of the dog
                                    my_dog.eat() Get name of the dog is eating 
                                    my_dog.greets() get the greeting of the dog
                                    my_dog.run() print out how the dog run
                                    my_dog.getDescription() get both the name and age of the dog
                                    
                                    my_big_dog.getName() get the name of the cat
                                    my_big_dog.getAge() get the age of the cat
                                    my_big_dog.eat() Get name of the cat is eating 
                                    my_big_dog.greets() get the greeting of the cat
                                    my_big_dog.swim() print out how the big dog swim 
                                    my_big_dog.getDescription() get both the name and age of the big dog
                                                                                                                                                                                
                                    ''')
                                    )
    

    args = parser.parse_args()

    if args.run_demo:
        # Instantiate objects from the subclasses
        my_cat = Cat(name="Sera", age=3)
        my_dog = Dog(name="Ødipus", age=5)
        my_big_dog = BigDog(name="Passop", age=7)

        # Test the methods for a cat
        print(my_cat.getName())         # Should print "Sera"
        print(my_cat.getAge())          # Should print 3
        print(my_cat.eat())             # Should print "Sera is eating."
        print(my_cat.getDescription())  # Should print "This is a Sera. And it is 3 years old."
        print(my_cat.greets())          # Should print "meow"
        print(my_cat.run())             # Should print "The cat runs very fast"
        print(my_dog.getName())         # Should print "Ødipus"
        print(my_dog.getAge())          # Should print 5
        print(my_dog.eat())             # Should print "Ødipus is eating."
        print(my_dog.getDescription())  # Should print "This is a Ødipus. And it is 5 years old."
        print(my_dog.greets())          # Should print "woof"
        print(my_dog.run())              # Should print "The dog runs faster than the cat"
        print(my_big_dog.getName())         # Should print "Passop"
        print(my_big_dog.getAge())          # Should print 7
        print(my_big_dog.eat())             # Should print "Passop is eating."
        print(my_big_dog.getDescription())  # Should print "This is a Passop. And it is 7 years old."
        print(my_big_dog.greets())          # Should print "woof" followed by "woooof"
        print(my_big_dog.swim())            # Should print "A big dog swims faster than a small dog."

        
if __name__ == '__main__':
    demo()
