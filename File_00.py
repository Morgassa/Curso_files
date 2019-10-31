import pandas as pd
url="http://www.anp.gov.br/arquivos/dadosabertos/distribuidores/planilha-empresas-cadastradas-agente-inutilizador.csv"
c=pd.read_csv(url)

print(c)