def MultiBitXor(a,b):
	result = ""
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
	remainder = DivReminder(newMessage[2:len(newMessage)],P)
	formatedRemainder = format(int(remainder,2),'#0{}b'.format(len(newMessage)))
	transmittedmessage = MultiBitXor(formatedRemainder[2:len(formatedRemainder)], newMessage[2:len(newMessage)])
	return transmittedmessage

def main():
	message = input()
	polynomial = input()
	message = message.replace(" ", "")
	message = message.replace("\n", '')
	polynomial = polynomial.replace(" ", "")
	polynomial = polynomial.replace("\n", "")
	transmittedMessage = generator(message,polynomial)
	VerifierInput = transmittedMessage + '\n'+polynomial+'\n'
	outputFile = open("transmittedMessage.txt", "+w")
	outputFile.write(transmittedMessage)
	print(VerifierInput)

if __name__ =='__main__':
	main()
