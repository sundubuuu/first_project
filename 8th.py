def send_mail(to_mail):
    from_email = 'alghost.lee@gmail.com'

    other_mail = ''
    if not '@' in to_mail :
        other_mail = 'test@gmail.com'

    print('other: ' + other_mail)

send_mail('test')
send_mail('lhb7310@naver.com')