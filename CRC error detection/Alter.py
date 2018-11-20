def Alter(correct_message , bit_position):
    num_bits = correct_message.bit_length()
    error_bit = 1 << (num_bits - bit_position)
    altered_msg = correct_msg ^ error_bit

    return altered_msg


#correct_msg = 50  #110010
#print(bin(Alter(correct_msg , 3)))
