
# This program is to test the Appointment class

def demo():
    import argparse
    import textwrap
    from P1024 import Appointment, Onetime,Daily,Monthly


    parser = argparse.ArgumentParser(prog='My test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                        An Appointment Program
                                    ----------------------------------------------------
                                    A simulated superclass Appointment  with subclasses of Oneime, Daily, Monthly
                                
                                    
                                    Methods:
                                    1) getDescription : Gets the description of the appointment
                                    @return the description

                                    2) getDate : Gets the date of the appointment.
                                    @return the date                                                         
                                                                 
                                    3) occursOn: Method that define the appointment occurs on specific date
                                    @return True/False/Day
                                    
                                    4) save : a method to append appointment in a file
                                    @return save the content of appointment
                                                                
                                    5) load : Method that load the appointment                   
                                    @return the content of appointment  
                                    
                                    6) __repr__ : Method that return a string representation                      
                                    @return string representation from subclasses
                                    
                                    7) add_appointment : Define a function to add appointments to a list 
                                     @parameter: appointments, appt_type, description, date
                                    @return Appointment: The newly created appointment object if the type is known
                                    
                                    8) get_date_input : Define a function to get date input from user
                                       @return  A string representing the date in "yyyy-mm-dd"
                                    
                                    9) save_appointments : Define a function to save appointment into a specicfile(txt)
                                     @parameter: appointments, appt_type, description, date
                                    @return the file name and content
                                    
                                    10) load_appointments_from_file : Define a function to load appointments from saved file
                                     @parameter: filename (str)
                                    @return load the appointments
                                    
                                    
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                        Usage
                                    --------------------------------------
                                    a =Appointment("See the doctor","2012-12-21")
                                    a.getDescription() get decription
                                    a.getDate() #get date
                                    #check appointment occurs in specific date
                                    
                                    o.occursOn ()# one time
                                    d.occursOn() # daily
                                    m.occursOn()# monthly
                                    test_appointment.save() #save file
                                    ...                                                                                                                                    
                                    ''')
                                    )
    
    parser.add_argument('--run_demo',action='store_true',help='Runs this demo')

    args = parser.parse_args()

    if args.run_demo:
    
        a =Appointment("See the doctor","2012-12-21")
        a.getDescription()
        a.getDate()
        print(a.getDate()) #expected to print out the date
        print(a.getDescription()) #expected to print out the description
        
        o = Onetime("See the doctor","2012-12-21")
        print(o.occursOn(2012,12,2)) #Expected to print out False
        
        d= Daily("See the doctor","2012-12-21") #Expected to print out True
        print(d.occursOn(2012,12,2))

        m= Monthly("See the doctor","2012-12-21") #Expected to print out True
        print(m.occursOn(2012,12,21))
              
        test_appointment = Appointment("Test Meeting", "2023-11-09")
        test_filename = "test_appointments.txt"
        test_appointment.save(test_filename)
        print("The save method works correctly.") #expected to print out this
        
    
        
if __name__ == '__main__':
    demo()










