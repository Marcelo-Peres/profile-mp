from pathlib import Path
from resume_data.eng import *
from PIL import Image
from streamlit_lottie import st_lottie
import streamlit as st, json, requests, os, shutil, pandas as pd

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'CV.pdf'
profile_pic = current_dir / 'assets' / 'mp-pic-01.png'
pycache_job = current_dir / 'jobs' / '__pycache__'
pycache_resume = current_dir / 'resume_data' / '__pycache__'
py_anime = 'https://assets5.lottiefiles.com/packages/lf20_2znxgjyt.json'

if os.path.exists(pycache_job):
    shutil.rmtree(pycache_job)

if os.path.exists(pycache_resume):
    shutil.rmtree(pycache_resume)

df_files = pd.DataFrame([file[:-3] for file in os.listdir('jobs')], columns=['base'])
df_files['imports'] = 'from jobs.' + df_files.base + ' import base'

list_jobs = list()
for job in df_files.index:
    exec(df_files.imports[job])
    list_jobs.append(base)

df = pd.DataFrame(list_jobs)


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

py_anime = load_lottie_url(py_anime)


# --- GENERAL SETTINGS ---
PAGE_TITLE = page_title
PAGE_ICON = page_icon
NAME = name
ROLE = role

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

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=330)
    st_lottie(py_anime, height=200, key='coding')

with col2:
    st.write('\n'*2)
    st.header(NAME)
    st.subheader(ROLE)
    st.markdown(DESCRIPTION)
    # st.download_button(
    #     label=' 📄 Download Resume',
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime='application/octet-stream',
    # )
    st.write('📫', EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].subheader(f'[{platform}]({link})')

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.markdown(qualification)
st.write(qualification_info)


# --- SKILLS ---
st.write('\n')
st.markdown(skills)
st.write(skills_info)


# --- WORK HISTORY ---
st.write('\n')
st.markdown(job_header)


# --- JOB 1
st.write('---')
st.markdown(df.job[0])
st.markdown(df.time[0])
st.write(df.info_[0], unsafe_allow_html=True)

# --- JOB 2
st.write('---')
st.markdown(df.job[1])
st.markdown(df.time[1])
st.write(df.info_[1], unsafe_allow_html=True)

# --- JOB 3
st.write('---')
st.markdown(df.job[2])
st.markdown(df.time[2])
st.write(df.info_[2], unsafe_allow_html=True)

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader('Projects & Accomplishments')
# st.write('---')
# for project, link in PROJECTS.items():
#     st.write(f'[{project}]({link})')
