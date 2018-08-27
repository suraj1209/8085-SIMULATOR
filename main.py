def verymain():
        x1=[]
        import register
        import parse
        #parse.get_Counter()
        parse.get_code()

        # print(register.data)
        for i,j in register.data.items():
            print(hex(i),':',j)

        register.PC=parse.PC
        errors=0
        l=0

        reg=('A','B','C','D','E','H','L','M')

        def getarg(x):
                if x=='A':return register.A
                if x=='B':return register.B
                if x=='C':return register.C
                if x=='D':return register.D
                if x=='E':return register.E
                if x=='H':return register.H
                if x=='L':return register.L
                if x=='M':return register.M

        while True:
                try:
                        code=register.data[register.PC]
                        l+=1
                        print(l)
                        print('*****',register.C,register.A,register.B)
                        register.set_M()
                        print(code[0])
                        if code[0].upper() not in ('INX','DCX','DAA','RET','RC','RNC','RP','RM','RZ','RNZ','RPE','RPO','HLT','RLC','RRC','RAL','RAR','CMA','CMC','STC','PCHL','XCHG','SPHL','XTHL','CMP','ANA','XRA','ORA','ADD','ADC','SUB','SBB','INR','DCR','DAD','LDAX','STAX','PUSH','POP','MOV','CPI','ANI','XRI','ORI','ADI','ACI','SUI','SBI','OUT','IN','MVI','JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO','LDA','LHLD','STA','SHLD','LXI'):
                            register.error[l]="NO such command or not Supported Currently"
                            break
                        try:
                                x1.append(code[0])
                                # print(register.PC)
                                if code[0].upper() in ('CMP','ANA','XRA','ORA','ADD','ADC','SUB','SBB','INR','DCR'):
                                        arg=code[1].upper()
                                        if arg in reg:
                                                f=getattr(register,code[0].upper())
                                                f(getarg(arg))
                                        else:
                                                register.error[l]="wrong argument"
                                                # errors+=1
                                                # print("wrong argument")
                                        register.PC+=1

                                elif code[0].upper() in ('MOV'):
                                        arg=[x.upper() for x in code[1].split(',')]
                                        if len(arg)==2:
                                                if arg[0] in reg and arg[1] in reg:
                                                        f=getattr(register,code[0].upper())
                                                        f(getarg(arg[0]),getarg(arg[1]))
                                                else:
                                                        register.error[l]="wrong argument"
                                                        # errors+=1
                                                        # print('wrong argument')
                                        else:
                                                register.error[l]="wrong no. of argument"
                                                # errors+=1
                                                # print("wrong no. of arguments")
                                        register.PC+=1
                                
                                elif code[0].upper() in ('CPI','ANI','XRI','ORI','ADI','ACI','SUI','SBI','OUT','IN'):
                                        x=code[1].split(',')
                                        if len(x) == 1:
                                                h=code[1]
                                                if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
                                                        h=h[:-1]
                                                        try:
                                                                x=int(h,16)
                                                                if x in range(256):
                                                                        f=getattr(register,code[0].upper())
                                                                        f(x)
                                                                else:
                                                                        raise ValueError
                                                        except ValueError:
                                                            register.error[l]="Enter 8 bit number"
                                                else:
                                                        register.error[l]="enter h or H at the end of 8 bit number"
                                                        # errors+=1
                                                        # print("enter h or H at the end of 8 bit number")
                                        else:
                                                register.error[l]="wrong no. of argument"
                                                # errors+=1
                                                # print('Wrong no. of arguments')
                                        register.PC+=2
                                
                                elif code[0].upper() in ('JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO','LDA','LHLD','STA','SHLD'):
                                        x=code[1].split(',')
                                        if len(x) == 1:
                                                h=code[1]
                                                if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
                                                        h=h[:-1]
                                                        try:
                                                                x=int(h,16)
                                                                if x in range(65536):
                                                                        f=getattr(register,code[0].upper())
                                                                        f(x)
                                                                        print(hex(register.PC))
                                                                        if register.PC not in register.data.keys():
                                                                            register.error[l]="No code in address you want to jump or no subroutine in address you want to call"
                                                                            break
                                                                else:
                                                                        raise ValueError
                                                        except ValueError:
                                                                # errors+=1
                                                                 register.error[l]="Enter 16 bit number"
                                                else:
                                                        register.error[l]="enter h or H at the end of 16 bit number"
                                                        # errors+=1
                                                        # print("enter h or H at the end of 16 bit number")
                                        else:
                                                register.error[l]="wrong no. of argument"
                                                # errors+=1
                                                # print('Wrong no. of arguments')
                                        if code[0].upper() not in ('JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO'):
                                                register.PC+=3
                                
                                elif code[0].upper() in ('MVI'):
                                        arg=[x.upper() for x in code[1].split(',')]
                                        if len(arg)==2:
                                                if arg[0] in reg:
                                                                h=arg[1]
                                                                if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
                                                                        h=h[:-1]
                                                                        try:
                                                                                x=int(h,16)
                                                                                if x in range(256):
                                                                                        f=getattr(register,code[0].upper())
                                                                                        f(getarg(arg[0]),x)
                                                                                else:
                                                                                        raise ValueError
                                                                        except ValueError:
                                                                                register.error[l]="Enter 8 bit number in argument 2"
                                                                                # errors+=1
                                                                                # print("Enter 8 bit number in argument 2")
                                                                else:
                                                                        register.error[l]="enter h or H at the end of 8 bit number in argument 2"
                                                                        # errors+=1
                                                                        # print("enter h or H at the end of 8 bit number in argument 2")						
                                                else:
                                                        register.error[l]="wrong argument 1"
                                                        # errors+=1
                                                        # print('wrong argument 1')
                                        else:
                                                register.error[l]="wrong no. of argument"
                                                # errors+=1
                                                # print("wrong no. of arguments")
                                        register.PC+=2

                                elif code[0].upper() in ('INX','DCX','DAD','LDAX','STAX','PUSH','POP'):
                                        arg=code[1].upper()
                                        if arg in ('B','D','H'):
                                                f=getattr(register,code[0].upper())
                                                f(getarg(arg))
                                        elif code[0].upper()=='DAD' and arg=='SP':
                                                register.DAD('SP')
                                        else:
                                                register.error[l]="wrong argument"
                                                # errors+=1
                                                # print('Wrong argument')
                                        register.PC+=1

                                elif code[0].upper() in ('LXI'):
                                        arg=[x.upper() for x in code[1].split(',')]
                                        if len(arg)==2:
                                                if arg[0] in ('B','D','H'):
                                                                h=arg[1]
                                                                if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
                                                                        h=h[:-1]
                                                                        try:
                                                                                x=int(h,16)
                                                                                if x in range(65536):
                                                                                        f=getattr(register,code[0].upper())
                                                                                        f(getarg(arg[0]),x)
                                                                                else:
                                                                                        raise ValueError
                                                                        except ValueError:
                                                                                 register.error[l]="Enter 16 bit number in argument 2"
                                                                                # errors+=1
                                                                                # print("Enter 16 bit number in argument 2")
                                                                else:
                                                                        register.error[l]="enter h or H at the end of 16 bit number in argument 2"
                                                                        # errors+=1
                                                                        # print("enter h or H at the end of 16 bit number in argument 2")						
                                                else:
                                                        register.error[l]="wrong argument 1"
                                                        # errors+=1
                                                        # print('wrong argument 1')
                                        else:
                                                register.error[l]="wrong no. of argument"
                                                # errors+=1
                                                # print("wrong no. of arguments")
                                        register.PC+=3

                                elif code[0].upper() in ('DAA','RLC','RRC','RAL','RAR','CMA','CMC','STC','PCHL','XCHG','SPHL','XTHL'):
                                        if len(code)==1:
                                                f=getattr(register,code[0].upper())
                                                f()
                                        else:
                                                register.error[l]="no arguments are needed"
                                                # error+=1
                                                # print("no arguments are needed")
                                        register.PC+=1

                                elif code[0].upper() =='HLT':
                                        break

                                elif code[0].upper() in ('RET','RC','RNC','RP','RM','RZ','RNZ','RPE','RPO'):
                                        if len(code)==1:
                                                f=getattr(register,code[0].upper())
                                                register.PC=f()
                                        else:
                                                register.error[l]="no arguments are needed"
                                                # error+=1
                                                # print("no arguments are needed")
                                        # register.PC+=1

                                else:
                                        register.error[l]="NO such command or not Supported Currently"
                                        # errors+=1
                                        # print('NO such command or not Supported Currently')

                        except IndexError:
                                print(l)
                                register.error[l]="argument is not given"
                                # print(121212)
                                if code[0].upper() in ('INX','DCX','CMP','ANA','XRA','ORA','ADD','ADC','SUB','SBB','INR','DCR','DAD','LDAX','STAX','PUSH','POP','MOV','DAA','RLC','RRC','RAL','RAR','CMA','CMC','STC','PCHL','XCHG','SPHL','XTHL'):
                                    register.PC+=1
                                elif code[0].upper() in ('CPI','ANI','XRI','ORI','ADI','ACI','SUI','SBI','OUT','IN','MVI'):
                                    register.PC+=2
                                elif code[0].upper() in ('JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO','LDA','LHLD','STA','SHLD','LXI'):
                                    register.PC+=3
                                # errors+=1
                                # print('argument is not given')
                except KeyError:
                        register.error['s end Exception']="HLT missing from end of the code or Call without Return statement"
                        # errors+=1
                        # print("'HLT missing from end of code")
                        break
                # print(x1)
        if register.PC in register.data.keys():
            if register.data[register.PC][0].upper() not in ('DAA','RET','RC','RNC','RP','RM','RZ','RNZ','RPE','RPO','RLC','RRC','RAL','RAR','CMA','CMC','STC','PCHL','XCHG','SPHL','XTHL','CMP','ANA','XRA','ORA','ADD','ADC','SUB','SBB','INR','DCR','DAD','LDAX','STAX','PUSH','POP','MOV','CPI','ANI','XRI','ORI','ADI','ACI','SUI','SBI','OUT','IN','MVI','JMP','JC','JNC','JP','JM','JZ','JNZ','JPE','JPO','CALL','CC','CNC','CP','CM','CZ','CNZ','CPE','CPO','LDA','LHLD','STA','SHLD','LXI'):
                register.data.pop(register.PC)
        # print(register.data)
        # print(register.sub_var)
        
# h='0'
# d='0'   
# def set_data():
#         from register import data
#         #h=input("Enter Staring address")
#         #if h=='':
#                 #counter,PC=0,0
#         #else:
#                 #if h[-1] in ['H','h']: #not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
#                         #h=h[:-1]
#         try:
#                 x=int(h,16)
#                 if x in range(65536):
#                         #d=input("Enter data")
#                         #if d[-1] in ['H','h']:
#                                 #d=d[:-1]
#                         try:
#                                 y=int(d,16)
#                                 if y in range(65536):
#                                         data[x]=y  
#                                 else:
#                                         raise ValueError
#                         except ValueError:
#                                 register.error["data"]="Error while giving the data"
#                                 # error+=1
#                                 # print("Error while giving the data")
#                 else:
#                         raise ValueError
#         except ValueError:
#                 register.error["address"]="Error while giving the data"
                # error+=1
                # print('error while giving address')
        
        # print(register.data)

# verymain()       
