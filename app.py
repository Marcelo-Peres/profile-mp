from pathlib import Path
from resume_data.base_info import *
from PIL import Image
from streamlit_lottie import st_lottie
import streamlit as st, json, requests, os, shutil

language = 'en'

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
# resume_file = current_dir / 'assets' / 'CV.pdf'
profile_pic = current_dir / 'assets' / 'mp_pic.png'
# pycache_resume = current_dir / 'resume_data' / '__pycache__'
py_anime = 'https://assets5.lottiefiles.com/packages/lf20_2znxgjyt.json'
print(current_dir)

# if os.path.exists(pycache_resume):
#     shutil.rmtree(pycache_resume)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

py_anime = load_lottie_url(py_anime)

# --- GENERAL SETTINGS ---
PAGE_TITLE = page_title(language)
PAGE_ICON = page_icon
NAME = name
ROLE = role(language)

DESCRIPTION = info
EMAIL = email
SOCIAL_MEDIA = social_media
# PROJECTS = {
#     '🏆 Sales Dashboard - Comparing sales across three stores': 'https://youtu.be/Sb0A9i6d320',
#     '🏆 Income and Expense Tracker - Web app with NoSQL database': 'https://youtu.be/3egaMfE9388',
#     '🏆 Desktop Application - Excel2CSV converter with user settings & menubar': 'https://youtu.be/LzCfNanQ_9c',
#     '🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel': 'https://pythonandvba.com/mytoolbelt/',
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# with open(resume_file, 'rb') as pdf_file:
#     PDFbyte = pdf_file.read()

PROFILE_PIC = Image.open(profile_pic)

# lang1 =

# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    lang = st.button('English')
    if lang:
        language = 'en'
        PAGE_TITLE = page_title(language)
        ROLE = role(language)
    st.image(PROFILE_PIC, width=330)
    st_lottie(py_anime, height=200, key='coding')

with col2:
    lang = st.button('Portuguese')
    if lang:
        language = 'pt'
        PAGE_TITLE = page_title(language)
        ROLE = role(language)
    else:
        language = 'en'
        
    st.write('\n'*2)
    st.header(NAME)
    st.subheader(ROLE)
    st.markdown(DESCRIPTION)
    st.write('📫', EMAIL)
    # st.download_button(
    #     label=' 📄 Download Resume',
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime='application/octet-stream',
    # )
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].subheader(f'[{platform}]({link})')

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.markdown(qualification(language))
st.write(qualification_info(language))


# --- SKILLS ---
st.write('\n')
st.markdown(skill(language))
st.write(skill_info(language))


# --- WORK HISTORY ---
st.write('\n')
st.markdown(job_header(language))


# --- JOB 1
st.write('---')
st.markdown(job_t03(language))
st.markdown(job_t03_time(language))
st.write(job_t03_info(language), unsafe_allow_html=True)

# --- JOB 2
st.write('---')
st.markdown(job_t02(language))
st.markdown(job_t02_time(language))
st.write(job_t02_info(language), unsafe_allow_html=True)

# --- JOB 3
st.write('---')
st.markdown(job_t01(language))
st.markdown(job_t01_time(language))
st.write(job_t01_info(language), unsafe_allow_html=True)

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader('Projects & Accomplishments')
# st.write('---')
# for project, link in PROJECTS.items():
#     st.write(f'[{project}]({link})')
