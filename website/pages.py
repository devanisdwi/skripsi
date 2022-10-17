import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle


st.set_page_config(page_title="Welcome!", page_icon="🙌", layout="wide")

with st.sidebar:
    choose = option_menu("Skripsi Dwi", ["Dokumentasi", "Clustering Demo"],
                         icons=['journal-richtext', '123'],
                         menu_icon="arrow-down-right-square-fill", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#262730"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#808080"},
        "nav-link-selected": {"background-color": "#0e1117"},
    }
)

# HALAMAN DOKUMENTASI
if choose == 'Dokumentasi':
    st.write("# Tugas Akhir Data Science 👩‍💻")

    st.markdown(
        """
        Platform ini merupakan hasil penelitian yang telah dikembangkan
        menggunakan konsep _Unsupervised Learning_
        pada bidang _Educational Data Mining_.

        **👈 Pilih menu yang telah tersedia pada dropdown disamping**
        
        ##### Disusun dan dikembangkan oleh:
        - Nama: [Devanis Dwi Sutrisno](https://www.linkedin.com/in/devanis-dwi-sutrisno/)
        - NIM: 201910370311078
        - Jurusan: Informatika
        - Fakultas: Teknik
        - Pertanyaan lebih lanjut: [devanisdwis@gmail.com](mailto:devanisdwis@gmail.com)
        
        ##### Dosen Pembimbing:
        - Dosen Pembimbing 1: [Vinna Rahmayanti SN., S.Si., M.Si.](https://scholar.google.com/citations?user=OU8ju6wAAAAJ&hl=en&oi=ao)
        - Dosen Pembimbing 2: [Evi Dwi Wahyuni S.Kom., M.Kom.](https://scholar.google.co.id/citations?user=ihgr_6kAAAAJ&hl=en)
    """
    )

elif choose == 'Clustering Demo':
    st.write("# Clustering 👩‍💻")

    with st.form(key='values_in_form'):
        text_style = '<p style="font-family:sans-serif; color:red; font-size: 15px;">These Input Fields are Required!</p>'
        st.markdown(text_style, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns( [1, 1, 1, 1, 1])
        with col1:
            code_module = st.selectbox('Code Module', ('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG'))
        with col2:
            gender = st.selectbox('Gender', ('M', 'F'))
        with col3:
            disability = st.selectbox('Disability', ('N', 'Y'))
        with col4:
            final_result = st.selectbox('Final Result', ('Pass', 'Fail'))
        with col5:
            score = st.slider('Score', 1,100,1)
        col6, col7, col8, col9, col10 = st.columns( [1, 1, 1, 1, 1])
        with col6:
            assessment_type = st.selectbox('Assessment Type', ('TMA', 'CMA'))
        with col7:
            activity_type = st.selectbox('Activity Type', ('resource','oucontent','url','homepage','subpage','glossary','forumng','oucollaborate','dataplus','quiz','ouelluminate','sharedsubpage','questionnaire','page','externalquiz','ouwiki','dualpane','repeatactivity','folder','htmlactivity'))
        with col8:
            total_activities = st.slider('Total Activities', 9,36,9)
        with col9:
            sum_click = st.slider('Sum Click', 1,3725,50)
        with col10:
            total_interaction = st.slider('Total Interaction', 14,315000,150)

        submitted = st.form_submit_button("Predict Learning Style")
    
    data = [{
        'code_module': code_module,
        'gender': gender,
        'disability': disability,
        'final_result': final_result,
        'score': score,
        'assessment_type': assessment_type,
        'activity_type': activity_type,
        'total_activities': total_activities,
        'sum_click': sum_click,
        'total_interaction': total_interaction,
    }]

    df_predict = pd.DataFrame(data, index=[0])

    pickle_in = open('kproto_model.pkl', 'rb') 
    clusters = pickle.load(pickle_in)

    if submitted: 
        prediction = clusters.predict(df_predict, categorical=[0, 1, 2, 3, 5, 6])
        if prediction == 0:
            pred = 'Visual'
        elif prediction == 1:
            pred = 'Audiotory'
        else:
            pred = 'Kinaesthetic'
        st.success('Your Learning Style is {}'.format(pred))