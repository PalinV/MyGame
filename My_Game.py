import random
class Human:
    width = 5
    length = 5
    def __init__(self):
        self.vector_face = 0 # Направление 1 - ось Х, 2 - ось У
        self.coord_x = 0
        self.coord_y = 0
        self.vectors = []
hero = Human()
hero.vector_face = 1
hero.coord_x = 1
hero.coord_y = 1
hero.vectors = []
bot = Human()
bot.vector_face = -1
bot.coord_x = bot.width
bot.coord_y = bot.length

# Объявляется функция определяющая возможные направления движения с учетом статического направления
def possible_vector_go(vector_face, coord_y, coord_x):
    if coord_y != 1 and coord_y != Human.length and coord_x != 1 and coord_x != Human.width:
       vectors = ['left', 'front', 'back', 'right'] 
    if vector_face == 1:
        # Перемещение по крайним верхней и нижней линиям  оси Х <->
        if coord_y == 1 and 1 < coord_x < Human.length :
            vectors = ['left', 'front', 'back']
        elif coord_y == Human.width and 1 < coord_x < Human.length:
            vectors = ['right', 'front', 'back']
        elif coord_y == 1 and coord_x == 1:
            vectors = ['left', 'front']
        elif coord_y == 1 and coord_x == Human.length:
            vectors = ['left', 'back']
        elif coord_y == Human.width and coord_x == 1:
            vectors = ['right', 'front']
        elif coord_y == Human.width and coord_x == Human.length:
            vectors = ['right', 'back']
        # Уперся в правый край граница ось У ->
        elif coord_x == Human.length and (coord_y != Human.length and coord_y != 1 ):
            vectors = ['left', 'right', 'back']
        
    elif vector_face == 2:
        if coord_x == 1 and 1 < coord_y < Human.length :
            vectors = ['right', 'front', 'back']
        elif coord_x == Human.width and 1 < coord_y < Human.length:
            vectors = ['left', 'front', 'back']
        elif coord_y == 1 and coord_x == 1:
            vectors = ['right', 'front']
        elif coord_y == 1 and coord_x == Human.length:
            vectors = ['right', 'front']
        elif coord_y == Human.width and coord_x == 1:
            vectors = ['right', 'back'] 
        elif coord_y == Human.width and coord_x == Human.length:
            vectors = ['left', 'back']
            # Уперся в верхний край граница ось У ->
        elif coord_y == Human.length and (coord_x != Human.length and coord_x != 1 ):
            vectors = ['left', 'right', 'back']
        
    elif vector_face == -1:
        if coord_y == 1 and 1 < coord_x < Human.length :
            vectors = ['right', 'front', 'back']
        elif coord_y == Human.width and 1 < coord_x < Human.length:
            vectors = ['left', 'front', 'back']
        elif coord_y == 1 and coord_x == 1:  
            vectors = ['right', 'back']
        elif coord_y == 1 and coord_x == Human.length:
            vectors = ['right', 'front']
        elif coord_y == Human.width and coord_x == 1:
            vectors = ['left', 'back']
        elif coord_y == Human.width and coord_x == Human.length:
            vectors = ['left', 'front']
            # Уперся в левый край граница ось У ->
        elif coord_x == 1 and (coord_y != Human.length and coord_y != 1 ):
            vectors = ['left', 'right', 'back']
        
    elif vector_face == -2:
        if coord_x == 1 and 1 < coord_y < Human.length :
            vectors = ['left', 'front', 'back']
        elif coord_x == Human.width and 1 < coord_y < Human.length:
            vectors = ['right', 'front', 'back']
        elif coord_y == 1 and coord_x == 1:
            vectors = ['left', 'back']
        elif coord_y == 1 and coord_x == Human.length:
            vectors = ['right', 'back']
        elif coord_y == Human.width and coord_x == 1:
            vectors = ['left', 'front']
        elif coord_y == Human.width and coord_x == Human.length:
            vectors = ['right', 'back']
            # Уперся в нижний край граница ось У ->
        elif coord_y == 1 and (coord_x != Human.length and coord_x != 1 ):
            vectors = ['left', 'right', 'back']
    return vectors


# Объявляется функция меняющие координаты персонажа
def move_character(vertor_go, vector_face, coord_x, coord_y):
    if hero.vector_face == 1:
        if vertor_go == "8":
            vector_face = 1
            coord_x += 1
        elif vertor_go == "2":
            coord_x -= 1
            vector_face = -1
        elif vertor_go == "4":           
            vector_face = 2
            coord_y += 1
        elif vertor_go == "6":
            vector_face = -2
            coord_y -= 1
       
    elif  hero.vector_face == 2:
        if vertor_go == "8":
            vector_face == 2
            coord_y += 1
        elif vertor_go == "2":
            vector_face = -2
            coord_y -= 1
        elif vertor_go == "4":           
            vector_face = -1
            coord_x -= 1
        elif vertor_go == "6":
            vector_face = 1
            coord_x += 1     
   
    elif hero.vector_face == -1:
        if vertor_go == "8":
            vector_face = -1
            coord_x -= 1
        elif vertor_go == "2":
            coord_x += 1
            vector_face = 1
        elif vertor_go == "4":           
            vector_face = -2
            coord_y -= 1
        elif vertor_go == "6":
            vector_face = 2
            coord_y += 1
       
    elif  hero.vector_face == -2:
        if vertor_go == "8":
            coord_y -= 1
        elif vertor_go == "2":
            vector_face = 2
            coord_y += 1
        elif vertor_go == "4":           
            vector_face = 1
            coord_x += 1
        elif vertor_go == "6":
            vector_face = -1
            coord_x -= 1     
    return [coord_x, coord_y]




for y in range(100):
# Создается поле     
    playing_field = [[0] * hero.length for i in range(hero.width)]
# Направление стрелки ГГ    
    if hero.vector_face % 2 and hero.vector_face > 0:
        symbol = '>'
    elif hero.vector_face % 2 and hero.vector_face < 0:
         symbol = '<'
    elif not hero.vector_face % 2 and hero.vector_face > 0:
        symbol = '^'
    else:
        symbol = '|'
# Размещение персонажа на карте    
    playing_field[hero.coord_y - 1][hero.coord_x - 1] = symbol
    playing_field[bot.coord_y - 1][bot.coord_x - 1] = '*'
    playing_field.reverse()
    for i in playing_field:
        print (i)    
# Вызывается функция определения возможных передвижений персонажей    
    vectors = possible_vector_go(bot.vector_face, bot.coord_y, bot.coord_x)
    random_vector = random.randrange(2, 10, 2)
    
    vectors = possible_vector_go(hero.vector_face, hero.coord_y, hero.coord_x)
    vectors1 = ""
    for vector in vectors:
        if vector == 'back':
            vectors1 += 'Назад - клавиша - 2 '
        elif vector == 'left':
            vectors1 += 'Влево - клавиша - 4 '
        elif vector == 'right':
            vectors1 += 'Вправо - клавиша - 6 '
        elif vector == 'front':
            vectors1+= 'Вперед - клавиша - 8 '
    while True:    
        vector = input(print(f'Куда дальше? Возможные направления: {vectors1}{hero.coord_x, hero.coord_y, hero.vector_face}'))    
        int_arr = [i for i in vectors1.split() if i.isnumeric() ]
        if not vector in int_arr:
            print("Ой-бой!!! Тааак нельзя!!!! Сооберись")
        else:
            break
    
    
    hero.coord_x, hero.coord_y = move_character(random_vector, hero.vector_face, hero.coord_x, hero.coord_y)        
    bot.coord_x, bot.coord_y = move_character(vector, bot.vector_face, hero.coord_x, hero.coord_y)
    