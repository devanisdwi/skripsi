import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="Welcome at Dwi's Skripsi!", page_icon="🙌", layout="wide")

with st.sidebar:
    choose = option_menu("Dwi's Skripsi", ["Dokumentasi", "Clustering Demo"],
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

    doc1, doc2, doc3, doc4 = st.columns([1,2,3,1])
    with doc2:
        # Check file path for debugging
        import os

        def file_selector(folder_path='.'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Select a file', filenames)
            return os.path.join(folder_path, selected_filename)

        filename = file_selector()
        st.write('You selected `%s`' % filename)
        
        st.write("### Visualisasi Hasil Klaster")
        image1 = Image.open('../distribution.png')
        image1 = image1.resize((600, 400))
        st.image(image1, caption='Cluster Distributions')

        image2 = Image.open('../centroid.png')
        image2 = image2.resize((600, 400))
        st.image(image2, caption='Cluster Centroids')
    with doc3:
        st.markdown("""
            # Tugas Akhir Data Science 👩‍💻
            **👈 Pilih menu yang telah tersedia pada navbar disamping**
            
            Platform ini merupakan hasil penelitian yang telah dikembangkan menggunakan konsep _Unsupervised Learning_ pada bidang _Educational Data Mining_.            
            
            **Disusun dan dikembangkan oleh:**
            - Nama: [Devanis Dwi Sutrisno](https://www.linkedin.com/in/devanis-dwi-sutrisno/)
            - Jurusan/Fakultas: Informatika/Teknik 
            - Pertanyaan lebih lanjut: [devanisdwis@gmail.com](mailto:devanisdwis@gmail.com)
            
            **Hasil atau keluaran dari penelitian ini berupa:**

            1. Data preprocessing menggunakan dataset yang berasal dari https://analyse.kmi.open.ac.uk/open_dataset
            2. Analisa Cluster menggunakan Elbow Method dan Silhouette Analysis
            3. Clustering Model menggunakan algoritma K-Prototypes
            4. Model Deployment menggunakan Streamlit Framework
        """)

elif choose == 'Clustering Demo':
    st.write("# Clustering Demo 👩‍💻")

    with st.form(key='values_in_form'):
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
    
    clusters = pickle.load(open('../kproto_model.pkl', 'rb'))

    if submitted: 
        prediction = clusters.predict(df_predict, categorical=[0, 1, 2, 3, 5, 6])
        if prediction == 0:
            pred = 'Visual'
        elif prediction == 1:
            pred = 'Audiotory'
        else:
            pred = 'Kinaesthetic'
        st.success('Your Learning Style is {}'.format(pred))
    
    st.write("---")

    st.write("### Deskripsi Klaster tiap Gaya Belajar:")
    dec1, dec2, dec3 = st.columns([1,1,1])
    with dec1:
        st.markdown("""
            1. Visual:
                - Mean score = 60
                - Mean total_interaction = 15
                - Mean total_activities = 22
                - Umumnya menyukai assessment_type berupa TMA (Tutor Marked Assessment)
                - Mayoritas memiliki Gender Laki-Laki
                - Sebagian besar Bukan Penyandang Disabilitas
                - Cenderung sedikit lebih banyak mendapatkan Final Status berupa Fail
        """)
    with dec2:
        st.markdown("""
            2. Audiotory:
                - Mean score = 67
                - Mean total_interaction = 30
                - Mean total_activities = 34
                - Umumnya menyukai assessment_type berupa TMA (Tutor Marked Assessment)
                - Mayoritas memiliki Gender Laki-Laki
                - Sebagian besar Bukan Penyandang Disabilitas
                - Cenderung sedikit lebih banyak mendapatkan Final Status berupa Pass
        """)
    with dec3:
        st.markdown("""
            3. Kinaesthetic:
                - Mean score = 81
                - Mean total_interaction = 66
                - Mean total_activities = 35
                - Cenderung mengerjakan kedua assessment_type berupa TMA dan CMA
                - Persebaran data gender laki-laki dan perempuan yang seimbang
                - Persebaran data penyandang disabilitas yang seimbang
                - Lebih banyak mendapatkan Final Status berupa Pass
        """)
