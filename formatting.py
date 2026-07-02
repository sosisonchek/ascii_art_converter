from PIL import Image
import numpy as np

def convertion(file, target_width, inversion):
    if inversion == 'y':
        gradients = '%@#*+=-:. '
    else:
        gradients = ' .:-=+*#%@'

    multiplier = (len(gradients) - 1) / 256
    
    with Image.open(file) as img:

        width, height = img.size
        aspect_ratio = height / width
        target_height = int(target_width * aspect_ratio * 0.5) # 0.5 - соотн. сторон символов

        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        image = img.convert('RGB').convert('L') # RGBA (если картинка .png) -> RGB -> грейскейл
        image_array = np.array(image)

    image_2dlist = image_array.tolist()

    ascii_list = []
    for row in image_2dlist:
        row_list = []

        for val in row:
            row_list.append(gradients[round(val * multiplier)])

        ascii_list.append(row_list)

    with open('lastlog.txt', 'w') as file:
        for i in ascii_list:
            for j in i:
                print(j, end='')
                file.write(j)
            print()
            file.write(f'\n')
    print('Картинка была сохранена в lastlog.txt')