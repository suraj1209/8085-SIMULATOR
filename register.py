data={}
# data={8272:249,8273:59}
flag={'Z':0,'CY':0,'P':0,'AC':0,'S':0}
PC=0
error={}
subroutine=[]
io={}
SP=61166#eeee

class Register:
	def __init__(self):
		self.value=0
		self.binary='0b00000000'
	
	def fbinary(self):
		self.binary=bin(self.value)
		if len(self.binary)<10:
			x=len(self.binary)-2
			y=self.binary[2:]
			self.binary='0b'+('0'*(8-x))+y	
		
	def __add__(self,other):
		set_aux(self,other)
		self.value=self.value+other.value
		if self.value>255:
			self.value=self.value-256
			flag['CY']=1
		else:
			flag['CY']=0
		self.fbinary()
		set_flag(self)
		return self
	def __sub__(self,other):
		if other.value<=self.value:
			self.value=self.value-other.value
			flag['CY']=0
		else:
			self.value=256+self.value-other.value
			flag['CY']=1
		self.fbinary()
		set_flag(self)
		return self

	def setvalue(self,val):
		if val<=255:
			self.value=val
			self.fbinary()

	def __repr__(self):
		return str(self.value)


A,B,C,D,E,H,L,M=Register(),Register(),Register(),Register(),Register(),Register(),Register(),Register()

def set_aux(a,b):
	x=a.value&15
	y=b.value&15
	if x+y>15:
		flag['AC']=1
	else:
		flag['AC']=0

def set_flag(a):
	x=0
	if a.value==0:
		flag['Z']=1
	else:
		flag['Z']=0
	if a.binary[2:][0]=='1':
		flag['S']=1
	else:
		flag['S']=0
	for i in range (0,len(a.binary[2:])):
		if a.binary[2:][i]=='1':
			x=x+1
	if x%2==0:
		flag['P']=1
	else:
		flag['P']=0

def MOV(x,a):
	x.setvalue(a.value)
	if(id(x)==id(M)):
		address=H.value*256+L.value
		data[address]=a.value


def MVI(x,a):
	x.setvalue(a)
	if(id(x)==id(M)):
		address=H.value*256+L.value
		data[address]=a

def LDA(add):
	global A
	if add in data.keys():
		A.setvalue(data[add])
	else:
		A.setvalue(0)

def regpair(b):
	global B,C,D,E,H,L
	if id(b) ==id(B):
		return [B,C] 
	elif id(b) ==id(D):
		return [D,E]
	if id(b) ==id(H):
		return [H,L]

def LDAX(b):
	global A,data
	pair=regpair(b)
	address=pair[0].value*256+pair[1].value# 100 base 16 is 256 base 10
	if address in data.keys():
		A.setvalue(data[address])
	else:
		A.setvalue(0)

def set_M():
	global H,L,M
	address=H.value*256+L.value# 100 base 16 is 256 base 10
	print(address)
	if address in data.keys():
		if type(data[address])==int:
			M.setvalue(data[address])
	else:
		M.setvalue(0)

# H.setvalue(32)
# L.setvalue(0)
# set_M()
# print(M)

def LXI(b,data):
	pair=regpair(b)
	if data>=0000 and data<=65535:#65535=ffff
		pair[0].setvalue(int(data/256))
		pair[1].setvalue(int(data%256))

		# yahape M ko update kar sakte hai

def LHLD(add):
	global H,L
	if add in data.keys():
		L.setvalue(data[add])
		H.setvalue(data[add+1])
	else:
		L.setvalue(0)
		H.setvalue(0)

def STA(add):
	global A
	if add>=0000 and add<=65535:#65535=ffff
		print(add,A.value)
		data[add]=A.value
		print(add,A.value)

def STAX(b):
	pair=regpair(b)
	address=pair[0].value*256+pair[1].value
	data[address]=A.value

def SHLD(address):
	global H,L
	data[address]=L.value
	data[address+1]=H.value
	print(data[address],data[address+1])

def XCHG():
	global H,L,D,E
	H,D=D,H
	L,E=E,L

def CMP(b):
	global A
	if A.value<b.value:
		flag['CY']=1
	elif A.value==b.value:
		flag['Z']=1
	else:
		flag['CY'],flag['Z']=0,0

def CPI(data):
	global A
	if A.value<data:
		flag['CY']=1
	elif A.value==data:
		flah['Z']=1
	else:
		flag['CY'],flag['Z']=0,0

def ANI(data):
	global A
	A.setvalue(A.value&data)
	flag['CY']=0
	flag['AC']=1
	set_flag(A)

def ANA(b):
	ANI(b.value)

def XRI(data):
	global A
	A.setvalue(A.value^data)
	flag['CY']=0
	flag['AC']=0
	set_flag(A)

def XRA(b):
	XRI(b.value)

def ORI(data):
	global A
	A.setvalue(A.value|data)
	flag['CY']=0
	flag['AC']=0
	set_flag(A)

def ORA(b):
	ORI(b.value)

def CMA():
	global A
	A.setvalue(255-A.value)

def CMC():
	if flag['CY']==1:
		flag['CY']=0
	elif flag['CY']==0:
		flag['CY']=1

def STC():
	flag['CY']=1

def ADD(b):
	global A
	A+b
	set_flag(A)
	#show()

def ADI(data):
	global A
	b=Register()
	b.setvalue(data)
	A+b
	set_flag(A)

def ADC(b):
	global A
	y=flag['CY']
	z=A.value
	c=Register()
	c.setvalue(flag['CY'])
	if id(b)==id(A):
		x=Register()
		x.setvalue(A.value)	
		A+c+x
	else:
		A+c+b
	if z==255 and y==1:
		flag['CY']=1
	set_flag(A)

def ACI(data):
	global A
	b=Register()
	b.setvalue(data)
	c=Register()
	c.setvalue(flag['CY'])
	A+c+b
	set_flag(A)

def SUB(b):
	global A
	A-b
	set_flag(A)

def SUI(data):
	global A
	b=Register()
	b.setvalue(data)
	A-b
	set_flag(A)

def SBB(b):
	global A
	y=flag['CY']
	z=A.value
	c=Register()
	c.setvalue(flag['CY'])
	if id(b)==id(A):
		x=Register()
		x.setvalue(A.value)	
		A-c-x
	else:
		A-c-b
	if z==0 and y==1:
		flag['CY']=1
	set_flag(A)

def SBI(data):
	global A
	b=Register()
	b.setvalue(data)
	c=Register()
	c.setvalue(flag['CY'])
	A-c-b
	set_flag(A)

def INR(b):
	global M
	y=flag['CY']
	x=Register()
	x.setvalue(1)
	set_aux(b,x)
	b=b+x
	set_flag(b)
	flag['CY']=y
	if(id(b)==id(M)):
		print('hello')
		address=H.value*256+L.value
		data[address]=M.value

def DCR(b):
	global M
	y=flag['CY']
	x=Register()
	x.setvalue(1)
	b=b-x
	set_flag(b)
	flag['CY']=y
	if(id(b)==id(M)):
		print('hello')
		address=H.value*256+L.value
		data[address]=M.value

# A.setvalue(1)
# DCR(A)
# print(flag['Z'])

def RRC():
        global A
        f=A.binary[2:]
        o=list(f)
        flag['CY']=o[7]
        o=o[-1:]+o[:-1]
        v=''.join(o)
        v=int(v,2)
        A.setvalue(v)

def RLC():
        global A
        f=A.binary[2:]
        o=list(f)
        flag['CY']=o[0]
        o=o[1:]+o[:1]
        v=''.join(o)
        v=int(v,2)
        A.setvalue(v)

def RAL():
        global A
        f=A.binary[2:]
        f=str(flag['CY'])+f
        o=list(f)
        o=o[1:]+o[:1]
        flag['CY']=o[0]
        o=o[1:]
        v=''.join(o)
        v=int(v,2)            
        A.setvalue(v)

def RAR():
        global A
        f=A.binary[2:]
        f=str(flag['CY'])+f
        o=list(f)
        o=o[-1:]+o[:-1]
        flag['CY']=o[0]
        o=o[1:]
        v=''.join(o)
        v=int(v,2)            
        A.setvalue(v)

def DAD(b):
	global SP
	p=flag['S']
	q=flag['AC']
	r=flag['Z']
	s=flag['P']
	if b!='SP':
		pair=regpair(b)
		L+pair[1]
		c=Register()
		c.setvalue(flag['CY'])
		H+c+pair[0]
	else:
		p1=Register()
		p2=Register()
		if SP>=0000 and SP<=65535:#65535=ffff
			p1.setvalue(int(SP/256))
			p2.setvalue(int(SP%256))
			L+p2
			c=Register()
			c.setvalue(flag['CY'])
			H+c+p1
	flag['S']=p
	flag['AC']=q
	flag['Z']=r
	flag['P']=s


def INX(b):
	pair=regpair(b)
	o=Register()
	o.setvalue(1)
	x=flag['CY']
	pair[1]=pair[1]+o
	c=Register()
	c.setvalue(flag['CY'])
	pair[0]=pair[0]+c
	flag['CY']=x

def DCX(b):
	pair=regpair(b)
	o=Register()
	o.setvalue(1)
	x=flag['CY']
	pair[1]=pair[1]-o
	c=Register()
	c.setvalue(flag['CY'])
	pair[0]=pair[0]-c
	flag['CY']=x

def JC(add):
	global PC
	if flag['CY']==1:
		PC=add
		# return PC
	else:
		PC+=3

def JNC(add):
	global PC
	if flag['CY']==0:
		PC=add
	else:
		PC+=3

def JP(add):
	global PC
	if flag['S']==0:
		PC=add
	else:
		PC+=3

def JM(add):
	global PC
	if flag['S']==1:
		PC=add
	else:
		PC+=3

def JZ(add):
	global PC
	if flag['Z']==1:
		PC=add
	else:
		PC+=3

def JNZ(add):
	global PC
	if flag['Z']==0:
		PC=add
	else:
		PC+=3

def JPE(add):
	global PC
	if flag['P']==1:
		PC=add
	else:
		PC+=3

def JPO(add):
	global PC
	if flag['P']==0:
		PC=add
	else:
		PC+=3

def JMP(add):
	global PC
	PC=add

def CC(add):
	global PC
	if flag['CY']==1:
		subroutine.append(PC+3)
		PC=add

def CNC(add):
	global PC
	if flag['CY']==0:
		subroutine.append(PC+3)
		PC=add

def CP(add):
	global PC
	if flag['S']==0:
		subroutine.append(PC+3)
		PC=add

def CM(add):
	global PC
	if flag['S']==1:
		subroutine.append(PC+3)
		PC=add

def CZ(add):
	global PC
	if flag['Z']==1:
		subroutine.append(PC+3)
		PC=add

def CNZ(add):
	global PC
	if flag['Z']==0:
		subroutine.append(PC+3)
		PC=add

def CPE(add):
	global PC
	if flag['P']==1:
		subroutine.append(PC+3)
		PC=add

def CPO(add):
	global PC
	if flag['P']==0:
		subroutine.append(PC+3)
		PC=add

def CALL(add):
	global PC
	subroutine.append(PC+3)
	PC=add
	print(PC)
	# subroutine.append(PC)

def getsub():
	try:													#*******Check for no. of call = return while pasing the file
		return(subroutine.pop())
	except IndexError:
		return 'e'					#handli it later

def RET():
	global PC,error
	x=getsub()
	if x!='e':
		PC=x
	else:
		error['Return']="Call statement without return"
	return PC


def RC():
	global PC,error
	if flag['CY']==1:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RNC():
	global PC,error
	if flag['CY']==0:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RP():
	global PC,error
	if flag['S']==0:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RM():
	global PC,error
	if flag['S']==1:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RZ():
	global PC,error
	if flag['Z']==1:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RNZ():
	global PC,error
	if flag['Z']==0:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RPE():
	global PC,error
	if flag['P']==1:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC


def RPO():
	global PC,error
	if flag['P']==0:
		x=getsub()
		if x!='e':
			PC=x
		else:
			error['Return']="Call statement without return"
		return PC

# PC=20
# print(PC)
# CALL(3000)
# RET()
# print(PC)



def PCHL():
	global PC
	PC=H.value*256+L.value
# *************************************handle RST in main program**************************************************
def PUSH(b):
	global SP
	if SP in range(65535):
		pair=regpair(b)
		SP=SP-1
		data[SP]=pair[0].value
		SP=SP-1
		data[SP]=pair[1].value
	else:
		error+1
		print('stack full')


def SSP(SP):
	if SP in data.keys():
		return data[SP]
	return 0

def POP(b):
	global SP
	pair=regpair(b)
	pair[1].setvalue(SSP(SP))
	if SP in data.keys():
		del data[SP]
	SP=SP+1
	pair[0].setvalue(SSP(SP))
	if SP in data.keys():	
		del data[SP]
	SP=SP+1

def XTHL():
	global SP
	x=SSP(SP)
	SP=SP+1
	y=SSP(SP)
	x,L.value=L.value,x
	y,H.value=H.value,y
	data[SP]=y
	SP=SP-1
	data[SP]=x

def SPHL():
	global SP
	SP=H.value*256+L.value

#B.setvalue(10)
#C.setvalue(15)
#D.setvalue(20)
#E.setvalue(30)
#PUSH(B)
#print(data)
#POP(H)
#print(H,L,data)
#PUSH(D)
#XTHL()
#print(H,L,data)
#SPHL()
#print(SP)
def show():
       print("Accumulator:",hex(A.value)[2:])
       print("Reg B:",hex(B.value)[2:])
       print("Reg C:",hex(C.value)[2:])
       print("Reg D:",hex(D.value)[2:])
       print("Reg E:",hex(E.value)[2:])
       print("Reg H:",hex(H.value)[2:])
       print("Reg L:",hex(L.value)[2:])
       print("FLAGS:")
       print("Sign:",flag['S'])
       print("Zero:",flag['Z'])
       print("Auxiliary Carry:",flag['AC'])
       print("Parity:",flag['P'])
       print("Carry:",flag['CY'])
       print("Program Counter:",hex(PC)[2:])
       print(error)
        
def IN(add):
	global A
	if add in io.keys():
		A.setvalue(io[add])
	else:
		A.setvalue(0)

def OUT(add):
	global A
	io[add]=A.value

# IN(20)
# print(A)
# A.setvalue(1)
# OUT(2)
# print(io)
def cclear():
	global error
	# print(data)
	# data.clear()
	# print(data)
	error.clear()
	# io.clear()
	A.setvalue(0)
	B.setvalue(0)
	C.setvalue(0)
	D.setvalue(0)
	E.setvalue(0)
	H.setvalue(0)
	L.setvalue(0)

# A.setvalue(30)
def DAA():
	global flag
	e=0
	z=flag['CY']
	h=hex(A.value)
	y=Register()
	x=h[-1]
	if int(x,16)>9 or flag['AC']==1:
		y.setvalue(6)
		A+y
		e=1
	flag['CY']=z
	x=h[-2]
	if x.lower()!='x':
		if int(x,16)>9 or flag['CY']==1:
			y.setvalue(96)
			A+y
			flag['CY']=1
	if e==1:
		flag["AC"]=1
	set_flag(A)
