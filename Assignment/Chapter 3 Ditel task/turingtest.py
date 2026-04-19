#3.6

user_prompt = input("What is your problem? : ")

question = bool(input("Have you had this problem before (True or False)? : "))

if question == True:
    print('Well, you have it again.')
if question == False:
    print('Well, you hve it now.')

"""
if the user goes ahead to write an out of context message it should see that the message isnt intelligent seeing as it prompts questions based on a set instruction.
then again if the user follows the instructions it could think it's a human giving a quick response except if the user prompts it again and keeps seeing the same responses and questions all the time
"""
