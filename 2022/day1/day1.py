with open('data.txt', 'r') as data:
    first = 0
    second = 0
    third = 0
    current = 0
    for i in enumerate(data):
        row = i[1].rstrip('\n')
        if row:
            current = current + int(row)
        else:
            # part 1
            if current > first:
                first = current

            # part 2
            # if current > first:
            #     third = second # make it 3rd
            #     second = first # make it 2nd
            #     first = current
            # elif current > second:
            #     second = current
            # elif current > third:
            #     third = current

            current = 0 # reset it blank line, new elf
    print('most calories: ', first)
    print('2nd calories: ', second)
    print('3rd calories: ', third)
    print('total: ', first + second + third)
