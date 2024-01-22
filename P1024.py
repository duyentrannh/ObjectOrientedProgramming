# This model define a class that models Appointment's functions

from datetime import datetime

class Appointment:
    
    def __init__(self,description,date):
        """
            Construct a class that represent the description and date
            Parameters: 
                description(str): The description of the appointment
                date (datetime.date) :The date of the appointment(YYYY-MM--DD)
        """
        self._description = description
        self._date = datetime.strptime(date, "%Y-%m-%d").date()
           
    def getDescription(self):
        """
            Define a getDescription method
            that return the description of the appointment
        """
        return self._description
    
    
    def getDate(self):
        """
            Define a getDate method 
            that return the date of the appointment
        """
        return self._date
    
    def occursOn(self, year, month, day):
        """
            Define a occursOn method to check if the appointment is occurs on a specific date.
            This method is abstract method and intended to override by subclasses.
            Parameters:
                year: the year of appointment to check
                month: the month of the appointment to check
                day: the day of the appointment to check
        """
        raise NotImplementedError
        
    def save(self, filename):
        """
            Define a save method to appends string representation of the appointment to afile
            Parameter:
                filename : the name of the file to which the appointment will be appended
                'a' is for append mode
            Then write the string representation to the file
        """
        with open(filename, 'a') as file:
            file.write(self.__repr__() + '\n')
            
    def load(self, description, date):
        """
            Define load method to load an appointment from a description and date.
        
            Parameters:
                description (str): Description of the appointment.
                date : The date of the appointment in "YYYY-MM-DD" format.
        """
        return
    

class Onetime(Appointment):
    """
    Create a subclass represents a one-time appointment that inherits from the Appointment class.
    
    This appointment occurs only once on a specified date.
    """
    
    def __init__(self,description,date):
        """
        Construct a new instance of a one-time appointment by calling the constructor of superclass
        
        Parameters:
            description (str): Description of the one-time appointment.
            date : The date of the appointment in "YYYY-MM-DD" format.
        """
        super().__init__(description, date)
        
        
    def occursOn(self, year, month, day):
        """
        Checks if the one-time appointment occurs on a specified date.
        This method is override from superclass
        Parameters:
            year (int): The year of the date to check.
            month (int): The month of the date to check.
            day (int): The day of the date to check.
            
        Returns:
            bool: True if the appointment occurs on the given date, otherwise False.
        """
        super().occursOn(year, month, day)
        if self._date == datetime(year, month, day).date():
            return True
        else:
            return False
        
    def __repr__(self):
        """
        Returns a string representation of the one-time appointment, including the date and description.
        
        Returns:
            str: A string stating when the one-time appointment is and what it is for.
        """
        return 'One-time appointment is on {}, and the appointment is for {}'.format(
            self._date.strftime("%Y-%m-%d"),
            self._description
        )
    
class Daily(Appointment):
    """
    Represents a daily appointment that inherits from the Appointment class.
    
    This appointment is considered to occur every day starting from a specified date.
    """
    def __init__(self,description,date):
        """
        Construct a new instance of a daily appointment by calling the 
        initializer of the superclass Appointment to set up the description 
        and starting date of the daily appointment.
        
        Parameters:
            description (str): Description of the daily appointment.
            date (str): The starting date of the appointment in "YYYY-MM-DD" format.
        """
        super().__init__(description, date)
        
        
    def occursOn(self, year, month, day):
        """
        Checks if the daily appointment occurs on a specified date.
        This method is override from superclass
        
        Parameters:
            year (int): The year of the date to check.
            month (int): The month of the date to check.
            day (int): The day of the date to check.
            
        Returns:
            bool: Always returns True since the appointment is daily.
        """
        super().occursOn(year, month, day)
        return True
    
    def __repr__(self):
        """
        Returns a string representation of the daily appointment, including the date and description.
        
        Returns:
            str: A string stating when the daily appointment is and what it is for.
        """
        return 'Daily appointment is on {}, and the appointment is for {}'.format(
            self._date.strftime("%Y-%m-%d"),
            self._description
        )
    
class Monthly(Appointment):
    """
    Represents a monthly appointment that inherits from the Appointment class.
    
    This appointment is considered to occur once a month on a specified date.
    """
    
    def __init__(self,description,date):
        """
        Construct a new instance of a daily appointment by calling the 
        initializer of the superclass Appointment to set up the description 
        and starting date of the daily appointment.
        
        Parameters:
            description (str): Description of the daily appointment.
            date (str): The starting date of the appointment in "YYYY-MM-DD" format.
        """
        super().__init__(description, date)
    

        
    def occursOn(self, year, month, day):
        """
        Checks if the monthly appointment occurs on a specified date.
        The appointment occurs if the day matches the day of the initial date set.
        
        Parameters:
            year (int): The year of the date to check (unused).
            month (int): The month of the date to check (unused).
            day (int): The day of the date to check.
            
        Returns:
            bool: True if the appointment occurs on the given day of the month, otherwise False.
        """
        super().occursOn(year, month, day)
        if self._date.day == day:
            return True
        else:
            return False
        
    def __repr__(self):
        """
        Returns a string representation of the monthly appointment, including the date
        and description.
        
        Returns:
            str: A string stating when the monthly appointment was set and what it is for.
        """
        return 'Monthly appointment is on {}, and the appointment is for {}'.format(
            self._date.strftime("%Y-%m-%d"),
            self._description
          )
        
def add_appointment(appointments, appt_type, description, date):
    """
    Adds a new appointment of a specified type to a list of appointments.

    Parameters:
        appointments (list): The list of appointments to which the new appointment will be added.
        appt_type (str): The type of appointment to create ('onetime', 'daily', or 'monthly').
        description (str): The description of the new appointment.
        date (str): The date when the appointment is scheduled, in "YYYY-MM-DD" format.

    Returns:
        Appointment: The newly created appointment object if the type is known, otherwise None.

    This function creates a new appointment based on the specified type. It constructs an appointment
    using the appropriate class (Onetime, Daily, or Monthly) and adds the new appointment object to the 
    provided list. If an unknown appointment type is given, it prints an error message and returns None.
    """
    appt_type = appt_type.lower().strip()
    if appt_type == "onetime":
        appointment = Onetime(description, date)
        
    elif appt_type == "daily":
        appointment = Daily(description, date)
        
    elif appt_type == "monthly":
        appointment = Monthly(description, date)
    else:
        print("Unknown appointment type")
        return None
    
    appointments.append(appointment)
    return appointment

def get_date_input():
    """
    Prompts the user to enter a date in the "yyyy-mm-dd" format and validates it.

    The function repeatedly prompts the user until a valid date format is entered.
    If an invalid format is entered, the user is informed and asked to try again.

    Returns:
        str: A string representing the date in "yyyy-mm-dd" format that has been validated.

    """
    date_input = input("Enter the date for the appointment (yyyy-mm-dd): ")
    try:
        
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        print("That's not a valid date format. Please try again.")
        return get_date_input()
    
        
def save_appointments(appointments, filename):
    """
    Reads the existing appointments from a file and stores them in a set.
    If the file does not exist, it passes silently and will create the file when saving.

    Parameters:
        appointments (list): A list of Appointment objects to save to the file.
        filename (str): The name of the file where appointments are saved.

    If the specified file does not exist, the function will handle the FileNotFoundError
    by ignoring it, under the assumption that the file will be created later when writing
    the new appointments.
    """
    existing_appointments = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                existing_appointments.add(line.strip())
    except FileNotFoundError:
        pass

    with open(filename, 'a') as file:
        """
        Appends new appointments to the file.

        This function iterates over the list of appointments and appends only the ones
        that are not already present in the file. It ensures that there are no duplicate
        appointments saved, maintaining the uniqueness of each appointment.

        Each appointment's string representation is checked against the set of existing 
        appointments. If it's not in the set, it is written to the file and then added 
        to the set to keep track of what has been saved.
        """
        for appointment in appointments:
            appointment_repr = appointment.__repr__()
            if appointment_repr not in existing_appointments:
                file.write(appointment_repr + '\n')
                existing_appointments.add(appointment_repr)
        
def load_appointments_from_file(filename):
    """
    Loads appointments from a given file into a list of Appointment objects.

    The function reads the file line by line and reconstructs Appointment objects
    based on the information contained in each line. It supports 'onetime', 'daily',
    and 'monthly' appointments. If an unknown format is encountered, it will print
    an error message and skip that line.

    Parameters:
        filename (str): The name of the file from which to load appointments.

    Returns:
        list: A list of Appointment objects loaded from the file.

    Each line in the file should have a specific format that includes the type of
    appointment, the date, and the description. The function parses this information
    and creates an instance of the corresponding subclass of Appointment.
    """
    loaded_appointments = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            # Extract the date and description based on the known format
            if 'One-time appointment is on' in line:
                appt_type = 'onetime'
                parts = line.replace('One-time appointment is on ', '').split(', and the appointment is for ')
            elif 'Daily appointment is on' in line:
                appt_type = 'daily'
                parts = line.replace('Daily appointment is on ', '').split(', and the appointment is for ')
            elif 'Monthly appointment is on' in line:
                appt_type = 'monthly'
                parts = line.replace('Monthly appointment is on ', '').split(', and the appointment is for ')
            else:
                print(f"Unknown appointment type in line: {line}")
                continue

            if len(parts) == 2:
                date, description = parts
                date = date.strip()

                # Create the appropriate appointment object
                if appt_type.lower() == 'onetime':
                    appointment = Onetime(description, date)
                    
                elif appt_type.lower() == 'daily':
                    appointment = Daily(description, date)
                    
                elif appt_type.lower() == 'monthly':
                    appointment = Monthly(description, date)
                else:
                    continue  
                
                loaded_appointments.append(appointment)

    return loaded_appointments

# Main program to take input from users
appointments = [] #List to store the appointments objects
done = False
while not done:
    #Get user action
    action = input("Choose an action - Add (A), Save (S), Load (L), Quit (Q): ").upper()
    if action == 'A': #Add new appointment
        description = input("Enter the description of the appointment: ")
        date = get_date_input() #Get the date for appointment
        appt_type = input("Enter the type of the appointment (Onetime, Daily, Monthly): ").lower()
        if appt_type == 'monthly': #montly case where the day is needed
            day = int(input("Enter the day of the month for the monthly appointment: "))
            appointment = add_appointment(appointments, appt_type, description, date) 
        else:
            appointment = add_appointment(appointments, appt_type, description, date)
            
    elif action == 'S':#Save current appointment to the file
        filename = input("Enter the filename to save appointments: ")
        save_appointments(appointments, filename)
        
    elif action == 'L': #Load appointments from the file 
        filename = input("Enter the filename from which to load appointments: ")
        loaded = load_appointments_from_file(filename)
        print(f"Loaded {len(loaded)} appointments.") #Print out the loaded appointments
        appointments.extend(loaded)
        for appt in loaded:
            print(appt)
        
    elif action == 'Q':
        print("Exiting program.")
        done = True
    else:
        print("Invalid action.")

