# 8.9. Messages. 
# Prepare a list containing a series of short messages, then pass it to a function called show_messages(), which should print each message on the list.
print("====")
def show_messages(input):
    for _print in input:
        print(_print)
inputs =['message 1','message 2', 'message 3']

show_messages(inputs)
# 8.10. Sending messages. 
# Start with the program from exercise 8.9. Then create a function called send_messages(), whose task will be to print all the messages and then move them to a new list called sent_messages. 
# After calling the function, print both lists to make sure the messages have been transferred correctly.
print("====")
sent_messages = []
def send_messages(input):
    while input:
        message_to_send = input.pop()
        print(message_to_send)
        sent_messages.append(message_to_send)
    
inputs =['message 1','message 2', 'message 3']
send_messages(inputs)
print(sent_messages)
print(inputs)
# 8.11. Archived messages. 
# Start with a copy of the code created in exercise 8.10. Call the send_messages() function with a copy of the message list. 
# After calling the function, print both lists to show that the original list still contains the messages.
print("====")
sent_messages = []
def send_messages(input):
    while input:
        message_to_send = input.pop()
        print(message_to_send)
        sent_messages.append(message_to_send)
    
inputs =['message 1','message 2', 'message 3']
send_messages(inputs[:])
print(sent_messages)
print(inputs)
