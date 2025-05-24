class Animal:
    def __init__(self):
        self.age = 1
    
    def birth(self):
        self.age += 1

if __name__ == '__main__':
    ani = Animal()
    print("11", ani.age)
    ani.birth()
    print("11", ani.age)