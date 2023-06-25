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
   page_title = 'MonumentValley'
)
st.header("WHAT'S THAT MONUMENT!?")
from PIL import Image


# importing css file to add more css to existing frontend
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("![Alt Text](https://i.gifer.com/8Nsb.gif)")
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
    st.image([image],width=400)
  
    server_url="http://127.0.0.1:8000/monument"
    res = requests.post(url =server_url, files={"file": ("filename", image, "image/jpeg")}, verify=False)
    st.subheader("Prediction is:")
    st.success(res.json().get("monument_type"))
    resultinter=res.json().get("monument_type")

    
    st.subheader("Description:")
    if resultinter=="Christ the Redeemer":
        # result= wikipedia.summary("Christ the Redeemer(statue)",sentences=10,auto_suggest=False)
        st.caption("Christ The Redeemer (Portuguese: Cristo Redentor, standard Brazilian Portuguese: [kɾistu ʁedẽtoʁ]) is an Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil, created by French sculptor Paul Landowski and built by Brazilian engineer Heitor da Silva Costa, in collaboration with French engineer Albert Caquot. Romanian sculptor Gheorghe Leonida sculpted the face. Constructed between 1922 and 1931, the statue is 30 metres (98 ft) high, excluding its 8-metre (26 ft) pedestal. The arms stretch 28 metres (92 ft) wide.[1][2] It is made of reinforced concrete and soapstone.[3][4][5] Christ The Redeemer differs considerably from its original design, as the initial plan was a large Christ with a globe in one hand and a cross in the other. Although the project organisers originally accepted the design, it later changed to the statue of today, with the arms spread out wide. The statue weighs 635 metric tons 625 long, 700 short tons, and is located at the peak of the 700-metre (2,300 ft) Corcovado mountain in the Tijuca National Park overlooking the city of Rio de Janeiro. A symbol of Christianity around the world, the statue has also become a cultural icon of both Rio de Janeiro and Brazil and was voted one of the New Seven Wonders of the World.")
    elif resultinter=="Amr ibn al-Aas Mosque":
        result= wikipedia.summary("Amr ibn al-As Mosque",sentences=10,auto_suggest=False)
        st.caption(result)
    elif resultinter=="Sun Temple Konark":
        result= wikipedia.summary("Konark Sun Temple",sentences=10,auto_suggest=False)
        st.caption(result)
    else:
        
        result= wikipedia.summary(resultinter,sentences=10,auto_suggest=False)
        st.caption(result)


    if resultinter=="Victoria Memorial":
        st_player("https://www.youtube.com/watch?v=OleS4iyWOwk")
        
    elif resultinter=="Charar-e-Sharief":
        st_player("https://www.youtube.com/watch?v=_usTEB6Yg74")
        
    elif resultinter=="India Gate":
        st_player("https://www.youtube.com/watch?v=KEZlHqH0AYo")
  
    elif resultinter=="Sun Temple Konark":
        st_player("https://youtu.be/LiH78uM94KU")
  
    elif resultinter=="Taj Mahal":
        st_player("https://www.youtube.com/watch?v=pnBrFAT-H30")
        
  
    elif resultinter=="Roman Colosseum":
        st_player("https://www.youtube.com/watch?v=CVyuqIoB7qg")
    
    elif resultinter=="Qutub Minar":
        st_player("https://www.youtube.com/watch?v=nxQ9my2ur-I")
    
    elif resultinter=="Pyramid of Giza":
        st_player("https://www.youtube.com/watch?v=CEl6P5wo6ro")
    
    elif resultinter=="Machu Pichu":
        st_player("https://www.youtube.com/watch?v=_OAwXV25Fls")
        
 
    elif resultinter=="Great Wall of China":
        st_player("https://www.youtube.com/watch?v=BUFLNJBj-KY")
        
    elif resultinter=="Golden Temple":
        st_player("https://www.youtube.com/watch?v=ia-cTmRiTIc")
        
    elif resultinter=="Gateway of India":
        st_player("https://www.youtube.com/watch?v=dT_ApSvWB9c")
    
   
    elif resultinter=="Eiffel Tower":
        st_player("https://www.youtube.com/watch?v=RmnRF_lNDbA")
        
    elif resultinter=="Christ the Redeemer":
        st_player("https://www.youtube.com/watch?v=k_615AauSds")
        
    
  
    elif resultinter=="Charminar":
        st_player("https://www.youtube.com/watch?v=_Dp-ljvGChA")
        
   
    elif resultinter=="Burj Khalifa":
        st_player("https://www.youtube.com/watch?v=lflCmjW7RlI")
   
        
    elif resultinter=="Amr ibn al-Aas Mosque":
        st_player("https://www.youtube.com/watch?v=plaxqrzafoQ")
        

        
        
    # sound_file = BytesIO()
    # tts = gTTS(result, lang='en')
    # tts.write_to_fp(sound_file)
    
    # st.audio(sound_file)
        
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
        
    
    
    
    
    
        
    



    

    