import os
import psycopg2
from psycopg2 import sql
from contract import Vendas
from dotenv import load_dotenv

import streamlit as st

load_dotenv('.env')

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        cursor = conn.cursor()

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
            )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.qtd_produto,
            dados.produto
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados inseridos com sucesso!")

    except Exception as e:
        st.error(f"Erro: {e}")
