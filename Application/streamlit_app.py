import joblib
import streamlit as st
import spacy

model = joblib.load('C:\\Users\\Lenovo\\Desktop\\E-Commerce text classification\\Model\\E-Commercetextclassifier.joblib')
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    return " ".join(filtered_tokens)

def main():
    st.title('Ecommerce Text Classifier')

    user_input = st.text_area('Enter the text to classify:', 'Type your text here...')

    if st.button('Classify'):
        preprocessed_input = preprocess(user_input)
        prediction = model.predict([preprocessed_input])[0]
        display_prediction(prediction)

def display_prediction(prediction):
    class_mapping = {
        0: 'Household',
        1: 'Books',
        2: 'Electronics',
        3: 'Clothing & Accessories'
    }

    st.subheader('Prediction:')
    st.write('The text belongs to the category:', class_mapping[prediction])

if __name__ == '__main__':
    main()
