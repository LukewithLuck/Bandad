import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Analista Pai-Banana", page_icon="🍌", layout="centered")

# 2. VISUAL (FRONT-END) - Amarelo, Preto e Branco
st.markdown("""
    <style>
    /* Fundo da página em Amarelo */
    .stApp {
        background-color: #fcdb05; 
    }
    /* Botão em Preto com texto Branco */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #000000;
        color: #ffffff;
        height: 3em;
        font-weight: bold;
        border: none;
    }
    /* Efeito ao passar o mouse no botão */
    .stButton>button:hover {
        background-color: #333333;
        color: #fcdb05;
    }
    /* Inputs (campos de texto) com borda preta */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #000000;
    }
    /* Estilo da Imagem */
    div[data-testid="stImage"] img {
        border-radius: 15px;
        border: 4px solid #000000;
    }
    /* Cor dos textos e títulos para Preto */
    h1, h2, h3, p, span, label {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SISTEMA DE SENHA (SEGURANÇA)
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🍌 Área Restrita da Família")
    senha = st.text_input("Digite a senha para entrar:", type="password")
    if st.button("Entrar"):
        if senha == "banana123": # <--- PODE MUDAR A SENHA AQUI
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Senha errada, fih! Pergunta pro Lucca.")
    st.stop()

# 4. CONTEÚDO DO APP (SÓ APARECE COM A SENHA)
st.title("🍌 Consultoria: Pai-Banana")
st.write("O analista mais 'preguiçoso' da internet.")

# Tenta carregar a imagem (Garanta que o nome no GitHub seja igual)
st.image("Gemini_Generated_Image_.jpg", use_column_width=True)

st.write("---")
pergunta = st.text_input("O que você quer que eu analise?")
arquivo = st.file_uploader("Ou mande uma foto:", type=["jpg", "png", "jpeg"])

respostas_deizy = [
    "A Deizy olhou e disse: 'Isso aí é perda de tempo, compra uma coca pra mim ou te dou um coro'.",
    "Veredito da Deizy: 'Se você gastar dinheiro com isso, não vou fazer janta'.",
    "Deizy falou: 'Achei feio e caro, mas vou gastar meu salário com Coca-Cola'.",
    "A patroa mandou avisar: 'Isso é golpe, sai dessa agora!'.",
    "Deizy disse: 'Pode até ser bom, mas se fizer isso nunca mais conta comigo pra nada'.",
    "Ele perguntou pra Deizy e ela respondeu: 'Pergunta pro Lucca, ele que é o gênio da computação'.",
    "Ele falou com a Deizy e ela respondeu: 'Manda pro Lucca, ele que é o faz-tudo aqui da casa'.",
    "Deizy examinou e concluiu: 'É perda de tempo!'.",
    "A Deizy não respondeu e brigou comigo por interromper o shorts dela.",
    "A Deizy não respondeu porque tava vendo notícia ruim no celular.",
    "A Deizy disse pra mim olhar, mas eu não vou olhar porque só quero ver YouTube e dormir de tarde."
]

# 5. LÓGICA DE AÇÃO (BACK-END)
if st.button("Consultar Especialista"):
    if pergunta or arquivo:
        # O Delay de 5 segundos que você pediu
        with st.status("Analisando seriamente...", expanded=True) as status:
            time.sleep(5)
            st.write("Conectando ao cérebro da Deizy...")
            time.sleep(2)
            status.update(label="Análise finalizada!", state="complete", expanded=False)
        
        # Mensagem de preguiça
        st.info("👴: Ah, tô com preguiça... Vou falar pra Deizy fazer isso.")
        time.sleep(2)
        
        # Resposta final da Deizy
        st.subheader("O que a Deizy disse:")
        st.error(random.choice(respostas_deizy))
    else:
        st.warning("Mande uma dúvida pro homem, fih
