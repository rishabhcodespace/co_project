# import sys
# file_input = sys.argv[1]
# file_output = sys.argv[2]



# # import pandas as pd
# # data = pd.read_csv(file_input)
# # print(data)

# import re
# file=open(file_input)
# instructions=[]
# i=0
# for s in file:
#   s=s.replace("(", ' ')
#   s=s.replace(")", ' ')
#   instructions.append(re.split(' |, | , | ,|,|\n', s))
#   for i in instructions:
#     for j in i:
#         if j=='':
#          i.remove(j)
         
# # print(instructions)
# Instruction_function = [instructions[i][0] for i in range(len(instructions))]
# if("hlt" in Instruction_function):
#     if(Instruction_function[-1]!="hlt"):
#         print("\nhlt not being used as the last instruction\n")  #virtual halt must be used as the last instruction.
#         quit()
# else:     #Checking if hlt is present in the program if it doesn't exist the program will not continue.
#     print(f"\nError: No virtual hlt present.\n")
#     quit()
 


# def binary_convertor(b,n):
#     nbits = n.bit_length() + 1

#     binary=f"{n & ((1 << nbits) - 1):0{nbits}b}"
#     if n>=0:
#         binary=(b-nbits)*'0'+binary
#         return binary
#     else:
#         binary=(b-nbits)*'1'+binary
#         return binary
    
# inst1=instructions.copy()
# for i in range(len(instructions)):
#     if ':' in instructions[i][0]:
#         instructions[i].remove(instructions[i][0])


# def label_convertor(labelname, labelLine):
  
#     num1=0
#     num2=0

#     for i in inst1:
#         if i[0]==labelname:
#            num1=i
#         if i[-1]==labelname:
#             num2=i
#     return (num2-num1)*4
    
# funct3={'add':'000', 'sub':'000', 'sll':'001', 'slt':'010',
#         'sltu':'011', 'xor':'100', 'srl':'101', 'or':'110','and':'111',
#         'lw':'010','addi':'000','sltiu':'011','jair':'000',
#         'sw':'010',
#         'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}



# #dictionary of instructions and and their funct7 values
# funct7={'add':'0000000', 'sub':'0100000', 'sll':'0000000', 'slt':'0000000',
#         'sltu':'0000000', 'xor':'0000000', 'srl':'0000000', 'or':'0000000','and':'0000000'}

# #dictionary of registers and their addresses
# registers={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100',
#            't0':'00101','t1':'00110','t2':'00111','s0':'01000','s1':'01001',
#            'a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110',
#            'a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011',
#            's4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000',
#            's9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101',
#            't5':'11110','t6':'11111'}



# def add(lst):
# 	new_list=[]
# 	new_list.append(funct7[lst[0]])
# 	new_list.append(registers[lst[3]])
# 	new_list.append(registers[lst[2]])
# 	new_list.append(funct3[lst[0]])
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0110011')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str
    
# def sub(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str



# def sll(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str


# def slt(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str


# def sltu(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str


# def xor(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str



# def srl(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str

# def OR(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str

# def AND(lst):
#     new_list=[]
#     new_list.append(funct7[lst[0]])
#     new_list.append(registers[lst[3]])
#     new_list.append(registers[lst[2]])
#     new_list.append(funct3[lst[0]])
#     new_list.append(registers[lst[1]])
#     new_list.append('0110011')
#     str=""
#     for i in new_list:
#       str+=i
#     return str

# #function for I-type instructions

# def lw(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(12,int(lst[2]))
# 	new_list.append(imm_str[-12:])
# 	new_list.append(registers[lst[3]])
# 	new_list.append("010")
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0000011')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# def addi(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(12,int(lst[3]))
# 	new_list.append(imm_str[-12:])
# 	new_list.append(registers[lst[2]])
# 	new_list.append("000")
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0010011')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# def sltiu(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(12,int(lst[3]))
# 	new_list.append(imm_str[-12:])
# 	new_list.append(registers[lst[2]])
# 	new_list.append("011")
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0010011')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# def jalr(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(12,int(lst[3]))
# 	new_list.append(imm_str[-12:])
# 	new_list.append(registers[lst[2]])
# 	new_list.append("000")
# 	new_list.append(registers[lst[1]])
# 	new_list.append('1100111')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# #function for S-type instructions
# def sw(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(12,int(lst[2]))
# 	new_list.append(imm_str[:-5])
# 	new_list.append(registers[lst[1]])
# 	new_list.append(registers[lst[3]])
# 	new_list.append(funct3[lst[0]])
# 	new_list.append(imm_str[-5:])
# 	new_list.append('0100011')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# #function for U-type instructions

# def lui(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(32,int(lst[2]))
# 	new_list.append(imm_str[:-12])
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0110111')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# def auipc(lst):
# 	new_list=[]
# 	imm_str=binary_convertor(32,int(lst[2]))
# 	new_list.append(imm_str[:-12])
# 	new_list.append(registers[lst[1]])
# 	new_list.append('0010111')
# 	str=""
# 	for i in new_list:
# 		str+=i
# 	return str

# #function for J-type instructions
# def jal(lst):
#   new_list=[]
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(20,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(20, int(imm))
#   new_list.append(imm_str[-20]+imm_str[-11:-1]+imm_str[-11]+imm_str[-20:-12])
#   new_list.append(registers[lst[1]])
#   new_list.append('1101111')
#   str=""
#   for i in new_list:
#     str+=i
#   return str

# # #function for B-type instructions
# def beq(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))

#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[2])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str



# def bne(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))
#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[-13])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str


# def bge(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))
#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[2])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str

# def bgeu(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))
#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[2])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str

# def blt(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))
#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[2])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str

# def bltu(lst,n):
#   try :
#     a=int(lst[2])
#     imm_str=binary_convertor(13,int(lst[2]))
#   except:
#     imm=label_convertor(lst[2],lst)
#     imm=binary_convertor(13, int(imm))
#   new_list=[]
#   new_list.append(imm[0])
#   new_list.append(imm[2:8])
#   new_list.append(registers[lst[2]])
#   new_list.append(registers[lst[1]])
#   new_list.append(funct3[lst[0]])
#   new_list.append(imm[-5:-1])
#   new_list.append(imm[2])
#   new_list.append('1100011')
#   str=""
#   for i in new_list:
#     str+=i
#   return str

# output_list=[]



# program_counter=0
# flag = 1
# for i in instructions:
 
#   if (i[0] == "add"):
#     if len(i) == 4:
#         # print(add(i))
#         output_list.append(add(i))
#         program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "sub"):
#     if len(i) == 4:
#       # print(sub(i))
#       output_list.append(sub(i))     
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1    

#   elif (i[0] == "sll"):
#     if len(i) == 4:
#       # print(sll(i))
#       output_list.append(sll(i))   
#       program_counter+=1
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "slt"):
#     if len(i) == 4:
#       # print(slt(i))
#       output_list.append(slt(i))

#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1  

#   elif (i[0] == "sltu"):
#     if len(i) == 4:
#       # print(sltu(i))
#       output_list.append(sltu(i))
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1    

#   elif (i[0] == "xor"):
#     if len(i) == 4:
#       # print(xor(i))
#       output_list.append(xor(i))
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1  

#   elif (i[0] == "srl"):
#     if len(i) == 4:
#       # print(srl(i))
#       output_list.append(srl(i))
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1         

#   elif (i[0] == "or"):
#     if len(i) == 4:
#       # print(OR(i))
#       output_list.append(OR(i))
         
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1 
   
#   elif (i[0] == "and"):
#     if len(i) == 4:
#       # print(OR(i))
#       output_list.append(AND(i))
         
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1 



#   elif (i[0] == "lw"):
#     if len(i) == 4:   
#       # print(lw(i))
#       output_list.append(lw(i))
      
#       program_counter+=1

#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1
    
#   elif (i[0] == "addi"):
#     if len(i) == 4: 
#     #  print(addi(i))
#      output_list.append(addi(i))
#      program_counter+=1   
      
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "sltiu"):
#     if len(i) == 4:
#       # print(sltiu(i))
#       output_list.append(sltiu(i))
#       program_counter+=1
      
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "jalr"):
#     if len(i) == 4:
#       # print(jalr(i))
#       output_list.append(jalr(i))
#       program_counter+=1
      
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "sw"):
#     if len(i) == 4:
#       # print(sw(i))
#       output_list.append(sw(i))
#       program_counter+=1
      
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "lui"):
#     if len(i) == 3:
#       # print(lui(i))
#       output_list.append(lui(i))
#       program_counter+=1
      
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1
    
#   elif (i[0] == "auipc"):
#     if len(i) == 3:
#       # print(auipc(i))
#       output_list.append(auipc(i))
#       program_counter+=1
#     else:
#       print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
#       flag = 0
#       program_counter+=1

#   elif (i[0] == "jal"):
#     if len(i) == 3:
#       # print(jal(i))
#       output_list.append(jal(i))
#       program_counter+=1
      
#   elif (i[0] == "beq"):
#         if len(i) == 4:
#             # print(beq(i,i[3]))
#             output_list.append(beq(i,i[3]))
#             program_counter+=1
#         else:
#             print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
#             flag = 0
#             program_counter+=1
#   elif (i[0] == "bne"):
#         if len(i) == 4:
#             # print(bne(i,i[3]))
#             output_list.append(bne(i,i[3]))
      
#             program_counter+=1
  
#         else:
#             print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
#             flag = 0
#   elif (i[0] == "bge"):
#         if len(i) == 4:
#             # print(bge(i,i[3]))
#             output_list.append(bge(i,i[3]))
      
#             program_counter+=1
#         else:
#             print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
#             flag = 0
#   elif (i[0] == "bgeu"):
#         if len(i) == 4:
#             # print(bgeu(i,i[3]))
#             output_list.append(bgeu(i,i[3]))
  
#             program_counter+=1
#         else:
#             print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
#             flag = 0


#   elif (i[0] == "blt"):
#         if len(i) == 4:
#             # print(blt(i,i[3]))
#             output_list.append(blt(i,i[3]))
#             program_counter+=1
      
#         else:
#             print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
#             flag = 0

#   elif (i[0] == "bltu"):
#         if len(i) == 4:
#             # print(bltu(i,i[3]))
#             output_list.append(bltu(i,i[3]))     
#             program_counter+=10
      
#   else:
#         with open file1
#         print("instructiontype error found :")
#         flag = 0   
#         program_counter+=1
#         break

# # co\ggh
# print(output_list)
# with open(file_output,"w") as file1:
#     Instruction_function = [instructions[i][0] for i in range(len(instructions))]
#     if("hlt" in Instruction_function):
#         if(Instruction_function[-1]!="hlt"):
#             file1.write("\nhlt not being used as the last instruction\n")  #virtual halt must be used as the last instruction.
#             quit()
#     else:     #Checking if hlt is present in the program if it doesn't exist the program will not continue.
#         file1.write(f"\nError: No virtual hlt present.\n")
#         quit()
#     for i in output_list:
#         file1.write(i)
#         file1.write("\n")      
   
import sys
file_input = sys.argv[1]
file_output = sys.argv[2]



# import pandas as pd
# data = pd.read_csv(file_input)
# print(data)

import re
file=open(file_input)
instructions=[]
i=0
for s in file:
  s=s.replace("(", ' ')
  s=s.replace(")", ' ')
  instructions.append(re.split(' |, | , | ,|,|\n', s))
  for i in instructions:
    for j in i:
        if j=='':
         i.remove(j)
         
# print(instructions)

def binary_convertor(b,n):
    nbits = n.bit_length() + 1

    binary=f"{n & ((1 << nbits) - 1):0{nbits}b}"
    if n>=0:
        binary=(b-nbits)*'0'+binary
        return binary
    else:
        binary=(b-nbits)*'1'+binary
        return binary
    
inst1=instructions.copy()
for i in range(len(instructions)):
    if ':' in instructions[i][0]:
        instructions[i].remove(instructions[i][0])


def label_convertor(labelname, labelLine):
    num1=0
    num2=0

    for i in inst1:
        if i[0]==labelname:
           num1=i
        if i[-1]==labelname:
            num2=i
    return (num2-num1)*4
    
funct3={'add':'000', 'sub':'000', 'sll':'001', 'slt':'010',
        'sltu':'011', 'xor':'100', 'srl':'101', 'or':'110','and':'111',
        'lw':'010','addi':'000','sltiu':'011','jair':'000',
        'sw':'010',
        'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}



#dictionary of instructions and and their funct7 values
funct7={'add':'0000000', 'sub':'0100000', 'sll':'0000000', 'slt':'0000000',
        'sltu':'0000000', 'xor':'0000000', 'srl':'0000000', 'or':'0000000','and':'0000000'}

#dictionary of registers and their addresses
registers={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100',
           't0':'00101','t1':'00110','t2':'00111','s0':'01000','s1':'01001',
           'a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110',
           'a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011',
           's4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000',
           's9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101',
           't5':'11110','t6':'11111'}

def add(lst):
	new_list=[]
	new_list.append(funct7[lst[0]])
	new_list.append(registers[lst[3]])
	new_list.append(registers[lst[2]])
	new_list.append(funct3[lst[0]])
	new_list.append(registers[lst[1]])
	new_list.append('0110011')
	str=""
	for i in new_list:
		str+=i
	return str
    
def sub(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str



def sll(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str


def slt(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str


def sltu(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str


def xor(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str



def srl(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str

def OR(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str

def AND(lst):
    new_list=[]
    new_list.append(funct7[lst[0]])
    new_list.append(registers[lst[3]])
    new_list.append(registers[lst[2]])
    new_list.append(funct3[lst[0]])
    new_list.append(registers[lst[1]])
    new_list.append('0110011')
    str=""
    for i in new_list:
      str+=i
    return str

#function for I-type instructions

def lw(lst):
	new_list=[]
	imm_str=binary_convertor(12,int(lst[2]))
	new_list.append(imm_str[-12:])
	new_list.append(registers[lst[3]])
	new_list.append("010")
	new_list.append(registers[lst[1]])
	new_list.append('0000011')
	str=""
	for i in new_list:
		str+=i
	return str

def addi(lst):
	new_list=[]
	imm_str=binary_convertor(12,int(lst[3]))
	new_list.append(imm_str[-12:])
	new_list.append(registers[lst[2]])
	new_list.append("000")
	new_list.append(registers[lst[1]])
	new_list.append('0010011')
	str=""
	for i in new_list:
		str+=i
	return str

def sltiu(lst):
	new_list=[]
	imm_str=binary_convertor(12,int(lst[3]))
	new_list.append(imm_str[-12:])
	new_list.append(registers[lst[2]])
	new_list.append("011")
	new_list.append(registers[lst[1]])
	new_list.append('0010011')
	str=""
	for i in new_list:
		str+=i
	return str

def jalr(lst):
	new_list=[]
	imm_str=binary_convertor(12,int(lst[3]))
	new_list.append(imm_str[-12:])
	new_list.append(registers[lst[2]])
	new_list.append("000")
	new_list.append(registers[lst[1]])
	new_list.append('1100111')
	str=""
	for i in new_list:
		str+=i
	return str

#function for S-type instructions
def sw(lst):
	new_list=[]
	imm_str=binary_convertor(12,int(lst[2]))
	new_list.append(imm_str[:-5])
	new_list.append(registers[lst[1]])
	new_list.append(registers[lst[3]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm_str[-5:])
	new_list.append('0100011')
	str=""
	for i in new_list:
		str+=i
	return str

#function for U-type instructions

def lui(lst):
	new_list=[]
	imm_str=binary_convertor(32,int(lst[2]))
	new_list.append(imm_str[:-12])
	new_list.append(registers[lst[1]])
	new_list.append('0110111')
	str=""
	for i in new_list:
		str+=i
	return str

def auipc(lst):
	new_list=[]
	imm_str=binary_convertor(32,int(lst[2]))
	new_list.append(imm_str[:-12])
	new_list.append(registers[lst[1]])
	new_list.append('0010111')
	str=""
	for i in new_list:
		str+=i
	return str

#function for J-type instructions
def jal(lst):
	new_list=[]
	imm_str=binary_convertor(20,int(lst[2]))
	new_list.append(imm_str[-20]+imm_str[-11:-1]+imm_str[-11]+imm_str[-20:-12])
	new_list.append(registers[lst[1]])
	new_list.append('1101111')
	str=""
	for i in new_list:
		str+=i
	return str

# #function for B-type instructions
def beq(lst,n):
	if (n.isdigit()):
		imm=binary_convertor(13,int(n))
	else:
		imm=label_convertor(lst[2],lst)
		imm=binary_convertor(13, int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[2])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str



def bne(lst,n):
	if  n.isdigit():
		imm=binary_convertor(13,int(n))
	else:
		imm = label_convertor(lst[2],lst)
		imm=binary_convertor(13,int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[-13])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str


def bge(lst,n):
	if  n.isdigit():
		imm=binary_convertor(13,int(n))
	else:
		imm = label_convertor(lst[2],lst)
		imm=binary_convertor(13,int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[2])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str

def bgeu(lst,n):
	if  n.isdigit():
		imm=binary_convertor(13,int(n))
	else:
		imm = label_convertor(lst[2],lst)
		imm=binary_convertor(13,int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[2])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str

def blt(lst,n):
	if  n.isdigit():
		imm=binary_convertor(13,int(n))
	else:
		imm = label_convertor(lst[2],lst)
		imm=binary_convertor(13,int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[2])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str

def bltu(lst,n):
	if  n.isdigit():
		imm=binary_convertor(13,int(n))
	else:
		imm = label_convertor(lst[2],lst)
		imm=binary_convertor(13,int(imm))
	new_list=[]
	new_list.append(imm[0])
	new_list.append(imm[2:8])
	new_list.append(registers[lst[2]])
	new_list.append(registers[lst[1]])
	new_list.append(funct3[lst[0]])
	new_list.append(imm[-5:-1])
	new_list.append(imm[2])
	new_list.append('1100011')
	str=""
	for i in new_list:
		str+=i
	return str

output_list=[]
program_counter=0
flag = 1
for i in instructions:

  if (i[0] == "add"):
    if len(i) == 4:
        # print(add(i))
        output_list.append(add(i))
        program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "sub"):
    if len(i) == 4:
      # print(sub(i))
      output_list.append(sub(i))     
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1    

  elif (i[0] == "sll"):
    if len(i) == 4:
      # print(sll(i))
      output_list.append(sll(i))   
      program_counter+=1
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "slt"):
    if len(i) == 4:
      # print(slt(i))
      output_list.append(slt(i))

      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1  

  elif (i[0] == "sltu"):
    if len(i) == 4:
      # print(sltu(i))
      output_list.append(sltu(i))
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1    

  elif (i[0] == "xor"):
    if len(i) == 4:
      # print(xor(i))
      output_list.append(xor(i))
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1  

  elif (i[0] == "srl"):
    if len(i) == 4:
      # print(srl(i))
      output_list.append(srl(i))
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1         

  elif (i[0] == "or"):
    if len(i) == 4:
      # print(OR(i))
      output_list.append(OR(i))
         
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1 
   
  elif (i[0] == "and"):
    if len(i) == 4:
      # print(OR(i))
      output_list.append(AND(i))
         
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1 



  elif (i[0] == "lw"):
    if len(i) == 4:   
      # print(lw(i))
      output_list.append(lw(i))
      
      program_counter+=1

    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1
    
  elif (i[0] == "addi"):
    if len(i) == 4: 
    #  print(addi(i))
     output_list.append(addi(i))
     program_counter+=1   
      
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "sltiu"):
    if len(i) == 4:
      # print(sltiu(i))
      output_list.append(sltiu(i))
      program_counter+=1
      
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "jalr"):
    if len(i) == 4:
      # print(jalr(i))
      output_list.append(jalr(i))
      program_counter+=1
      
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "sw"):
    if len(i) == 4:
      # print(sw(i))
      output_list.append(sw(i))
      program_counter+=1
      
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "lui"):
    if len(i) == 3:
      # print(lui(i))
      output_list.append(lui(i))
      program_counter+=1
      
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1
    
  elif (i[0] == "auipc"):
    if len(i) == 3:
      # print(auipc(i))
      output_list.append(auipc(i))
      program_counter+=1
    else:
      print("\nError in Line", program_counter + 1,": add must contain 3 parameters\n")
      flag = 0
      program_counter+=1

  elif (i[0] == "jal"):
    if len(i) == 3:
      # print(jal(i))
      output_list.append(jal(i))
      program_counter+=1
      
  elif (i[0] == "beq"):
        if len(i) == 4:
            # print(beq(i,i[3]))
            output_list.append(beq(i,i[3]))
            program_counter+=1
        else:
            print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
            flag = 0
            program_counter+=1
  elif (i[0] == "bne"):
        if len(i) == 4:
            # print(bne(i,i[3]))
            output_list.append(bne(i,i[3]))
      
            program_counter+=1
  
        else:
            print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
            flag = 0
  elif (i[0] == "bge"):
        if len(i) == 4:
            # print(bge(i,i[3]))
            output_list.append(bge(i,i[3]))
      
            program_counter+=1
        else:
            print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
            flag = 0
  elif (i[0] == "bgeu"):
        if len(i) == 4:
            # print(bgeu(i,i[3]))
            output_list.append(bgeu(i,i[3]))
  
            program_counter+=1
        else:
            print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
            flag = 0


  elif (i[0] == "blt"):
        if len(i) == 4:
            # print(blt(i,i[3]))
            output_list.append(blt(i,i[3]))
            program_counter+=1
      
        else:
            print("\nError in Line",0 +  0  + program_counter + 1,": add must contain 3 parameters\n")
            flag = 0

  elif (i[0] == "bltu"):
        if len(i) == 4:
            # print(bltu(i,i[3]))
            output_list.append(bltu(i,i[3]))     
            program_counter+=10
      
  else:
        print("instructiontype error found :")
        flag = 0   
        program_counter+=1
        break

# co\ggh
# print(output_list)
with open(file_output,"w") as file1:
    for i in output_list:
        file1.write(i)
        file1.write("\n")      
   



    

 

        




    

 

        
