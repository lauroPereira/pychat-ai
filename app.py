from datetime import datetime
from pydantic import ValidationError
import streamlit as st

from contract import Vendas
from database import salvar_no_postgres

def main():

    st.title("Sistema CRM")

    email = st.text_input("Email do Vendedor", "teste@domain.com")
    data = st.date_input("Data da Compra")
    hora = st.time_input("Hora da Compra")
    valor = st.number_input("Valor da Venda")
    qtd_produto = st.number_input("Quantidade de produtos")
    produto = st.selectbox("Produto", ["Produto A", "Produto B", "Produto C"])
    

    if st.button("Salvar"):
        try:
            data_hora=datetime.combine(data, hora)
            venda =Vendas(
                data=data_hora,
                email=email,
                valor=valor,
                qtd_produto=qtd_produto,
                produto=produto
            )

            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")


if __name__ == "__main__":
    main()
