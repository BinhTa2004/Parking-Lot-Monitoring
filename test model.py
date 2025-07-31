import cv2
import os
from glob import glob
from ultralytics import solutions

# --- CONFIG ---
IMAGE_FOLDER = "data_test_models/UFPR05"
MODEL_PATH = "models/best.pt"
SLOT_JSON = "slots/UFPR05.json"
FPS = 3  # ảnh/giây

# --- Load model parking ---
parkingmanager = solutions.ParkingManagement(
    model=MODEL_PATH,
    json_file=SLOT_JSON
)

# --- Load Image List ---
image_paths = sorted(glob(os.path.join(IMAGE_FOLDER, "*.jpg")))

# --- Display each image continuously ---
for img_path in image_paths:
    img = cv2.imread(img_path)
    if img is None:
        continue

    # Predicting occupancy slot
    results = parkingmanager(img)

    # Image Show
    cv2.imshow("Smart Parking Lot", results.plot_im)
    if cv2.waitKey(int(1000 / FPS)) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
