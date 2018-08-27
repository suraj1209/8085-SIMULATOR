from register import PC,data
from register import error
sub_var=0
counter=2000
def set1():
        global counter,PC
        counter,PC=8192,8192
def get_Counter(h):
        global PC,counter,error
        if h=='':
                # print("hello")
                counter,PC=8192,8192
        else:
		#if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
			#h=h[:-1]
                try:
                        x=int(h,16)
                        if x<65536:
                                # print("hello1")
                                counter,PC=x,x
                        elif x>=65536:
                                set1()
                                print("hello2")
                                raise ValueError
                except ValueError:
                        # print("hello3")
                        error["address"]='error while giving address.Taking default address=2000H'
			# error+=1
			# print('error while giving address')

def get_code():
	global counter
	with open ("code.txt") as file:
		lines=[line.replace('\n','') for line in file.readlines()]
		# print(lines)
		for line in lines:
			t=tuple(line.split(' '))
			data[counter]=t
			IncrementPC(t,1)


def get_subroutine():
        global sub_var
        with open ("subroutine.txt") as file:
                lines=[line.replace('\n','') for line in file.readlines()]
                for line in lines:
                        t=tuple(line.split(' '))
                        data[sub_var]=t
                        IncrementPC(t,2)

def IncrementPC(t,f):
	global counter,sub_var
	if t[0].upper() in ('XTHL','PUSH','POP','NOOP','HLT','DI','EI','RIM','SIM','CMP','ANA','XRA','ORA','RLC','RRC','RAL','RAR','CMA','CMC','STC','PCHL','ADD','ADC','DAD','SUB','SBB','INR','INX','DCR','DCX','DAA','MOV','LDAX','STAX','XCHG','SPHL','RET','RC','RNC','RP','RM','RZ','RNZ','RPE','RPO'):
                if f==1:
                        counter+=1
                else:
                        sub_var+=1
	if t[0].upper() in ('CPI','ANI','XRI','ORI','ADI','ACI','SUI','SBI','MVI','OUT','IN'):
                if f==1:
                        counter+=2
                else:
                        sub_var+=2
	if t[0].upper() in ('JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO','LXI','LDA','LHLD','STA','SHLD',''):
                if f==1:
                        counter+=3
                else:
                        sub_var+=3

#get_Counter()
#get_code()
