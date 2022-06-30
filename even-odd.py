
def extract_evens_odds(string):
    even = []
    odd = []
    for i in string:
        if int(i) % 2 == 0:
            even.append(i)
        if int(i) % 2 == 1:
            odd.append(i)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
    print("Number of Evens:", len(even))
    print("Number of Odd:", len(odd))
    return "Even numbers:", even, "Odd numbers:", odd


print(extract_evens_odds("7894738975984375847589437286184391349"))

