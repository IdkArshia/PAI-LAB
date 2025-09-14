countries = {
    "China": 1416096094,
    "Indonesia": 285721236,
    "Us": 347275807,
    "India": 1463865525
}
def find_highest():
    h1 = h2 = h3 = 0
    c1 = c2 = c3 = None   
    for country, pop in countries.items():
        if pop > h1:  # new highest
            c3, h3 = c2, h2
            c2, h2 = c1, h1
            c1, h1 = country, pop
        elif pop > h2:  # second highest
            c3, h3 = c2, h2
            c2, h2 = country, pop
        elif pop > h3:  # third highest
            c3, h3 = country, pop
    print(f"Highest population: {c1} ({h1})")
    print(f"Second highest: {c2} ({h2})")
    print(f"Third highest: {c3} ({h3})")
find_highest()
