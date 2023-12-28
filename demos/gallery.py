import streamlit as st
from markdowns import ele
import os
import shutil

if 'links' not in st.session_state:
    st.session_state.links = None

if 'user_links' not in st.session_state:
    st.session_state.user_links = None

if 'prompt_sess' not in st.session_state:
    st.session_state.prompt_sess = []

vids_links = ["vids/mysterious_island.mp4", "vids/venice.mp4", 
                "vids/mars.mp4", "vids/animal_world.mp4"]


user_vids_links = []


st.session_state.links = vids_links
st.session_state.user_links = user_vids_links
st.session_state.prompt_sess.append(st.session_state.userprompt)
# journey to mysterious island, somewhere in pacific ocean - realistic
# zootopia - cartoonish
# Depict a story of, Young Boy gifts flower's to a girl in Venice and confesess his love to her - anime
# A little boy's journey to mars with a home made rocket - realistic

st.markdown("<h1 style='text-align: centre; color: yellow;'>Gallery</h1>", unsafe_allow_html=True)
st.write("Vids generated through this app :)")

direc = "C:\\Python3.10.1\\Lib\\site-packages\\QtDesigner\\VsCode Py\\story_gen\\dir_mp4"

directory_path = os.listdir(direc)

def side_bar_view():
    return ele.sides

side = side_bar_view()
st.sidebar.write(side)


if st.session_state.upload:
    if os.path.isdir(direc):
        for i in directory_path:
            st.session_state.user_links.append(i)
    else:
        pass


for i in range(0, len(st.session_state.links), 2):
    col1, col2 = st.columns(2)
    col1.video(st.session_state.links[i])
    if i + 1 < len(st.session_state.links):
        col2.video(st.session_state.links[i + 1])

st.markdown("<h1 style='text-align: centre; color: yellow;'>Your videos will show up here</h1>", unsafe_allow_html=True)

for i in range(0, len(st.session_state.user_links), 2):
    col1_, col2_ = st.columns(2)
    col1_.video(direc+'\\'+st.session_state.user_links[i])
    if i + 1 < len(st.session_state.user_links):
        col2_.video(direc+'\\'+st.session_state.user_links[i + 1])

# shutil.rmtree("dir_png")

