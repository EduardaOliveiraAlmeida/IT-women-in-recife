from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Mulheres na Tecnologia").config("spark.rpc.message.maxSize", 2047).getOrCreate()

# Ler o arquivo CSV diretamente do HDFS
df = spark.read.csv("hdfs://localhost:9870/user/duda/dados/mulheres_tecnologia/cloudgirls.csv", header=True,
                    inferSchema=True)

# Exibir os primeiros registros
df.show()

# Exemplo de análise: Contagem de registros por bairro
df.groupBy("cidades").count().show()

# Exemplo de salvar os resultados no HDFS
df.groupBy("cidades").count().write.csv('hdfs://localhost:9870/user/duda/resultados/contagem_bairros_cloudgirls.csv')

# Encerrar a sessão Spark
spark.stop()