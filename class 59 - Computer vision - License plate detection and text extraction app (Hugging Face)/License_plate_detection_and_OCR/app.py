import cv2
import gradio as gr
from ultralytics import YOLO
import easyocr

# Load model once
trained_model = YOLO("License_plate_detection_model_v2.pt")

# Load OCR once
ocr_reader = easyocr.Reader(['en'], gpu=False)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = "output.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    class_names = trained_model.names

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO inference
        results = trained_model.predict(frame, conf=0.5)[0]

        boxes = results.boxes.xyxy.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy().astype(int)

        for box, score, cls in zip(boxes, scores, classes):
            x1, y1, x2, y2 = map(int, box)

            # Crop plate safely
            plate_img = frame[max(0,y1):max(0,y2), max(0,x1):max(0,x2)]

            plate_text = "N/A"
            if plate_img.size > 0:
                ocr_result = ocr_reader.readtext(plate_img)
                if ocr_result:
                    plate_text = " ".join([res[1] for res in ocr_result])

            label = f"{plate_text} {score:.2f}"

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Label background
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame, (x1, y1 - h - 10), (x1 + w, y1), (0, 255, 0), -1)

            # Label text
            cv2.putText(frame, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        out.write(frame)

    cap.release()
    out.release()

    return output_path


demo = gr.Interface(
    fn=process_video,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.Video(label="Processed Video"),
    title="YOLO License Plate Detection + OCR"
)

if __name__ == "__main__":
    demo.launch()