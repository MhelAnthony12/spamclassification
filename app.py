import streamlit as st
import joblib

model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("SMS Spam Classifier")
st.write("Enter a message and let the model predict if it's **spam** or **ham**:")

user_input = st.text_area("Type your message here:")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        vectorized_input = vectorizer.transform([user_input])   
        prediction = model.predict(vectorized_input)
        prediction_prob = model.predict_proba(vectorized_input).max()
    
        if prediction =="spam":
            st.error(f"The message is classified as **Spam** with a probability of {prediction_prob:.2%}.")
        else:
            st.success(f"The message is classified as **Ham** with a probability of {prediction_prob:.2%}.")


