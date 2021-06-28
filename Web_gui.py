import streamlit as st
from streamlit.elements import selectbox

class_options = ['Stock','FII', 'ETF', 'REIT']
market_options = ['B3','US', 'EU']

def main():
    st.set_page_config(
        page_title="PyHMS Central",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Cadastro de Compra e Venda")

    Ticker = st.text_input('Ticker:')
    date = st.date_input('Purshase Date:')

    col1,col2,x = st.beta_columns(3)

    with col1:
        QTY = st.number_input('QTY:')
        active_class = st.selectbox('Select Class:',class_options)
    with col2:
        Un_price = st.number_input('UN Price:',help='Unitary Price Paid')
        market = st.selectbox('Select Market:',market_options)

    
    col3,col4,x,x,x,x,x,x= st.beta_columns(8)
    with col3:
        st.button('Cadastrar Compra')
    with col4:
        st.button('Cadastrar Venda')




    
    


    

    



if __name__ == "__main__":
    main() 