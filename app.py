import streamlit as st
import pickle as pkl
import numpy as np
import traceback
import locale
from datetime import datetime
from streamlit.components.v1 import html
import streamlit.components.v1 as components

locale.setlocale(locale.LC_ALL,'en_IN')

# model_type_mapping={'Linear':'linear_model.sav',
#    'Forest':'forest_model.sav','Best Forest':'best_forest_model.sav'}

# Set title of page
st.set_page_config(page_title="Company Profit Prediction")
st.title('Company Profit prediction model')
# Load the model
model_name='models\\best_forest_model.sav'
load_model=pkl.load(open(model_name,'br'))

def pred(x):
    # Prediction function
    x=np.array(x).reshape(1,-1)
    return load_model.predict(x)[0]
# Input fields
# [R&D Spend,Administration,Marketing]
# Output field: [Profit]
def main():
    try:
        # Input from the user
        print('Hello')
        rd=st.number_input('Enter Research & Development cost (R&D)[in lakhs]', min_value=100, step=1)
        administration=st.number_input('Enter Administration cost [in lakhs]', min_value=100, step=1)
        marketing=st.number_input('Enter Marketing cost[in lakhs]', min_value=100, step=1)
        if st.button('Predict Profit'):
            # Prediction
            inputs=[rd,administration,marketing]
            profit=pred(inputs)
            profit=locale.format_string("%.2f",profit,grouping=True)
            st.write('Profit estimation is: {}/-'.format(profit))
            print('Predicted')
    except:
        print('\n\n\n\nException occured but handled silently')
        traceback.print_exc()
        st.write("Enter all options correctly to show details")

def alert(message):
    # Used to make alert boxes in streamlit app
    # Still haven't used this in any program.

    # Define your javascript
    my_js = "alert('{}');".format(message)
    # Wrap the javascript as html code
    my_html = f"<script>{my_js}</script>"
    html(my_html)

if __name__=="__main__":
    main()