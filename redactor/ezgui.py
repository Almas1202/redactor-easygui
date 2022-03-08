from easygui import *
from PIL import Image, ImageFilter

path = fileopenbox("Открыть путь до файла")
source = Image.open(path, 'r')
w, h = source.size
original = source

while True:
    ans = buttonbox("Выберите действие?", choices=['Обрезка', 'Ресайз', 'Наложение цветового фильтра', 'Наложение фильтра', 'Сохранить в jpg', 'Сохранить в png'])

    #Чоп-чоп
    if ans == 'Обрезка':
        ob = []  # мы должны начать с пустого списка для правильной работы метода.
        ob = multenterbox(f'У изображения вот такой вот размер {w}, {h}. Введите значения x1, y1, x2, y2', 'Обрезка', ['x1', 'y1', 'x2', 'y2'])
        source.crop((int(ob[0]), int(ob[1]), int(ob[2]), int(ob[3])))
        w, h = source.size
        source.show

    if ans == 'Ресайз':
        res = buttonbox('Как изменять картинку', choices = ['Имею ширину и высоту', 'Пропорционально ширине', 
        'Пропорционально высоте'])

        #По ширине и высоте
        if res == 'Имею ширину и высоту':
            wnh = []
            wnh = multenterbox(f'У изображения вот такой вот размер {w}, {h}. Введите новые значения высоты и длины', 'Ресайз',  ['Длина', 'Высота'])
            result = source.resize((int(wnh[0]), int(wnh[1])), Image.NEAREST)
            source = result
        #Пропорчионально ширине
        if res == 'Пропорционально ширине':
            new_w = int(enterbox(f'У изображения вот такой вот размер {w}, {h}. Новая ширина:'))
            new_h = int(new_w * h / w)
            result = source.resize((new_w, new_h), Image.NEAREST)
            source = result
        #Пропорционально высоте
        if res == 'Пропорционально высоте':
            new_h = int(enterbox(f'У изображения вот такой вот размер {w}, {h}. Новая высота:'))
            new_w = int(new_h * w / h)
            result = source.resize((new_w, new_h), Image.NEAREST)
            source = result
        w, h = source.size
        source.show()
        msgbox('Успешно выполнено')
    
    #Цветовые фильтры
    if ans == 'Наложение цветового фильтра':
        chcl = buttonbox("Выберите цветовой фильтр", 
        choices=['красный', 'зеленый', 'желтый', 'голубой', 'негатив', 'черно-белое'])
        if chcl == "красный":
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (r, int(g/3), int(b/3), 255))
        elif chcl == 'зеленый':
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r/3), int(g), int(b/3), 255))
        elif chcl == 'желтый':
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r), int(g), int(b/10), 255))
        elif chcl == 'голубой':
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), (int(r/3), int(g/3), int(b), 255))
        elif chcl == 'негатив':
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    source.putpixel((i, j), ((255 - r), (255 - g), (255 - b), 255))
        elif chcl == 'черно-белое':
            for i in range(w):
                for j in range(h):
                    r, g, b = source.getpixel((i, j))
                    gray = int(r * 0.212 + g * 0.715 + b * 0.0746)
                    source.putpixel((i, j), (gray, gray, gray, 255))
        source.show()
        msgbox('Успешно выполнено')
    
    #Нормальные фильтры
    if ans == 'Наложение фильтра':
        chfil = buttonbox("Выберите цветовой фильтр", 
        choices=['Размытие', "Детализация", "Контуризация", "Выделение контуров", "Тиснение"])
        if chfil == 'Размытие':
            source = source.filter(ImageFilter.BLUR)

        elif chfil == "Детализация":
            source = source.filter(ImageFilter.DETAIL)
        
        elif chfil == "Контуризация":
            source = source.filter(ImageFilter.CONTOUR)
        
        elif chfil == "Выделение контуров":
            source = source.filter(ImageFilter.EDGE_ENHANCE)
        
        elif chfil == "Тиснение":
            source = source.filter(ImageFilter.EMBOSS)
        source.show()
        msgbox('Успешно выполнено')
    
    if ans == 'Сохранить в jpg':
        for w in range(0, 20):
            for h in range(0, 20):
                source.putpixel((w,h),(0, 155, 0, 0))

        rgb_im = source.convert('RGB')
        rgb_im.save('new_img.jpg')
        break

    if ans == 'Сохранить в png':
        #Зеленый квадрат
        for w in range(0, 20):
            for h in range(0, 20):
                source.putpixel((w,h),(0, 155, 0, 0))
        source.save("new_img.png")
        break