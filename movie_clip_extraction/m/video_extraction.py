#Needs: ffmpeg.exe
import os
import moviepy.config_defaults as movieconf
from moviepy.editor import *
import moviepy.video.fx.all as vfx


def set_my_ffmpeg_path(settings):
    #my_ffmpeg_path = "C:\\Users\\Atrakaz\\Google Drive\\ContinousBackup\\ProgramsOnDrive\\WinPython-32bit-2.7.10.2\\ffmpeg-20160908-2793ebd-win32-shared\\bin\\"
    my_ffmpeg_path = settings.my_ffmpeg_path
    return my_ffmpeg_path


def extract_one_clip(settings, video_fip, start, stop, out_video_fip):
    my_ffmpeg_path = set_my_ffmpeg_path(settings)
    movieconf.FFMPEG_BINARY = os.path.join(my_ffmpeg_path, "ffmpeg.exe")

    video = VideoFileClip(video_fip)
    clip = video.subclip( time_string_to_seconds(start), time_string_to_seconds(stop) )
    if settings.fade:
        dur_fade_in = float(settings.fade_interval)
        dur_fade_out = float(settings.fade_interval)
        clip = fade_in_and_out_clip(clip, dur_fade_in, dur_fade_out)
    clip.write_videofile(out_video_fip, fps=25)


def time_string_to_seconds(time_string):
    time_value_list = time_string.split('.')
    if len(time_value_list)==1:
        time = float(time_value_list[0])
    elif len(time_value_list)==2:
        time = float(time_value_list[1])
        time += 60*float(time_value_list[0])
    elif len(time_value_list)==3:
        time = float(time_value_list[2])
        time += 60*float(time_value_list[1])
        time += 60*60*float(time_value_list[0])
    else:
        print 'Error: time convertion' #The program will crash after this print.
    return time


def fade_in_and_out_clip(clip, dur_in=1, dur_out=1):
    clip = fade_frame(clip, dur_in, dur_out)
    clip = fade_sound(clip, dur_in, dur_out)
    return clip
def fade_frame(clip, dur_in, dur_out):
    clip=clip.fx(vfx.fadein, duration=dur_in)
    clip=clip.fx(vfx.fadeout, duration=dur_out)
    return clip
def fade_sound(clip, dur_in, dur_out):
    clip=clip.fx(afx.audio_fadein, 1.0)
    clip=clip.fx(afx.audio_fadeout, 1.0)
    return clip

