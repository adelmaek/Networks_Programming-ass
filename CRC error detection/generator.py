def MultiBitXor(a,b):
	result=""
	for i in range(0,len(b)):
		if a[i] == b[i]:
			result += '0'
		else:
			result += '1'
	return result

def DivReminder(d,G):
	#G is the polynomial and d is the data with the appended zeros "i.e. the division is d/G"
	quotient = []
	selector = len(G)
	i = int(len(G)+1)
	temp=d[0:selector]
	while selector < len(d):
		if temp[0] == '1':
			quotient.append('1')
			XorResult = MultiBitXor(G,temp)
			temp = str(XorResult[1:i])+str(d[selector])
		else:
			quotient.append('0')
			XorResult= MultiBitXor('0'*selector,temp)
			temp= str(XorResult[1:i])+str(d[selector])
		selector+=1
	if temp[0] =='1':
		reminder = MultiBitXor(G,temp)
	else:
		reminder= MultiBitXor('0'*selector,temp)
	return reminder


def generator(M,P):
	#M is the message before appending the zeros , P is the polynomial
	noOfZeros= int(len(P)-1)
	newMessage= bin(int(M,2) << int(noOfZeros))
	print('newMessage: ',newMessage[2:len(newMessage)])
	remainder = DivReminder(newMessage[2:len(newMessage)],P)
	formatedRemainder = format(int(remainder,2),'#0{}b'.format(len(newMessage)))
	print('formatedremainder: ',formatedRemainder[2:len(formatedRemainder)])
	return MultiBitXor(formatedRemainder[2:len(formatedRemainder)],newMessage[2:len(newMessage)])


message = input('input the message: ')
polynomial = input('input the polynomial: ')
print('message: ',int(message))
print('transmittedMessage: ',generator(message,polynomial))
#print(format(generator(message,polynomial), 'b'))
