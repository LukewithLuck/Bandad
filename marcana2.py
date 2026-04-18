import streamlit as st
import random
import time
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Analista Pai-Banana", page_icon="🍌", layout="centered")

# 2. VISUAL (FRONT-END)
st.markdown("""
    <style>
    .stApp { background-color: #fcdb05; }
    .stButton>button {
        width: 100%; border-radius: 10px;
        background-color: #000000; color: #ffffff;
        height: 3em; font-weight: bold; border: none;
    }
    .stTextInput>div>div>input { border-radius: 10px; border: 2px solid #000000; }
    div[data-testid="stImage"] img { border-radius: 15px; border: 4px solid #000000; }
    h1, h2, h3, p, span, label { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. SISTEMA DE SENHA
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🍌 Área Restrita")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar"):
        if senha == "banana123":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Senha errada!")
    st.stop()

# 4. CONTEÚDO DO APP
st.title("🍌 Consultoria: Pai-Banana")

# --- PROTEÇÃO DA IMAGEM ---
NOME_IMAGEM = "foto.jpg"

if os.path.exists(NOME_IMAGEM):
    st.image(NOME_IMAGEM, use_column_width=True)
else:
    st.warning(f"⚠️ Atenção Lucca: O arquivo '{NOME_IMAGEM}' não foi encontrado no GitHub. Verifique o nome!")

st.write("---")
pergunta = st.text_input("O que você quer que eu analise?")
arquivo = st.file_uploader("Ou mande uma foto:", type=["jpg", "png", "jpeg"])

respostas_deizy = [
    "A Deizy olhou e disse: 'Isso aí é perda de tempo, compra uma coca pra mim'.",
    "Veredito da Deizy: 'Se você gastar dinheiro com isso, não vou fazer janta'.",
    "Deizy falou: 'Achei feio e caro, mas vou gastar meu salário com Coca-Cola'.",
    "A patroa mandou avisar: 'Isso é golpe, sai dessa agora!'.",
    "Deizy disse: 'Pode até ser bom, mas se fizer isso nunca mais conta comigo pra nada'.",
    "Ele perguntou pra Deizy e ela respondeu: 'Pergunta pro Lucca, ele que é o gênio da computação'.",
    "Deizy examinou e concluiu: 'É perda de tempo!'.",
    "A Deizy não respondeu porque tava vendo notícia no celular.",
    "A Deizy disse pra mim olhar, mas eu não vou olhar porque só quero YouTube."
]

if st.button("Consultar Especialista"):
    if pergunta or arquivo:
        with st.status("Analisando...", expanded=True) as status:
            time.sleep(5)
            st.write("Incomodando a Deizy...")
            time.sleep(2)
            status.update(label="Análise finalizada!", state="complete", expanded=False)
        
        st.info("👴: Ah, tô com preguiça... Vou falar pra Deizy fazer isso.")
        time.sleep(2)
        st.subheader("O que a Deizy disse:")
        st.error(random.choice(respostas_deizy))
    else:
        st.warning("Mande uma dúvida pro homem, fih!")
