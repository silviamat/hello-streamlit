import streamlit as st

def intro():
    import streamlit as st

    st.write("# Camino, cami, caminito, caminin, camicao, ca, caminator, caminota, caminoska, caminibiris, chemin, path...")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        No me está gustando nada que estes triste, así que te he hecho esto.
        :gray[(Que también es uno de los resources del womENcourage pero eso es secreto, para ti solo soy monísima y la mejor novia del mundo)]

        **👈 Así que aquí tienes cositas para hacer** 
        """
    )

def mapping_demo():
    import streamlit as st
    import folium
    from streamlit_folium import st_folium
    import pandas as pd

    data = pd.DataFrame({
        'lon': [-3.7, 2, -6, -7, -3, -122, -118, -105],
        'lat': [40.4, 48, 42, 36.8, 36.9, 37, 34, 40],
        'name': ['Madrid', 'Paris', 'Leon', 'Huelva', 'Torrenueva', 'San Francisco', 'Los Angeles', 'Boulder'],
    }, dtype=str)

    st.title("Todos los sitios donde hemos estado juntas 🫶")

    # Create a Folium map centered on the world
    world_map = folium.Map(location=[0, 0], zoom_start=2)

    for i in range(0, len(data)):
        folium.Marker(
            location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
            popup=data.iloc[i]['name'],
        ).add_to(world_map)

    # Display the map in Streamlit
    st_folium(world_map, width=700, height=500)

def plotting_demo():
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt

    # Define the function to plot a heart shape
    def plot_heart():
        slider1 = st.slider('Slider 1', min_value=0, max_value=10, value=6)
        slider2 = st.slider('Slider 2', min_value=0, max_value=15, value=6)
        slider3 = st.slider('Slider 3', min_value=0, max_value=250, value=20)
        t = np.linspace(slider1, slider2, slider3)
        x = 16 * np.sin(t) ** 3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

        fig, ax = plt.subplots()
        ax.plot(x, y, color='red')
        ax.set_aspect('equal')
        ax.axis('off')

        st.pyplot(fig)

    # Streamlit app
    st.title("Dibujito que tienes que descubrir 🔎")
    st.write("Tienes que mover los sliders hasta descubrir el dibujo secreto (seguro que se te da bien secretista :)).")

    plot_heart()

def data_frame_demo():
    import streamlit as st
    from PIL import Image

    # Title of the app
    st.title("Image Display App")

    # Upload an image
    uploaded_file = "/Users/silvia/Desktop/Hackathon/streamlit/IMG_2366.JPG"

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Display the image
        st.image(image, caption='Uploaded Image.', use_column_width=True)


page_names_to_funcs = {
    "Intro 📍": intro,
    "Dibujito 🖼️": plotting_demo,
    "Mapita 🗺️": mapping_demo,
    "Un besito 💋": data_frame_demo
}

demo_name = st.sidebar.selectbox("Elige :)", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
