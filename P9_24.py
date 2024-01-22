# This module defines the Message class that models an email message which has a recipient,
# a sender and a message text. 

class Message:

    # Class variables to track the total number of message sent and save the message log.
    _no_messages = 0
    _log = {}

    # Construct a Message class that takes the sender and recipient, and no message_text.
    #@param sender the sender name 
    #@param recipient the recipient name
    #message_text with no value
    def __init__(self, sender,recipient):
        self._sender = sender
        self._recipient = recipient
        self._message_text = []

    # Define a method to get the sender name.
    # @return the sender name
    def getSender(self):
        return self._sender

    # Define a method to get the recipient name.
    # @return the recipient name
    def getRecipient(self):
        return self._recipient
    
    # Define a method to append a line of text to the message body
    #@param message the message content
    def addMessage(self,message):
        self._message_text.append(message)
    
    # Define a method to make the message into one long string
    # @return like : "From: Harry Morgan\nTo: Rudolf Reindeer\n . . ."
    def toString(self):
        theMessage = "From: {}\nTo: {}\n".format(self._sender,self._recipient) 
        theMessage += "\n".join(self._message_text)
        return theMessage
    
    #Define a method automatically invoked after a message is appended.
    def log_messages(self):
        Message._no_messages += 1  # Increment total message count

    # Create a new dictionary for the log entry
        log_entry = {self._recipient: "\n".join(self._message_text)}
        
    # Check if sender is in the log, create entry if not
        if self._sender not in Message._log:
            Message._log[self._sender] = {}

    # Append the log entry for the recipient under the sender
        Message._log[self._sender].update({self._recipient: "\n".join(self._message_text)})
        
