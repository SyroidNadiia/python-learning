num = int(input('Enter num: '))

if num >= 55: 
    print('yes')
    if num == 100:
        print("Num is 100")
elif num == 40:
    print("num is 40")
else: 
    print('Else')
    
# тернарний оператор
data = "info"
correct = True if data == "info" else False
