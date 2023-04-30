class Human:
    width = 5
    length = 5
    def __init__(self):
        self.vector_face = 'x'
        self.coord_x = 1
        self.coord_y = 1
        self.vectors = []
    
    def possible_vector_go(self):
        if self.coord_y != 1 and self.coord_y != self.length and self.coord_x != 1 and self.coord_x != self.width:
           self.vectors = ['left', 'front', 'back', 'right'] 
        if self.vector_face == 'x':
        # Перемещение по крайним верхней и нижней линиям  оси Х <->
            if self.coord_y == 1 and 1 < self.coord_x < self.length :
                self.vectors = ['left', 'front', 'back']
            elif self.coord_y == self.width and 1 < self.coord_x < self.length:
                self.vectors = ['right', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.vectors = ['left', 'front']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.vectors = ['left', 'back']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.vectors = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.vectors = ['right', 'back']
        # Уперся в правый край граница ось У ->
            elif self.coord_x == self.length and (self.coord_y != self.length and self.coord_y != 1 ):
                self.vectors = ['left', 'right', 'back']
        
        elif self.vector_face == 'y':
            if self.coord_x == 1 and 1 < self.coord_y < self.length :
                self.vectors = ['right', 'front', 'back']
            elif self.coord_x == self.width and 1 < self.coord_y < self.length:
                self.vectors = ['left', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.vectors = ['right', 'front']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.vectors = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.vectors = ['right', 'back'] 
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.vectors = ['left', 'back']
            # Уперся в верхний край граница ось У ->
            elif self.coord_y == self.length and (self.coord_x != self.length and self.coord_x != 1 ):
                self.vectors = ['left', 'right', 'back']
        
        elif self.vector_face == '-x':
            if self.coord_y == 1 and 1 < self.coord_x < self.length :
                self.vectors = ['right', 'front', 'back']
            elif self.coord_y == self.width and 1 < self.coord_x < self.length:
                self.vectors = ['left', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:  
                self.vectors = ['right', 'back']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.vectors = ['right', 'front']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.vectors = ['left', 'back']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.vectors = ['left', 'front']
            # Уперся в левый край граница ось У ->
            elif self.coord_x == 1 and (self.coord_y != self.length and self.coord_y != 1 ):
                self.vectors = ['left', 'right', 'back']
        
        elif self.vector_face == '-y':
            if self.coord_x == 1 and 1 < self.coord_y < self.length :
                self.vectors = ['left', 'front', 'back']
            elif self.coord_x == self.width and 1 < self.coord_y < self.length:
                self.vectors = ['right', 'front', 'back']
            elif self.coord_y == 1 and self.coord_x == 1:
                self.vectors = ['left', 'back']
            elif self.coord_y == 1 and self.coord_x == self.length:
                self.vectors = ['right', 'back']
            elif self.coord_y == self.width and self.coord_x == 1:
                self.vectors = ['left', 'front']
            elif self.coord_y == self.width and self.coord_x == self.length:
                self.vectors = ['right', 'back']
            # Уперся в нижний край граница ось У ->
            elif self.coord_y == 1 and (self.coord_x != self.length and self.coord_x != 1 ):
                self.vectors = ['left', 'right', 'back']

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
cntr = 0
for y in range(100):

# Отображается поле и положение персонажа    
    playing_field = [[0] * hero.length for i in range(hero.width)]
    H = 5
    if hero.vector_face[:1] == '-':    
        H = H * -1
    playing_field[hero.coord_y - 1][hero.coord_x - 1] = H
    playing_field.reverse()
    for i in playing_field:
        print (i)    
    
    hero.possible_vector_go()
    vectors = ""
    for vector in hero.vectors:
        if vector == 'back':
            vectors += 'Назад - клавиша - 2 '
        elif vector == 'left':
            vectors += 'Влево - клавиша - 4 '
        elif vector == 'right':
            vectors += 'Вправо - клавиша - 6 '
        elif vector == 'front':
            vectors += 'Вперед - клавиша - 8 '
   
    while True:    
        vector = input(print(f'Куда дальше? Возможные направления: {vectors}{hero.coord_x, hero.coord_y, hero.vector_face}'))    
        int_arr = [i for i in vectors.split() if i.isnumeric() ]
        if not vector in int_arr:
            print("Ой-бой!!! Тааак нельзя!!!! Сооберись")
        else:
            break
            
    hero.go(vector)