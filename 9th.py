datafile = open('textfile.txt','a', encoding = 'utf-8')
user_input = input('input:')
datafile.write(user_input +'\n')