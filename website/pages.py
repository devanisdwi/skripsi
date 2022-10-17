from operator import index
import streamlit as st
from streamlit_option_menu import option_menu
from collections import deque
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import pickle
from raceplotly.plots import barplot

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

    model = pickle.load(open('kproto_model.pkl','rb'))
    model2 = pickle.dump(open('diabetes_model.pkl', 'wb'))
    df = pd.read_csv('df_pred.csv')

    st.write('---')

    st.markdown('<p class="font">Set Parameters...</p>', unsafe_allow_html=True)

    value_list_code_module = list(df['code_module'].unique())
    value_list_code_module = deque(value_list_code_module)
    value_list_code_module.appendleft('-')

    value_list_gender = list(df['gender'].unique())
    value_list_gender = deque(value_list_gender)
    value_list_gender.appendleft('-')

    value_list_disability = list(df['disability'].unique())
    value_list_disability = deque(value_list_disability)
    value_list_disability.appendleft('-')

    value_list_final_result = list(df['final_result'].unique())
    value_list_final_result = deque(value_list_final_result)
    value_list_final_result.appendleft('-')

    value_list_score = list(df['score'].unique())
    value_list_score = deque(value_list_score)
    value_list_score.appendleft('-')

    value_list_assessment_type = list(df['assessment_type'].unique())
    value_list_assessment_type = deque(value_list_assessment_type)
    value_list_assessment_type.appendleft('-')

    value_list_activity_type = list(df['activity_type'].unique())
    value_list_activity_type = deque(value_list_activity_type)
    value_list_activity_type.appendleft('-')

    value_list_total_activities = list(df['total_activities'].unique())
    value_list_total_activities = deque(value_list_total_activities)
    value_list_total_activities.appendleft('-')

    value_list_sum_click = list(df['sum_click'].unique())
    value_list_sum_click = deque(value_list_sum_click)
    value_list_sum_click.appendleft('-')

    value_list_total_interaction = list(df['total_interaction'].unique())
    value_list_total_interaction = deque(value_list_total_interaction)
    value_list_total_interaction.appendleft('-')

    with st.form(key='values_in_form'):
        text_style = '<p style="font-family:sans-serif; color:red; font-size: 15px;">These Input Fields are Required!</p>'
        st.markdown(text_style, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns( [1, 1, 1, 1, 1])
        with col1:
            item_code_module = st.selectbox('Code Module:', value_list_code_module, index=0, help='Choose the column in your data that represents the bars, e.g., AAA, BBB, etc.') 
        with col2:
            item_gender = st.selectbox('Gender:', value_list_gender, index=0, help='e.g., M for Male and F for Female') 
        with col3:
            item_disability = st.selectbox('Disability:', value_list_disability, index=0, help='e.g., Y for Persons with Disabilities and N for Non-Disabilty') 
        with col4:
            item_final_result = st.selectbox('Final Result:', value_list_final_result, index=0, help='Choose the column in your data that represents the bars, e.g., Pass and Fail') 
        with col5:
            item_score = st.slider('Score', 0,100,0, step=1, help='Adjust the width of the chart')

        col6, col7, col8, col9, col10 = st.columns( [1, 1, 1, 1, 1])
        with col6:
            item_assessment_type = st.selectbox('Assessment Type:', value_list_assessment_type, index=0, help='TMA (Tutor Marked Assignment): Essay, Analysis, etc and CMA (Computer Marked Assignment): Multiple Choice Questions') 
        with col7:
            item_activity_type = st.selectbox('Activity Type:', value_list_activity_type, index=0, help='Choose the column in your data that represents the bars, e.g., forum, quiz, etc.') 
        with col8:
            item_total_activities = st.slider('Total Activities',9,36,9, step=1, help='Adjust the width of the chart') 
        with col9:
            item_sum_click = st.slider('Sum Click',1,3725,1, step=50, help='Adjust the width of the chart') 
        with col10:
            item_total_interaction = st.slider('Total Interaction',1,315000,1, step=100, help='Adjust the width of the chart') 

        inputs = [[item_code_module, item_gender, item_disability, item_final_result, item_score, item_assessment_type, item_activity_type, item_total_activities, item_sum_click, item_total_interaction]]
        
        submitted = st.form_submit_button("Predict Learning Style")

        if submitted:
            result = model.predict(inputs)
            update_result = result.flatten()
            st.success('The Learning Style is {}'.format(submitted))
        else:
            st.warning("You must complete the required fields")

    