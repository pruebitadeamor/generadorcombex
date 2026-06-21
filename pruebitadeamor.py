import os
import random
import sys
import time
import names
from tqdm import tqdm
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==================== COLORES (Solo Rojo, Azul, Morado) ====================
RESET = "\033[0m"
ROJO = "\033[38;5;196m"
ROJO2 = "\033[38;5;160m"
AZUL = "\033[38;5;27m"
AZUL2 = "\033[38;5;21m"
MORADO = "\033[38;5;201m"
MORADO2 = "\033[38;5;165m"
MORADO3 = "\033[38;5;93m"

def print_colored(text, color):
    print(f"{color}{text}{RESET}")

def eliminar_lineas_duplicadas(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        unique_lines = list(set(lines))
        duplicates = len(lines) - len(unique_lines)

        print_colored(f"Archivo: {file_path}", AZUL)
        print_colored(f"Líneas originales: {len(lines)}", MORADO)
        print_colored(f"Duplicados eliminados: {duplicates}", ROJO)
        print()

        directory = "/sdcard/SinDuplicadas"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.basename(file_path)
        output_path = os.path.join(directory, filename)

        with open(output_path, "w", encoding="utf-8") as file:
            file.writelines(unique_lines)

        print_colored(f"✅ Archivo guardado en: {output_path}", MORADO)

    except Exception as e:
        print_colored(f"❌ Error: {e}", ROJO)

def mostrar_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    time.sleep(0.1)
    
    header = f"""
{MORADO}╔══════════════════════════════════════════════════════════════╗
{ROJO}║                 Ƹ̵̡Ӝ̵̨̄Ʒ  DAVO COMBO GENERATOR  Ƹ̵̡Ӝ̵̨̄Ʒ               ║
{MORADO}╚══════════════════════════════════════════════════════════════╝{RESET}

{AZUL}     𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚
    
{ROJO}          ▄▀▄▀▄  DAVO  ▄▀▄▀▄
          █░█░█  COMBOS  █░█░█
          ▀░▀░▀  POWER   ▀░▀░▀
    
{AZUL}     𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚ 𓂃₊ཐི༑ཋྀ˚

{MORADO}               Edit by DAVO © 2026
{RESET}"""
    print(header)
    time.sleep(0.3)

def generar_linea(menu, combo_opt, names_list=None):
    if names_list:
        rname = random.choice(names_list)
        rlastname = random.choice(names_list)
    else:
        rname = names.get_first_name()
        rlastname = names.get_last_name()

    if menu == "1":
        num = random.randint(2000, 2026)
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "2":
        left = rname
        right = rlastname
    elif menu == "3":
        num = random.randint(1, 499)
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "4":
        num = random.randint(500, 999)
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "5":
        num = random.randint(1900, 2026)
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "6":
        num = random.choice(["0","00","000","0000"])
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "7":
        num = random.choice(["111","222","333","444","555","666","777","888","999"])
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "8":
        num = random.choice(["123","1234","12345","321","4321","54321"])
        left = f"{rname}{num}"
        right = f"{rname}"
    elif menu == "9":
        num = random.choice(["123","1234","12345","123456","321","4321","54321","654321"])
        left = rname
        right = num
    else:
        left = rname
        right = rlastname

    if combo_opt == "1":
        return f"{left}:{right}"
    elif combo_opt == "2":
        return f"{right}:{left}"
    else:
        return f"{left}:{left}" if random.random() < 0.5 else f"{right}:{right}"

def main():
    # Crear carpeta de combos
    COMBO_DIR = "/storage/emulated/0/combo"
    if not os.path.exists(COMBO_DIR):
        try:
            os.makedirs(COMBO_DIR)
            print_colored(f"✅ Carpeta creada: {COMBO_DIR}", MORADO)
        except Exception as e:
            print_colored(f"⚠️ No se pudo crear la carpeta. Usando /sdcard en su lugar.", ROJO)
            COMBO_DIR = "/sdcard"

    while True:
        mostrar_header()
        
        print_colored("""
𝕋𝕚𝕡𝕠 𝕕𝕖 ℂ𝕠𝕞𝕓𝕠 𝕡𝕒𝕣𝕒 𝕔𝕣𝕖𝕒𝕣

1) USER:PASS 2000 AL 2026
2) USER:PASS SIMPLE NOMBRE-NOMBRE
3) USER:PASS 1 AL 499
4) USER:PASS 500 AL 999
5) USER:PASS AÑO DE NACIMIENTO
6) USER:PASS 0 AL 0000
7) USER:PASS 111-999 (repetidos)
8) USER:PASS 123 AL 12345
9) USER:NUMB 123 AL 123456
10) CREA UN COMBO CON TU LISTA
11) ELIMINAR LINEAS DUPLICADAS
12) SALIR
        """, MORADO)

        menu = input(f"{AZUL}Ingrese una opción → {RESET}").strip()

        if menu == "12":
            print_colored("\n👋 Gracias por usar DAVO Combo Generator. ¡Hasta pronto!", ROJO)
            sys.exit()

        elif menu == "11":
            file_path = input(f"{AZUL}Ingrese la ruta del archivo .txt: {RESET}").strip()
            if os.path.exists(file_path):
                if input(f"{MORADO}¿Eliminar duplicados? (1=Sí): {RESET}") == "1":
                    eliminar_lineas_duplicadas(file_path)
            else:
                print_colored("❌ Archivo no encontrado.", ROJO)
            input(f"{AZUL}\nPresiona Enter...{RESET}")
            continue

        # Opción 10 - Con lista propia
        elif menu == "10":
            file_path = input(f"{AZUL}Ruta del archivo .txt ('10' para volver): {RESET}").strip()
            if file_path == "10":
                continue
            if not os.path.exists(file_path):
                print_colored("❌ Archivo no encontrado.", ROJO)
                input(f"{AZUL}Presiona Enter...{RESET}")
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                names_list = [line.strip() for line in f if line.strip()]

            hwm = int(input(f"{AZUL}Número de líneas (x2): {RESET}"))
            threads = int(input(f"{MORADO}Número de hilos (1-15): {RESET}").strip())
            threads = max(1, min(15, threads))

            filename = input(f"{AZUL}Nombre del Combo: {RESET}").strip()
            output_file = os.path.join(COMBO_DIR, f"{filename}.txt")

            print_colored("Tipo de combinación:", MORADO)
            print_colored("1 = Solo Izquierda", ROJO)
            print_colored("2 = Solo Derecha", AZUL)
            print_colored("3 = Ambas", MORADO)
            combo_opt = input(f"{AZUL}Elige: {RESET}").strip() or "3"

            lines_set = set()
            lock = threading.Lock()

            def worker():
                while len(lines_set) < hwm * 2:
                    line = generar_linea(menu, combo_opt, names_list)
                    line_nl = line + "\n"
                    with lock:
                        if line_nl not in lines_set:
                            lines_set.add(line_nl)
                            with open(output_file, "a", encoding="utf-8") as f:
                                f.write(line_nl)
                            return True
                return False

            with tqdm(total=hwm, desc="Generando", ncols=70, colour="magenta") as pbar:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    futures = [executor.submit(worker) for _ in range(hwm)]
                    for future in as_completed(futures):
                        if future.result():
                            pbar.update(1)

            print_colored(f"\n✅ Combo guardado en: {output_file}", MORADO)
            input(f"{AZUL}Presiona Enter...{RESET}")
            continue

        # Opciones 1-9
        elif menu in ["1","2","3","4","5","6","7","8","9"]:
            filename = input(f"{AZUL}Nombre del Combo: {RESET}").strip()
            hwm = int(input(f"{AZUL}Número de líneas (x2): {RESET}"))
            threads = int(input(f"{MORADO}Número de hilos (1-15): {RESET}").strip())
            threads = max(1, min(15, threads))

            output_file = os.path.join(COMBO_DIR, f"{filename}.txt")

            combo_opt = "3"
            if menu != "2":
                print_colored("Tipo de combinación:", MORADO)
                print_colored("1 = Solo Izquierda", ROJO)
                print_colored("2 = Solo Derecha", AZUL)
                print_colored("3 = Ambas", MORADO)
                combo_opt = input(f"{AZUL}Elige: {RESET}").strip() or "3"

            lines_set = set()
            lock = threading.Lock()

            def worker():
                while len(lines_set) < hwm * 2:
                    line = generar_linea(menu, combo_opt)
                    line_nl = line + "\n"
                    with lock:
                        if line_nl not in lines_set:
                            lines_set.add(line_nl)
                            with open(output_file, "a", encoding="utf-8") as f:
                                f.write(line_nl)
                            return True
                return False

            with tqdm(total=hwm, desc="Generando", ncols=70, colour="magenta") as pbar:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    futures = [executor.submit(worker) for _ in range(hwm)]
                    for future in as_completed(futures):
                        if future.result():
                            pbar.update(1)

            print_colored(f"\n✅ Combo guardado en: {output_file}", MORADO)
            input(f"{AZUL}Presiona Enter para continuar...{RESET}")

        else:
            print_colored("❌ Opción no válida.", ROJO)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\n\n👋 Saliendo de DAVO Combo Generator...", ROJO)
        sys.exit()