class Person:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "Person( id = {} )".format(self.id)


# [Person(id=0), Person(id=1), Person(id=2)]
p_list = [Person(id) for id in range(3)]

"""
[   
    Person(id=0), Person(id=1), Person(id=2), 
    Person(id=0), Person(id=1), Person(id=2), 
    Person(id=0), Person(id=1), Person(id=2)
]
"""
list_list = p_list * 3

list_list[0].id = 999

"""
浅复制
[   
    Person( id = 999 ), Person( id = 1 ), Person( id = 2 ), 
    Person( id = 999 ), Person( id = 1 ), Person( id = 2 ), 
    Person( id = 999 ), Person( id = 1 ), Person( id = 2 )
]
"""
print(list_list)
