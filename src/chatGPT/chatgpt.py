import openai


# Se rellena con la API key
openai.api_key = "api_key" 

userquery = input("Ingrese su consulta: ")

if not userquery.strip():
    print("Por favor, ingrese una consulta válida.")
else:   
    
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