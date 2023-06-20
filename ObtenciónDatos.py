import requests
import datetime
import pandas as pd
import ta


def obtener_precios_criptomonedas():
    criptomonedas = ["bitcoin", "ethereum", "binancecoin", "ripple", "cardano", "solana", "dogecoin", "polkadot",
                     "uniswap", "litecoin"]
    fecha_actual = datetime.datetime.now()
    fecha_hace_30_dias = fecha_actual - datetime.timedelta(days=30)
    precios_por_hora = {}

    for criptomoneda in criptomonedas:
        url = f"https://api.coingecko.com/api/v3/coins/{criptomoneda}/market_chart/range?vs_currency=usd&from={int(fecha_hace_30_dias.timestamp())}&to={int(fecha_actual.timestamp())}&interval=1h"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            precios = data.get("prices")

            if precios:
                precios_por_hora[criptomoneda] = precios
            else:
                print(f"No se encontraron datos para {criptomoneda}")
        #else:
            #print(f"Error al obtener los precios de {criptomoneda}")

    return precios_por_hora


def calcular_rsi(precios):
    cierres = pd.Series([precio[1] for precio in precios])
    rsi = ta.momentum.RSIIndicator(cierres).rsi()
    return rsi


precios = obtener_precios_criptomonedas()
df_rsi = pd.DataFrame()
df_precio = pd.DataFrame()

for criptomoneda, precios_por_hora in precios.items():
    if len(precios_por_hora) > 0:
        rsi = calcular_rsi(precios_por_hora)
        df_rsi[criptomoneda] = rsi
        df_precio[criptomoneda] = [precio[1] for precio in precios_por_hora]
    else:
        print(f"No se encontraron datos para {criptomoneda}")

fechas = pd.date_range(end=datetime.datetime.now() - datetime.timedelta(days=30), periods=len(df_rsi), freq="H")
df_rsi.index = fechas

# Crear una columna de fechas con los índices para df_precios
fechas_precios = pd.date_range(end=datetime.datetime.now(), periods=len(df_precio), freq="H")
df_precio.index = fechas_precios

#print(df_rsi)
#print(df_precio)

