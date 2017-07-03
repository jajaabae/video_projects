#Needs: ffmpeg and Numpy
from m.settings import Settings
import os
import sys
import moviepy.config_defaults as movieconf
from moviepy.editor import *

def set_default_paths():
    my_ffmpeg_path = "C:\\Users\\Atrakaz\\Google Drive\\ContinousBackup\\ProgramsOnDrive\\WinPython-32bit-2.7.10.2\\ffmpeg-20160908-2793ebd-win32-shared\\bin\\"
    #movie_folder = r"K:\fileFolder\mine_media\mine_prosjekter\zouk\PY_convertering"
    #movie_folder = r"K:\fileFolder\mine_media\mine_prosjekter\zouk\Input_Petersburg\Instruksjon"
    settings = Settings(os.getcwd())
    movie_folder = settings.movie_folder
    os.chdir(movie_folder)
    return my_ffmpeg_path, movie_folder


def get_setings_and_defaults():
    movies_to_convert=["MVI_2806.MOV"]
    return movies_to_convert


def get_output_name(input_name, out_name_addition):
    output_name = input_name.split('.')
    output_name = '.'.join(output_name[0:-1])+out_name_addition
    return output_name

class stdout_silencer():
    def __init__(self):
        self.save_stdout = sys.stdout
    def silence_stdout(self):
        sys.stdout = open('trash.txt', 'w')
    def restore_stdout(self):
        sys.stdout = self.save_stdout

def notInFolder(output_name):
    is_in_folder = False
    for item in os.listdir(os.getcwd()):
        if item.split('.')[0] == output_name:
            is_in_folder = True
    return is_in_folder

def list_all_non_compressed_moviefiles(movie_file_endings, out_name_addition):
    non_compressed_moviefiles = None
    for item in os.listdir(os.getcwd()):
        #if os.path.isfile(item) and not out_name_addition in item and item[-4:] == movie_file_endings:
        ############# DANGER: #############
        if os.path.isfile(item) and not out_name_addition in item and item[-4:] == movie_file_endings and not notInFolder(get_output_name(item, out_name_addition)):
            if non_compressed_moviefiles == None:
                non_compressed_moviefiles = []
            non_compressed_moviefiles.append(item)
    return non_compressed_moviefiles

def main():
    [my_ffmpeg_path, movie_folder] = set_default_paths()

    movieconf.FFMPEG_BINARY = os.path.join(my_ffmpeg_path, "ffmpeg.exe")
    
    movies_to_convert = None
    out_name_addition = '_compressed'
    #movie_file_endings = '.MOV'
    #movie_file_endings = '.mpg'
    #movie_file_endings = '.MP4'
    movie_file_endings = '.mp4'

    movies_to_convert = list_all_non_compressed_moviefiles(movie_file_endings, out_name_addition)
    print (movies_to_convert)
    
    for input_name in movies_to_convert:
        print input_name
        video = VideoFileClip(input_name)
        output_name = get_output_name(input_name, out_name_addition)
        print output_name
        video.write_videofile(output_name+".mp4",fps=25)
        print


if __name__ == '__main__':
    main()

