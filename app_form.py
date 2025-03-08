import streamlit as st

st.title("User Information Form")

form_values = {
    "name": None,
    "age": None,
    "height": None,
    "weight": None,
    "bmi": None,
    "gender": None,
}

with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["age"] = st.number_input("Enter your age: ", min_value=0, step=1)
    form_values["height"] = st.number_input("Enter your height (cm): ", min_value=0, step=1)
    form_values["weight"] = st.number_input("Enter your weight (kg): ", min_value=0, step=1)
    form_values["bmi"] = st.number_input("Enter your BMI: ", min_value=0, step=1)
    form_values["gender"] = st.selectbox("Select your gender: ", ["Male", "Female", "Other"])


    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
            st.success("Form submitted successfully")

