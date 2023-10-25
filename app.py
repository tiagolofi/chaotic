
import streamlit as st
from drome import Drome
from PIL import Image

d = Drome()

col1, col2, col3 = st.columns(3)

with col1:

    creature = st.selectbox(d.get_names_creatures())

with col2:

    select_local = st.button('Choose Battle Local')

    if select_local:

        st.image(
            Image.open(
                d.location_random()
            )
        )        
