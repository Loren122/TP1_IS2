import openai, sys # Se importan los paquetes necesarios para el programa


# Se rellena con la API key
openai.api_key = "api_key"

def obtener_consulta():
    userquery = input("Ingrese su consulta: ")
    return userquery.strip() # Retorna la consulta

def realizar_consulta(userquery):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125", # Modelo de lenguaje utilizado
        messages=[{"role": "user", "content": userquery}], # Consulta del usuario
        temperature=1,  # Parámetro de creatividad del modelo
        max_tokens=50,  # Máximo número de tokens en la respuesta
        top_p=1,  # Parámetro de generación de texto
        frequency_penalty=0,  # Penalización por repetición de palabras
        presence_penalty=0,  # Penalización por falta de coherencia
    )
    return response.choices[0].message.content # Retorna la respuesta de chatGPT

def main():
    historial = [] # Almacena consultas
    buffer = [] # Almacena consultas y respuestas

    if "--convers" in sys.argv: # Verifica si se quiere acceder al modo de conversación
        print("--Modo de conversación activado--")

    while True:
        try:
            userquery = obtener_consulta()
            historial.append(userquery)
            respuesta = realizar_consulta(userquery)
            buffer.append(userquery)
            buffer.append(respuesta)
            
            # Imprime la conversación entre el usuario y chatGPT
            print("You:", userquery)
            print("chatGPT:", respuesta)
            
        except ValueError as ve: # Manejo de excepción para consultas inválidas
            print(f"Error: {ve}")
            
        except Exception as e: # Manejo de excepción para otros errores
            print(f"Error inesperado: {e}") 

if __name__ == "__main__":
    main() # Este bloque se ejecuta cuando el archivo se ejecuta como programa principal