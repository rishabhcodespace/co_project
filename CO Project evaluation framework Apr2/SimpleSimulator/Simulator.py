import sys


def binary_convertor(b, n):
  nbits = n.bit_length() + 1
  binary = f"{n & ((1 << nbits) - 1):0{nbits}b}"

  if n >= 0:
    binary = (b - nbits) * '0' + binary
    return binary
  else:
    binary = (b - nbits) * '1' + binary
    return binary


def twos_complement_to_decimal(bin_str):
  bin_str = str(bin_str)
  if bin_str[0] == '1':
    inverted_bin_str = ''.join('1' if bit == '0' else '0' for bit in bin_str)
    positive_equivalent = int(inverted_bin_str, 2) + 1
    return -positive_equivalent
  else:
    return int(bin_str, 2)


registers = {
    '00000': 0,
    '00001': 0,
    '00010': 256,
    '00011': 0,
    '00100': 0,
    '00101': 0,
    '00110': 0,
    '00111': 0,
    '01000': 0,
    '01001': 0,
    '01010': 0,
    '01011': 0,
    '01100': 0,
    '01101': 0,
    '01110': 0,
    '01111': 0,
    '10000': 0,
    '10001': 0,
    '10010': 0,
    '10011': 0,
    '10100': 0,
    '10101': 0,
    '10110': 0,
    '10111': 0,
    '11000': 0,
    '11001': 0,
    '11010': 0,
    '11011': 0,
    '11100': 0,
    '11101': 0,
    '11110': 0,
    '11111': 0
}

def add(rd, rs1, rs2):
  global registers
  global pc
  rd1 = registers[rs1] + registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = registers[rs2
  # return registers


def sub(rd, rs1, rs2):
  global pc
  global registers
  rd1 = registers[rs1] - registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2
  # return registers


def slt(rd, rs1, rs2):
  global registers
  global pc
  if binary_convertor(32,
                      registers[rs1]) < binary_convertor(32, registers[rs2]):
    rd1 = 1
    registers[rd] = rd1
    # registers[rs1] = rs1
    # registers[rs2] = rs2
  # return registers


def sltu(rd, rs1, rs2):
  global pc
  global registers
  new_list = []
  if binary_convertor(32,
                      registers[rs1]) < binary_convertor(32, registers[rs2]):
    rd1 = 1
    registers[rd] = rd1
    # registers[rs1] = rs1
    # registers[rs2] = rs2
    # return registers


def xor(rd, rs1, rs2):
  global pc
  global registers
  # rd = xor_convertor(rs1, rs2)
  # def getXOR(x, y):
  #   return (x | y) & (~x | ~y)
  rd1 = registers[rs1] ^ registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2


def sll(rd, rs1, rs2):
  global pc
  global registers

  rd1 = registers[rs1] << registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2

  # return registers


def srl(rd, rs1, rs2):
  global pc
  global registers
  rd1 = registers[rs1] >> registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2
  # return registers


def or_(rd, rs1, rs2):
  global pc
  global registers
  rd1 = registers[rs1] | registers[rs2]
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2
  # # return registers


def and_(rd, rs1, rs2):
  global pc
  global registers
  rd1 = int(registers[rs1]) & int(registers[rs2])
  registers[rd] = rd1
  # registers[rs1] = rs1
  # registers[rs2] = rs2
  # return registers


def beq(imm, rs1, rs2):
  global pc
  if rs1 == rs2:
    pc = pc + twos_complement_to_decimal(imm) - 4


def bne(imm, rs1, rs2):
  global pc
  if rs1 != rs2:
    pc = pc + twos_complement_to_decimal(imm) - 4


def bge(imm, rs1, rs2):
  global pc
  if rs1 >= rs2:
    pc = pc + twos_complement_to_decimal(imm) - 4


def bgeu(imm, rs1, rs2):
  global pc
  if binary_convertor(32, rs1) >= binary_convertor(32, rs2):
    pc = pc + twos_complement_to_decimal(imm) - 4


def blt(imm, rs1, rs2):
  global pc
  if rs1 <= rs2:
    pc = pc + twos_complement_to_decimal(imm) - 4


def bltu(imm, rs1, rs2):
  global pc
  if binary_convertor(32, rs1) <= binary_convertor(32, rs2):
    pc = pc + twos_complement_to_decimal(imm) - 4


def main(file_in, file_out):
  global pc
  with open(file_in, 'r') as f:
    instructions = f.readlines()

  typeR_list = ['0110011']
  typeS_list = ['0100011']
  typeI_list = ['0000011', '0010011', '1100111']
  typeB_list = ['1100011']
  typeU_list = ['0110111', '0010111']
  typeJ_list = ['1101111']

  def typeR(instruction):
    global pc
    global registers
    rd = instruction[-12:-7]
    rs1 = instruction[-20:-15]
    rs2 = instruction[-25:-20]

    if instruction[-15:-12] == '000':
      if instruction[-32:-25] == '0000000':
        add(rd, rs1, rs2)

      elif instruction[-32:-25] == '0100000':
        sub(rd, rs1, rs2)

    elif instruction[-15:-12] == '001':
      sll(rd, rs1, rs2)

    elif instruction[-15:-12] == '010':
      slt(rd, rs1, rs2)

    elif instruction[-15:-12] == '011':
      sltu(rd, rs1, rs2)

    elif instruction[-15:-12] == '100':
      xor(rd, rs1, rs2)

    elif instruction[-15:-12] == '101':
      srl(rd, rs1, rs2)

    elif instruction[-15:-12] == '110':
      or_(rd, rs1, rs2)

    elif instruction[-15:-12] == '111':
      and_(rd, rs1, rs2)

  def typeI(instruction):
    global pc
    rd = instruction[-12:-7]
    imm = instruction[-32:-20]
    rs = instruction[-20:-15]
    if instruction[-7:] == '0000011':
      registers[rd] = twos_complement_to_decimal(mem[hex(
          registers[rs] + twos_complement_to_decimal(imm))])  #lw instruction
    elif instruction[-7:] == '0010011':
      if instruction[-15:-12] == '000':
        registers[rd] = registers[rs] + twos_complement_to_decimal(
            imm)  #adi instruction
      elif instruction[-15:-12] == '011':
        if binary_convertor(registers[rs]) < binary_convertor(
            twos_complement_to_decimal(imm)):  #sltiu instruction
          registers[rd] = 1
    elif instruction[-7:] == '1100111':
      rd = pc + 4
      pc = (registers[rs] + twos_complement_to_decimal(imm))
      pc = binary_convertor(32,pc)
      pc = pc[:-1] + '0'
      pc = twos_complement_to_decimal(pc)-4

  def typeB(instruction):
    imm = instruction[-32] + instruction[-8] + instruction[
        -31:-25] + instruction[-12:-8] + '0'
    rs1 = registers[instruction[-20:-15]]
    rs2 = registers[instruction[-25:-20]]
    if instruction[-15:-12] == '000':
      beq(imm, rs1, rs2)
    elif instruction[-15:-12] == '001':
      bne(imm, rs1, rs2)
    elif instruction[-15:-12] == '100':
      blt(imm, rs1, rs2)
    elif instruction[-15:-12] == '101':
      bge(imm, rs1, rs2)
    elif instruction[-15:-12] == '110':
      bltu(imm, rs1, rs2)
    elif instruction[-15:-12] == '111':
      bgeu(imm, rs1, rs2)
  
  def typeU(instruction):
    global pc
    imm = instruction[-32:-12]
    rd=instruction[-12:-7]
    if instruction[-7:] == '0110111':
      registers[rd] = twos_complement_to_decimal(imm + '000000000000')
    elif instruction[-7:] == '0010111':
      imm = twos_complement_to_decimal(imm)
      registers[rd] = pc + (imm << 12) 

  mem = {
      '0x10000': 0,
      '0x10004': 0,
      '0x10008': 0,
      '0x1000c': 0,
      '0x10010': 0,
      '0x10014': 0,
      '0x10018': 0,
      '0x1001c': 0,
      '0x10020': 0,
      '0x10024': 0,
      '0x10028': 0,
      '0x1002c': 0,
      '0x10030': 0,
      '0x10034': 0,
      '0x10038': 0,
      '0x1003c': 0,
      '0x10040': 0,
      '0x10044': 0,
      '0x10048': 0,
      '0x1004c': 0,
      '0x10050': 0,
      '0x10054': 0,
      '0x10058': 0,
      '0x1005c': 0,
      '0x10060': 0,
      '0x10064': 0,
      '0x10068': 0,
      '0x1006c': 0,
      '0x10070': 0,
      '0x10074': 0,
      '0x10078': 0,
      '0x1007c': 0
  }  #dict to store memory address and its values
  c = 0
  pc = 0
  while (pc <= 128):
    instruction = instructions[c].strip()
    if instruction == '00000000000000000000000001100011':
      break
    op = instruction[-7:]
    if op in typeR_list:
      typeR(instruction)

    elif op in typeI_list:
      typeI(instruction)

    elif op in typeS_list:

      imm = instruction[-32:-25] + instruction[-12:-7]
      rs2 = instruction[-25:-20]
      rs1 = instruction[-20:-15]
      mem[hex(registers[rs1] +
              twos_complement_to_decimal(imm))] = binary_convertor(
                  32, registers[rs2])

    elif op in typeB_list:
      typeB(instruction)

    elif op in typeU_list:
      typeU(instruction)

    elif op in typeJ_list:
      imm = instruction[-32] + instruction[-20:-12] + instruction[
          -21] + instruction[-31:-21] + '0'
      rd = instruction[-12:-7]
      registers[rd] = pc + 4
      pc += twos_complement_to_decimal(imm)
      pc = binary_convertor(32,pc)
      pc = pc[:-1] + '0'
      pc = twos_complement_to_decimal(pc) -4

    pc += 4
    c = pc // 4

    with open(file_out, 'a') as f:
      f.write('0b')
      f.write(binary_convertor(32, pc))
      f.write(' ')
      for i in registers.keys():
        f.write('0b')
        f.write(binary_convertor(32, int(registers[i])))
        f.write(' ')
      f.write('\n')
  with open(file_out, 'a') as f:
    f.write('0b')
    f.write(binary_convertor(32, pc))
    f.write(' ')
    for i in registers.keys():
      f.write('0b')
      f.write(binary_convertor(32, int(registers[i])))
      f.write(' ')
    f.write('\n')
  with open(file_out, 'a') as f:
    for i in mem.keys():
      f.write(f'0x000{i[2:]}')
      f.write(':0b')
      f.write(str(binary_convertor(32,int(twos_complement_to_decimal(mem[i])))))
      f.write('\n')
file_input = sys.argv[1]
file_output = sys.argv[2]  
with open(file_output, 'w') as f:
  f.write('')
main(file_input, file_output)
