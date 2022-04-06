emp = []
emp.append({'name':'taehwa','age':30,'position':'manager'})
emp.append({'name':'yongseong','age':28,'position':'intern'})
emp.append({'name':'jungeon','age':32,'position':'ceo'})

count = 0

for dict in emp :
    if dict['position'] == 'ceo' :
        continue
    
    if dict['age'] >= 30 :
        count += 1


print('30이상인 사람 수:',count)