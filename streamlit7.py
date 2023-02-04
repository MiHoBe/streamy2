import streamlit as st

st.title("Streamlit Tutorial App")
st.write("This is a new app")
button1 = st.button("Click me")

if button1:
    st.write("This is some text")

# Checkbox (header für bessere Strukturierung)
st.header("Checkbox Section")

like = st.checkbox("Do you like?")
button2 = st.button("Submit")
if button2: 
    if like:
        st.write("Thanks. I like it too")
    else:
        st.write("Sorry")

# Radio Button
st.header("Radio Button")
animal = st.radio("What Animal ist your favorite?", ("Lions", "Tiger", "Bears"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lions":
        st.write("ROAR!")

        
# Selectbox (Dropdown)
st.header("Selectbox Section")

animal2 = st.selectbox("What Animal ist your favorite?", ("Lions", "Tiger", "Bears"))
button4 = st.button("Submit Animal 2")  # Titel muss anders sein als bei Radio Button
if button4:
    st.write(animal)
    if animal == "Lions":
        st.write("ROAR!")

# Multiselect
st.header("Multiselect")
options = st.multiselect("What animals do you like?", ["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")
if button5:
    st.write(options)

# Slider
st.header("Slider")
epochs_num = st.slider("How many Epochs?", 1,100, 10) # letzte Zahl nicht nötig, gibt Startwert an
if st.button("Slider Button"):
    st.write(epochs_num)

# Textinput
st.header("Textinput")
user_text = st.text_input("What's your favorite movie?", "Star Wars Ep")  # zweiter Wert nicht nötig, gibt Platzhalter an
if st.button("Text Button"):
    st.write(user_text)   # Wenn es Zahl sein soll: st.write(int(user_text))

# Zahleninput
user_num = st.number_input("What's your favorite number?")
if st.button("Numer Button"):
    st.write(user_num)


# Text-Area
txt = st.text_area('Text to analyse', '''Hier könnte ein längerer Text stehen, den ich gerade nicht habe''')


# Just ein Demo mit Platzhalter-Funktion
def run_sentiment_analysis(txt):
    st.write(f"Analysis done. {txt}") # F-String nur, um neuen Text im Textfeld auszugeben

st.write('Sentiment:', run_sentiment_analysis(txt))


