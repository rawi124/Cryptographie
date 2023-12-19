import subprocess
import time

def pin_verif(code):
    pin_secret = [ '3', '7', '0', '4']
    if len(code) != 4: return False
    for i in range(4):
        time.sleep(0.1)
        if code[i] != pin_secret[i]: return False
    return True

cle = ""
PIN_TAILLE = 4
while len(cle) != PIN_TAILLE:
    runtime_l = -1
    best_key = ""
    for i in range(10):
        temp = cle + str(i) + "0" * (PIN_TAILLE - len(cle) - 1)
        start_time = time.time()
        result = pin_verif(temp)
        # result = subprocess.run("./output/pin4.exe", temp, shell=True)
        execution_time = time.time() - start_time
        if runtime_l < execution_time:
            best_key = str(i)
            runtime_l = execution_time
    cle += best_key

print(f"PIN : {cle}")