import time
while True:
    print ('Enter your text:')
    text = input ()
    alphabet = 'abcdefghıijklmnoöpqrsştuüvyz.? '
    animated_text_list = list()
    
    for i in range(len(text)):
        index = alphabet[0:alphabet.index(text[i])+1]
        
        animated_text_list.append(index)
    
    print ('---------------------------')
    
    for i in range(len(animated_text_list)):   
        for m in range(len(animated_text_list[i])):
            print(f'\r{ text[0:i]+ animated_text_list[i][m]}', end= ''),
            time.sleep(.015)
        

