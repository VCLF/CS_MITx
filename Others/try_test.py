try:
    raise 
    i = int(input('give me a number'))
    print(1/i)
except ZeroDivisionError: print('You provided a zero!')
finally: print(1/(i-1))

