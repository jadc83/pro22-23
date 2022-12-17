try:
    def relation_to_luke (personaje):
        blood = {("Darth Vader", "father"),
                ("Leia", "sister"),
                ("Han", "brother in law"),
                ("R2D2", "Droid")}
        parentescos = dict(blood)
        if personaje == "":
            print("Luke, I am your father.")
        else:
            print(f"Luke, I am your {parentescos[personaje]}.")
