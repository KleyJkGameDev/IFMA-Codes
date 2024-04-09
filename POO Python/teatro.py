from time import sleep
message = "te amo minha princesa"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(message)):
    
    for j in range(len(alfabeto)):
        prefix = alfabeto[j]
        current_str = message[:i+1] + prefix
        if current_str == message:
            break
        sleep(0.01)
        print(current_str)
        
    if current_str == message:
        print(current_str)
        break
    
    for k in range(len(alfabeto)):
        prefix = alfabeto[k]
        current_str = message[:i+1] + prefix
        if current_str == message:
            break
        sleep(0.01)
        print(current_str)
    sleep(0.01)
