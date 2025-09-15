class phone:

    def call(self):
        print("You can call")
    def message(self):
        print("You can message")
class samsung(phone):
    def photo(self):
        print("You can take photo")

ss=samsung()
ss.call()
ss.message()
ss.photo()
    