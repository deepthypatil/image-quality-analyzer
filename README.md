# Image Quality Analyzer
An AI-powered image quality analyzer built with **Python**, **OpenCV**, and **machine learning**.  
The system extracts five key image quality metrics:  
- Brightness  
- Contrast  
- Noise  
- Resolution  
- Blurriness  

It uses a trained **RandomForest Classifier** to predict whether an image is of **good** or **bad** quality.  
The model is deployed with **Streamlit** for interactive use.  

## Features  
- Automatic feature extraction from images  
- Machine learning–based quality prediction  
- User-friendly web interface with Streamlit  

## Tech Stack  
- Python  
- OpenCV  
- scikit-learn  
- Streamlit  

## How to Run  
```bash
pip install -r requirements.txt
streamlit run app.py
