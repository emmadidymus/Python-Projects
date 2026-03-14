def my_function(fname,lname):
    print("Hello,",fname,lname)

person = {"fname":"Emmanuel", "lname":"Sebastian"}
my_function(**person)
