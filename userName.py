# Diccionario para sustituir letras por símbolos o números
sustituciones = {
    'o': '0',
    'i': '1',
    'e': '3',
}
prefijos_comunes = ["the", "its", "real", "official"]
sufijos_comunes = ["123", "01", "00", "official", "x", "_x", "ok"]

def sustituir_letras(nombre, sustituir_primera=False):
    """
    Reemplaza letras del nombre con números o símbolos según el diccionario.
    """
    nombre_sustituido = nombre
    for letra, reemplazo in sustituciones.items():   
        nombre_sustituido = nombre_sustituido.replace(letra, reemplazo)
        if sustituir_primera:
            # Reemplaza solo la primera aparición de la letra
            nombre_sustituido = nombre_sustituido.replace(letra, reemplazo, 1)
        else:
            # Reemplaza todas las apariciones de la letra
            nombre_sustituido = nombre_sustituido.replace(letra, reemplazo)
    return nombre_sustituido

def generar_nombres_usuario(nombre_completo, anio=None):
    # Separar el nombre completo en partes
    partes = nombre_completo.split()
    nombre = partes[0].lower()
    apellido = partes[1].lower() if len(partes) > 1 else ""

    

    # Lista para almacenar los nombres de usuario posibles (utilizando un set para eliminar duplicados)
    posibles_nombres = set()

    # Generar combinaciones básicas
    posibles_nombres.add(f"{nombre}{apellido}")
    posibles_nombres.add(f"{nombre}_{apellido}")
    posibles_nombres.add(f"{nombre}.{apellido}")
    posibles_nombres.add(f"{nombre[0]}{apellido}")
    posibles_nombres.add(f"{nombre}{apellido[0]}")
    posibles_nombres.add(f"{nombre[0]}_{apellido}")
    posibles_nombres.add(f"{nombre}_{apellido[0]}")
    posibles_nombres.add(f"{nombre}{apellido}123")
    posibles_nombres.add(f"{nombre}{apellido}00")
    posibles_nombres.add(f"{nombre}{apellido}01")
    posibles_nombres.add(f"{nombre}{apellido}0")  # Nueva combinación con 0 al final


    for prefijo in prefijos_comunes:
        posibles_nombres.add(f"{prefijo}{nombre}{apellido}")
    for sufijo in sufijos_comunes:
        posibles_nombres.add(f"{nombre}{apellido}{sufijo}")
        
    # Crear variaciones con números (incluyendo santibrito0)
    for i in range(10):
        posibles_nombres.add(f"{nombre}{apellido}{i}")
        posibles_nombres.add(f"{nombre}_{apellido}{i}")
        
    if anio:
        posibles_nombres.add(f"{nombre}{apellido}{anio}")
        posibles_nombres.add(f"{nombre}_{apellido}{anio}")
    
    # Variaciones con iniciales y números
    iniciales = f"{nombre[0]}{apellido[0]}"
    posibles_nombres.add(iniciales)
    for i in range(100, 105):
        posibles_nombres.add(f"{iniciales}{i}")

    posibles_nombres.add(f"{nombre}{apellido}{apellido[-1]}")
    posibles_nombres.add(f"{nombre}{nombre[-1]}{apellido}{apellido[-1]}")
    posibles_nombres.add(f"{nombre}{nombre[-1]}{apellido}")


    # Combinaciones utilizando primeras letras del nombre y apellido
    posibles_nombres.add(f"{nombre[:3]}{apellido}")
    posibles_nombres.add(f"{nombre[:4]}{apellido}")
    posibles_nombres.add(f"{nombre[:5]}{apellido}")
    posibles_nombres.add(f"{nombre[:6]}{apellido}")
    posibles_nombres.add(f"{nombre[:3]}_{apellido}")
    posibles_nombres.add(f"{nombre[:4]}_{apellido}")
    posibles_nombres.add(f"{nombre[:5]}_{apellido}")
    posibles_nombres.add(f"{nombre[:6]}_{apellido}")
    
    # Nuevas combinaciones agregando números al final de esas variaciones cortas
    for i in range(10):
        posibles_nombres.add(f"{nombre[:3]}{apellido}{i}")
        posibles_nombres.add(f"{nombre[:4]}{apellido}{i}")
        posibles_nombres.add(f"{nombre[:5]}{apellido}{i}")
        posibles_nombres.add(f"{nombre[:6]}{apellido}{i}")
        posibles_nombres.add(f"{nombre[:3]}_{apellido}{i}")
        posibles_nombres.add(f"{nombre[:4]}_{apellido}{i}")
        posibles_nombres.add(f"{nombre[:5]}_{apellido}{i}")
        posibles_nombres.add(f"{nombre[:6]}_{apellido}{i}")
        

    # Otras combinaciones (invirtiendo nombre y apellido)
    posibles_nombres.add(f"{apellido}{nombre}")
    posibles_nombres.add(f"{apellido}_{nombre}")
    posibles_nombres.add(f"{apellido}.{nombre}")
    
     # Variaciones con guiones en el medio
    posibles_nombres.add(f"{nombre}-{apellido}")
    posibles_nombres.add(f"{apellido}-{nombre}")

    # Variaciones con mayúsculas
    posibles_nombres.add(f"{nombre.capitalize()}{apellido.capitalize()}")
    posibles_nombres.add(f"{nombre.capitalize()}_{apellido.capitalize()}")
    
    # Variaciones con sustitución de letras (aplicar a todas las combinaciones generadas)
    nuevas_variaciones = set()
    for nombre_variacion in posibles_nombres:
        nuevas_variaciones.add(sustituir_letras(nombre_variacion))
        
        nuevas_variaciones.add(sustituir_letras(nombre_variacion, sustituir_primera=True))
  
    # Unir las variaciones originales y las sustituidas
    posibles_nombres.update(nuevas_variaciones)

    # Eliminar duplicados y convertir de nuevo a lista
    posibles_nombres = list(posibles_nombres)
    
    #print(posibles_nombres)

    return posibles_nombres

# Ejemplo de uso
nombre_completo = ""
variaciones = generar_nombres_usuario(nombre_completo)
