"""
Algoritmo de busca gulosa de Araranguá até Tubarão
"""


class Cidade:
    """
    Classe para representar uma cidade

    Atributos:
    - nome (str): nome da cidade;
    - distancia_total (float): distância da cidade até a cidade de destino (nesse caso, até Tubarão);
    - cidades_prox (Cidade): lista de todas as cidades adjacentes.
    """

    def __init__(self, nome: str, distancia_total: float):
        self.nome = nome
        self.distancia_total = distancia_total
        self.cidades_prox = []

    def add_cidade_prox(self, *cidades):
        for cidade in cidades:
            self.cidades_prox.append(cidade)


# Tabela das cidades
ararangua = Cidade("Araranguá", 77.4)  # Cidade inicial
sapiranga = Cidade("Sapiranga", 83.3)
maracaja = Cidade("Maracajá", 66.7)
forquilhinha = Cidade("Forquilhinha", 76.7)
nova_veneza = Cidade("Nova Veneza", 82.0)
criciuma = Cidade("Criciúma", 65.9)
sideropolis = Cidade("Siderópolis", 77.5)
treviso = Cidade("Treviso", 74.0)
urussanga = Cidade("Urussanga", 54.6)
treze_de_maio = Cidade("Treze de Maio", 27.5)
cocal_do_sul = Cidade("Cocal do Sul", 51.8)
icara = Cidade("Içara", 52.7)
morro_da_fumaca = Cidade("Morro da Fumaça", 40.9)
sangao = Cidade("Sangão", 26.8)
rincao = Cidade("Balnerário Rincão", 58.0)
esplanada = Cidade("Balnerário Esplanada", 45.0)
jaguaruna = Cidade("Jaguaruna", 21.2)
tubarao = Cidade("Tubarão", 0.0)  # Cidade de destino

# Adicionando as cidades adjacentes
ararangua.add_cidade_prox(sapiranga, rincao, maracaja)
sapiranga.add_cidade_prox(maracaja)
rincao.add_cidade_prox(icara, esplanada)
maracaja.add_cidade_prox(forquilhinha)
icara.add_cidade_prox(criciuma, morro_da_fumaca, rincao)
esplanada.add_cidade_prox(morro_da_fumaca, sangao)
forquilhinha.add_cidade_prox(nova_veneza, criciuma)
criciuma.add_cidade_prox(forquilhinha, icara, cocal_do_sul)
morro_da_fumaca.add_cidade_prox(icara, sangao, esplanada)
sangao.add_cidade_prox(jaguaruna, treze_de_maio, tubarao)
nova_veneza.add_cidade_prox(sideropolis)
cocal_do_sul.add_cidade_prox(urussanga, treze_de_maio)
jaguaruna.add_cidade_prox(tubarao)
treze_de_maio.add_cidade_prox(cocal_do_sul, sangao, tubarao)
sideropolis.add_cidade_prox(nova_veneza, treviso, urussanga)
urussanga.add_cidade_prox(treviso, sideropolis, cocal_do_sul, treze_de_maio)
tubarao.add_cidade_prox(jaguaruna, treze_de_maio, sangao)


# Busca gulosa recursiva
def busca_gulosa(cidade: Cidade):
    global menor_distancia

    for cidade in cidade.cidades_prox:
        if (menor_distancia > cidade.distancia_total):
            menor_distancia = cidade.distancia_total
            if cidade.distancia_total == 0.0:
                menor_distancia = 0.0
                print(f" > {cidade.nome} ({menor_distancia})")
                break
            else:
                print(f"{cidade.nome} ({menor_distancia}) > ")
                busca_gulosa(cidade)


# Busca gulosa de Araranguá até Tubarão
global menor_distancia
menor_distancia = ararangua.distancia_total
print(f"Araranguá ({ararangua.distancia_total}) >")
busca_gulosa(ararangua)
