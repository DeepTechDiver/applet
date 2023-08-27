import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame  # 导入pygame库，用于播放音乐

# 定义一个图片切换器类
class ImageSwitcher:
    # 初始化函数
    def __init__(self):
        # 创建一个Tk窗口
        self.root = tk.Tk()
        # 隐藏窗口边框
        self.root.overrideredirect(1)
        # 创建一个标签，用于显示图片
        self.image_label = tk.Label(self.root)
        # 将标签添加到窗口中
        self.image_label.pack()
        # 绑定鼠标右键点击事件，弹出选项框
        self.image_label.bind("<Button-3>", self.on_image_click)
        # 绑定鼠标左键长按拖动事件
        self.image_label.bind("<B1-Motion>", self.on_drag)
        # 定义一个图片列表，存储所有的图片
        self.images = [
            Image.open("img/1.png").resize((520, 520)),
            Image.open("img/2.png").resize((520, 520)),
            Image.open("img/3.png").resize((520, 520)),
            Image.open("img/4.png").resize((520, 520)),
            Image.open("img/5.png").resize((520, 520))
        ]
        # 定义一个变量，记录当前显示的图片索引
        self.current_image_index = 0
        # 更新图片
        self.update_image()
        # 初始化pygame
        pygame.init()
        # 加载背景音乐
        pygame.mixer.music.load('img/music.mp3')
        # 播放背景音乐，-1表示循环播放
        pygame.mixer.music.play(-1)

    # 定义鼠标右键点击事件处理函数
    def on_image_click(self, event):
        # 创建一个菜单
        menu = tk.Menu(self.root, tearoff=0)
        # 定义一个标签列表，对应每个图片的标签
        image_labels = ["144p", "360p", "480p", "720p", "1080p"]
        # 遍历图片列表，为每个图片添加一个菜单项
        for i in range(len(self.images)):
            menu.add_command(label=image_labels[i], command=lambda i=i: self.switch_to_image(i))
        # 添加一个关闭选项
        menu.add_command(label="关闭", command=self.root.quit)
        # 在鼠标点击的位置弹出菜单
        menu.post(event.x_root, event.y_root)

    # 定义鼠标左键长按拖动事件处理函数
    def on_drag(self, event):
        # 获取鼠标当前的位置
        x, y = event.x_root, event.y_root
        # 移动窗口到鼠标当前的位置
        self.root.geometry(f"+{x}+{y}")

    # 定义一个函数，用于切换图片
    def switch_to_image(self, index):
        # 更新当前显示的图片索引
        self.current_image_index = index
        # # 如果当前图片是第五张图片，触发烟花特效
        # if index == 4:
        #     self.fireworks_effect()  # 调用烟花特效函数
        # 更新图片
        self.update_image()

    # 定义一个函数，用于更新图片
    def update_image(self):
        # 获取当前显示的图片
        image = ImageTk.PhotoImage(self.images[self.current_image_index])
        # 更新标签的图片
        self.image_label.config(image=image)
        # 保存图片，防止被垃圾回收
        self.image_label.image = image

    # # 定义一个函数，用于实现烟花特效
    # def fireworks_effect(self):
    #     # 创建一个顶级窗口
    #     top = tk.Toplevel(self.root)
    #     # 隐藏窗口边框
    #     top.overrideredirect(1)
    #     # 设置窗口背景为黑色
    #     top.configure(background='black')
    #     # 创建一个Canvas，用于绘制烟花
    #     canvas = tk.Canvas(top, bg='black', width=300, height=300)
    #     canvas.pack()
    #     # 创建一个烟花对象
    #     firework = Firework(canvas, 200, 200)
    #     # 启动烟花
    #     firework.launch()
    #     # 设置窗口在屏幕中的位置
    #     top.geometry("+300+300")
    #     # 3秒后关闭窗口
    #     top.after(3000, top.destroy)
    #     self.create_firework(canvas)

    # def create_firework(self, canvas):
    #     x = random.randint(50, 750)
    #     y = 550
    #     canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="red")

    #     for _ in range(30):
    #         dx = random.uniform(-5, 5)
    #         dy = random.uniform(-5, 5)
    #         canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="orange", outline="orange")
    #         x += dx
    #         y -= dy
    #         self.root.update()
    #         canvas.after(50)
    #         canvas.delete("all")

    #     self.create_firework(canvas)

# 创建一个图片切换器对象
app = ImageSwitcher()
# 启动Tk窗口的消息循环
app.root.mainloop()