-- Semana 02 - KPIs e Agregações com PostgreSQL

-- 1. Preço médio dos imóveis por bairro
SELECT bairro, ROUND(AVG(preco), 2) AS preco_medio
FROM imoveis
GROUP BY bairro
ORDER BY preco_medio DESC;

-- 2. Área média dos imóveis por zona
SELECT zona, ROUND(AVG(area_m2), 1) AS area_media
FROM imoveis
GROUP BY zona
ORDER BY area_media DESC;

-- 3. Top 5 bairros com maior preço médio por m²
SELECT bairro, ROUND(AVG(preco_m2), 2) AS media_preco_m2
FROM imoveis
GROUP BY bairro
ORDER BY media_preco_m2 DESC
LIMIT 5;

-- 4. Quantidade de imóveis por zona
SELECT zona, COUNT(*) AS total_imoveis
FROM imoveis
GROUP BY zona
ORDER BY total_imoveis DESC;

-- 5. Valor total de imóveis listados por bairro
SELECT bairro, SUM(preco) AS soma_total
FROM imoveis
GROUP BY bairro
ORDER BY soma_total DESC;

-- 6. Bairros com mais de 3 imóveis listados
SELECT bairro, COUNT(*) AS total
FROM imoveis
GROUP BY bairro
HAVING COUNT(*) > 3
ORDER BY total DESC;

-- 7. Bairros com preço médio por m² acima de R$ 7.000
SELECT bairro, ROUND(AVG(preco_m2), 2) AS preco_medio_m2
FROM imoveis
GROUP BY bairro
HAVING AVG(preco_m2) > 7000
ORDER BY preco_medio_m2 DESC;

-- 8. Zonas com menor preço médio
SELECT zona, ROUND(AVG(preco), 2) AS preco_medio
FROM imoveis
GROUP BY zona
ORDER BY preco_medio ASC;