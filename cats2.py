from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

ALLOWED_TAGS = ['sleep', 'crazy', 'cute', 'babycat', 'strange', 'jump', 'smile', 'fight',
                'black', 'white', 'red', 'siamese', 'bengal']


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window(url):
    img = load_image(url)
    if img:
        new_window = Toplevel()
        new_window.title("Изображение котика")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

def open_tagged_cat():
    tag = tag_combobox.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    open_new_window(url_with_tag)

def open_random_cat():
    url = 'https://cataas.com/cat'
    open_new_window(url)

def exit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_tagged_cat)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


tag_label = Label(text="Выберите тег")
tag_label.pack(pady=10)

tag_combobox = ttk.Combobox(values=ALLOWED_TAGS)
tag_combobox.pack()

update_button1 = Button(text="Обновить котика по тегу", command=open_tagged_cat)
update_button1.pack(pady=10)

button_random_cat = Button(window, text="Случайный котик", command=open_random_cat)
button_random_cat.pack(pady=10)

update_button = Button(text="Обновить случайного котика", command=open_random_cat)
update_button.pack(pady=10)


window.mainloop()
