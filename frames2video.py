import cv2
import os
from moviepy import ImageSequenceClip, AudioFileClip
from tqdm import tqdm


def make_video(frames_folder: str = "./wframes", 
               output_video_path: str = 'badapple_edition.mp4',
               fps: int = 30,
               audio_path: str | None = None
               ): 
    video_clip = ImageSequenceClip(frames_folder, fps=fps)
    if audio_path is not None:
        audio_clip = AudioFileClip(audio_path)
        if video_clip.duration > audio_clip.duration:
            video_clip = video_clip.subclipped(0, audio_clip.duration)
        else:
            audio_clip = audio_clip.subclipped(0, video_clip.duration)

        video_clip = video_clip.with_audio(audio_clip)

    video_clip.write_videofile(
        output_video_path,
        codec='libx264', 
        audio_codec='aac', 
        temp_audiofile='temp-audio.m4a',
        remove_temp=True
    )


if __name__ == "__main__":
    make_video('./wframes', audio_path="【東方】Bad Apple!! ＰＶ【影絵】 (256  kbps).mp3")
