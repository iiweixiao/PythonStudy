# 作者:  Bruce
# 时间： 2022/5/19
help_info = '''
start - to start the car
stop - to stop the car
quit - to exit
'''

flag = ''
while True:
    choice = input('>')
    if choice == 'start':
        if flag == 'start':
            print('Car is started! What are you doing?')
        else:
            print('Car started...Ready to go!')
        flag = 'start'
        continue
    elif choice == 'stop':
        if flag == 'stop':
            print('Car is stopped! What are you doing?')
        else:
            print('Car stopped.')
        flag = 'stop'
        continue
    elif choice == 'help':
        print(help_info)
    elif choice == 'quit':
        break
    else:
        print("I don't understand that...")