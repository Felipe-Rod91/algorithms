# Cria um dicionário vazio para armazenar os dados das páginas
cache = {}

# Verifica se a URL solicitada já está no cache
def get_page(url):
    if cache.get(url): # Se estiver, retorna os dados armazenados no cache para esta URL
        return cache(url)
    else: # Se não estiver, pega os dados, armazena no cache e depois os retornam
        data = get_data_from_server(url)
        cache[url] = data
        return data
