import requests
import pandas as pd

def main():
    # 1. Definimos la URL de la API
    url = "https://jsonplaceholder.typicode.com/users"
    
    # 2. Hacemos la petición GET
    response = requests.get(url)
    
    # 3. Verificamos el status
    if response.status_code == 200:
        data = response.json()  # Esto es una lista de dicts
        
        # 4. Convertimos a DataFrame
        df = pd.DataFrame(data)
        
        # 5. Imprimimos un preview para verificar
        print("Data obtenida de la API:\n", df.head(), "\n")
        
        # 6. (Opcional) Seleccionamos solo columnas relevantes (ejemplo)
        df = df[["id", "name", "username", "email", "phone"]]
        
        # 7. Guardamos en un CSV
        df.to_csv("users_data.csv", index=False)
        print("CSV 'users_data.csv' generado con éxito.")
    else:
        print(f"Error en la petición. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()
