import pyautogui
import time
import keyboard
from PIL import ImageGrab

# Variável de controle do botão
on_off = False

def find_color_on_screen(target_color, screen_width, screen_height):
    screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

    for x in range(0, screen_width, 15):
        for y in range(0, screen_height, 15):
            pixel_color = screen.getpixel((x, y))

            if pixel_color == target_color:
                return x, y

    return None

def click_color_on_screen(target_color, screen_width, screen_height):
    while True:
        if on_off:
            position = find_color_on_screen(target_color, screen_width, screen_height)
            if position:
                x, y = position
                pyautogui.moveTo(x, y, duration=0.25)  # Movimento suave do mouse
                pyautogui.click(x, y)
        time.sleep(0.02)  # Intervalo de 1 segundo entre as verificações

# Tamanho específico da tela a ser analisado
screen_width = 1920  # Defina a largura desejada da tela
screen_height = 1080  # Defina a altura desejada da tela

# Cor RGB que você deseja procurar
target_color = (255, 219, 195)  # RGB da cor alvo (vermelho puro)

# Função para alternar o botão ligar/desligar
def toggle_on_off():
    global on_off
    on_off = not on_off

# Configuração do botão de ativação
keyboard.add_hotkey('Ctrl', toggle_on_off)

# Chama a função para clicar na cor alvo na tela em um loop controlado pelo botão on_off
click_color_on_screen(target_color, screen_width, screen_height)
