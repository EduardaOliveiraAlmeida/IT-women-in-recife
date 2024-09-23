import os

# Caminho local do arquivo CSV
caminho_arquivo_local = 'dados/cidades.csv'

# Caminho no HDFS onde os dados serão carregados
caminho_hdfs = '/user/duda/dados/mulheres_tecnologia/'

# Comando para copiar o arquivo do sistema de arquivos local para o HDFS
comando = f'hadoop fs -put {caminho_arquivo_local} {caminho_hdfs}'

# Executar o comando
os.system(comando)

print(f'Arquivo {caminho_arquivo_local} carregado com sucesso no HDFS em {caminho_hdfs}')