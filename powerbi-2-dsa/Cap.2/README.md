### Estudo de caso 1
#### Definição do problema
No desafio proposto neste estudo de caso, o cenário apresentado é o seguinte: Você é Analista de Dados na empresa XYZ Corporation International, uma revendedora de automóveis de luxo com sede em São Paulo. 
A empresa começou sua operação no Brasil em 2016 e atua nos quatro estados da região sudeste,
mais os estados do Paraná e Bahia.

Seu  gerente  vai  apresentar  os  resultados  da  equipe  comercial  para  o  novo  CEO  da 
empresa  e  precisa  da  sua  ajuda  para  construir  um  Dashboard  que  represente  os  dados  de 
vendas no período de 2016 a 2019.

Sua fonte de dados é um arquivo Excel com dados coletados do sistema de vendas e CRM da empresa,
com a as seguintes colunas:

|                |Descrição                          
|----------------|-------------------------------
|DataNotaFiscal  |Data de emissão da nota fiscal        
|Fabricante      |Fabricante do veículo       
|Estado          |Estado onde foi realizada a venda
|PrecoVenda      |Peço de venda do veículo
|PrecoCusto      |Preço de custo do veículo para a empresa
|TotalDesconto   |Total de Desconto fornecido sobre o preço de venda
|CustoEntrega    |Custo de entrega do veículo ao proprietário
|CustoMaoDeobra  |Custo de Mão de Obra (secretária, mecânico, etc...)
|NomeCliente     |Nome do cliente que comprou o veículo
|Modelo          |Modelo do veículo
|Cor             |Cor do veículo
|Ano             |Ano de fabricação do veículo

Seu gerente precisa das seguintes informações:

- Total de Vendas por Ano
- Custo de Entrega do Veículo Por Fabricante
- Custo de Mão de Obra Por Estado
- Total de Vendas Geral e Matriz de Vendas

Além  disso,  pode  ser  interessante, se  o  CEO  puder  visualizar  o 
total  de  vendas  por estado e se as vendas estão acima ou abaixo da média. 
Seu gerente já sabe que um assunto será abordado pelo CEO durante a apresentação. 
O CEO está avaliando se continua ou não com a venda de automóveis da marca Jaguar e ele gostaria de saber como
evoluíram as vendas de automóveis deste fabricante por ano e por estado.

#### Solução
##### Visão geral
![Visão Geral](https://raw.githubusercontent.com/suhribeiro/datascience_projects/master/powerbi-2-dsa/Cap.2/images/visao_geral.JPG)
##### Por fabricante
![Fabricante](https://raw.githubusercontent.com/suhribeiro/datascience_projects/master/powerbi-2-dsa/Cap.2/images/fabricante.JPG)
##### Dados usados e arquivo .pbix

[Dados](https://github.com/suhribeiro/datascience_projects/tree/master/powerbi-2-dsa/Cap.2/data)

[Arquivo .pbix](https://github.com/suhribeiro/datascience_projects/blob/master/powerbi-2-dsa/Cap.2/Estudo%20de%20Caso1.pbix)