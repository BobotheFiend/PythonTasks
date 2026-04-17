print("""
                __________________________  
                |                   3310 |
                |                        |
                |          NOKIA         |
                |________________________|
                |        Main Menu       |
                | 1.  Phone book         |
                | 2.  Messages           |
                | 3.  Chat               |
                | 4.  Call register      |
                | 5.  Tones              |
                | 6.  Settings           |
                | 7.  Call divert        |
                | 8.  Games              |
                | 9.  Calculator         |
                | 10. Reminders          |
                | 11. Clock              |
                | 12. Profiles           |
                | 13. SIM Service        |
                | 0.  Back to main menu  |
                |________________________|
                |                        |
                |          menu          | 
                |                        |
                | power           <  >   |
                |                        |
                |    1              3    |
                            2             
                |    4              6    |
                            5             
                |    7              9    |
                            8             
                |                        |
                            0             
                |________________________|  """
                                               )

menu = int(input("press a number to access Main MENU options: "))

match (menu):
    case 1:     
        print("""Phonebook"           |
             | 1.  Search             |
             | 2.  Service Nos.       |
             | 3.  Add name           |
             | 4.  Erase              |
             | 5.  Edit               |
             | 6.  Assign tone        |
             | 7.  Send b'card        |
             | 8.  Options            |
             | 9.  Speed dails        |
             | 10. Voice tags         |
             | 0.  Back to main menu""" ) 

        phonebook = int(input("Press a number from the option to access Phonebook menu: "))
        match (phonebook):
            case 1: print("Search")
            case 2: print("Service Nos.")
            case 3: print("Add name")
            case 4: print("Erase")
            case 5: print("Edit")
            case 6: print("Assign tone")
            case 7: print("Send b'card")
            case 8: 
                    print("Options",
                          "1. Type of view",
                          "2. Memory status",
                          "0. Back to Phonebook Menu",
                            "Press a number to from 0-2: ")
                    options = int(input("Press a number to access Options: "))
                    match (options):
                        case 1: print("Type of view")
                        case 2: print("Memory Status")
                        case _: print("invalid input")
            case 9: print("Speed dails")
            case 10: print("Voice tags")
            case _: print("Invalid input")     
    
    case 2: 
            print("Messages ")
            messages = int(input("Press a number to access Messages menu: "))
            match (messgaes):
                case 1: print("Write messages")
                case 2: print("Inbox")
                case 3: print("Outbox")
                case 4: print("Picture messages")
                case 5: print("Templates")
                case 6: print("Smileys")
                case 7: 
                        print("Message settings")
                        message_settings = int(input("Press a number to access Messasge Settings options: "))
                        match (message_settings):
                            case 1: 
                                    print("Set 1")
                                    set_one = int(input("Press a number to Set 1 options: "))
                                    match (set_one):
                                        case 1: print("Message centre number")
                                        case 2: print("Message sent as")
                                        case 3: print("Message validity")
                                        case _: print("Invalid input")
                            case 2: 
                                    print("Common")
                                    common = int(input("Press a number to Common options: "))
                                    match (set_one):
                                        case 1: print("Delivery reports")
                                        case 2: print("Reply via same centre")
                                        case 3: print("Charavter support")
                                        case _: print("Invalid input")
                            case _: print("Invalid option")
                case 8: print("Info service")
                case 9: print("Voice mailbox number")
                case 10: print("Service command editor")
                case _: print("invalid input") 

    case 3: print("Chat")

    case 4: 
            print("Call register")
            call_register = int(input("Press a number to access Call register menu: "))
            match (call_register):
                case 1: print("Missed calls")
                case 2: print("Recieved calls")
                case 3: print("Dialled numbers")
                case 4: print("Erase recent call lists")
                case 5: 
                        print("Show call duration")
                        show_call_duration = int(input("Press a number to Show Call Duration options: "))
                        match (show_call_duration):
                            case 1: print("Last call duration")
                            case 2: print("All calls' duration")
                            case 3: print("Recieved calls' duration")
                            case 4: print("Dialled calls' duration")
                            case 5: print("Clear timers")
                            case _: print("Invalid input")
                case 6: 
                        print("Show call costs")
                        show_call_cost = int(input("Press a number to Show Call Cost options: "))
                        match (show_call_cost):
                            case 1: print("Last call cost")
                            case 2: print("All calls' cost")
                            case 3: print("Clear counters")
                            case _: print("Invalid input")
                case 7: 
                        print("Call cost settings")
                        call_cost_settings = int(input("Press a number to Call Cost Settings options: "))
                        match (call_cost_settings):
                            case 1: print("Call cost limit")
                            case 2: print("Show costs in")
                            case _: print("Invalid input")
                case 8: print("Prepaid credit")
                case _: print("invalid input")
 
    case 5: 
            print("Tones")
            tones = int(input("Press a number to access Tones menu: "))
            match (tones):
                case 1: print("Ringing tone")
                case 2: print("Ringing volume")
                case 3: print("Incoming call alert")
                case 4: print("Composer")
                case 5: print("Message alert tone")
                case 6: print("Keypad tones")
                case 7: print("Warning and game tones")
                case 8: print("Vibrating alert")
                case 9: print("Screen saver")
                case _: print("invalid input")

    case 6: 
            print("Settings")
            settings = int(input("Press a number to access Settings menu: "))
            match (settings):
                case 1: 
                        print("Call settings")
                        call_settings = int(input("Press a number to Call Settings options: "))
                        match (call_settings):
                            case 1: print("Automatic redial")
                            case 2: print("Speed dialing")
                            case 3: print("Call waiting options")
                            case 4: print("Own number sending")
                            case 5: print("Phone line in use")
                            case 6: print("Automatic answer")
                            case _: print("Invalid input")
                case 2: 
                        print("Phone settings")
                        phone_settings = int(input("Press a number to Phone Settings options: "))
                        match (phone_settings):
                            case 1: print("Language")
                            case 2: print("Cell info display")
                            case 3: print("Welcome note")
                            case 4: print("Network selection")
                            case 5: print("Lights")
                            case 6: print("Confirm SIM service actions")
                            case _: print("Invalid input")
                case 3: 
                        print("Security settings")
                        security_settings = int(input("Press a number to Security Settings options: "))
                        match (security_settings):
                            case 1: print("PIN code request")
                            case 2: print("Call barring service")
                            case 3: print("Fixed dialling")
                            case 4: print("Closed user group")
                            case 5: print("Phone security")
                            case 6: print("Change access codes")
                            case _: print("Invalid input")
                case 4: print("Restore factory settings")
                case _: print("invalid input") 

    case 7: print("Call divert")
 
    case 8: 
            print("""Games
                  1. Snake II"""
                              )
            games = int(input("Press a number ti access the Games option: "))
            match = (games)
                case 1 = print("Snake II")
                case _ = print("Invalid input")

    case 9: print("Calculator")
 
    case 10: print("Reminders")
 
    case 11:
            print("""    Clock 
                    1. Alarm clock
                    2. Clock Settings
                    3. Date settinga 
                    4. Stopwatch",   
                    5. Countdown timer 
                    6. Auto update of date and time"""
                               )
            clock = int(input("Press a number to access Clock menu: "))
            match (clock):
                case 1: print("Alarm clock")
                case 2: print("Clock setings")
                case 3: print("Date settings")
                case 4: print("Stopwatch")
                case 5: print("Countdown timer")
                case 6: print("Auto update of date and time")
                case _: print("invalid input")  
                        
    case 12: print("Profiles") 

    case 13: print("SIM Service") 

    case 0: print("Power off")

    case _: print("Invalid option")

