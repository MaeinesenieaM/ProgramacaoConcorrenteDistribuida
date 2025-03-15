import time
import threading

def calculo(i):
    print(f"Começo da thread: {i}")
    time.sleep(2)
    print(f"Fim da thread {i}")

T1 = threading.Thread(target = calculo, args = {1})
T2 = threading.Thread(target = calculo, args = {2})


tempo_start = time.time()
T1.start()
T2.start()
T1.join()
T2.join()
tempo_end = time.time()

print(f"Termino do programa! Tempo executado: {tempo_end - tempo_start:.2f}")


