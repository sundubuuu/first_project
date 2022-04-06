with open('textfile.txt','a', encoding = 'utf-8') as datafile :
    user_input = input('input :')
    datafile.write(user_input + '\n')