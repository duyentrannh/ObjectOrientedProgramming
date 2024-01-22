# This program is to test the Country class from excercise Business P9.23

#Import the modules
import argparse
import textwrap
from P9_23_Dict import CountryDict

def main():
    parser = argparse.ArgumentParser(prog='My test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                        Country Information
                                    ------------------------------------------------------------------------------
                                    A simulated class that models a country which has a name, population and area.
                                    In addition, using dictionary classes to get the largest area, population and density.
                                    
                                    Methods:
                                    class Country
                                    1) getName : Gets the name of the country.
                                    @return the country name

                                    2) getPopulation : Gets the population of the country
                                    @return the country population                                                        
                                                                 
                                    3) getArea : Gets the area of the country
                                    @return the country area
                                    
                                    4) getPopulationdensity : Gets the population density of the country
                                    @return the country population density (= population/area)
                                    
                                    5) toString : a method to make the country information into one long string 
                                    @return name, population, area, population density.
                                                                 
                                    class CountryDict : class uses methods to answer 3 questions

                                    1) addCountry : Add country to create a country dictionary
                                    @returnt the country dictionary

                                    2) country_with_largest_area : Get the countries area
                                    @returnt the country with largest area
                                    
                                    3) country_with_largest_population : Get the countries population
                                    @returnt the country with largest population
                                    
                                    4) country_with_largest_population density : Get the countries population density
                                    @returnt the country with largest population density 
                                
                                    5) getInput : Get inputs from user with valid format
                                    @return the value that user supplied                                                                                                                                                                                                                                                                                                
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                        Usage
                                    --------------------------------------
                                    country = Country()
                                    country.getName()  #get the country name 
                                    country.getPopulation()  #get the country population
                                    country.getArea()  #get the country area
                                    country.getPopulationdensity()  #get the country populationdensity                                                                            
                                    country.toString()  #Get country values: name, area, population, population density in one long string
                                                            
                                    country_dict = CountryDict()
                                    country_dict.addCountry('USA')   # add a country
                                    country_dict.country_with_largest_area() # Get country with largest area
                                    country_dict.country_with_largest_population() # Get country with largest population     
                                    country_dict.country_with_largest_populationdensity() # Get country with largest population density
                                    country_dict.getInput() # Get user input with valid values                                                                                                                                                                                                           
                                    ''')
                                    )
    
    parser.add_argument('--run_demo',action='store_true',help='Runs this demo')

    args = parser.parse_args()

    if args.run_demo:
        run_demo()

def run_demo():
    countrydict = CountryDict()
    countrydict.addCountry('USA',1000000,20.5)
    countrydict.addCountry('UK',800000,43.3)
    countrydict.addCountry('Norway',500000,13.3)
    print("Country with the largest area:" , countrydict.country_with_largest_area())

    print("Country with the largest population:",countrydict.country_with_largest_population())

    print("Country with the largest population density:",countrydict.country_with_largest_population_density())

        
if __name__ == '__main__':
    main()
