# 🚗 License Plate Detection with YOLO + Streamlit  

This project demonstrates **real-time License Plate Detection** using a **YOLO model** and a simple **Streamlit web app**.  
It allows you to detect license plates from:  

- 📷 **Live Camera (Webcam)**  
- 🖼️ **Uploaded Images**  
- 💾 **Save Screenshots** with detection results  

---

## 📂 Project Structure  

```plaintext
📦 License-Plate-Detection
 ┣ 📜 app.py             # Streamlit app
 ┣ 📜 best.pt            # Trained YOLO weights
 ┣ 📜 requirements.txt   # Dependencies
 ┗ 📜 README.md          # Project documentation
```

---

## ⚡ Features  

- 🚀 YOLOv8 model for license plate detection  
- 🎥 Real-time detection via webcam  
- 🖼️ Image upload support for testing  
- 💾 Save detected frames as screenshots  
- ⚡ Easy to run with Streamlit  

---

## 🛠️ Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/YOUR-USERNAME/License-Plate-Detection.git
cd License-Plate-Detection
pip install -r requirements.txt
```

---

## 🚀 Run the App  

```bash
streamlit run app.py
```


---

## 📌 Requirements  

- 🐍 Python 3.8+  
- 📦 Streamlit  
- 📷 OpenCV  
- 🤖 Ultralytics (YOLO)  
- 🔢 Numpy  

Or install them manually:  

```bash
pip install streamlit opencv-python ultralytics numpy
```

---

## 🎯 Future Improvements  

- 📹 Add support for video file detection (mp4/avi)  
- 🔍 Integrate OCR to extract license plate numbers  
- ☁️ Deploy on Streamlit Cloud or Docker  

---

## 👩‍💻 Author  

Developed by **Menna Reda**  

---

