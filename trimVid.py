from moviepy.video.io.VideoFileClip import VideoFileClip

def crop_video(input_path, output_path, start_time, end_time):
    video = VideoFileClip(input_path)
    
    cropped_video = video.subclip(start_time, end_time)
    
    # writes file
    cropped_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    #closes the video to free up the memory
    video.close()
    cropped_video.close()

input_video_path = "E:\\SIH'2024\\Women\\videos\\video24.mp4"
output_video_path = "E:\\SIH'2024\\Women\\videos\\video241.mp4"
start_time = 00  # start time from which the video should be cropped
end_time = 25   # end time till which tume the video should be cropped

crop_video(input_video_path, output_video_path, start_time, end_time)