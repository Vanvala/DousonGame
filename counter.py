# This prog count for player

begin = int(input('Enter begining of the count:'))
end = int(input('Enter ending of the count, not include:'))
interval = int(input('Enter interval of the count:'))

for i in range(begin, end, interval):
    print(i)
