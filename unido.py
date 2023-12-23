from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_proxy_driver(ip, port):
    proxy = Proxy({
        'proxyType': 'MANUAL',
        'httpProxy': ip + ":" + port,
        'sslProxy': ip + ":" + port
    })
    options = webdriver.ChromeOptions()
    options.proxy = proxy
    driver = webdriver.Chrome(options=options)
    return driver

with open('proxy.txt', 'r') as f:
    proxies = f.readlines()

for proxy in proxies:
    ip, port = proxy.strip().split(':')
    
    try:
        # Prueba de proxy sin interacciones con el sitio web
        driver = create_proxy_driver(ip, port)
        print(f"Opened browser with proxy: {ip}:{port}")
        driver.get('sitio objetivo')  # Reemplaza con la URL correcta
        time.sleep(10)  # Agregar aquí cualquier espera necesaria
        driver.quit()
        print(f"Closed browser with proxy: {ip}:{port}")
        
        # Interacciones con el sitio web después de cada prueba de proxy
        driver = create_proxy_driver(ip, port)
        print(f"Opened browser with proxy for site interaction: {ip}:{port}")
        url = "sitio objetivo"  # Reemplaza con la URL correcta
        driver.get(url)
        
        # interacciones con el sitio web después de cargar la URL
        elemento_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "IDBOTON")) and
            EC.presence_of_element_located((By.CLASS_NAME, "IDCLASE"))
        )
        time.sleep(10)
        # Hacer clic en el botón
        elemento_boton.click()

       

        
        # Busca y haz clic en el segundo botón
        elemento_enviar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "IDBOTON")) and
            EC.presence_of_element_located((By.CLASS_NAME, "IDCLASE"))
        )

        # Haz clic en el segundo botón
        
        elemento_enviar.click()
                        
        print("Site interaction successful")

    except Exception as e:
        print(f"Error with proxy {ip}:{port} - {str(e)}")
    finally:
        
        driver.quit()
        print(f"Closed browser after site interaction: {ip}:{port}")
