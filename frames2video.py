import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip


frame_width = 1440
frame_height = 1080
fps = 30

output_video_path = 'badapple_edition.mp4'
frames_folder = os.path.dirname(os.path.dirname(__file__)) + "/badapple/wframes"

out = cv2.VideoWriter(output_video_path, cv2.VideoWriter.fourcc(*'mp4v'), 
                      fps, (frame_width, frame_height))

for frame_name in os.listdir(frames_folder):  # sorted(os.listdir(frames_folder), key=lambda x: int(x.split('_')[1][:-4])):
    frame_path = os.path.join(frames_folder, frame_name)
    frame = cv2.imread(frame_path)
    out.write(frame)
    # print(i)

out.release()
cv2.destroyAllWindows()

print('adding audio')
video = VideoFileClip("badapple_edition.mp4")
audio = AudioFileClip("【東方】Bad Apple!! ＰＶ【影絵】 (256  kbps).mp3")

video = video.set_audio(audio)
video.write_videofile("sound_output.mp4", codec="libx264")
