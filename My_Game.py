class Human:
    width = 3
    length = 3
    def __init__(self):
        self.vector_face = 'x'
        self.coord_x = 1
        self.coord_y = 1
        self.r = []
    
    def possible_vector_go(self):
        if self.vector_face == 'x':
            if self.coord_y == 1 and 1 < self.coord_x < self.length :
                self.r = ['left', 'front', 'back']
            elif self.coord_y == self.width and 1 < self.coord_x < self.length:
                self.r = ['right', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.r = ['left', 'front']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.r = ['left', 'back']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.r = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.r = ['right', 'back']
        
        elif self.vector_face == 'y':
            if self.coord_x == 1 and 1 < self.coord_y < self.length :
                self.r = ['right', 'front', 'back']
            elif self.coord_x == self.width and 1 < self.coord_y < self.length:
                self.r = ['left', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.r = ['right', 'front']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.r = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.r = ['right', 'back'] 
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.r = ['left', 'back']
   
        if self.vector_face == '-x':
            if self.coord_y == 1 and 1 < self.coord_x < self.length :
                self.r = ['right', 'front', 'back']
            elif self.coord_y == self.width and 1 < self.coord_x < self.length:
                self.r = ['left', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:  
                self.r = ['right', 'back']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.r = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.r = ['left', 'back']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.r = ['left', 'front']
        
        elif self.vector_face == '-y':
            if self.coord_x == 1 and 1 < self.coord_y < self.length :
                self.r = ['left', 'front', 'back']
            elif self.coord_x == self.width and 1 < self.coord_y < self.length:
                self.r = ['right', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.r = ['left', 'back']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.r = ['right', 'back']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.r = ['left', 'front']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.r = ['right', 'back']
    

    def go(self, vertor_go):
        
        if self.vector_face == 'x':
            if vertor_go == "8":
                self.coord_x += 1
            elif vertor_go == "2":
                self.coord_x -= 1
                self.vector_face = "-x"
            elif vertor_go == "4":           
                self.vector_face = "y"
                self.coord_y += 1
            elif vertor_go == "6":
                self.vector_face = "-y"
                self.coord_y -= 1
       
        elif  self.vector_face == 'y':
            if vertor_go == "8":
                self.coord_y += 1
            elif vertor_go == "2":
                self.vector_face = "-y"
                self.coord_y -= 1
            elif vertor_go == "4":           
                self.vector_face = "-x"
                self.coord_x -= 1
            elif vertor_go == "6":
                self.vector_face = "x"
                self.coord_x += 1     
       
        elif self.vector_face == '-x':
            if vertor_go == "8":
                self.coord_x -= 1
            elif vertor_go == "2":
                self.coord_x += 1
                self.vector_face = "x"
            elif vertor_go == "4":           
                self.vector_face = "-y"
                self.coord_y -= 1
            elif vertor_go == "6":
                self.vector_face = "y"
                self.coord_y += 1
       
        elif  self.vector_face == '-y':
            if vertor_go == "8":
                self.coord_y -= 1
            elif vertor_go == "2":
                self.vector_face = "y"
                self.coord_y += 1
            elif vertor_go == "4":           
                self.vector_face = "x"
                self.coord_x += 1
            elif vertor_go == "6":
                self.vector_face = "-x"
                self.coord_x -= 1     


hero = Human()
while True:
    hero.possible_vector_go()
    vectors = ""
    for vector in hero.r:
        if vector == 'front':
            vectors += 'Вперед - клавиша - 8 '
        elif vector == 'back':
            vectors += 'Назад - клавиша - 2 '
        elif vector == 'left':
            vectors += 'Влево - клавиша - 4 '
        elif vector == 'right':
            vectors += 'Вправо - клавиша - 6 '
    
    while True:    
        vector = input(print(f'Куда дальше? Возможные направления: {vectors}{hero.coord_x, hero.coord_y, hero.vector_face}'))    
        int_arr = [i for i in vectors.split() if i.isnumeric() ]
        if not vector in int_arr:
            print("Так нельзя!!!! Соберись")
        else:
            break
            
    hero.go(vector)