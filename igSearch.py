from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from userName import generar_nombres_usuario
import time

brave_binary_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe' 
STATUS_PAGE_NOT_FOUND = 404
STATUS_USER_FOUND = 200


class InstagramScraper:
    def __init__(self, brave_binary_path):
        self.options = self.setup_options(brave_binary_path)
        self.driver = webdriver.Chrome(options=self.options)
        
    def setup_options(self, brave_binary_path):
        options = Options()
        options.binary_location = brave_binary_path
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-session-crashed-bubble")
        options.add_argument("--headless")  # Modo headless para evitar la interfaz gráfica
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_argument("--disable-css")
        options.add_argument("--disable-javascript")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        return options
    
    def search_user(self, user):
        self.driver.get(f'https://www.instagram.com/{user}/')
        try:
            title = self.driver.title
            if "Página no encontrada" in title:
                status_code = STATUS_PAGE_NOT_FOUND
                #print(f"| \033[91m{status_code}\033[0m User: {user} No existe.")
            else:
                status_code = STATUS_USER_FOUND
                index = title.find('(')
                result = title[:index] if index != -1 else title
                print(f"| \033[92m{status_code}\033[0m User: {result[:10]}  \n| https://www.instagram.com/{user}/")
        except Exception as e:
            print(f"Error en la búsqueda de {user}: {e}")
            
    def close(self):
        self.driver.quit()

class UserNameGenerator:
    def __init__(self, nombre_completo):
        self.nombre_completo = nombre_completo

    def generar_variaciones(self):
        return generar_nombres_usuario(self.nombre_completo)
    
class App:
    def __init__(self, nombre_completo, brave_binary_path):
        self.nombre_completo = nombre_completo
        self.instagram_scraper = InstagramScraper(brave_binary_path)
        self.username_generator = UserNameGenerator(nombre_completo)

    def run(self):
        variaciones = self.username_generator.generar_variaciones()
        for nombre in variaciones:
            self.instagram_scraper.search_user(nombre)
        self.instagram_scraper.close()





if __name__ == "__main__":
    start_time = time.time()
    nombre_completo = ""

    app = App(nombre_completo, brave_binary_path)
    app.run()
    print(f"Tiempo total de ejecución: {time.time() - start_time} segundos")