# This program is to test the Message class from excercise Business P9.24

def demo():
    import argparse
    import textwrap
    from P9_24 import Message


    parser = argparse.ArgumentParser(prog='My test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                        An email Message
                                    ----------------------------------------------------
                                    A simulated class that models an email message which has a recipient,
                                    a sender and a message text.
                                    
                                    Methods:
                                    1) getSender : Gets the name of the sender.
                                    @return the sender name

                                    2) getRecipient : Gets the name of the recipient.
                                    @return the recipient name                                                         
                                                                 
                                    3) addMessage : Append a line of text to the message body.
                                    @param message the message text
                                    
                                    4) toString : a method to make the message into one long string 
                                    @return like:"From: Harry Morgan\nTo: Rudolf Reindeer\n . . ."
                                                                 
                                    5) log_messages : a method automatically invoked after a message is appended.                         
                                    @return: _no_messages and append _log using the sender,
                                    the recipient and the message body.                                                                                                                                                                                                                   
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                        Usage
                                    --------------------------------------
                                    sender = " "    # the sender name 
                                    recipient = " " # the recipient name
                                    message = Message (sender, recipient) # Get the sender and recipient name
                                    message.addMessage("Content of message") # Append a line of text to the message body.
                                    message.toString() # a method to make the message into one long string
                                    message.log_message()  # a method i) increase _no_messages and append _log using the sender,
                                                           the recipient and the message body.
                                                                                                                                                                                
                                    ''')
                                    )
    
    parser.add_argument('--run_demo',action='store_true',help='Runs this demo')

    args = parser.parse_args()

    if args.run_demo:
        sender = "Rafael Nadal"
        recipient = "Roger Federer"
        message  = Message(sender,recipient)
        message.addMessage("Hello Roger, ")
        message.addMessage("How are you? I hope you are doing well. I would like to invite you to join one of the tennis match for charitable purpose.")
        message.addMessage("Are you available on 20th November? Please check and let me know.")
        message.addMessage("I am looking forward to hearing from you.")
        message.addMessage("Bests Regards,")
        message.addMessage("Rafael")
        message.log_messages()
       

        sender = "Maria"
        recipient = "Max"
        message1  = Message(sender,recipient)
        message1.addMessage("Hello Max, ")
        message1.addMessage("How are you? I hope you are doing well.")
        message1.addMessage("Winter is comming.")
        message1.addMessage("Bests Regards,")
        message1.addMessage("Maria")
        message1.log_messages()

        sender = "Taylor"
        recipient = "Selena"
        message2  = Message(sender,recipient)
        message2.addMessage("Hello Selena, ")
        message2.addMessage("How are you? I hope you are doing well.")
        message2.addMessage("Happy Birthday.")
        message2.addMessage("Bests Regards,")
        message2.addMessage("Taylor")
        message2.log_messages()

        # Print the message log and total number of messages sent
        print("Message Log:", Message._log)
        print("Total Messages Sent:", Message._no_messages)

        
if __name__ == '__main__':
    demo()

