emails = ['a@naver.com', 'b@naver.com', 'lhb7310', 'c@naver.com']
for email in emails :
    if '@' not in email :
        continue
    print('send email',email)