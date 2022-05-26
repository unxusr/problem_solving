def get_shortest_string():
    countries = {"Egypt", "Spain", "Germany", "South Africa", "USA", "UK"}
    shortest = []
    k = 100
    for i in countries:
        if len(i) <= k:
            k = len(i)
            shortest.append(i)
    for j in shortest:
        if len(j) <= k:
            k = len(j)
            print("Shortest string length is:",  j)


get_shortest_string()
