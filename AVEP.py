# Automate video editing using python

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip, AudioFileClip, afx, CompositeAudioClip

# cutting and merging videos
clip1 = VideoFileClip("one.mp4").subclip(10, 20) # secify the video to be cropped and duration of clipping.( here, 10sec-20sec)
clip2 = VideoFileClip("two.mp4").subclip(10, 20)
clip3 = VideoFileClip("one.mp4").subclip(20 ,30)

combined = concatenate_videoclips([clip1, clip2, clip3])
combined.write_videofile("merged.mp4")        # the merged video result


# Adding effects over videos
clip1 = VideoFileClip("one.mp4").subclip(10, 20)
clip2 = VideoFileClip("two.mp4").subclip(10, 20)
clip3 = VideoFileClip("one.mp4").subclip(20 ,30)
clip4 = VideoFileClip("one.mp4").subclip(10, 20).fx(vfx.colorx, 1.5)\
                                                .fx(vfx.lum_contrast, 0, 50, 128) # Ths will change color and contrast of clip 4
                                                
combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.write_videofile("efects.mp4")   

# To make transition effects
clip1 = VideoFileClip("one.mp4").subclip(10, 20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1) # fadein and fadeout effects
clip2 = VideoFileClip("two.mp4").subclip(10, 20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip3 = VideoFileClip("one.mp4").subclip(20 ,30).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip4 = VideoFileClip("one.mp4").subclip(10, 20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.write_videofile("transition.mp4")

# To add audio into video
clip1 = VideoFileClip("one.mp4").subclip(10, 20)
clip2 = VideoFileClip("two.mp4").subclip(10, 20)
clip3 = VideoFileClip("one.mp4").subclip(20 ,30)
clip4 = VideoFileClip("one.mp4").subclip(10, 20)

audio = AudioFileClip("Intro.mp4").fx(afx.audio_fadein, 1). fx(afx.volumex, 0.4)      # We don't need and mp3 file for audio, mp4 is also permitted

combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile("Added_Audio.mp4")
