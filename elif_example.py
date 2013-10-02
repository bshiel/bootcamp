number= raw_input('Type a number: ')
number= int(number)

if number >0 and number <50:
    print 'minor'
elif number >= 50 and number < 1000:
    print 'major'
else:
    print 'severe'
