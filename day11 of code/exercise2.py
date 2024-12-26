a=int(input('enter hours'))
b=input('enter name: ')
if (a>=0 and a<=12):
    print('good moring',b)
elif (a>=12 and a<16):
    print('good afternoon',b)
elif (a>=16 and a<20):
    print('good evening',b)
elif (a>=20 and a<0):
    print('good night',b)
else:
    print('all done')
