def MultiBitXor(a,b):
	result=""
	for i in range(0,len(b)):
		if a[i]==b[i]:
			result+='0'
		else:
			result+='1'
	return result


def DivReminder(d,G):
#G is the polynomial and d is the data with the appended zeros "i.e. the division is d/G"
	quotient=[]
	selector=len(G)
	i=int(len(G)+1)
	temp=d[0:selector]
	while selector<len(d):
		if temp[0]=='1':
			quotient.append('1')
			XorResult=MultiBitXor(G,temp)
			temp=str(XorResult[1:i])+str(d[selector])
		else:
			quotient.append('0')
			XorResult=MultiBitXor('0'*selector,temp)
			temp=str(XorResult[1:i])+str(d[selector])
		selector+=1
	if temp[0]=='1':
		reminder=MultiBitXor(G,temp)
	else:
		reminder=MultiBitXor('0'*selector,temp)
	return reminder


def Verifier(d,G):
	temp='0'*len(G)
	reminder=DivReminder(d,G)
	if reminder==temp:
		print('sent succesfully')
	else:
		print('sent with error')

def main():
	data=input('input sent message:		')
	divisor=input('enter the divisor polynomial coefficients:	')
	Verifier(data,divisor)


if __name__ =='__main__':
	main()