# Projeto AWS – Data Guy

## Visão Geral
Este projeto demonstra uma arquitetura moderna de engenharia de dados utilizando AWS, com foco em pipelines escaláveis, governados e orientados ao consumo analítico.

## Arquitetura
- Airflow para orquestração
- Amazon S3 como Data Lake (Medallion)
- Amazon Redshift para consumo analítico
- Power BI como camada de visualização

## Arquitetura Medallion
- **Bronze**: dados brutos
- **Silver**: dados limpos e tipados
- **Gold**: dados agregados e prontos para BI

## Orquestração
O Airflow é utilizado exclusivamente para orquestração, garantindo:
- Reprocessamento
- Retry
- Observabilidade

## Estratégia de Custo
- Cargas incrementais
- Agregações antecipadas
- Redução de volume lido no Redshift

## Consumo BI
O modelo foi desenhado priorizando:
- Baixa cardinalidade
- Modelo estrela
- Performance no consumo

## Trade-offs
Decisões técnicas foram tomadas considerando custo, prazo e maturidade do projeto.
