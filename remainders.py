data = []
remainders = []
result = []

while(True):
    number = input('Enter a number(If you want to exit enter stop):')

    if number == 'stop':
        break

    try:
        number = int(number)
        data.append(number)
    except:
        print(number + " not a number")
        pass

if len(data):
    for value in data:
        remainders.append(value%5)

    for index in range(len(data)):
        result.append(data[index] / remainders[index])

    print(result)
else:
    print("No numbers entered.")
