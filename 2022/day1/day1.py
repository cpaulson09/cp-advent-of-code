with open('data.txt', 'r') as data:
    first, second, third, current = 0, 0, 0, 0
    for i in enumerate(data):
        row = i[1].rstrip('\n')
        if row:
            current = current + int(row)
        else:
            if current > first:
                third = second # make it 3rd
                second = first # make it 2nd
                first = current
            elif current > second:
                second = current
            elif current > third:
                third = current
            current = 0 # reset (blank line, new elf)
    print('total: ', first + second + third)