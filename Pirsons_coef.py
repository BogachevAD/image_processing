from PIL import Image
from PIL import ImageOps
import math

k = 20

#img1 = ImageOps.flip(Image.open(f"{k}.bmp"))

img1 = Image.open(f"{k}.bmp").rotate(180, expand=True)

img2 = Image.open(f"ver_1_num_pict_{k}.bmp")

img3 = Image.open(f"ver_2_num_pict_{k}.bmp")

img4 = Image.open(f"ver_3_num_pict_{k}.bmp")

img5 = Image.open(f"ver_4_num_pict_{k}.bmp")

img6 = Image.open(f"ver_5_num_pict_{k}.bmp")


a = [img1, img2, img3, img4, img5, img6]

def coef_corr(Image1, Image2):
    im1 = Image1.load()
    im2 = Image2.load()
    # Введем переменные для расчета
    # Среднее значение яркости пикселей первого изображения avg_pix_br_1
    Summ1 = 0

    # Среднее значение яркости пикселей второго изображения
    Summ2 = 0

    # Cумма в числителе
    Summ_ch = 0

    # Cумма в знаменателе
    Summ_zn_1 = 0
    Summ_zn_2 = 0

    if (Image1.size == Image2.size):
        x1, y1 = Image1.size
        for x in range(0, x1):
            for y in range(0, y1):
                Summ1 = Summ1 + im1[x, y]
                Summ2 = Summ2 + im2[x, y]
    else:
        print("Размер изображений не совпадают!")

    avg_pix_br_1 = Summ1 / (x1 * y1)
    # print(Summ1, avg_pix_br_1)

    avg_pix_br_2 = Summ2 / (x1 * y1)
    # print(Summ2, avg_pix_br_2)

    if (Image1.size == Image2.size):
        x1, y1 = Image1.size
        for x in range(0, x1):
            for y in range(0, y1):
                Summ_ch = Summ_ch + ((im1[x, y] - avg_pix_br_1) * (im2[x, y] - avg_pix_br_2))
                Summ_zn_1 = Summ_zn_1 + (im1[x, y] - avg_pix_br_1) ** 2
                Summ_zn_2 = Summ_zn_2 + (im2[x, y] - avg_pix_br_2) ** 2
    else:
        print("Размер изображений не совпадают!")

    Pirsons_coef = Summ_ch / math.sqrt(Summ_zn_1 * Summ_zn_2)

    return round(Pirsons_coef, 5)


"""print(f'Коэффициент корреляции Пирсона равен: {coef_corr(img1, img2)}')
print(f'Коэффициент корреляции Пирсона равен: {coef_corr(img3, img4)}')"""

spisok = []
d = {}

for i in range(1, 6):
    d[f'img{i+1}'] = coef_corr(img1, a[i])
    spisok.append(coef_corr(img1, a[i]))
print(f'Коэффициенты корреляции для 5 тестовых изображений: {d}\n {spisok}')

try:
    with open("out.txt", "a") as file:
        file.write(f'Coef{k}: {d}\n')
except:
    print(f"Ошибка")
finally:
    file.close()