import streamlit as st
import pickle

st.title("Hello. Welcome to this Gait Analysis!")

dt = pickle.load(open('C:/Users/91636/OneDrive/Attachments/Desktop/PROJECT/pages/bagging_model (1).pkl','rb'))

def predict_neuro_disease(force1, force2):
    #X = d3[['forcel', 'forcer']]
    #y = d3[['target1', 'target2']].apply(lambda x: 'Yes' if x[0]==1 and x[1]==1 else 'No', axis=1)
    #dt = DecisionTreeClassifier()
    #bagging_classifier = BaggingClassifier(dt, n_estimators=10, random_state=42)
    #bagging_classifier.fit(X, y)
    if force1 > (15*weight) or force2 > (15*weight):
      return "The person has a neurological disease."
    else:
      user_input = [[force1, force2]]
      prediction = dt.predict(user_input)[0]
      if prediction == 'Yes':
          return "The person has a neurological disease."
      else:
          return "The person does not have a neurological disease."

page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://media.istockphoto.com/id/936401534/vector/stethoscope-on-blue-background.jpg?s=612x612&w=0&k=20&c=3GnEh8wJe1JP-BgIWZ94goP_7bj3n_x91hIRwF4Dd9Q= ");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}"""
    
st.markdown(page_bg_img, unsafe_allow_html=True)

weight = st.number_input("Enter your weight: ")
force1 = st.number_input("Enter the force exerted by left foot: ")
force2 = st.number_input("Enter the force exerted by right foot: ")


if st.button("Submit"):
    result = predict_neuro_disease(force1, force2)

    st.write(result)