import pandas as pd
import streamlit as st # pip install streamlit
import matplotlib.pyplot as plt


class StreamlitServer():
    
    def __init__(self, data) -> None:
        self.DF = StreamlitServer.convert_to_dataframe(data)
    
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
            st.write(df)
            
            # Gráfico de barras
            st.subheader(f'Gráfico de {key}')
            fig, ax = plt.subplots()
            df['Destination'].value_counts().plot(kind='bar', ax=ax)
            st.pyplot(fig)

            # Gráfico de distribuição
            st.subheader(f'Distribuição de {key}')
            st.bar_chart(df['Destination'].value_counts())

            # Acumulando contagens para o gráfico de rosquinha
            total_counts[key] = len(df)

        # Gráfico de rosquinha
        st.subheader('Percentual de Dados Relacionados')
        fig, ax = plt.subplots()
        ax.pie(total_counts.values(), labels=total_counts.keys(), autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
        ax.axis('equal')  
        st.pyplot(fig)

