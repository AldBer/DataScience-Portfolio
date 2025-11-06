-- Semana 03 – Filtros Avançados e Subqueries

-- 1. Operadores lógicos avançados
SELECT *
FROM imoveis
WHERE preco_m2 > 8000 AND quartos >= 3;
-- 2. BETWEEN para faixas de valores
SELECT *
FROM imoveis
WHERE preco BETWEEN 500000 AND 1000000;
-- 3. IN para múltiplas comparações
SELECT *
FROM imoveis
WHERE bairro IN ('Jardins', 'Itaim Bibi', 'Moema')
ORDER BY bairro ASC;
-- 4. LIKE para padrões de texto
SELECT *
FROM imoveis
WHERE bairro LIKE 'P%';
-- 5. Subquery simples no WHERE
SELECT *
FROM imoveis
WHERE preco > (SELECT AVG(preco) FROM imoveis)
ORDER BY area_m2 ASC;
-- 6. Subquery no SELECT
SELECT bairro, preco,
(SELECT AVG(preco) FROM imoveis) AS media_geral
FROM imoveis;
-- 7. Subquery correlacionada
SELECT bairro, preco
FROM imoveis i
WHERE preco = (
SELECT MAX(preco)
FROM imoveis
WHERE bairro = i.bairro
);
-- 9. Ordenação múltipla
SELECT *
FROM imoveis
ORDER BY zona ASC, preco DESC;
-- 10. Contagem de bairros com subquery
SELECT COUNT(DISTINCT bairro) AS total_bairros
FROM imoveis;