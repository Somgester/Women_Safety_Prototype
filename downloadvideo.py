# import pafy 
  
# url = "https://www.youtube.com/watch?v=eACohWVwTOc"
# video = pafy.new(url) 
  
# streams = video.streams 
# for i in streams: 
#     print(i) 
      
# # get best resolution regardless of format 
# best = video.getbest() 
  
# print(best.resolution, best.extension) 
  
# # Download the video 
# best.download() 

# import yt_dlp as youtube_dl

# def download_video(url, folder_name='videos', filename='video16.mp4'):
#     # Create the output directory if it doesn't exist
#     import os
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
    
#     # Construct the full path for the downloaded video
#     output_path = os.path.join(folder_name, filename)
    
#     # Download the video
#     ydl_opts = {
#         'outtmpl': output_path,
#         'format': 'best',
#     }
    
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
    
#     print(f"Video downloaded to {output_path}")
# take input from user
# download_video('https://www.youtube.com/watch?v=5kAnh6smxLg')



import yt_dlp as youtube_dl
import os

def download_video(url, folder_name='NonHarassmentVideo', filename='extracted_segment.mp4'):

    # Create the output directory if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Construct the full path for the downloaded video
    output_path = os.path.join(folder_name, filename)
    
    # Download the video
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print(f"Video downloaded to {output_path}")

# Example usage
download_video('https://youtu.be/HaKBtnQMdBc?si=brt8onVquox75DRA')
