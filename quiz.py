class Test:
    def __init__(self):
        self._value = "protected"
 
t = Test()
print(t._value)
