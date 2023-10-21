import streamlit as st

from utils.load_boilerplate import setup_page_config
from utils.fetch_markdown import render_markdown
from utils.carrousel import carrousel_build

setup_page_config()

# content
st.title("History of attacks")


# image slide
carroussel_paths = [
    'static/history/types_of_powerplants.png',
    'static/history/planttype_hist.png',
    'static/history/powerplants_geodata2019.png',
    'static/history/uranium_periodic_table.png',
    'static/history/nuclear_fuel_lifecycle.png',
    'static/history/nuclear_energy_efficiency.png'
]

hist_data = render_markdown('static/history/history.md')

st.markdown(hist_data[:2271], unsafe_allow_html=True)

st.image("static/history/natanz_satelite_img.png")

st.markdown(hist_data[2271:6655])

st.image("static/history/windows_sc_arrow.png")

st.markdown(hist_data[6655:7404])

st.image("static/history/siemens_plcs.png")

st.markdown(hist_data[7404:7910])

st.image("static/history/centrifuge_schematic.png")

st.markdown(hist_data[7910:12275])

st.image("static/history/west_ukraine_bo.png")

st.markdown(hist_data[12275:])

st.subheader("Further references:")

st.video('https://www.youtube.com/watch?v=9DCwyuH29SI')

carrousel_build(carroussel_paths, 'hist_demo_path')
