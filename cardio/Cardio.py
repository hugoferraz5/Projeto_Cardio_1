import pickle
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing   import RobustScaler, MinMaxScaler, LabelEncoder

class Cardio(object):
    def __init__(self):
        self.MinMax_scaler = pickle.load(
            open("model/numerical_scaler.pkl", "rb")
        )
        

    def data_cleaning(self, df1):
        ##2.4 Formatação dos dados

        df1.columns = ['id', 'idade', 'genero', 'altura', 'peso', 'pressao_arterial_sistolica'
                       , 'pressao_sanguinea_diastolica','colesterol', 'glicose', 'fuma', 'alcool', 
                       'atividade_fisica', 'presenca_ou_ausencia_de_doença_cardiovascular']

        df1['altura'] = round(df1['altura']/100,2)
        
        
        # dtypes
        df1['genero'] = df1['genero'].astype( str )

        a = pd.CategoricalDtype(categories=[1, 2, 3], ordered=True)
        df1['colesterol'] = df1['colesterol'].astype( a )

        b = pd.CategoricalDtype(categories=[1, 2, 3], ordered=True)
        df1['glicose'] = df1['glicose'].astype( b )

        df1['fuma'] = df1['fuma'].astype( str )

        df1['alcool'] = df1['alcool'].astype( str )

        df1['atividade_fisica'] = df1['atividade_fisica'].astype( str )

        df1['presenca_ou_ausencia_de_doença_cardiovascular'] = df1['presenca_ou_ausencia_de_doença_cardiovascular'].astype( str )

        
        return df1
    
    
    def data_mean(self, x):
        if x['altura'] < 1:
            mean = x['altura'].loc[(x['altura'] >= 1) & (x['altura'] <= 2.1)].mean()
            return round(mean,2)
        elif x['altura'] > 2.1:
            mean = x['altura'].loc[(x['altura'] >= 1) & (x['altura'] <= 2.1)].mean()
            return round(mean,2)
        else:
            return x['altura']

    def feature_engineering(self, df2):
        
        # Removendo outlierss
        df2['altura'] = df2.apply(self.data_mean, axis=1)

        data_remove = df2.loc[(df2['peso'] < 40) | (df2['peso'] > 150)] 
        df2 = df2.drop(data_remove.index)

        data_remove1 = df2.loc[(df2['pressao_sanguinea_diastolica'] < 60) | (df2['pressao_sanguinea_diastolica'] > 150)]
        df2 = df2.drop(data_remove1.index)

        data_remove2 = df2.loc[(df2['pressao_arterial_sistolica'] < 90) | (df2['pressao_arterial_sistolica'] > 210)]
        df2 = df2.drop(data_remove2.index)
        
        df3 = df2.copy()
        
        # Tabela de pressões
        df3['tabela_pressoes'] = ''
        for idx, _ in df3.iterrows():
            if (df3['pressao_arterial_sistolica'].at[idx]<120) & (df3['pressao_sanguinea_diastolica'].at[idx]<80):
                df3['tabela_pressoes'].at[idx]='Normal'
            elif (df3['pressao_arterial_sistolica'].at[idx]<140) | (df3['pressao_sanguinea_diastolica'].at[idx]<90):
                df3['tabela_pressoes'].at[idx]='PreHipertensão'
            elif (df3['pressao_arterial_sistolica'].at[idx]<160) | (df3['pressao_sanguinea_diastolica'].at[idx]<100):
                df3['tabela_pressoes'].at[idx]='Hipertensão1'
            elif (df3['pressao_arterial_sistolica'].at[idx]<=180) |(df3['pressao_sanguinea_diastolica'].at[idx]<=110):
                df3['tabela_pressoes'].at[idx]='Hipertensão2'
            else:
                df3['tabela_pressoes'].at[idx]='CriseHipertensiva'

        #Valores do IMC(Índice Massa Corpórea)
        Altura_quadrado = (df3['altura']*df3['altura'])
        df3['IMC'] = np.divide(df3['peso'], Altura_quadrado)

        # Categorias do IMC
        df3['tabela_IMC'] = ''
        for idx, _ in df3.iterrows():
            if (df3['IMC'].at[idx]<18.5):
                df3['tabela_IMC'].at[idx]='Abaixo do Peso'
            elif (df3['IMC'].at[idx]>=18.5) & (df3['IMC'].at[idx]<=24.9):
                df3['tabela_IMC'].at[idx]='Normal'
            elif (df3['IMC'].at[idx]>25) & (df3['IMC'].at[idx]<=29.9):
                df3['tabela_IMC'].at[idx]='Sobrepeso'
            else:
                df3['tabela_IMC'].at[idx]='Obesidade'

        
        # Valor padrão de IMC
        IMC_Normal = 21
        # Criando feature diferença de IMC
        df3['diferença_IMC'] = df3['IMC'] - IMC_Normal

    
        return df3

    

    def data_preparation(self, df5):
        df5 = df5.drop(['id'], axis=1)
        
        # Carregar o data set
        df6 = df5.copy()
        
        # Dividindo em treino e teste
        X = df6.drop(['presenca_ou_ausencia_de_doença_cardiovascular'], axis=1)
        y = df6[['presenca_ou_ausencia_de_doença_cardiovascular']]
        
        scale = X[['idade', 'altura', 'peso', 'pressao_arterial_sistolica', 'pressao_sanguinea_diastolica', 'IMC', 'diferença_IMC']]
        # Reescalando os dados numerical
        numerical = self.MinMax_scaler.transform(scale.values)
        numerical = pd.DataFrame(numerical, columns=scale.columns)
        
        # Selecionando a coluna Gênero
        Genero = X[['genero']]
        # Enumerando em ordem os índices
        Genero.reset_index(drop=True, inplace=True)
        # Dividindo em valores binários 
        Genero = pd.get_dummies(Genero, drop_first=True)
        
        # Selecionando as colunas binárias
        binary = X[['fuma','alcool','atividade_fisica']]
        # Enumerando em ordem os índices
        binary = binary.reset_index(drop=True)
        
        # Selecionando as colunas categorical
        categorical = X[['colesterol','glicose','tabela_IMC','tabela_pressoes']]
        # Enumerando em ordem os índices
        categorical.reset_index(drop=True, inplace=True)
        
        # Criado uma base de dados de frequência em relação ao total para Colesterol
        cont_colesterol = categorical['colesterol'].value_counts().to_dict()
        data1_colesterol = pd.DataFrame(cont_colesterol.items(), columns=['Valor','Contagem'])
        data1_colesterol['frequencia'] = data1_colesterol['Contagem'] / data1_colesterol['Contagem'].sum()

        # Criado uma base de dados de frequência em relação ao total para Glicose
        cont_glicose = categorical['glicose'].value_counts().to_dict()
        data1_glicose = pd.DataFrame(cont_glicose.items(), columns=['Valor','Contagem'])
        data1_glicose['frequencia'] = data1_glicose['Contagem'] / data1_glicose['Contagem'].sum()

        # Criado uma base de dados de frequência em relação ao total para TabelaIMC
        cont_tabelaIMC = categorical['tabela_IMC'].value_counts().to_dict()
        data1_tabelaIMC = pd.DataFrame(cont_tabelaIMC.items(), columns=['Valor','Contagem'])
        data1_tabelaIMC['frequencia'] = data1_tabelaIMC['Contagem'] / data1_tabelaIMC['Contagem'].sum()

        # Criado uma base de dados de frequência em relação ao total para TabelaPressões 
        cont_tabelapressões = categorical['tabela_pressoes'].value_counts().to_dict()
        data1_tabelapressões = pd.DataFrame(cont_tabelapressões.items(), columns=['Valor','Contagem'])
        data1_tabelapressões['frequencia'] = data1_tabelapressões['Contagem'] / data1_tabelapressões['Contagem'].sum()
        
        # Transformando a base de dados de frequência criada em dicionário
        freq_colesterol = data1_colesterol.set_index('Valor').to_dict()['frequencia']
        freq_glicose = data1_glicose.set_index('Valor').to_dict()['frequencia']
        freq_weight_status = data1_tabelaIMC.set_index('Valor').to_dict()['frequencia']
        freq_tabelapressões = data1_tabelapressões.set_index('Valor').to_dict()['frequencia']
        
        # Criando base de dados
        cat_codificado = pd.DataFrame()

        # Substituir os valores da base de dados real para as frequência obtidas
        cat_codificado['colesterol'] =  categorical['colesterol'].map(freq_colesterol)
        cat_codificado['glicose'] =  categorical['glicose'].map(freq_glicose)
        cat_codificado['tabela_IMC'] =  categorical['tabela_IMC'].map(freq_weight_status)
        cat_codificado['tabela_pressoes'] =  categorical['tabela_pressoes'].map(freq_tabelapressões)
        
        # Concatenando os dados de transformação de treino
        X = pd.concat([numerical, Genero, binary, cat_codificado], axis=1)
        
        
        X = X.astype(float)
        y = y.astype(float)
        
        df6 = X[['idade','peso','pressao_arterial_sistolica','pressao_sanguinea_diastolica',
                'IMC','diferença_IMC','tabela_pressoes']]
        
        return df6

    def get_prediction(self, model, original_data, test_data):
        
        predictions = model.predict_proba(test_data)[::,1]
        # join predictions into the original data
        original_data['predictions'] = predictions
        original_data.sort_values( 'predictions', ascending = False )
        
        return original_data
    