class Human:
    width = 5
    length = 5
    def __init__(self):
        self.vector_face = 0 # Направление 1 - ось Х, 2 - ось У
        self.coord_x = 0
        self.coord_y = 0
        self.vectors = []
    
    def possible_vector_go(self):
        if self.coord_y != 1 and self.coord_y != self.length and self.coord_x != 1 and self.coord_x != self.width:
           self.vectors = ['left', 'front', 'back', 'right'] 
        if self.vector_face == 1:
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
        
        elif self.vector_face == 2:
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
        
        elif self.vector_face == -1:
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
        
        elif self.vector_face == -2:
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

hero = Human()
hero.vector_face = 1
hero.coord_x = 1
hero.coord_y = 1
hero.vectors = []
def move_hero(vertor_go):
    for i in (1, -1, 2, -2):
        if i < 0:
            change_coord = -1
        else:
            change_coord = 1
        if i == hero.vector_face:
            for j in range(2, 10, 2):
                if str(j) == vertor_go:
                    if j == 2:
                        hero.vector_face *= -1
                    # Было Х меняется на У
                    elif j == 4 and hero.vector_face % 2: # 1 или -1
                        if hero.vector_face < 0:
                            hero.vector_face -=  1 
                        else:
                            hero.vector_face += 1
                    # Было У меняется на Х
                    elif j == 4 and not (hero.vector_face % 2):     # 2 или -2
                        hero.vector_face = int(hero.vector_face / 2) * -1 if not (hero.vector_face % 2) else (hero.vector_face + change_coord) * -1
                     # Было Х меняется на У
                    elif j == 6 and hero.vector_face % 2:
                        if hero.vector_face < 0: 
                            vector_face = (hero.vector_face - 1) * -1 
                        else:
                            vector_face = (hero.vector_face + 1) * -1
                    # Условие У
                    elif j == 6 and not (hero.vector_face % 2):
                        hero.vector_face = int(hero.vector_face / 2) if not (hero.vector_face $ 2) else hero.vector_face + change_coord
                    
                    if hero.vector_face % 2:   # Для Х
                        hero.coord_x += change_coord
                    else:                           # Для У
                        hero.coord_y += change_coord                
            break            
    
    
    
    
    # if hero.vector_face == 'x':
    #     if vertor_go == "8":
    #         hero.vector_face = "x"
    #         hero.coord_x += 1
    #     elif vertor_go == "2":
    #         hero.coord_x -= 1
    #         hero.vector_face = "-x"
    #     elif vertor_go == "4":           
    #         hero.vector_face = "y"
    #         hero.coord_y += 1
    #     elif vertor_go == "6":
    #         hero.vector_face = "-y"
    #         hero.coord_y -= 1
       
    # elif  hero.vector_face == 'y':
    #     if vertor_go == "8":
    #         hero.vector_face == 'y'
    #         hero.coord_y += 1
    #     elif vertor_go == "2":
    #         hero.vector_face = "-y"
    #         hero.coord_y -= 1
    #     elif vertor_go == "4":           
    #         hero.vector_face = "-x"
    #         hero.coord_x -= 1
    #     elif vertor_go == "6":
    #         hero.vector_face = "x"
    #         hero.coord_x += 1     
   
    # elif hero.vector_face == '-x':
    #     if vertor_go == "8":
    #         hero.vector_face = "-x"
    #         hero.coord_x -= 1
    #     elif vertor_go == "2":
    #         hero.coord_x += 1
    #         hero.vector_face = "x"
    #     elif vertor_go == "4":           
    #         hero.vector_face = "-y"
    #         hero.coord_y -= 1
    #     elif vertor_go == "6":
    #         hero.vector_face = "y"
    #         hero.coord_y += 1
       
    # elif  hero.vector_face == '-y':
    #     if vertor_go == "8":
    #         hero.coord_y -= 1
    #     elif vertor_go == "2":
    #         hero.vector_face = "y"
    #         hero.coord_y += 1
    #     elif vertor_go == "4":           
    #         hero.vector_face = "x"
    #         hero.coord_x += 1
    #     elif vertor_go == "6":
    #         hero.vector_face = "-x"
    #         hero.coord_x -= 1     






for y in range(100):

# Отображается поле и положение персонажа    
    playing_field = [[0] * hero.length for i in range(hero.width)]
   
    
    playing_field[hero.coord_y - 1][hero.coord_x - 1] = hero.vector_face
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
            
    move_hero(vector)