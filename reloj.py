import tkinter as Tkinter
from tkinter import Label  # Importe a classe Label separadamente
import time

# Variável para rastrear o idioma atual
idioma = "portugues"

def toggle_idioma():
    global idioma
    if idioma == "portugues":
        idioma = "ingles"
        label.config(text="Digital Clock")
        toggle_button.config(text="Mudar para Português")
    else:
        idioma = "portugues"
        label.config(text="Relógio Digital")
        toggle_button.config(text="Mudar para Inglês")

def aumentar_contraste():
    # Função para aumentar o contraste do texto
    # Você pode implementar isso conforme necessário
    pass

app_window = Tkinter.Tk()
app_window.title("Relógio Digital")
app_window.geometry("510x150")
app_window.resizable(1, 1)
app_window.option_add('*Font', 'Boulder 68 bold')

text_font = ("Boulder", 68, 'bold')
background = "#a2e000"
foreground = "#570600"
border_width = 25

# Título da janela para melhor usabilidade
app_window.title("Relógio Digital")
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

label = Tkinter.Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

toggle_button = Tkinter.Button(app_window, text="Mudar para Inglês", command=toggle_idioma)
toggle_button.grid(row=1, column=1)

# Botão para aumentar contraste (usabilidade)
contraste_button = Tkinter.Button(app_window, text="Aumentar Contraste", command=aumentar_contraste)
contraste_button.grid(row=2, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
