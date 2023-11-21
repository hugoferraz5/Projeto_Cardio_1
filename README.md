# Projeto_cardio

# 1 Contexto
Neste projeto temos uma Empresa fictícia que detecta pacientes com Doenças Cardiovasculares através dos dados.

<div align="center">
<img src="https://user-images.githubusercontent.com/91911052/169045300-9dfc0381-d940-4221-8e2a-e294e50b0523.jpg" width="700px" />
</div>

## 1.1 O que é Doença Cardiovascular
* Doenças Cardiovasculares são a principal causa de mortes no mundo. De acordo com dados da Organização Mundial da Saúde, essas enfermidades matam cerca de 17,7 milhões pessoas todos os anos. Somente no Brasil, são contabilizados mais 300 mil óbitos anualmente.
* Os dados mostram ainda que mais de 75% das mortes provocadas por doenças cardiovasculares são registradas em países de baixa e média renda, sendo que 80% dos óbitos são causados especificamente por ataques cardíacos e derrames.
* De acordo com a entidade, grande parte dessas vítimas tinha comportamentos considerados não-saudáveis, como o tabagismo, o consumo de alimentos com excesso de sal e a prática de atividade física não-adequada.

1. Pressão alta
2. Insuficiência cardíaca
3. Ataque cardíaco
4. Miocardite
5. Arritmia cardíaca


# 2 Apresentação
A ProjetoCardio é uma empresa fictícia responsável pela detecção precoce de pacientes com Doença Cardiovascular nas suas fases iniciais por um determinado preço.

Atualmente, na empresa existem médicos especializados no assunto, mas devido à carga horária elevada deles que se revezam para diminuir os riscos e uma acuracidade entre 55% e 65% na detecção das doenças devido à complexidade do diagnóstico, se tornou necessário a detecção dessa doença através dos dados. Nela, é cobrado uma valor de R$500,00 a partir de 50% de acuracidade e a cada 5% é acrescido R$500,00 no valor.Abaixo de 50% não é cobrado valor. 

Logo, percebemos que a empresa possui um determinado lucro ou prejuízo, a depender da acuracidade da detecção por causa dos custos com todo o processo, pagamento de funcionários, entre outros.Os dados podem ser encontrados em: <a href="https://www.kaggle.com/sulianova/cardiovascular-disease-dataset">Kaggle</a>

O projeto completo pode ser encontrado neste link:
<a href="https://github.com/hugoferraz5/Projeto_Cardio_1/blob/main/Projeto%20Cardio.ipynb">Projeto_Cardio_1</a>

Foi criado uma API local e ela pode ser acessada aqui:
<a href="https://github.com/hugoferraz5/Projeto_Cardio_1/blob/main/test_api_handler.py">APIlocal</a>

Passo a passo do projeto: 

|Atributo | Definição
------------ | -------------
|id | ID dos pacientes|
|age | Idade dos pacientes |
|gender | Gênero dos pacientes - 1: Mulher - 2: Homem|
|weight | Peso dos pacientes  |
|ap_hi | Pressão arterial sistólica de cada paciente |
|ap_lo | Pressão sanguinea diastólica	|
|cholesterol | 1: Baixo Colesterol - 2: Medio Colesterol - 3:Alto Colesterol|
|gluc | 1: Glicose Normal - 2: Glicose Acima do Normal - 3: Glicose Bem Acima do Normal|
|smoke | 0: Não Fuma - 1: Fuma |
|alco | 0: Não Bebe - 1: Bebe |
|active | 0: Não Pratica Atividade Física - 1: Pratica Atividade Física |
|cardio | 0: Não Possui Doença Cardiovascular - 1: Possui Doença Cardiovascular |

# 3 Premissas de negócio
* A tabela de risco cardiovascular foi essencial para análise de detecção
* O IMC(Índice de Massa Corpórea) também foi essencial na construção do modelo
* Os gráficos ajudaram a ter mais clareza nas análises
* A idade foi deixada em quantidade de dias para não perder informações
* O histórico de cada paciente ajudou nas conclusões

# 4 Passo a passo da solução

* **Questão de Negócios** - Fazer a predição de futuros pacientes da empresa e descobrir de forma rápida se possui Doença Cardiovascular ou não, com o objetivo de aumentar seu lucro.
* **Entendimento do negócio** - Entender o histórico dos pacientes através da sua idade, sua altura, peso, se pratica esporte com frequência, taxas de colesterol e glicose, se fuma, bebe e suas pressões diastólicas e sistólicas. A partir desses dados, fazer as análises.
* **Coleta de Dados** - Coletar os dados do site Kaggle
* **Limpeza dos Dados** - Fazer a limpeza dos dados se existirem valores discrepantes e valores vazios através da linguagem Python. 
* **Exploração dos Dados** - Explorar os dados através de respostas à perguntas do CEO da empresa, achar bons insights pelas hipóteses levantadas e apresenta-los por meio de gráficos.
* **Modelagem dos Dados** - Fazer boas modelagens(correlações, reescalonamento, codificações, frequência dos dados) afim de facilitar as leituras dos modelos de Machine Learning. Achar os melhores recursos para os algoritmos.
* **Algoritmo de Machine Learning** - Com os dados modelados, vamos usar alguns algoritmos de Machine Learning de classificação para achar a melhor acurácia. Uso de Validação Cruzada e hiperparâmetros para melhorar ainda mais os modelos e colocar em prática no final.
* **Avaliação de Algoritmo** - Comparação dos resultados dos algoritmos de classificação usados e utilizar o de melhor acurácia para colocar em prática a questão de negócios.
* **Deploy** - Através do cloud da AWS, implantamos o nosso modelo de Machine Learning e esse modelo responderá requisições via API, de início, apenas localmente.
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/acd63cbe-28d1-4f67-a35f-e0067e25bea7.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 5 Análises exploratórias dos dados
**Variável de Destino**
<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/25e94cff-7ba7-4ffd-8910-ded6da9a8248.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

**Variável Numérica**
<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/9b106e0a-2108-4880-93d8-79dbf6a1ee0b.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>
**Variável Categórica**
<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/e9392d4e-a764-48e8-a955-a53bae4cd91f.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## Insights de negócio

* **H1**. Em cada classe de idade a maioria das pessoas não tem doença cardiovascular

**Falso**: As pessoas com faixa etária acima de 56 anos começam a ser maioria com doença cardiovascular como observado nos 2 gráficos abaixo..

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/0358cbe1-1edd-4f48-bbf1-706c45b2973a.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/84f91db3-8b69-4f23-b202-ad3d57389cec.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H2**. Pessoas que fumam tem mais chances de ter Doença Cardiovascular

**Falso**: Tanto pessoas que fumam, quanto pessoas que não fumam, tem chances de terem Doença Cardiovascular.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/4490ae6d-0482-421a-bed6-16203adcf86a.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H3**. Mulheres tem mais chances de ter Doença Cardiovascular

**Falso**: De acordo com o gráfico, mulheres tem menos chance de ter Doença Cardiovascular que os homens.Ambos merecem atenção.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/542b2fdd-006b-4cc9-9b76-e09432f2afc8.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H4**. Pessoas mais pesadas tem mais chances de ter Doença Cardiovascular

**Verdadeiro**:Pessoas com Doença Cardiovascular possuem, em sua maioria, peso entre 65kg e 85kg, diferente dos que não tem, no qual possuem entre 62kg e 79kg.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/7295f068-45c0-41e6-a073-16d74bc980a1.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H5**. Pessoas que não fazem atividade física tem muito mais chances de ter Doença Cardiovascular

**Falso**: De acordo com o gráfico, pessoas que não fazem atividade física tem mais chances de ter Doença Cardiovascular, mas não numa diferença grande.De qualquer forma, incentivar a prática.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/46218c99-77d6-4159-a99e-d514f9243459.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H6**. Pessoas que fumam e bebem simultaneamente tem mais chances de ter doença cardiovascular 

**Falso**: Pessoas que fumam e bebem simultaneamente tem menos quantidade populacional diagnosticada com Doença Cardiovascular.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/d6e2a68d-7ba6-4a1b-a3bc-d4e4402c3ee4.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 6 Machine Learning

Usamos vários modelos de Machine Learning de classificação com o objetivo de obter a melhor acurácia e a menor quantidade de Falsos negativos. Pelo lado dos pacientes é importante a menor quantidade posível dos **falsos negativos**(revocação) e pelo lado da empresa é importante observar os **falsos positivos**(precisão). O f1-score que é o equilíbrio entre revocação(recall) e precisão(precision) não foi o maior no modelo **LGBMClassifier**, mas pesou o fato das outras acurácias serem maiores.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/487c27d8-eddf-443a-94fa-bb46d341af3b.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

Se observarmos na matriz da confusão, o modelo **LGBMClassifier** é um dos que tem menos falsos positivos e falsos negativos que é bastante importante e o modelo **SGDClassifier** possui uma precisão(precision) bem baixa, então se torna mais um motivo desse modelo ser o escolhido.

<img src="https://github.com/hugoferraz5/Projeto_Cardio_1/assets/91911052/202ed730-d2d6-43dd-accf-92eb0a75c244.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.1 Resultados para o negócio

Após todo esse processo, podemos ter um resultado se a empresa vai ter lucro ou não. Atualmente, ela possui uma acurácia máxima de 65% nos seus diagnósticos médicos. A cada 5% adicional, acima de 50%, é cobrado R$500,00 a mais dos clientes.



|Acurácia de Diagnóstico | Preço       | Regra              | Exemplo                      |
:------------------------ | :----------- | :------------------ | :-----------------------------|
| 50% para baixo         | R\$0\,00       | Nenhum             | Acurácia = 45% \-> R\$0.00      |
| Acima de 50%           | R\$500\,00 mínimo | +R\$500\.00 a cada 5% | Acurácia = 60% \-> R\$1.500 |




Nosso modelo conseguiu atingir uma acurácia entre **72,15%** e **75,67%** com a base de dados dos 70000 clientes da empresa. Então, na melhor das hipóteses, se pelo método normal todos que possuem ou não DCV conseguissem uma acurácia médica de 65%, a empresa faturaria **R\$105 milhões** e pela nossa precisão atingida, na melhor das hipóteses(75,67%) a empresa faturaria **R\$179\.69 milhões**, uma diferença de **R\$74\.69 milhões**(lucro bastante positivo) e na pior das hipóteses(72,15%) a empresa faturaria **R\$155\.05 milhões**, uma diferença de **R\$50\.05 milhões**(lucro bastante positivo também).

|                         | Melhor cenário     | Pior cenário        | 
:------------------------ | :------------------| :------------------ | 
| Atualmente              | R\$105.000.000\,00 | R\$35.000.000\,00   | 
| Após nosso modelo       | R\$179.690.000\,00 | R\$155.005.000\,00  | 
| Diferença               | R\$74.690.000\,00 | R\$50.005.000\,00    | 


## 6.2 Desempenho de Machine Learning

O modelo usado foi o **SGDClassifier** e os resultados obtidos foram esses abaixo.

|Modelo         | Precisão             | Revocação           |f1-score              | ROC AUC            |  
:-------------- | :--------------------| :------------------ | :--------------------| :------------------| 
|LGBMClassifier | 0.7391 (+/- 0.0176)| 0.6833 (+/- 0.0168) | 0.7101 (+/- 0.0137)  |0.7887 (+/- 0.0136) |             

# 7 Próximos passos
* Um aplicativo ou programa para informar de imediato ao paciente sua probabilidade de ter ou não à doença.
* Em caso de possível sobrecarga no uso do aplicativo, disponibilizar na entrada da empresa máquinas para o cliente apenas colocar seus dados e saber na hora. 
* Importante obter mais informações dos clientes para colocar na base de dados.
* Usar outras ferramentas para uso da API globalmente.

# 8 Ferramentas utilizadas

Manipulação e limpeza dos dados: pandas, numpy

VIsualização dos dados: matplotlib, seaborn

Machine learning: Classificação (scikit-learn e LGBMClassifier), selação de features (Extra Tree Classifier e Boruta)

Ambiente Cloud: Flask, requests, Ngrok, desenho de API e AWS
