emails = ['taehwa@gmail.com','dlxoghk@gmail.com','yongseong']
desc = 'For developer'
students_count = 10

if '@' not in emails :
    print('Wrong')
if 'developer' in desc :
    a = desc.replace('developer','beginner')
    print(a)
if students_count >=5 :
    students_count=5
    print('"Exceed"')

b= 'Python is awesome'
if 'awesome' in a[:6] :
    print('step 3')
print('step4')