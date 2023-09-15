import os
# import tkinter
import tkinter as ttk
from tkinter import filedialog
import camera_detection
import image_detection
import video_detection
# import ml

def open_camera():
    camera_detection.detect_human_in_camera()

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("file", "*.jpg *.png *.jpeg")])
    if file_path:
        image_detection.detect_human_in_image(file_path)
        # hacky asf way of showing images how do i do this pls help
        cmd = "open ~/fun/sih/rhtd/src/output_image.jpg"
        os.system(cmd)


def open_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    if file_path:
            # function in video_detection.py
            video_detection.detect_human_in_camera()
            # hacky asf way of showing videos ??? pls help
            # cmd = "mpv ~/fun/sih/rhtd/src/output_image.jpg"
            # os.system(cmd)

def image_classification():
    ml.get_image_info()


# ui bullshit
# image = Image.open("path_to_your_image.png")

# Create the main application window
root = ttk.Tk()
root.geometry("700x500")
root.title("Human Detection App")

# Create buttons for camera, image, and video
camera_button = ttk.Button(root, text="Use the Camera", command=open_camera)
camera_button.pack()
image_button = ttk.Button(root, text="Use a Image", command=open_image)
image_button.pack()
img_classic = ttk.Button(root, text="classify a image", command=image_classification)
img_classic.pack()
video_button = ttk.Button(root, text="Use a Video", command=open_video)
video_button.pack()
root.mainloop()
