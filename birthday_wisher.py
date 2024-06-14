from datetime import datetime
import pywhatkit as kit
def birthday_greeting(name):
    return f"Happiest Birthday to you {name},\nMay you live a thousnad years \nnote:this is an automated message sent using python script written by kaushik joshi (he wanted to flex his coding skills)"

def send_message(message,when,phone):
    time_obj = datetime.strptime(when, "%H%M")  
    send_hr = time_obj.hour
    send_min = time_obj.minute
    kit.sendwhatmsg(phone,message,send_hr,send_min)

if __name__=='__main__':
    person=input("enter the name: ")
    when=input("enter time in hhmm format (24hrs): ")
    ph=input("enter the recipients phone number: ")
    send_message(birthday_greeting(person),when,'+91'+ph)

    



