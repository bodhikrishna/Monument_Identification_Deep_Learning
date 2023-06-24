import requests
import pandas as pd
import wikipedia
import streamlit as st
from PIL import Image
from geopy.geocoders import Nominatim
from gtts import gTTS
from io import BytesIO
from streamlit_player import st_player
import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
    page_title = 'Image feature prediction'
)
st.header("WHAT'S THAT MONUMENT!?")
from PIL import Image


# importing css file to add more css to existing frontend
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("![Alt Text](https://media.giphy.com/media/doXBzUFJRxpaUbuaqz/giphy.gif)")
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("WEB APPLICATION")

# displays a file uploader widget
image = st.file_uploader("Choose an image")
def get_map(loc):
        geolocator=Nominatim(user_agent="Bodhi Krishna")
        location=geolocator.geocode(loc)
        return location.address,location.latitude,location.longitude

# displays the select widget for the styles
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

# displays a button
if image:
    st.header("Showing Preview of the uploaded image below:")
    st.image([image],width=300)
  
    server_url="http://127.0.0.1:8000/monument"
    res = requests.post(url =server_url, files={"file": ("filename", image, "image/jpeg")}, verify=False)
    st.subheader("Prediction is:")
    st.success(res.json().get("monument_type"))
    resultinter=res.json().get("monument_type")

    
    st.subheader("Description:")


    if resultinter=="hawa mahal":
        result= wikipedia.summary("Hawa Mahal",sentences=10,auto_suggest=False)
        st.caption(result)
    elif resultinter=="victoria memorial":
        result=wikipedia.summary("Victoria Memorial",sentences=10,auto_suggest=False)
        st.caption(result)
    elif resultinter=="Charar-E- Sharif":
        result=wikipedia.summary("Charar-i-Sharief",sentences=10,auto_suggest=True)
        st.caption(result)
    elif resultinter=="India gate":
        result=wikipedia.summary("India Gate",sentences=10,auto_suggest=False)
        st.caption(result)
    elif resultinter=="mysore_palace":
        result=wikipedia.summary("Mysore Palace",sentences=10,auto_suggest=False)
        st.caption(result)
    elif resultinter=="Sun Temple Konark":
        result=wikipedia.summary("Konark Sun Temple",sentences=10,auto_suggest=False)
        st_player("https://youtu.be/LiH78uM94KU")
        st.caption(result)
    elif resultinter=="tanjavur temple":
        result=wikipedia.summary("Thanjavur Temple",sentences=10,auto_suggest=True)
        st.caption(result)


        
    else:
        result= wikipedia.summary(resultinter,sentences=10,auto_suggest=False)
        st.caption(result)
        
    sound_file = BytesIO()
    tts = gTTS(result, lang='en')
    tts.write_to_fp(sound_file)
    
    st.audio(sound_file)
        
    address,latitude,longitude=get_map(resultinter)
    pos=folium.Map(height=400,location=[latitude,longitude],zoom_start=17)
    folium.Marker(
        [latitude,longitude],popup=address,tooltip="Click Here to view address",icon=folium.Icon(color='red',icon='none')
    ).add_to(pos)
    # folium.TileLayer('Stamen Terrain').add_to(pos)
    # folium.TileLayer('Stamen Toner').add_to(pos)
    # folium.TileLayer('Stamen Water Color').add_to(pos)
    # folium.TileLayer('cartodbpositron').add_to(pos)
    # folium.TileLayer('cartodbdark_matter').add_to(pos)
    # folium.LayerControl().add_to(pos)
    
    st_data = st_folium(pos,width=1250)
        
    
    
    
    
    
        
    



    

    