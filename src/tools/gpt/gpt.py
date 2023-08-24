import json
import openai

# Abre el archivo JSON en modo de lectura
with open('../../../config.json', 'r') as file:
    config = json.load(file)
    api_key = config['openai']['api_key']

openai.api_key = api_key

# # Crear una instancia del objeto Usage
# usage = openai.Usage()

# # Obtener información de uso actualizada
# usage.retrieve()

# # Imprimir información de uso
# print(usage.data)
# print("Tokens utilizados: ", usage.data["data"]["attributes"]["api_usage"]["tokens_used"])
# print("Tokens restantes: ", usage.data["data"]["attributes"]["api_usage"]["tokens_remaining"])
# print("Límite de tokens: ", usage.data["data"]["attributes"]["api_usage"]["token_quota"])


# Llama a la API de OpenAI para obtener información de la cuenta
response = openai.Completion.create(engine="text-davinci-003", prompt="cuantos tokens disponibles?", max_tokens=100)

# Imprime la cantidad de tokens disponibles
print(response)
print("\n")
print("Tokens disponibles:", response['data'])

input()