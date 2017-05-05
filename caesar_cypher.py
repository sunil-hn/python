def rotate_word(string, shift):
    o_s = ""
    for i in range(0, len(string)):
        
        if (ord(string[i]) > 90):   #lower case 
            o_s = o_s + chr( int (((ord(string[i]) - 97 ) + shift)%26 + 97) )
        elif(ord(string[i]) == 32): #space
            o_s = o_s + string[i]
        else:                       #upper case 
            o_s = o_s + chr( int (((ord(string[i]) - 65 ) + shift)%26 + 65) )
            
    return o_s

print("Enter a string")
input_string = input()
print("Enter the shift")
num = input()
output_string = rotate_word(input_string, int(num))
print("Output string is", output_string)
