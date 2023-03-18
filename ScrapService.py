import os
import subprocess
import datetime
import time
import pyfiglet

DIRLOG = ""
DIRMESSAGE = ""
BANNER = pyfiglet.figlet_format("SCRAPPING")

print(BANNER)
PORT = int(input("Digite o número da porta: "))

while True:
    # Cria uma string com a data e hora atual
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Cria o nome do arquivo de log com a data e hora atual
    log_filename = f"{PORT}_{timestamp}.log"
    # Cria o caminho completo para o arquivo de log
    log_filepath = os.path.join(DIRLOG, log_filename)
    # Cria o arquivo de log se não existir
    open(log_filepath, "a").close()
    # Executa o comando Bash para enviar a menssagem para quem conectar e gravar a saída no arquivo de log atual
    command = f"sudo nc -lvnp {PORT} < {os.path.join(DIRMESSAGE)} 1>>{log_filepath} 2>>{log_filepath}"
    print("Running...")
    subprocess.call(command, shell=True)
    # Pausa o loop por 2 segundos
    time.sleep(2)
