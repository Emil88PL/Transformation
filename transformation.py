x = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
z = []
u = []

try:
    for letter in x:
        encoded_letter_down = ord(letter)>>8
        encoded_down = chr(encoded_letter_down) 
        #print(encoded_down)
        #print(encoded_letter_down)
        
        u.append(encoded_down)
        
        encoded_letter_up = chr((ord(letter))-((ord(letter)>>8)<<8))
        y = encoded_letter_up
        #print(y)
        
       
        #encoded_letter_up = ord(letter)<<8
        #print(chr(encoded_letter_up))
        u.append(y)
       
       
finally:
    result = ''.join(str(item) for item in u)
    print(result)
    print("Done!")