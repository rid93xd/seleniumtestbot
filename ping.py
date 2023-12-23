import subprocess

def hacer_ping(ip):
    try:
        
        resultado = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1, text=True)

        # Comprueba si el ping fue exitoso (0) o no (otros valores)
        if resultado.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al hacer ping a {ip}: {str(e)}")
        return False

def filtrar_proxies(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada:
        lineas = entrada.readlines()

    proxies_validos = []

    for linea in lineas:
        ip_puerto = linea.strip()
        ip = ip_puerto.split(':')[0]

        if hacer_ping(ip):
            proxies_validos.append(ip_puerto)

    with open(archivo_salida, 'w') as salida:
        for proxy_valido in proxies_validos:
            salida.write(f"{proxy_valido}\n")

if __name__ == "__main__":
    archivo_entrada = "proxy.txt"
    archivo_salida = "proxy2.txt"

    filtrar_proxies(archivo_entrada, archivo_salida)
