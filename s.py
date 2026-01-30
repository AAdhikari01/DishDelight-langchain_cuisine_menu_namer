import streamlit as st
import langchain_helper

# Page title
st.markdown("<h1 style='color:orange; text-align:center;'>🍽️ Restaurant Name Generator</h1>", unsafe_allow_html=True)
st.write("---")  # horizontal separator

# Sidebar cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a cuisine 🌍", 
    (
        "Chinese","Japanese","Korean","Thai","Vietnamese","Indian","Nepali",
        "Malaysian","Indonesian","Filipino","Italian","French","Spanish","Greek",
        "Moroccan","Persian","Israeli","Ethiopian","Nigerian","South African",
        "Tunisian","American","Mexican","Brazilian","Argentinian","Peruvian",
        "Caribbean","Asian Fusion","Italian-American","Modern European",
        "Vegan / Plant-based","Street Food / Casual"
    )
)

if cuisine:
    # Get restaurant name, meaning, and menu
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    
    # Restaurant name
    st.markdown(f"<h2 style='color:orange;'>🏷️ {response['restaurant_name']}</h2>", unsafe_allow_html=True)
    
    # Meaning
    st.markdown("<h3 style='color:orange;'>💡 Meaning</h3>", unsafe_allow_html=True)
    st.info(response['meaning'])  # info box for neat look
    
    # Menu items
    st.markdown("<h3 style='color:orange;'>🍴 Menu Items</h3>", unsafe_allow_html=True)
    for item in response['menu_items']:
        st.markdown(f"• {item}")  # bullet points
    
    # Optional: add some spacing at the bottom
    st.write("\n\n")
