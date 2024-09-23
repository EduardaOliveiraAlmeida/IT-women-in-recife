import geopandas as gpd
import matplotlib.pyplot as plt

# Carregar o GeoDataFrame com os dados
bairros = gpd.read_file("dados/bairros_com_dados.shp")

# Exibir o mapa com a quantidade de mulheres
bairros.plot(column='quantidade_mulheres', cmap='OrRd', legend=True)
plt.title('Distribuição de Mulheres na Tecnologia por Bairro')
plt.show()
