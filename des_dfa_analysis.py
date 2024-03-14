PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# SBOX
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# S box as key, storing the affected faults that end up in the S box
S_BOX_AFFECTED = {0: [1, 2, 3, 4, 5, 32],
                  1: [4, 5, 6, 7, 8, 9],
                  2: [8, 9, 10, 11, 12, 13],
                  3: [12, 13, 14, 15, 16, 17],
                  4: [16, 17, 18, 19, 20, 21],
                  5: [20, 21, 22, 23, 24, 25],
                  6: [24, 25, 26, 27, 28, 29],
                  7: [1, 28, 29, 30, 31, 32]}

real_cipher_6_bits_expanded = None
faulty_cipher_6_bits_expanded = {}

real_cipher = ['ßåýåÚ\x9f\\\x9d']
faulty_ciphertexts = ['ßàýáÚ\x9e\\\x19', 'ßäýåÚ\x9fÜ\x89', 'ßàýåÚ\x1f\\\x9d',
               'ßåýå[\x9f\x1c\x89', 'ßäýuÛ\x9fX\x89', 'ßå}õÚ\x9fX\x9d', 'ßeýõÛ\x9f\\\x9d', 'KåüõÚ\x9f\x18\x9d', 'Ëå¼õÚ\x9f\x18½', 'ßå¼åÚ\x9f|\x9d', 'ÛåüåÚ¿\\\x9d', 'Ïå¼åú\x9fLÝ', 'Ëå¼ÅÚ\x9fMÝ', 'ßåÝåÚ\x9fLÝ', 'ßÅýåÞ\x9fMÝ', 'ÿåíåÞß]Ü', '\x9fåíåÞß\\Ô', 'ßåíåÚ\x9fT\x9c', '\x9fåýåÚ×\\\x9d', 'ßåíä\x92Ï\\\x9c', '\x9fåííÚË\\\x9c', 'ßåõäÚ\x8f\\\x9d', 'ßíýå\x9a\x8b\\\x9d', '×¥ýä\x8a\x8f\\\x9d', 'Þ¥ùäÊ\x8f\\\x9f', 'ß¥ùåÊ\x9f^\x9d', 'Þ¥ùåÚ\x9d\\\x9d', 'ßµýáÈ\x9f\\\x9d', 'Þµý£Ê\x9f\\\x9d', 'ßõÿ¥Ú\x9f\\\x9d', 'ßçý¥Ú\x9e\\\x9d', 'ÝàýáÚ\x9e\\\x8d']


def string_to_bit_array(text):  # Convert a string into a list of bits
    array = list()
    for char in text:
        binval = binvalue(char, 8)  # Get the char value on one byte
        array.extend(
            [int(x) for x in list(binval)])  # Add the bits to the final list
    return array

def bit_array_to_string(array):  # Recreate the string from the bit array
    res = ''.join([chr(int(y, 2)) for y in
                   [''.join([str(x) for x in _bytes]) for _bytes in
                    nsplit(array, 8)]])
    return res

'''Takes in a decimal number and the bit field, returns the string 
representation of the decimal number '''
def binvalue(val,
             bitsize):  # Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0" + binval  # Add as many 0 as needed to get the wanted size
    return binval

def nsplit(s, n):  # Split a list into sublists of size "n"
    return [s[k:k + n] for k in range(0, len(s), n)]

'''Transforms the string representation of a binary value into a list'''
def binvalue_to_bit_array(bit_string):
    bit_arr = [None] * len(bit_string)
    for i in range(len(bit_string)):
        bit_arr[i] = int(bit_string[i])
    return bit_arr

def reverse_table(table, output_arr, input_arr):
    for i in range(len(input_arr)):
        output_arr[table[i] - 1] = input_arr[i]
    return [value for value in output_arr]

def expand(table, block):
    return [block[x - 1] for x in table]

def xor_function(t1, t2):
    return [x ^ y for x, y in zip(t1, t2)]

def bit_array_to_decimal(bit_array):
    power = len(bit_array) - 1
    sum = 0
    for bit_value in bit_array:
        if (int(bit_value) == 1):
            sum += pow(2, power)
        power -= 1
    return sum

def substitute_six_bits(sbox_input, sbox):
    row = int(str(sbox_input[0]) + str(sbox_input[5]), 2)
    column = int(str(sbox_input[1]) + str(sbox_input[2]) + str(sbox_input[3])\
             + \
             str(sbox_input[4]), 2)
    return sbox[row][column]


real_cipher_r16_block = None
faulty_cipher_r16_blocks = {}

PI_1_bits = string_to_bit_array(real_cipher[0])
r16_l16 = [0] * len(PI_1_bits)

# Reverse Inverse Permutation
r16_l16 = reverse_table(PI_1, r16_l16, PI_1_bits)
r16_l16_subset = nsplit(r16_l16, 32)

# Retrieve L16 and R16 blocks
r16_block = [value for value in r16_l16_subset[0]]
l16_block = [value for value in r16_l16_subset[1]]
# Save R16 Block for final comparison
real_cipher_r16_block = [value for value in r16_block]
# print(real_cipher_r16_block)
real_cipher_r16_block = nsplit(real_cipher_r16_block, 4)
# print(real_cipher_r16_block)

# Retrieve and expand r_15 block out
r15_block = l16_block
expanded_r15_block = expand(E, r15_block)
res = nsplit(expanded_r15_block, 6)
real_cipher_6_bits_expanded = [val for val in res]
fault = 1

# Retrieve and expand r_15 block out for all faulty ciphertexts
for i in range(len(faulty_ciphertexts)):
    PI_1_bits_faulty = string_to_bit_array(faulty_ciphertexts[i])
    r16_l16_faulty = [0] * len(PI_1_bits_faulty)

    r16_l16_faulty = reverse_table(PI_1, r16_l16_faulty, PI_1_bits_faulty)
    r16_l16_subset_faulty = nsplit(r16_l16_faulty, 32)

    r16_block_faulty = [value for value in r16_l16_subset_faulty[0]]
    l16_block_faulty = [value for value in r16_l16_subset_faulty[1]]

    faulty_cipher_r16_blocks[fault] = [value for value in r16_block_faulty]

    r15_block_faulty = l16_block_faulty
    expanded_r15_block_faulty = expand(E, r15_block_faulty)

    res = nsplit(expanded_r15_block_faulty, 6)
    faulty_cipher_6_bits_expanded[fault] = [val for val in res]
    fault += 1

for key in faulty_cipher_r16_blocks:
    faulty_cipher_r16_blocks[key] = nsplit(faulty_cipher_r16_blocks[key], 4)

sbox_faulty_cipher_grouped_6_bits = {}
# retrieve all bits from faulted r15 blocks and put them in their respective
# s_box group
for s_box in S_BOX_AFFECTED:
    current_fault_list = S_BOX_AFFECTED[s_box]
    for val in current_fault_list:
        if s_box not in sbox_faulty_cipher_grouped_6_bits:
            sbox_faulty_cipher_grouped_6_bits[s_box] = list()
        sbox_faulty_cipher_grouped_6_bits[s_box].append(
            faulty_cipher_6_bits_expanded[val][s_box])

# initialize all the 6-bit key possibilities
six_bit_keys_possibilities = {}
for i in range(64):
    str_bit_value = binvalue(i, 6)
    six_bit_keys_possibilities[i] = binvalue_to_bit_array(str_bit_value)

s_box_key_matching_table = {0: list(),
                            1: list(),
                            2: list(),
                            3: list(),
                            4: list(),
                            5: list(),
                            6: list(),
                            7: list()}

# Brute force every key possibility for each S-BOX
# for curr_sbox in range(8):
#     all_combos = sbox_faulty_cipher_grouped_6_bits[curr_sbox]
#     for block in all_combos:
#         faulted_list = list()
#         for key_val in range(64):
#                 curr_key_value = six_bit_keys_possibilities[key_val]
#                 curr_SBOX_table = S_BOX[curr_sbox]
#                 s_box_fault_input = xor_function(block, curr_key_value)
#                 faulty_result = substitute_six_bits(s_box_fault_input,
#                                              curr_SBOX_table)
#                 s_box_real_input = xor_function(real_cipher_6_bits_expanded[
#                                                     curr_sbox], curr_key_value)
#                 real_result = substitute_six_bits(s_box_real_input,
#                                                   curr_SBOX_table)
#                 # print("real result: " + str(real_result) + " faulty result: "
#                 #       + str(faulty_result))
#
#                 if (real_result == faulty_result):
#                     faulted_list.append(bit_array_to_decimal(six_bit_keys_possibilities[
#                                             key_val]))
#         s_box_key_matching_table[curr_sbox].append(faulted_list)

# Brute force every key possibility for each S-BOX
for curr_sbox in range(8):
    curr_fault_list = S_BOX_AFFECTED[curr_sbox]
    for fault_num in curr_fault_list:
        curr_r16 = real_cipher_r16_block[curr_sbox]
        curr_r16_fault = faulty_cipher_r16_blocks[fault_num][curr_sbox]

        r16_xor_r16_fault = xor_function(curr_r16, curr_r16_fault)
        # print(r16_xor_r16_fault)
        # print(bit_array_to_decimal(r16_xor_r16_fault))

        all_combos = sbox_faulty_cipher_grouped_6_bits[curr_sbox]
        for fault_block in all_combos:
            hypotheses = list()
            for key_val in range(64):
                curr_key_block = six_bit_keys_possibilities[key_val]
                curr_sbox_table = S_BOX[curr_sbox]

                # S(E(R'15) XOR K16)
                sbox_fault_input = xor_function(fault_block, curr_key_block)
                faulty_result = substitute_six_bits(sbox_fault_input, curr_sbox_table)
                faulty_result_bit_array = binvalue_to_bit_array(binvalue(
                    faulty_result, 4))

                # S(E(R15) XOR K16)
                real_block = real_cipher_6_bits_expanded[curr_sbox]
                sbox_real_input = xor_function(real_block, curr_key_block)
                real_result = substitute_six_bits(sbox_real_input, curr_sbox_table)
                real_result_bit_array = binvalue_to_bit_array(binvalue(
                    real_result, 4))

                # S(E(R'15) XOR K16) XOR S(E(R15) XOR K16)
                resultant_xor = xor_function(faulty_result_bit_array,
                                             real_result_bit_array)

                print("resultant_xor:", resultant_xor)
                print("r16_xor_r16_fault:", r16_xor_r16_fault)
                print("------")

                if (resultant_xor == r16_xor_r16_fault):
                    hypotheses.append(curr_key_block)
            s_box_key_matching_table[curr_sbox].append(hypotheses)

print(s_box_key_matching_table)
