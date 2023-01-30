import pyautogui
import tkinter as tk
import time

def pegar_coordenadas():
    global coordenadas
    time.sleep(2)
    coordenadas = pyautogui.position()
    label_coordenadas.config(text=f"Coordenadas: {coordenadas}")

def pixel_alterado(coordenadas):
    global cor_anterior
    # Obtenha a cor do pixel nas coordenadas especificadas
    cor_atual = pyautogui.screenshot().getpixel(coordenadas)
    
    # Verifique se a cor é diferente da cor anterior
    if cor_atual != cor_anterior:
        # Atualize a cor anterior para a cor atual
        cor_anterior = cor_atual
        
        # Clique no pixel
        pyautogui.click(coordenadas)
            
        # Atualize a label para mostrar que houve uma ação
        label_acao.config(text="Ação realizada!")
        root.update()
        parar_script()


# Flag para rastrear se o script está em execução
script_executando = False

def parar_script():
    global script_executando
    script_executando = False
    label_acao.config(text="Script desligado!")

def iniciar_script():
    global script_executando, cor_anterior
    script_executando = True
    label_acao.config(text="Script ligado!")
    
    # Obtenha a cor inicial do pixel nas coordenadas especificadas
    cor_anterior = pyautogui.screenshot().getpixel(coordenadas)
    
    while script_executando:
        pixel_alterado(coordenadas)
        time.sleep(0.5)

# Crie a GUI
root = tk.Tk()
root.title("AutoClick-Cord")
root.geometry("250x120")
root.attributes("-topmost", True)

# Crie o botão para pegar as coordenadas
botao_coordenadas = tk.Button(root, text="Pegar Coordenadas", command=pegar_coordenadas)
botao_coordenadas.pack()

# Crie o botão iniciar
botao_iniciar = tk.Button(root, text="Ligar", command=iniciar_script)
botao_iniciar.pack()

# Crie o botão parar
botao_parar = tk.Button(root, text="Desligar", command=parar_script)
botao_parar.pack()

# Crie a label para mostrar as coordenadas
label_coordenadas = tk.Label(root, text="Coordenadas: N/A")
label_coordenadas.pack()

# Crie a label para mostrar as ações do script
label_acao = tk.Label(root, text="Script desligado!")
label_acao.pack()

# Inicie a GUI
root.mainloop()
