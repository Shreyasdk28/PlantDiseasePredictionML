import streamlit as st
import tensorflow as tf
import numpy as np

#tensorflow model prediction
def model_prediction(test_image):
    model=tf.keras.models.load_model('trainedmodel.keras')
    #preprocessing
    # 1 in output is one batch but we need 32 batches
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    prediction=model.predict(input_arr)
    result_ind=np.argmax(prediction)
    return result_ind

#UI

#sidebar
st.sidebar.title("Dashboard")
app_mode=st.sidebar.selectbox("Select Page",["Home","About","Disease Detection"])

#homepage
if(app_mode=="Home"):
    st.header("PLANT DISEASE DETECTION SYSTEM")
    image_path="home_page.jpeg"
    st.image(image_path,use_container_width=True)#stretch it
    st.markdown("""
    ## Welcome to the Plant Disease Detection Platform! 🌱🩺

Our goal is to assist you in diagnosing plant diseases quickly and accurately. Simply upload a plant image, and our system will analyze it to detect any potential issues. Together, we can safeguard your crops and ensure healthier yields!

### How It Works
1. **Upload an Image:** Navigate to the **Disease Detection** page and upload an image of the affected plant.
2. **Processing:** The system will apply cutting-edge algorithms to identify any signs of disease.
3. **Results:** Get immediate results with actionable insights and recommendations.

### Why Choose Our Platform?
- **High Precision:** Powered by the latest machine learning models to ensure accurate disease detection.
- **Easy to Use:** Designed with a user-friendly interface for a smooth and intuitive experience.
- **Fast Results:** Get disease identification within seconds to make quick, informed decisions.

### Get Started
Click on the **Disease Detection** page in the sidebar to upload your plant image and begin your analysis!

### About Us
Learn more about my project, and my vision on the **About** page.
""")

elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
            ### About Dataset
            This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
            This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
            A new directory containing 33 test images is created later for prediction purpose.
            #### Content
            1. trained on 70295 images
            2. tested on 33 images
            3. validated on 17572 images
            """)
elif(app_mode=="Disease Detection"):
    st.header("Disease Detection")
    test_image=st.file_uploader("Choose an image")
    if(st.button("Show Image")):
        st.image(test_image,use_container_width=True)
    #predict button
    if(st.button("Predict")):
        st.write("Our Prediction")
        #st.balloons()
        #st.snow()
        with st.spinner("Please Hold on"):    
            result_ind=model_prediction(test_image)
            #defining class
            class_name=['Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy']
            
            st.success("Model is Predicting {}".format(class_name[result_ind]))
        
    