# 🚗 Smart Parking Lot Monitoring
An intelligent system that detects and counts vehicles entering or exiting a parking lot using YOLOv8. Designed for real-time monitoring and traffic flow analysis in parking areas.

---

## 📌 Features
- 📦 Detects vehicles from camera/video using YOLOv8
- 🧮 Counts vehicles crossing a defined entry/exit line
- 🖼️ Draws bounding boxes and counts on live feed
- 📂 Works with video files or webcam (RTSP optional)

---

## 📡 Live Demo
<p align="center">
  <img src="demo/UFPR04.gif" width="600" alt="UFPR04">
  <br>
  <em> 📍 UFPR04
</p>

<p align="center">
  <img src="demo/UFPR05.gif" width="600" alt="UFPR05">
  <br>
  <em> 📍 UFPR05
</p>

---

## 📦Data
- The data is sourced from the UFPR Parking Lot Database by the Federal University of Paraná (Brazil), which includes multiple camera angles from various parking lots. Extracted frames were annotated using Roboflow, and the [Segment Anything Model (SAM) by Facebook](https://segment-anything.com/) was also utilized to accelerate and improve annotation accuracy, which was quickly leveraged through tools like [Ultralytics](https://docs.ultralytics.com/models/sam/)
- Data source: https://web.inf.ufpr.br/vri/databases/parking-lot-database/

---

## ⚙️ Setup Instructions
### Clone the Repository
```bash
git clone https://github.com/BinhTa2004/Parking-Lot-Monitoring.git
cd Parking-Lot-Monitoring
