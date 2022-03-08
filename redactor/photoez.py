from PIL import Image, ImageFilter

source = Image.open("фото.jpeg")
w, h = source.size

color_ch = ['красный', 'зеленый', 'желтый', 'голубой', 'негатив', 'черно-белое']
number = 1
filters = ['Размытие', "Детализация", "Контуризация", "Выделение контуров", "Тиснение"]
print('Какие изменения вы хотите сделать с изображением?')
print()
print('Обрезка - 1')
print('Ресайз - 2')
print('Наложение цветового фильтра - 3')
print('Наложение фильтра - 4')
print('Сохранить и выйти - 5')

while True:
    ans = int(input("Выберите действие: "))

    #Чоп-чоп
    if ans == 1:
        print('У изображения вот такой вот размер', w, h)
        x1, y1, x2, y2 = [int(input("Введите координаты по очереди: ")) for i in range(4)]
        result = source.crop((x1, y1, x2, y2))
        source = result
        w, h = source.size
        source.show()


    #Ресайз
    if ans == 2:
        print('1 - имею ширину и высоту')
        print('2 - пропорционально ширине')
        print('3 - пропорционально высоте')
        resize_type = int(input('Каким способом поменять размер? (1-3) '))
        print('У изображения вот такой вот размер', w, h)
        #По ширине и высоте
        if resize_type == 1:
            new_w = int(input('Новая ширина: '))
            new_h = int(input('Новая высота: '))
            result = source.resize((new_w, new_h), Image.NEAREST)
            source = result
        #Пропорчионально ширине
        if resize_type == 2:
            new_w = int(input('Новая ширина: '))
            new_h = int(new_w * h / w)
            result = source.resize((new_w, new_h), Image.NEAREST)
            source = result
        #Пропорционально высоте
        if resize_type == 3:
            new_h = int(input('Новая высота: '))
            new_w = int(new_h * w / h)
            result = source.resize((new_w, new_h), Image.NEAREST)
            source = result
        w, h = source.size
        source.show()


    #Цветовые фильтры
    if ans == 3:
        for i in color_ch:
            print(f"{number} - {i}")
            number += 1
        chcl = int(input(f'Выберете цвет (1-{number-1}) '))
        number = 1
        if chcl == 1:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (r, int(g/3), int(b/3), 255))
        elif chcl == 2:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r/3), int(g), int(b/3), 255))
        elif chcl == 3:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r), int(g), int(b/10), 255))
        elif chcl == 4:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r/3), int(g/3), int(b), 255))
        elif chcl == 5:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), ((255 - r), (255 - g), (255 - b), 255))
        elif chcl == 6:
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    gray = int(r * 0.212 + g * 0.715 + b * 0.0746)
                    source.putpixel((i, j), (gray, gray, gray, 255))
        source.show()
    
    #Нормальные фильтры
    if ans == 4:
        for i in filters:
            print(f"{number} - {i}")
            number += 1
        chfil = int(input(f'Выберете фильтр (1-{number-1}) '))
        number = 1
        if chfil == 1:
            source = source.filter(ImageFilter.BLUR)

        elif chfil == 2:
            source = source.filter(ImageFilter.DETAIL)
        
        elif chfil == 3:
            source = source.filter(ImageFilter.CONTOUR)
        
        elif chfil == 4:
            source = source.filter(ImageFilter.EDGE_ENHANCE)
        
        elif chfil == 5:
            source = source.filter(ImageFilter.EMBOSS)
        source.show()

        
    if ans == 5:
        #Зеленый квадрат
        for w in range(0, 20):
            for h in range(0, 20):
                source.putpixel((w,h),(0, 155, 0, 0))
        source.save("img.jpg")
        break