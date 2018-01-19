import time

name = raw_input('Enter your name: ')
name = name[0].upper() + name[1:]
#age = raw_input('Enter your age ' + name + ': ')

#To validate age
while True:
    isint = True
    age = raw_input('Enter your age ' + name + ':')

    try:
        age = int(age)
    except ValueError:
        print 'Entered age is not an integer.'
        isint = False

    if isint == True:
        break

print '\n' + 'Hi ' + name + ' your age is ' + str(age) +'.'

t = time.asctime(time.localtime(time.time()))

y = int(t[-4:])

offset = 100 - int(age)


print name + ' you\'ll turn 100 years on ' + str(y + offset) + '.'
