### Estudo de caso 2
#### Definição do problema
No desafio proposto neste estudo de caso, o cenário apresentado é o seguinte: Você  é  Analista  de  Dados  na  empresa 
PontoMaximo,  uma rede  de  varejo  que  vende produtos eletrônicos e eletrodomésticos com lojas espalhadas por diversas cidades do Brasil.
A empresa começou sua operação no Brasil em 2012 e atua nos quatro estados da região sudeste 
mais os estados do Paraná e Bahia.

A empresa está montando a estratégia de vendas para o próximo ano e precisa saber 
**qual  dos  fabricantes  dos  produtos  vendidos,  apresenta  melhor  desempenho  nas  vendas**.
O objetivo é descartar os fabricantes cujos produtos possuem poucas vendas e tentar negociar 
melhores condições com os principais fabricantes.

Em paralelo a isso, a empresa gostaria de ter diferentes visões das vendas realizadas nos 
últimos 4 anos (período de 2012 a 2015). Deve ser possível segmentar os relatórios de vendas 
por  diferentes  informações  e  por  diferentes  ângulos.  Estas  informações  irão  suportar  as 
estratégias da empresa para o próximo ano.

Sua fonte de dados é um arquivo Excel com dados coletados do sistema de vendas, CRM e ERP da empresa.
O conjunto de dados foi entregue pelo departamento de TI com as seguintes colunas: 

|                |Descrição                          
|----------------|-------------------------------
|ID-Produto      |Identificador único de cada produto    
|Produto         |Nome do produto    
|Categoria       |Categoria do produto
|Segmento        |Segmento do produto
|Fabricante      |Fabricante do produto
|Loja            |Loja onde foi efetuada a venda
|Cidade          |Cidade da loja onde foi efetuada a venda
|Estado          |Estado da loja onde foi efetuada a venda
|Vendedor        |Nome do vendedor
|ID-Vendedor     |ID-Vendedor
|DatVenda        |Data da venda
|ValorVenda      |Valor da venda

#### Solução

##### Modelagem star schema
![Star Schema]()
##### Por fabricante
![Fabricante]()
##### Dados usados e arquivo .pbix
[Dados]()

[Arquivo .pbix]()