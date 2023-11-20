from tokenize import Token
from core.text_completion import *
from core.text_completion import TextCompletion
import run
import streamlit as st

st.set_page_config(
    page_title="YouSum",
    page_icon=":movie_camera:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title(':movie_camera: Youtube :red[Summarizer]', anchor=False)
# st.subheader('Seja muito bem-vindo ao trabalho de conclusão de curso de NLP do Instituo Mauá de Tecnologia.')
st.markdown('\n\n')

texto_abertura = """Seja muito bem-vindo ao youtube summarizer. 
                    \n Uma ferramenta que permite capturar as principais informações de seus videos preferidos do youtube.
                    Para utiliza-la é muito simples: copie a url do video desejado e cole no box abaixo, espere o video carregar, para confirmação de que se trata do video correto, e depois é só clicar em 'Resumir'.
                    """

st.write(texto_abertura)

url = st.text_input('Insira sua URL no box abaixo:')

if url:
    try:
        st.video(url)
    except:
        pass
   
if st.button('Resumir', type='primary'):
    formatted_output = run.yt_trancript(url)
    num_tokens = run.tokens_proc(formatted_output)
    comp = TextCompletion(prompt=formatted_output, num_token=num_tokens)

    st.divider()
    with st.chat_message('user'):
        message_placeholder = st.empty()
        message_placeholder.markdown("Aguarde um momento enquanto estou processando sua solicitação..")
        for r in comp.final_response():
            message_placeholder.markdown(str(r) + "▌")

        message_placeholder.markdown(r)
