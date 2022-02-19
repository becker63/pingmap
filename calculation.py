import math


def main(playerping):
    with open('ping', 'r') as f:
                pingss = (f.read()).split("\n")

    city = []
    pings = []
    for line in pingss:
        line2 = line.replace(" ", "-")
        split2 = line2.split(":")
        for line in split2:
            if '.' in line:
                clean = line.replace("ms", "")
                pings.append(float(clean))
            else:
                city.append(line)

    def get_digit(number, n):
        return number // 10**n % 10


    check = int(playerping)

    def lastresort(lst, K):
        return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

    print("\n===============================\n")
    offset = 2
    output = []
    for ping in pings:
        if get_digit(int(ping), 1) == 0 and get_digit(int(ping), 2) == 0:
            k = int(ping) + offset
            c = int(ping) - offset
            rg = range(c,k)
            if check in rg:
                output.append(ping)
            else:
                output.append(lastresort(pings, check))

        elif get_digit(int(ping), 0) > 0:
            k = int(ping) + 5
            c = int(ping)
            rg = range(c,k)
            if check in rg:
                output.append(f"{c}   {k}:   {ping}")
            else:
                output.append(lastresort(pings, check))
    output2 = mylist = list(dict.fromkeys(output))

    output3 = []

    for line in pingss:
        for line2 in list(output2):
            if str(line2) in line:
                with open('output', 'a') as f:
                    #print(line)
                    output3.append(line)


    with open('output', 'w') as f:
        f.write("")
    

    with open('citys', 'r') as f:
        op = (f.read()).split("\n")
        #print(op)
        for item in output3:
            #print(item)
            out = item
            a = item.split(':')
            for item2 in a:
                if not 'ms' in item2:
                    p = str(item2.replace('ms', ''))
                    for item3 in op:
                        if str(p) in item3:
                           with open('output', 'a') as f:
                               item3 = op
                               print(p)
                               f.write(p + "\n")
main(50)