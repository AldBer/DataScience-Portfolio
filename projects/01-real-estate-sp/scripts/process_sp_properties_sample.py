import pandas as pd
import numpy as np
from faker import Faker

# Lista de distritos OFICIAIS de SP 
DISTRITOS_OFICIAIS = [
    'ÁGUA RASA','ALTO DE PINHEIROS','ANHANGUERA','ARICANDUVA','ARTUR ALVIM',
    'BARRA FUNDA','BELA VISTA','BELÉM','BOM RETIRO','BRÁS','BRASILÂNDIA','BUTANTÃ',
    'CACHOEIRINHA','CAMBUCI','CAMPO BELO','CAMPO GRANDE','CAMPO LIMPO','CANGAIBA',
    'CAPÃO REDONDO','CARRÃO','CASA VERDE','CIDADE ADEMAR','CIDADE DUTRA','CIDADE LIDER',
    'CIDADE TIRADENTES','CONSOLAÇÃO','CURSINO','ERMELINO MATARAZZO','FREGUESIA DO Ó',
    'GRAJAÚ','GUAIANASES','MOEMA','IGUATEMI','IPIRANGA','ITAIM BIBI','ITAIM  PAULISTA',
    'ITAQUERA','JABAQUARA','JAÇANÃ','JAGUARA','JAGUARÉ','JARAGUÁ','JARDIM ÂNGELA',
    'JARDIM HELENA','JARDIM PAULISTA','JARDIM SÃO LUÍS','JOSÉ BONIFÁCIO','LAPA',
    'LIBERDADE','LIMÃO','MANDAQUI','MARSILAC','MOOCA','MORUMBI','PARELHEIROS','PARI',
    'PARQUE DO CARMO','PEDREIRA','PENHA','PERDIZES','PERUS','PINHEIROS','PIRITUBA',
    'PONTE RASA','RAPOSO TAVARES','REPÚBLICA','RIO PEQUENO','SACOMÃ','SANTA CECÍLIA',
    'SANTANA','SANTO AMARO','SÃO LUCAS','SÃO MATEUS','SÃO MIGUEL','SÃO RAFAEL',
    'SAPOPEMBA','SAÚDE','SÉ','SOCORRO','TATUAPÉ','TREMEMBÉ','TUCURUVI','VILA ANDRADE',
    'VILA CURUÇÁ','VILA FORMOSA','VILA GUILHERME','VILA JACUÍ','VILA LEOPOLDINA',
    'VILA MARIA','VILA MARIANA','VILA MATILDE','VILA MEDEIROS','VILA PRUDENTE',
    'VILA SÔNIA','SÃO DOMINGOS','LAJEADO',
]

def criar_dataset_realista(n_imoveis=1000):
    fake = Faker('pt_BR')
    
    dados = []
    for _ in range(n_imoveis):
        distrito = np.random.choice(DISTRITOS_OFICIAIS)
        
        # Preços médios realistas por distrito
        precos_base = {
            'ITAIM BIBI': 15000, 'JARDIM PAULISTA': 12000, 'MOEMA': 10000,
            'VILA OLIMPIA': 9000, 'BROOKLIN PAULISTA': 8000, 'PINHEIROS': 7000,
            'VILA ANDRADE': 6000, 'LAPA': 5000, 'PERDIZES': 5500,
        
        }
        
        preco_base = precos_base.get(distrito, 3000)
        preco = np.random.normal(preco_base, preco_base * 0.3)
        
        dados.append({
            'bairro': distrito,  # Já usando distritos oficiais!
            'preco': max(100000, abs(preco)),
            'area_m2': np.random.randint(30, 300),
            'quartos': np.random.randint(1, 5),
            'banheiros': np.random.randint(1, 4),
            'vagas': np.random.randint(0, 3)
        })
    
    return pd.DataFrame(dados)

# Criar e salvar dataset
df_realista = criar_dataset_realista(2000)
df_realista.to_csv('sp_properties_realista.csv', index=False)