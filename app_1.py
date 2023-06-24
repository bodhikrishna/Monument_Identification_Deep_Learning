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

import numpy as np
from keras.models import load_model

model = load_model("saved_trained_model.h5")

st.set_page_config(
    page_title = 'Image feature prediction'
)
st.header("WHAT'S THAT MONUMENT!?")
from PIL import Image

st.title("WEB APPLICATION")



