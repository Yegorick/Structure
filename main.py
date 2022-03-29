# Stack

class Stack:
    def __init__(self, *args):
        self.__spis = list(args)

    def empty(self):
        if len(self.__spis) == 0:
            return True
        return False

    def size(self) :
        return len(self.__spis)

    def top(self):
        return len(self.__spis) - 1

    def push(self, el):
        self.__spis.append(el)

    def pop(self):
        self.__spis.pop(-1)
    
    def __str__(self):
        return str(self.__spis)


st = Stack(1, 2, 3, 4, 5, 6)
st.pop()
st.push(10)
st.pop()
print(st.size())
print(st.top())

print(st)
