from collections import deque

def palindrome(text):
    d = deque()
    lst = str(text).upper().replace(' ', '')

    for el in lst:
        d.append(el)

    while len(d)>1:
            if d.pop() == d.popleft():
                continue
            else:
                print(f'{text} не є поліндромом')
                break
    else:
        print(f'{text} є поліндромом')

text = '123qwewq321'
palindrome(text)
                
            
        