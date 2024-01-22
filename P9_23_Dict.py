# This module defines and implement a class Country that store the name of the country,
# its population and its area. Then write a program that reads in a set of countries, and print 
# •    The country with the largest area.
# •    The country with the largest population.
# •    The country with the largest population density (people per square kilometer (or mile)).
# And develop these methods using the dictionary classes.

class Country:
    #Construct  a Country class that takes the name of country, population and area.
    #@param name the name of country
    #@param population the population of country
    #@param area the area of the country
    def __init__(self,name, population, area):
        self._name = name
        self._population = population
        self._area = area
    
    # Define method to get name of country.
    #@return the country name 
    def getName(self):
        return self._name
    
    # Define method to get population of country.
    #@return the country population 
    def getPopulation(self):
        return self._population
    
    # Define method to get area of country.
    #@return the country area 
    def getArea(self):
        return self._area
    
    # Define method to get the population density of country.
    #@return the country population density 
    def getPopulationdensity(self):
        return int(self._population/self._area)
    
    #Define a method to get information in one long string
    #@return related information about the country
    def toString(self):
        countryinfo = "Name: {}, Population: {}, Area: {},Population density: {} ".format(self.getName(),self.getPopulation(),self.getArea(),self.getPopulationdensity()) 
        return countryinfo

# Using dictionary class

class CountryDict:
    #Construct an empty list to store contry dictionary
    def __init__(self):
        self._countries = []

    # Define a method to create dictionary of a country
    def addCountry(self, name, population, area):
        country = {
            "name": name,
            "population": population,
            "area": area
        }
        self._countries.append(country) # then add the country dictionary to the list
    
    #Define method to get the largest area
    #Assume the first country has the largest area initially,then compare each country's area with the current largest, then
    #@return the country with largest area
    def country_with_largest_area(self):
        largest = self._countries[0]
        for country in self._countries:
            if country["area"] > largest["area"]:
                largest = country
        return self.toString(largest)

    #Define method to get the largest population
    #Assume the first country has the largest population initially,then compare each country's population with the current largest, then
    #@return the country with largest population
    def country_with_largest_population(self):
        largest = self._countries[0]
        for country in self._countries:
            if country["population"] > largest["population"]:
                largest = country
        return self.toString(largest)
    
    #Define method to get the largest population density
    #Assume the first country has the largest population density initially,then compare each country's population density with the current largest, then
    #@return the country with largest population density 
    def country_with_largest_population_density(self):
        largest = self._countries[0]
        for country in self._countries:
            if country["population"]/country["area"] > largest["population"]/largest["area"]:
                largest = country
        return self.toString(largest)
    
    def toString(self,country):
        # Convert the country dictionary details to a formatted string
        countryinfo = "Name: {}, Population: {}, Area: {}, Population density: {}".format(
            country["name"], country["population"], country["area"], int(country["population"]/country["area"])) 
        return countryinfo


    # Gets the user inputs, with valid values
    #@return the values that user supplied

    def getInput(self):
        valid_name = False # Get the country name input, it must be alphabet letter
        while not valid_name:
            name = input("Enter country name: ")
            if name.isalpha():
                valid_name = True
            else:
                print("Please enter a valid country name (no numbers or special characters).") # if not correct value, print this message to users
        
        population = int(input("Enter country population: ")) #get population by integer value
        area = float(input("Enter country area: ")) # get the area by the float value
        self.addCountry(name, population, area)

        
#Define this start program when want to start the unput process
def start_program():
    country_dict = CountryDict()       
    num_countries = int(input("How many countries do you want to add? "))

    for _ in range(num_countries):
        country_dict.getInput()
    #Print out the results
    print("Country with the largest area:", country_dict.country_with_largest_area())
    print("Country with the largest population:", country_dict.country_with_largest_population())
    print("Country with the largest population density:", country_dict.country_with_largest_population_density())

if __name__ == "__main__":
    start_program()