import openai


# Se rellena con la API key
openai.api_key = "api_key" 

try:
    
    historial = []
    
    while True:
    
        userquery = input("Ingrese su consulta: ")
        
        if userquery.strip(): # Se agrega la consulta al historial
            historial.append(userquery)
            
        elif historial: # Si el historial no esta vacio, se puede acceder a la ultima consulta
            userquery = historial[-1]
            
        else:
            raise ValueError("Por favor, ingrese una consulta válida.")  
        
        
        # Se realiza la consulta a través de la API de ChatGPT
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
        {
        # Consulta del usuario
        "role": "user",
        "content": userquery }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        # Se muestra la conversacion entre usuario y chatGPT
        print("You:", userquery)
        print("chatGPT:", response.choices[0].message.content)
    
except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Error inesperado: {e}")