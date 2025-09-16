class phone:
    def __init__(self):
        print("this is phone")

class smart_phone(phone):
    def __init__(self):
        super().__init__()
        print("this is smart phone")

s1=smart_phone()