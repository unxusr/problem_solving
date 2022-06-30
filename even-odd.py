
def extract_evens_odds(string):
    even = []
    odd = []
    for i in string:
        if i.isnumeric():
            if int(i) % 2 == 0:
                even.append(i)
            if int(i) % 2 == 1:
                odd.append(i)
        elif i.isalpha():
            print(i, "is a letter")
    # print("Even numbers:", even)
    # print("Odd numbers:", odd)
    print("Number of Evens:", len(even))
    print("Number of Odds:", len(odd))
    return "Even numbers:", even, "Odd numbers:", odd


print(extract_evens_odds("jdjd78947389759843jdnfkns75847589437286184391349"))

