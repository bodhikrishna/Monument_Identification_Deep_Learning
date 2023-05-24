import requests
import wikipedia
import streamlit as st
from PIL import Image
# import httpx
# from requests_toolbelt.multipart.encoder import MultipartEncoder

st.set_page_config(
    page_title = 'Image Feature Prediction',
    page_icon = '😇'
)
st.header("HERITAGE IDENTIFICATION OF MONUMENTS USING DEEP LEARNING")
from PIL import Image
# img = Image.open("Future_of_Artificial_Intelligence.gif")
#st.image(img, width=500)

# importing css file to add more css to existing frontend
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("![Alt Text](https://media.giphy.com/media/doXBzUFJRxpaUbuaqz/giphy.gif)")
# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("WEB APPLICATION")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays the select widget for the styles
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

# displays a button
if image:
    st.header("Showing Preview of the uploaded image below:")
    st.image([image],width=300)
    # files = {"file": image.getvalue()}
    # m = MultipartEncoder(
    #     fields={'file': ('filename', files, 'image/jpg')}
    #     )
    server_url="http://127.0.0.1:8000/monument"
    # r = httpx.post(server_url,
    #                   data=m,
    #                   timeout=8000)
    res = requests.post(url =server_url, files={"file": ("filename", image, "image/jpeg")}, verify=False)
    st.subheader("Prediction is:")
    # st.subheader(res.json())
    st.success(res.json().get("monument_type"))
    resultinter=res.json().get("monument_type")

    
    st.subheader("Description:")


    if resultinter=="hawa mahal":
        result= wikipedia.summary("Hawa Mahal",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="victoria memorial":
        result=wikipedia.summary("Victoria Memorial",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="alai_darwaza":
        result=wikipedia.summary("Alai Darwaza",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="alai_minar":
        # result=wikipedia.summary("Alai Minar",sentences=5,auto_suggest=False)
        st.caption("Alai Minar is an unfinished Minar located on the northern side of the Qutub Minar within the extended boundary of Quwwat-ul-Islam mosque. Its construction was undertaken by Alauddin Khilji. Alauddin Khilji wanted to erect a tower double the height of Qutub Minar. However, his death left it incomplete with its height reaching only up to 24.5 metres. Alauddin Khilji had doubled the area of Quwwat-ul-Islam mosque and had drawn inspiration from the Qutub Minar. He thought of making a similar new Minar complementing with its extended premises so that it is proportionate to the enlarged mosque in the same way as the Qutub Minar was to the original premises of the mosque.")
    elif resultinter=="Charar-E- Sharif":
        result=wikipedia.summary("Charar-i-Sharief",sentences=5,auto_suggest=True)
        st.caption(result)
    elif resultinter=="India gate":
        result=wikipedia.summary("India Gate",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="iron_pillar":
        result=wikipedia.summary("Iron Pillar Delhi",sentences=5)
        st.caption(result)
    elif resultinter=="jamali_kamali_tomb":
        result=wikipedia.summary("Jamali Kamali Tomb",sentences=5)
        st.caption(result)
    elif resultinter=="lotus_temple":
        result=wikipedia.summary("Lotus Temple",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="mysore_palace":
        result=wikipedia.summary("Mysore Palace",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="Sun Temple Konark":
        result=wikipedia.summary("Konark Sun Temple",sentences=5,auto_suggest=False)
        st.caption(result)
    elif resultinter=="tanjavur temple":
        result=wikipedia.summary("Thanjavur Temple",sentences=5,auto_suggest=True)
        st.caption(result)


        
    else:
        result= wikipedia.summary(resultinter,sentences=5,auto_suggest=False)
        st.caption(result)



    

    