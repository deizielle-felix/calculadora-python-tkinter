import re
from tkinter import *

# Cores -----------------
color_1 = '#1e1f1e'  # Cinza
color_2 = '#EB6536'  # Laranja
color_3 = '#F2F1F0'  # Branco

# Definição da janela
window = Tk()
window.title('Calculadora')
window.geometry('330x366')

# Definição de frames
frame_screen = Frame(window, width=330, height=75, bg=color_1)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=330, height=410)
frame_body.grid(row=1, column=0)

# StringVar para exibir os eventos
text_value = StringVar()

# Criação da label do resultado
result_label = Label(frame_screen, textvariable=text_value, fg=color_3, bg=color_1, width=22, height=2,
                     font='Inter 15', relief=FLAT, anchor='e', justify=RIGHT, padx=7)
result_label.place(x=9, y=10)

# Variável que guarda todos os botões apertados até que se forme uma expressão matemática
history = ''


def create_buttons(text, frame=frame_body, width=6, height=2, font='Inter', special=False):
    """
    Cria botões para a calculadora.

    :param text: str: Texto no botão.
    :param frame: Frame: Frame onde o botão será colocado.
    :param width: int: Largura do botão.
    :param height: int: Altura do botão.
    :param font: str: Fonte do botão.
    :param special: bool: Indica se o botão possui uma cor diferente dos demais.
    :return: Botão criado.
    """
    global color_2, color_3
    if special:
        return Button(frame, text=text, command=lambda: set_value(text),
                      bg=color_2, fg=color_3, width=width, height=height, font=font)
    else:
        return Button(frame, text=text, command=lambda: set_value(text),
                      width=width, height=height, font=font)


def set_value(event):
    """
    Esta função atualiza o visor com os valores digitados ou operações selecionadas.

    :param event: str: Evento ocorrido (valor digitado).
    :return: None
    """
    global history
    if event == 'del':
        history = history[:-1]
    elif event == 'C':
        history = ''
    elif event == '=':
        if calculate():
            history = calculate()
    else:
        history += event
    # Definição do valor da StringVar
    text_value.set(history)


def calculate():
    """
    Esta função calcula a expressão matemática inserida pelo usuario.

    :return: str: Resultado do cálculo ou False se a expressão for inválida.
    """
    global history
    if 'x' in history:
        history = history.replace('x', '*')
    if any(op in history for op in ['-', '+', '*', '/', '%']):
        if '(' in history:
            pattern = re.compile(r'.*[-+*/%]\(')
            check = re.match(pattern, history)
            if not check:
                return False
        try:
            result = eval(history)
            return result
        except:
            return False
    else:
        return history


# Botões
buttons_data = [
    ('C', False, 0, 0), ('(', False, 85, 0), (')', False, 165, 0), ('+', True, 245, 0),
    ('7', False, 0, 58), ('8', False, 85, 58), ('9', False, 165, 58), ('/', True, 245, 58),
    ('4', False, 0, 116), ('5', False, 85, 116), ('6', False, 165, 116), ('x', True, 245, 116),
    ('1', False, 0, 174), ('2', False, 85, 174), ('3', False, 165, 174), ('-', True, 245, 174),
    ('del', False, 0, 232), ('0', False, 85, 232), ('.', False, 165, 232), ('=', True, 245, 232),
]

for button in buttons_data:
    create_buttons(button[0], special=button[1]).place(x=button[2], y=button[3])

window.mainloop()


