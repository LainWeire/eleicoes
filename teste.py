import streamlit as st
import streamlit_authenticator as stauth


st.text("Como deseja se registrar?")

if 'user_type' not in st.session_state:
    st.session_state.user_type = None

if st.button('Escola'):
    st.session_state.user_type = 'Escola'


if st.button('Aluno'):
    st.session_state.user_type = 'Aluno'

def ver_preenchidos(campos): # funcao p ver se cada ebtrada foi preenchida
    return all(campos.values())


if st.session_state.user_type == 'Escola': # registrar escpla
    
    estado = st.text_input("Estado:", value="", placeholder="Digite aqui...")
    cidade = st.text_input("Cidade:", value="", placeholder="Digite aqui...")
    endereço = st.text_input("Endereço:", value="", placeholder="Digite aqui...")
    codigo_inep = st.text_input("Código Inep / Mec:  ", value="", placeholder="Digite aqui...")

    campos_escola = {
        'Estado': estado,
        'Cidade': cidade,
        'Endereço': endereço,
        'Código Inep / Mec': codigo_inep
    }
    if st.button("Registrar Escola"):
        if ver_preenchidos(campos_escola):
            st.success("Escola registrada com sucesso!")

        else:
            st.error("Por favor, preencha todos os campos.")


elif st.session_state.user_type == 'Aluno': # registrar aluno
    foto = st.file_uploader("Foto do aluno:", type=["jpg", "jpeg", "png"])
    nome = st.text_input("Nome do aluno:", value="", placeholder="Digite aqui...")
    cpf = st.text_input("CPF do aluno:", value="", placeholder="Digite aqui...")
    responsavel = st.text_input("Responsável do aluno:", value="", placeholder="Digite aqui...")

    if foto is not None:
        st.image(foto, caption="Foto do aluno", width=100)
    
    campos_aluno = {
        'Nome': nome,
        'CPF': cpf,
        'Responsável': responsavel,
        'Foto': foto
    }

    if st.button("Registrar Aluno"):
        if ver_preenchidos(campos_aluno):
            st.success("Escola registrada com sucesso!")

        else:
            st.error("Por favor, preencha todos os campos.")


