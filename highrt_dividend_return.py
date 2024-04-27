import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

tickers = ['PETR3.SA', 'VALE3.SA', 'BBDC3.SA', 'BBAS3.SA']

data_atual = datetime.now().date()

data_limite = (data_atual - timedelta(days=5*365))

total_dividendos_por_empresa = {}

for ticker in tickers:
    try:
        data = yf.Ticker(ticker)
        dividendos = data.dividends

        dividendos_ultimos_cinco_anos = [dividendo for dividendo in dividendos.items(
        ) if data_limite <= dividendo[0].date() <= data_atual]

        total_dividendos = sum(dividendo[1] for dividendo in dividendos_ultimos_cinco_anos)

        total_dividendos_por_empresa[ticker] = total_dividendos

        dividendos_por_ano = {}

        for data, valor in dividendos_ultimos_cinco_anos:
            ano = data.year
            if ano not in dividendos_por_ano:
                dividendos_por_ano[ano] = []
            dividendos_por_ano[ano].append(valor)

        anos = list(dividendos_por_ano.keys())
        valores = [sum(dividendos_por_ano[ano]) for ano in anos]

        plt.figure()
        plt.bar(anos, valores, color='gray')
        plt.title(f"Dividendos pagos por ano - {ticker}")
        plt.xlabel("Ano")
        plt.ylabel("Valor total do dividendo")

        for i, valor in enumerate(valores):
            plt.text(anos[i], valor, f"{valor:.2f}", ha='center', va='bottom')

        plt.tight_layout()

        plt.show()
    except:
        pass

empresa_maior_retorno = max(total_dividendos_por_empresa, key=total_dividendos_por_empresa.get)

plt.figure()
plt.bar(total_dividendos_por_empresa.keys(), total_dividendos_por_empresa.values(), color='gray')
plt.title("Total de dividendos pagos nos últimos 5 anos")
plt.xlabel("Ticker")
plt.ylabel("Valor total do dividendo")
plt.xticks(rotation=45)
plt.tight_layout()

plt.text(empresa_maior_retorno, total_dividendos_por_empresa[empresa_maior_retorno],
         f"Maior retorno: {total_dividendos_por_empresa[empresa_maior_retorno]:.2f}",
         ha='center', va='bottom')

plt.show()