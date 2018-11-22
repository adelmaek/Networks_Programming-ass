def Alter(correct_message , bit_position):
    correct_message = int(correct_message , 2)
    #print(correct_message)
    bit_position = int(bit_position)
    num_bits = correct_message.bit_length()
    if bit_position <  correct_message.bit_length():
        error_bit = 1 << (num_bits - bit_position)
        altered_msg =  correct_message ^ error_bit
    else :
        altered_msg =  correct_message
    print('altered message: ' + bin(altered_msg)[2:].zfill(correct_message.bit_length()))
    return bin(altered_msg)[2:].zfill(correct_message.bit_length()


#correct_msg = 50  #110010
#print(bin(Alter(correct_msg , 3)))
