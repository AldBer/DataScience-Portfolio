-- Semana 01 - Queries básicas com base nos dados de imóveis de São Paulo

-- 1. Ver os 10 primeiros registros da tabela
SELECT * FROM imoveis
LIMIT 10;

-- 2. Imóveis localizados no bairro 'Perdizes'
SELECT * FROM imoveis
WHERE bairro = 'Perdizes';

-- 3. Top 5 imóveis com maior preço por metro quadrado
SELECT * FROM imoveis
ORDER BY preco_m2 DESC
LIMIT 5;

-- 4. Imóveis com mais de 3 quartos e área superior a 100 m²
SELECT * FROM imoveis
WHERE quartos > 3 AND area_m2 > 100;

-- 5. Imóveis da zona Sul com preço inferior a R$ 600.000
SELECT * FROM imoveis
WHERE zona = 'Sul' AND preco < 600000;

-- 6. Imóveis com preço entre R$ 500.000 e R$ 800.000
SELECT * FROM imoveis
WHERE preco BETWEEN 500000 AND 800000;

-- 7. Listar bairros únicos presentes na base de dados
SELECT DISTINCT bairro FROM imoveis
ORDER BY bairro;

-- 8. Quantidade total de imóveis registrados
SELECT COUNT(*) FROM imoveis;

-- 9. Verificar colunas específicas (bairro, área e preço)
SELECT bairro, area_m2, preco FROM imoveis
LIMIT 10;