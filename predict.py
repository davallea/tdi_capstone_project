import pickle
import re
import emoji
import streamlit as st

from help_functions import clean

model = pickle.load(open('gs_lr_pipe.pkl', 'rb'))

def app():
    st.title('Spanish dialect predictor')
    st.markdown('Are you ready to get your dialect identified?')
    
    text = st.text_input('What\'s up?')
    text = clean(text)
    pred = model.predict([text])[0]

    if pred == 0:
        st.write("Spain")
    else:
        st.write("Peru")


if __name__ == '__main__':
   app()


         