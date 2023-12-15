import streamlit as st
import os
from streamlit_option_menu import option_menu
from translator import translation_func
from PIL import Image
import jieba
from xpinyin import Pinyin

try:
    os.mkdir("temp_folder")
except:
    pass

# Add a logo (optional) in the sidebar
logo = Image.open(r'.\assets\2023-12-13 17.08.27.png')
st.sidebar.image(logo, width=120)

# Add the expander to provide some basic information about the app
st.sidebar.markdown("### My Little Language learning App")
with st.sidebar.expander("About the App"):
    st.write("""
        This language learning App is built by Sharone Li using Streamlit. Check out her medium article for more details about the app and source code.
     """)
st.sidebar.markdown(
    "You can build your own language learning app using streamlit and Google Translate API. \n\n I only showed a few "
    "languages in this app, but you can certainly expand to other languages as well. Have fun!")
# Add a horizontal menu bar
choose = option_menu("What do you want to learn today?", ['Chinese', 'French', 'German', 'Japanese', 'Spanish'],
                     icons=['book', 'book', 'book', 'book', 'book'],
                     menu_icon="app-indicator", default_index=0,
                     styles={
                         "container": {"padding": "5!important", "background-color": "#fafafa"},
                         "icon": {"color": "orange", "font-size": "20px"},
                         "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px",
                                      "--hover-color": "#eee"},
                         "nav-link-selected": {"background-color": "#02ab21"},
                     },
                     orientation='horizontal'
                     )
# Add a input text box that allows users to type a sentence in English
st.markdown(""" <style> .font {                                          
font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Please type a sentence below</p>', unsafe_allow_html=True)
text = st.text_input("Example:", value="I am interested in data science.")

if choose == "Chinese":
    if st.button("Show Translation and Audio"):
        input = 'en'
        output = 'zh'
        translation_text = translation_func(input, output, text)

        st.write('  ')
        segments = jieba.cut(translation_text)  # used for chinese text segmentation
        seg_output = " ".join(segments)
        html_str = f"""
        <style>
        p.a {{
        font: bold {30}px Courier;
        }}
        </style>
        <p class="a">{seg_output}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)  # display the translated text in Chinese characters
        st.write('  ')

        p = Pinyin()
        pinyined = p.get_pinyin(seg_output, splitter='',
                                tone_marks='marks')  # Get pinyin (the official romanization system for Standard Chinese in mainland China)
        html_str2 = f"""
        <style>
        p.a {{
        font: bold {25}px Courier;
        }}
        </style>
        <p class="a">{pinyined}</p>
        """
        st.markdown(html_str2, unsafe_allow_html=True)  # display pin yin
