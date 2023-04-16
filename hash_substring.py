# Karlis Olmanis 221RDB255
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    izvele = input()
    if "I" in izvele:
        raksts = input().rstrip()
        teksts = input().rstrip()
    elif "F" in izvele:
        nos = "06"
        if "a" not in nos:
            with open(f"tests/{nos}") as file:
                txt = file.read().split("\n")
                raksts = txt[0].rstrip()
                teksts = txt[1].rstrip()
                
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (raksts, teksts)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(raksts, teksts):
    # this function should find the occurances using Rabin Karp alghoritm 
    occ = []
    r = len(raksts)
    t = len(teksts)
    for i in range(t-r+1):
        txt = teksts[i:i+r]
        if hash(raksts) == hash(txt):
            occ.append(i)
    return occ
# return an iterable variable


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
