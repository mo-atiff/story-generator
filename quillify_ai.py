import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

from st_pages import Page, show_pages
from markdowns import ele
import re

import requests
import io
from io import BytesIO
import os
from PIL import Image
from moviepy.editor import *

from IPython.display import display, HTML
import pyttsx3
import math
import shutil
import spacy
import mutagen 
from mutagen.wave import WAVE 
import random
import string


nlp = spacy.load("en_core_web_sm")

st.set_page_config(
    page_title="Story to Audio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages(
    [
        Page("quillify_ai.py", "AI Customized Story", "🤖"),
        Page("demos/demo.py", "Customize Your Story", "📚"),
        Page("demos/gallery.py", "Gallery", "📸"),
    ]
)

if 'openai' not in st.session_state:
	st.session_state.openai = None

if 'huggingtok' not in st.session_state:
	st.session_state.huggingtok = None

if 'userprompt' not in st.session_state:
	st.session_state.userprompt = None

if 'data' not in st.session_state:
	st.session_state.data = None

if 'story' not in st.session_state:
	st.session_state.story = None

if 'imgstyle' not in st.session_state:
	st.session_state.imgstyle = None

if 'upload' not in st.session_state:
    st.session_state.upload = False

if 'gens' not in st.session_state:
    st.session_state.gens = None

def side_bar_view():
    return ele.sides

def cleanResume(resumeText):
    resumeText = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",resumeText).split())
    resumeText = re.sub(r'[^\x00-\x7F]+',r' ', resumeText)
    resumeText = ''.join(resumeText.splitlines())
    return resumeText


def extract_adjective_noun_combinations(sentence):
    doc = nlp(sentence.lower())
    adjective_noun_combinations = []
    for token in doc:
        if token.dep_ == "amod" and token.head.pos_ == "NOUN":
            adjective_noun_combinations.append(f"{token.text} {token.head.text}")
    return adjective_noun_combinations


def generate_video_with_audio(temp_images, audio_file_path, duration):
    clip = ImageSequenceClip(temp_images, fps=1)
    slow_clip = clip.speedx(0.13)

    video_clip = slow_clip.to_videofile("temp_output_video.mp4", codec='libx264', fps=1)

    audio_clip = AudioFileClip(audio_file_path)

    vid = VideoFileClip("temp_output_video.mp4")
    vid = vid.subclip(0, duration+2)
    video_clip = vid.set_audio(audio_clip)

    os.makedirs("dir_mp4", exist_ok=True)


    random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    random_digits = ''.join(random.choice(string.digits[1:]) for _ in range(3))
    random_file_name = random_chars + random_digits
    
    output_video_path = os.path.join("dir_mp4", f"{random_file_name}.mp4")
    video_clip.write_videofile(output_video_path, codec='libx264', fps=1)

    return output_video_path


def image_generator(tups):
    # st.write(tups)
    blob = []
    j = 1
    err_imgs = 0
    with st.status("Creating Images...", expanded=True) as status:
        st.write('Crafting your masterpiece-just a cosmic heartbeat away! 🌌✨ Just 2-5 mins #ArtistryInProgress')
        for i in tups:
            image_bytes = query({
                "inputs": i,
                # "seed" : 42
            })

            st.write(f"BYTES LEN OF IMAGE - {j} : ", len(image_bytes))

            if len(image_bytes) < 900:
                image_bytes2 = query({
                "inputs": i,
                })

                if len(image_bytes2) > 900:
                    blob.append(image_bytes2)
                    st.write(f"BYTES LEN OF IMAGE - {j} : ", len(image_bytes2))

                else:
                    st.write(f"STILL BYTES LEN OF IMAGE - {j} ARE - {len(image_bytes2)}")
                    # err_imgs+=1
            
            
            if len(image_bytes) > 900:
                blob.append(image_bytes)

            elif len(image_bytes) < 900 and len(image_bytes2) < 900:
                err_imgs+=1

            st.write(f"Created Image - {j}")
            j+=1

        status.update(label="Images created sucessfully!", state="complete", expanded=False)

    if err_imgs > 0:
        st.error(f"{err_imgs} error image generated by app")
    return blob


side_bar = side_bar_view()
with st.sidebar : 
    api_gpt = st.text_input('Enter OpenAI API key', value=st.session_state.openai)
    st.session_state.openai = api_gpt

    # st.markdown("<hr>", unsafe_allow_html=True)

    hug_tok = st.text_input('Enter Hugging Face API token', value=st.session_state.huggingtok)
    st.session_state.huggingtok = hug_tok

    # st.markdown("<hr>", unsafe_allow_html=True)

API_URL = "https://api-inference.huggingface.co/models/openskyml/dalle-3-xl"
headers = {"Authorization": f"Bearer {st.session_state.huggingtok}"}


def speak_text(text, voice, rate=150):
    engine = pyttsx3.init()

    print("TEXT : ", text, '\n')
    print("VOICE : ", voice, '\n')

    engine.setProperty('voice', voice)
    engine.setProperty('rate', rate)


    download_dir = 'dir_mp3'
    # os.makedirs(download_dir, exist_ok=True)

    # # file_path = os.path.join(download_dir, "my_audio.mp3") 
    # file_path = os.path.join(download_dir, "my_audio.wav") 
    
    # engine.save_to_file(text, file_path)
    # engine.runAndWait()
    # engine.stop()
    full_path = os.path.join(os.getcwd(), download_dir)
    st.write("FULL PATH : ", full_path)
    file_path = os.path.join(full_path, "my_audio.wav")
    st.write("FILE PATH : ", file_path)
    text = text.decode("latin-1")
    proxy = engine._proxy
    engine.save_to_file(text, file_path)
    proxy.notify('finished-utterance', completed=True)

    # engine.save_to_file(text, file_path)
    st.write(text, file_path)
    engine.runAndWait()
    engine.stop()

    return file_path


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    # st.write(response)
    return response.content


def main():

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown(side_bar, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: centre; color: #007BA7;'>QUILIFY.ai</h1>", unsafe_allow_html=True)
    with st.expander("Important"):
        st.warning("If you come across a sea of error images, consider reloading an app and regenerating the video. The glitch might be tied to the DALL-E model hosted on Hugging Face. 🔄🚀")
    st.markdown("**🌟 Welcome to our Creative Haven! Unleash your imagination and craft a story that will captivate the universe. 🚀✨**")

                    
    plot = st.text_input("What epic tale is brewing in your mind? Share it with us :)", value=st.session_state.userprompt, placeholder="A young cute little boy with blue eyes embarks on his journey to moon, In a rocket made by him and his friends.")
    st.session_state.userprompt = plot

    if plot and api_gpt and hug_tok:
        dis = False
        dis_slider=False
        dis_gen=False
        dis_style=False
    else:
        dis = True
        dis_slider = True
        dis_gen = True
        dis_style = True

    count_of_words = st.slider('Number of Words for Story', min_value=50, max_value=700, disabled=dis_slider)
    gens, style = st.columns(2)
    genders = gens.radio('Select Gender of your Voice', ['Male', 'Female'], disabled=dis_gen, horizontal=True)
    st.session_state.gens = genders
    img_style = style.radio('Select Style of your Image', ['Realistic', 'Cartoon', 'Anime'], disabled=dis_style, horizontal=True)
    st.session_state.imgstyle = img_style
    _, but_place, _ = st.columns(3)
    txt_to_story = but_place.button('Generate Story', key='generate_story', disabled=dis)

    if not api_gpt:
        st.error('Please Enter OpenAI API key')

    else:
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=.9, openai_api_key=st.session_state.openai)

    if txt_to_story:
        no_of_imgs = count_of_words/12

        prompt1 = PromptTemplate(
            template = """
                    You are given story title : {title}.\n
                    Your task is to generate a story plot of {num_of_words} words for it.\n
                    Also make sure You generate {no_of_img} fullstops(Gramatical symbol), while making the story.\n
                    Please return me only story generated, no additional content like the text 'full stop' at last shouldn't be there!
            """, input_variables=["title", "num_of_words", "no_of_img"]
        )

        prompt_chain1 = LLMChain(llm=llm, prompt=prompt1)
        LLM_chain = SequentialChain(chains=[prompt_chain1], input_variables = ["title", "num_of_words", "no_of_img"], verbose=True)
        cnt_imgs = math.ceil(no_of_imgs)
        # st.write(cnt_imgs)
        story = LLM_chain({"title":plot, "num_of_words":count_of_words, "no_of_img":cnt_imgs})['text']
        st.session_state.story = story

        st.markdown("<h4 style='text-align: centre;'>GENERATED STORY</h5>", unsafe_allow_html=True)
        st.markdown(f"***{st.session_state.story}***", unsafe_allow_html=True)
    

        if "The Title of the story needs more details for story generation" in story:
            st.error('Please provide more details for story generation')
            st.stop()

        voices = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0", 
                        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"]


        if genders=="Male":
            bytes_path = speak_text(story, voices[0])
        else:
            bytes_path = speak_text(story, voices[1])

        # st.write(bytes_path)
        st.write("BYTES ABS PATH : ", os.path.abspath(bytes_path))
        with open(bytes_path, "r") as mp3_file:
            aud_bytes = mp3_file.read()

        # st.write(aud_bytes)

        audio = WAVE(bytes_path)  
        audio_info = audio.info 
        duration_audio = int(audio_info.length)

        st.audio(aud_bytes, format='audio/wav')

        st.session_state.data = story

        text_for_img = story.split('.')

        noun_adj = extract_adjective_noun_combinations(plot)
        noun_adj = ' '.join(noun_adj)

        text_for_img = [i+' '+noun_adj+' '+img_style+' Very detailed, full HD ' for i in text_for_img]


        binary_img = image_generator(text_for_img)

        temp_images = []

        os.makedirs("dir_png", exist_ok=True)

        for i, image_bytes in enumerate(binary_img):
            png_file_path = os.path.join("dir_png", f"image_{i+1}.png")
            with open(png_file_path, "wb") as png_file:
                png_file.write(image_bytes)

            temp_images.append(png_file_path)



        try:
            output_video_path = generate_video_with_audio(temp_images, bytes_path, duration_audio)

            _, container, _ = st.columns([1, 4, 1])
            container.video(data=output_video_path)


        except Exception as e:
            st.write(e)
            st.error('Sorry! Unexpected error occurred please re-generate the story')


        st.markdown("*Video was uploaded to Gallery 🤗*")
        st.session_state.upload = True
            
        # shutil.rmtree("dir_mp3")
        # shutil.rmtree("dir_mp4")
        shutil.rmtree("dir_png")

if __name__ == '__main__':
    main()
