# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()
    if "I" in choice:
        raksts = input().rstrip()
        teksts = input().rstrip()
    elif "F" in choice:
        nose = "06"
        if "a" not in nose:
            with open(f"tests/{nose}") as file:
                text = file.read().split("\n")
                raksts = text[0].rstrip()
                teksts = text[1].rstrip()
    
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

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    ocx = []
    r = len(raksts)
    t = len(teksts)
    for i in range(t-r+1):
        text = teksts[i:i+r]
        if hash(raksts) == hash(text):
            ocx.append(i)
    return ocx
    # and return an iterable variable
    


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

