import math
class coord:
	__result = [0,0]
	def __rounded(numb):
		if str(numb).split(".")[-1]=='0': return round(numb)
		else: return numb
	def __compactSqrt(number):
		lastRes = 0
		for numb in range(1,number+1):
			if number%numb==0:
				sqrtRes = coord.__rounded(math.sqrt(numb))
				if type(sqrtRes)==int:
					lastRes = f'{sqrtRes}√{coord.__rounded(number/numb)}'
		if lastRes.split("√")[0]=="1": lastRes = lastRes[1:]
		return lastRes
	def __numberInSqrt(number):
		mainSqrt = number.split("√")
		if len(mainSqrt)==2 and len(mainSqrt[0])>0:
			return (int(mainSqrt[0])**2)*int(mainSqrt[1])
		else:
			return int(''.join(mainSqrt))
	def __fixMidAngle(number):
		removeDot = str(number).split(".")[1]
		if len(removeDot)>=14 and removeDot[0]=='0' and str(number)[-1]=="1":
			return round(float(number))
		else: return coord.__rounded(number)
	def create(a,b):
		if type(a)==tuple and type(b)==tuple:
			a = list(a)
			b = list(b)
		if type(a)==list or type(b)==list:
			coord.__result[0]=b[0]-a[0]
			coord.__result[1]=b[1]-a[1]
			if len(a) == 3 and len(b) == 3:
				coord.__result.append(0)
				coord.__result[2]=b[2]-a[2]
		return tuple(coord.__result)
	def add(*vectors):
		coord.__result = [0,0]
		for vector in vectors:
			if type(vector)==tuple or type(vector)==list:
				coord.__result[0]+=vector[0]
				coord.__result[1]+=vector[1]
				if len(vector)==3:
					coord.__result.append(0)
					coord.__result[2]+=vector[2]
					if(list(coord.__result)[-1]==0): coord.__result.pop()
		return tuple(coord.__result)
	def subtract(*vectors):
		coord.__result = [vectors[0][0],vectors[0][1]]
		for vector in vectors[1:]:
			if type(vector)==tuple or type(vector)==list:
				coord.__result[0]-=vector[0]
				coord.__result[1]-=vector[1]
				if len(vector)==3:
					coord.__result.append(0)
					coord.__result[2]-=vector[2]
		return tuple(coord.__result)
	def multi(k,*vectors):
		coord.__result = [0,0]
		vectorList = []
		for vector in vectors:
			if type(vector)==tuple or type(vector)==list:
				coord.__result[0]=k*vector[0]
				coord.__result[1]=k*vector[1]
				if len(vector)==3:
					coord.__result.append(0)
					coord.__result[2]=k*vector[2]
					if(list(coord.__result)[-1]==0): coord.__result.pop()
			vectorList.append(tuple(coord.__result))
		if len(vectorList)>1: return vectorList
		else: return vectorList[0]
	def co_exp(a,b):
		coord.__result = [0,0]
		vecto = 0
		if type(a)==tuple and type(b)==tuple:
			a = list(a)
			b = list(b)
		if type(a)==list or type(b)==list:
			coord.__result[0]=a[0]*b[0]
			coord.__result[1]=a[1]*b[1]
			vecto += coord.__result[0] + coord.__result[1]
			if len(a)==3 and len(b)==3:
				coord.__result.append(0)
				coord.__result[2]=a[2]*b[2]
				vecto += coord.__result[2]
		return vecto
	def average(*vectors):
		vectoLength = len(list(vectors))
		sumVector = list(coord.add(*vectors))
		coord.__result[0]=coord.__rounded(sumVector[0]/vectoLength)
		coord.__result[1]=coord.__rounded(sumVector[1]/vectoLength)
		if len(sumVector)==3: coord.__result[2]=coord.__rounded(sumVector[2]/vectoLength)
		return tuple(coord.__result)
	def size(vector,compact=False):
		vectorLength = 0
		for vec in list(vector):
			vectorLength+=vec**2
		sqrtLength = math.sqrt(vectorLength)
		if not compact:
			return coord.__rounded(sqrtLength)
		else:
			if type(coord.__rounded(sqrtLength))==int:
				return coord.__rounded(sqrtLength)
			elif type(coord.__rounded(sqrtLength))==float:
				return coord.__compactSqrt(vectorLength)
	def mid_angle(a,b):
		numerator = coord.co_exp(a,b)
		a_length = coord.__numberInSqrt(coord.size(a,True))
		b_length = coord.__numberInSqrt(coord.size(b,True))
		denominator = math.sqrt(a_length*b_length)
		degMidAng = math.degrees(math.acos(numerator/denominator))
		return coord.__fixMidAngle(degMidAng)