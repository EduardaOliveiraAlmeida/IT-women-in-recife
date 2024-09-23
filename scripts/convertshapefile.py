import geopandas as gpd

# Carregar o shapefile
bairros = gpd.read_file("dados/cidades.shp")

bairros.to_csv("data/cidades.csv", index=False)