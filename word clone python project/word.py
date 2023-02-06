n = int(input('enter no.of lines: '))

print('enter string')

st = ""

for i in range(0, n):

    st = st+input()+"\n"

print(st)

axs = ''

L = (',', '.', '?', '!', ':', ';', '&')

for i in st:

    if i not in L:

        axs = axs+i.lower()

print(axs)

word_list = axs.split()

list_word_2 = st.split()

while(1):

    print('for counting no.of words press 1')

    print('for counting no.of alphabets press 2')

    print('for searching any word available in string or not .. press 3')

    print(
        'for reversing whole string  [order of words+order of alphabets in words] press 4')

    print('for finding frequency of given word in string...press 5')

    print('for finding frequency of given letter in string press 6')

    print('for replacing one letter with another letter  press 7')

    print('for printing all the unique words press 8')

    print('for printing all the duplicate words press 9')

    print('for printing all the words whose occurrence is greater than k press 10')

    print('for finding longest word in the sting press 11')

    print('for finding frequency of each  vowel press 12')

    print('for finding frequency of each  consonant press 13')

    print(' for reversing string (ORDER OF WORDS NOT LETTERS) press 14')

    print('for reversing string (ORDER OF WORDS NOT TO BE CHANGED BUT ORDER OF LETTERS TO CHANGE) press 15')

    print('for changing whole string into lower case press 16')

    print('for changing whole string into upper case press 17')

    print('for changing lower case letters to upper case and upper case letters to lower case press 18 ')

    print('for printing all the special characters press 19')

    print('for removing particular word from the string press 20')

    n = int(input('enter the number corresponding to the programme which you want: '))

    if n == 1:

        word_list = axs.split()

        count = 0

        for word in word_list:

            count = count+1

        print(count)

    elif (n == 2):

        count = 0

        for i in st:

            if 64 < ord(i) < 91 or 96 < ord(i) < 123:

                count = count+1

        print(count)

    elif n == 3:

        word = input(
            'give input of which word you want to search(in lower_case): ')

        if word in word_list:

            print('yes')

        else:

            print('no')

    elif n == 4:

        rev_str = ''

        for i in range(len(st)-1, -1, -1):

            rev_str = rev_str+st[i]

        print(rev_str)

    elif n == 5:

        count = 0

        word = input('give word: ')

        for i in word_list:

            if i == word:

                count = count+1

        print(count)

    elif n == 6:

        x = input(
            'enter the letter whose frequency you want to find(in lower_case): ')

        count = 0

        for i in axs:

            if i == x:

                count = count+1

        print(count)

    elif n == 7:

        x = input('enter the letter you want to change: ')

        y = input('enter the charector you want to replace with: ')

        z = ''

        for i in st:

            if i.lower() == x:

                z = z+str(y)

            else:

                z = z+str(i)

        print(z)

    elif n == 8:

        c = []

        d = []

        for i in word_list:

            if i not in c:

                c.append(i)

        for j in c:

            count = 0

            for i in word_list:

                if i == j:

                    count = count+1

            if count == 1:

                d.append(j)

        print(d)

    elif n == 9:

        c = []

        d = []

        for i in word_list:

            if i not in c:

                c.append(i)

        for j in c:

            count = 0

            for i in word_list:

                if i == j:

                    count = count+1

            if count != 1:

                d.append(j)

        print(d)

    elif n == 10:

        k = int(input('enter the number k: '))

        c = []

        d = []

        for i in word_list:

            if i not in c:

                c.append(i)

        for j in c:

            count = 0

            for i in word_list:

                if i == j:

                    count = count+1

            if count > k:

                d.append(j)

        print(d)

    elif n == 11:

        max = 0

        for i in word_list:

            if len(i) > max:

                max = len(i)

                t = i

        max = len(t)

        for i in word_list:

            if max == len(i):

                print(i)

    elif n == 12:

        L = ['a', 'e', 'i', 'o', 'u']

        dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for i in axs:

            if i in L:

                dic[i] = dic[i]+1

        print(dic)

    elif n == 13:

        L = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
             'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        dic = {'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
               'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        for i in axs:

            if i in L:

                dic[i] = dic[i]+1

        print(dic)

    elif n == 14:

        rev_list = list()

        for i in range(len(list_word_2)-1, -1, -1):

            rev_list.append(list_word_2[i])

        print(rev_list)

        print(' '.join(rev_list))

    elif n == 15:

        rev_lis = list()

        for word in list_word_2:

            temp = ''

            for i in range(len(word)-1, -1, -1):

                temp = temp+word[i]

            rev_lis.append(temp)

        print(' '.join(rev_lis))

    elif n == 16:

        lower_string = ''

        for i in st:

            num = ord(i)

            if 64 < num < 92:

                num = num+32

            else:

                num = num

            lower_string = lower_string+chr(num)

        print(lower_string)

    elif n == 17:

        upper_string = ''

        for i in st:

            num = ord(i)

            if 96 < num < 123:

                num = num-32

            else:

                num = num

            upper_string = upper_string+chr(num)

        print(upper_string)

    elif n == 18:

        temp = ''

        for ch in st:

            num = ord(ch)

            if 96 < num < 123:

                num = num-32

            elif 64 < num < 92:

                num = num+32

            temp = temp+chr(num)

        print(temp)

    elif n == 19:

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

        list_alpha = list(alphabet)

        lst = []

        for i in st:

            if i not in list_alpha:

                lst.append(i)

        print(lst)

    elif n == 20:

        y = input('enter the letter you want you remove: ')

        stri = ''

        for i in st:

            if y == i:

                stri = stri+''

            else:

                stri = stri+i

        print(stri)

    print('you want to continue or not,press 1 to continue and 0 to stop')

    c = int(input())

    if c == 0:

        break
