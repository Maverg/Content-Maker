import os
import shutil
from moviepy.editor import *
from pytube import YouTube
import random
from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx import fadein, fadeout

def extract_frames(video_file, frames_folder, music_file):
    # Load the video
    video = VideoFileClip(video_file)

    # Create the frames folder if it doesn't exist
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)

    # Randomly select 6 timestamps within the duration of the video
    duration = video.duration
    random_timestamps = [random.uniform(0, duration) for _ in range(5)]

    # Extract frames at the selected timestamps
    for i, timestamp in enumerate(random_timestamps):
        frame = video.get_frame(timestamp)
        frame_path = os.path.join(frames_folder, f"frame_{i}.jpg")  # Save each frame as a jpg file
        imageio.imwrite(frame_path, frame)  # Write the frame to disk
    
    return frames_folder




def create_video(frames_folder, music_file, output_video):
    # Load the frames
    frame_files = sorted([os.path.join(frames_folder, f) for f in os.listdir(frames_folder) if not f.startswith('.')])

    # Initialize a list to hold video clips for each frame
    clips = []

    # Create a video clip for each frame with fade in and out effects
    for frame_file in frame_files:
        frame_clip = ImageClip(frame_file, duration=4.2)  # Each frame shows for 3 seconds
        frame_clip = frame_clip.fadein(1).fadeout(1)  # Apply fade in and out effects
        clips.append(frame_clip)

    # Concatenate all the frame clips
    final_clip = concatenate_videoclips(clips)


    # Load the entire audio clip
    music = AudioFileClip(music_file)


    # Extract the segment from 63 to 84 seconds
    #music_segment = music.subclip(63, 84)

    # Apply a 3-second fadeout effect to the music segment
    music = music.audio_fadein(1).audio_fadeout(3)

    # Set the audio
    final_clip = final_clip.set_audio(music)

    # Write the final video to the output file
    final_clip.write_videofile(output_video, codec="libx264", fps=24)




def main():
    # Input paths
    video_file = "/Users/maverick/Desktop/Content/Video/cursedframes.mp4"
    frames_folder = "/Users/maverick/Desktop/Content/Frames"  # Directory to store extracted frames
    music_file = "/Users/maverick/Desktop/Content/Song/audiosegment.mp3"

    # Extract frames from the video
    frames_folder = extract_frames(video_file, frames_folder, music_file)

    print("Frames have been extracted and saved in:", frames_folder)

    # Output video path
    output_video = "/Users/maverick/Desktop/Content/Final_Videos/video_output.mp4"

    # Create video from frames with background music
    create_video(frames_folder, music_file, output_video)

    print("Video has been created:", output_video)

    # Delete the frames folder
    shutil.rmtree(frames_folder)



if __name__ == "__main__":
    main()
