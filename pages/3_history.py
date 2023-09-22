import streamlit as st


st.set_page_config(
    page_title="Ironhack", 
    page_icon="☢️",
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items=None
    )


hide_streamlit_style = """
    <style>
    
    footer {
        visibility:hidden;
    }
    footer:after {
        content: 'Ironhack deliverable - Group 5 ®️';
        visibility: visible;
        display: block;
        position: relative;
        #background-color: red;
        padding: 5px;
        top: 2px;
    }
    </style>
"""
# Inject CSS with Markdown
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# home button
home_url = "https://ironhackdeliverable-group5.streamlit.app/"
st.markdown(f"""
<a href={home_url} target="_self"><button style="background-color:GreenYellow;">Home</button></a>
""", unsafe_allow_html=True)

# content
st.title("History of how it's been attacked in the past")

st.image('static/types_of_powerplants.png')

st.markdown("""A brief summary of some of the most relevant attacks to critical energy infrastructure. 
            Note, not all of these relate directly to nuclear-energy but to energy in general.

**Early Incidents (2000s)**:

    	In the early 2000s, cyberattacks on the energy sector were relatively rare, but incidents like 
        the 2000 "ILOVEYOU" virus highlighted vulnerabilities in computer systems.
        Possible Mitigations: Many attacks start with phishing emails. Training employees to recognize phishing 
        attempts, as seen in the "ILOVEYOU" virus incident, can prevent initial breaches.

**Stuxnet (2010)**:

    	Stuxnet, a highly sophisticated worm, targeted Iran's nuclear program but inadvertently spread to other countries. 
        It demonstrated the potential for state-sponsored cyberattacks on critical infrastructure, including energy facilities. 
        The birth of cyberweapons.
        - Possible Mitigations: Network segmentation involves dividing a network into isolated segments, limiting access to 
        critical systems. Air gapping physically disconnects critical systems from the internet, making it harder for malware 
        like Stuxnet to spread. Keeping software and systems up-to-date can help prevent vulnerabilities that malware exploits. 
        For instance, Stuxnet exploited unpatched Windows vulnerabilities.

**Ukraine Power Grid Attack (2015 and 2016)**:

    	In 2015 and 2016, Ukraine experienced two separate cyberattacks on its power grid. The attackers used malware to disrupt 
        power distribution, leaving hundreds of thousands of people without electricity. These attacks are often attributed to 
        Russian state-sponsored hackers.
        - Possible Mitigations: IDPS can detect and respond to suspicious activities. They could have helped identify and mitigate 
        the Ukraine power grid attacks and the Dragonfly group's activities.
        Having well-defined incident response plans is critical. Quick responses to incidents like the Ukraine power grid attacks 
        and the Colonial Pipeline ransomware attack can minimize damage.

**Dragonfly (2017)**:

    	The Dragonfly group, believed to have ties to Russia, targeted energy companies in the U.S. and Europe. They conducted 
        reconnaissance and gained access to critical systems, raising concerns about potential future attacks.

**TRISIS/Triton (2017)**:

    	In 2017, the TRISIS (or Triton) malware was discovered targeting a Saudi Arabian petrochemical plant. 
        It was designed to manipulate the plant's safety systems, posing significant risks to both personnel and the facility itself.
""")

st.subheader('Concentration of commissioned plants around the world')

st.image('static/powerplants_geodata2019.png')