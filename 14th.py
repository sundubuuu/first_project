try:
    int('adef')
except Exception as e :
    print(e)
finally:
    print('done')  