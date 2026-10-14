
def count():
    user = input("Enter a word: ")
    vowels = "a,e,i,o,u"
    def check(word):
        if word == "":
            return 0
        if word[0].lower() in vowels:
            return 1 + check(word[1:])
        else:
            return check(word[1:])
    print(check(user))

count()
