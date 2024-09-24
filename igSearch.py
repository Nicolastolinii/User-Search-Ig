from userName import generar_nombres_usuario
import time
import requests

STATUS_PAGE_NOT_FOUND = 404
STATUS_USER_FOUND = 200
HEADER_05 = "Pragma"


class InstagramScraper:
    def __init__(self):
        pass    
    def search_user(self, user):
        try:
            response = requests.get(f'https://www.instagram.com/{user}/')
            headers_list = list(response.headers.items())
            if headers_list[5][0] == HEADER_05:
                status_code = STATUS_PAGE_NOT_FOUND
                print(f"| \033[91m{status_code}\033[0m User: {user} No encontrado o estructura de cabecera diferente.")
            else:
                status_code = STATUS_USER_FOUND
                print(f"| \033[92m{status_code}\033[0m User: {user} encontrado.\n| https://www.instagram.com/{user}/")
        except Exception as e:
            print(f"Error en la búsqueda de {user}: {e}")
            
class UserNameGenerator:
    def __init__(self, nombre_completo):
        self.nombre_completo = nombre_completo

    def generar_variaciones(self):
        return generar_nombres_usuario(self.nombre_completo)
    
class App:
    def __init__(self, nombre_completo):
        self.nombre_completo = nombre_completo
        self.instagram_scraper = InstagramScraper()
        self.username_generator = UserNameGenerator(nombre_completo)
        
    def run(self):
        variaciones = self.username_generator.generar_variaciones()
        for nombre in variaciones:
            self.instagram_scraper.search_user(nombre)



if __name__ == "__main__":
    start_time = time.time()
    nombre_completo = ""
    
    app = App(nombre_completo)
    app.run()
    print(f"Tiempo total de ejecución: {time.time() - start_time} segundos")