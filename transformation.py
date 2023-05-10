# First way

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
    print("First way")
    result = ''.join(str(item) for item in u)
    print(result)
    print("Done!")
    

# Second way
asci_i = []

for i in x:
    asci_i.append(hex(ord(i)).lstrip("0x"))
    


#print(asci_i)
print("Second way")
for n in asci_i:
    print(bytearray.fromhex(n).decode(), end="")
