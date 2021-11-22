import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
T = 100
# Выбираем encoder
# В данном случае FFMpeg
# Для этого он должен быть установлен в системе
FFMpegWriter = manimation.writers['ffmpeg']
# fps - число кадров в секунду
writer = FFMpegWriter(fps=25)
# размер шрифта для подписей
mpl.rcParams['legend.fontsize'] = 10
# Нам понадобится класс, описывающий рисунок
fig = plt.figure()
# Настройки encoder’а
# 200 - dpi (число точек на дюйм)
writer.setup(fig, "video.avi" , 200)
# Создаём сетку
x = np.arange(0, np.pi * 5, 0.1)
for t in range(0, T):
# Заводим функцию на сетке
	y = np.sin(x - 2 * np.pi * t / T)
# Рисуем
	plt.plot(x, y)
	plt.title("T = %f" % (t))
# Сохраняем кадр
	writer.grab_frame()
# Очищаем рисунок для следующей итерации
	plt.clf()