import os

def image_choosing():
    image_names = os.listdir('images')

    print('Выберите картинку')
    for i, val in enumerate(image_names):
        print(f'{i}) {val}', end=' ')
    print('')

    while True:
        choice_image = int(input())
        choice_size = int(input("Введите предпочитаемую ширину: "))
        if choice_image < len(image_names):
            return (os.path.join('images', image_names[choice_image]), choice_size)