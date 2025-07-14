
-- 1. Imóveis no bairro Perdizes
SELECT * FROM imoveis WHERE bairro = 'Perdizes';

-- 2. Top 5 por maior preço/m²
SELECT * FROM imoveis ORDER BY preco_m2 DESC LIMIT 5;

-- 3. Imóveis com mais de 3 quartos e área > 100m²
SELECT * FROM imoveis WHERE quartos > 3 AND area_m2 > 100;

-- 4. Zona Sul com preço abaixo de R$600.000
SELECT * FROM imoveis WHERE zona = 'Sul' AND preco < 600000;

-- 5. Preço entre R$500 mil e R$800 mil
SELECT * FROM imoveis WHERE preco BETWEEN 500000 AND 800000;

-- 6. Bairros únicos
SELECT DISTINCT bairro FROM imoveis;
