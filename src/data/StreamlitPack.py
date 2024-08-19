import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

class StreamlitServer:
    
    def __init__(self, data) -> None:
        self.DF = self.convert_to_dataframe(data)
    
    @staticmethod
    def convert_to_dataframe(data):
        dfs = {}
        for key, value in data.items():
            dfs[key] = pd.DataFrame(value[1:], columns=value[0])
        return dfs

    def server(self):
        st.title('AlliedWare - Streamlit Server')

        total_counts = {}

        for key, df in self.DF.items():
            st.header(f'{key}')
            
            if df.empty:
                st.write('Nenhum dado disponível para exibição.')
                continue

            st.write(df)
            
            # Gráfico de barras
            st.subheader(f'Gráfico de {key}')
            fig, ax = plt.subplots()
            if 'Destination' in df.columns:
                df['Destination'].value_counts().plot(kind='bar', ax=ax)
                st.pyplot(fig)
            else:
                st.write('Coluna "Destination" não encontrada.')

            # Gráfico de distribuição
            st.subheader(f'Distribuição de {key}')
            if 'Destination' in df.columns:
                st.bar_chart(df['Destination'].value_counts())
            else:
                st.write('Coluna "Destination" não encontrada.')

            # Acumulando contagens para o gráfico de rosquinha
            total_counts[key] = len(df)

        # Gráfico de rosquinha
        st.subheader('Percentual de Dados Relacionados')
        if total_counts:
            fig, ax = plt.subplots()
            ax.pie(total_counts.values(), labels=total_counts.keys(), autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
            ax.axis('equal')  
            st.pyplot(fig)
        else:
            st.write('Nenhum dado disponível para o gráfico de rosquinha.')
