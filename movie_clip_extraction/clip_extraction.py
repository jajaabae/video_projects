import os

from m.folder_digger import folder_digger_fips
from m.settings import Settings

import m.file_name_manipulation
reload(m.file_name_manipulation)
import m.txt_extraction_info
reload(m.txt_extraction_info)
import m.video_extraction
reload(m.video_extraction)

from m.file_name_manipulation import * #get_core_name, file_name_and_path, replace_slashes
from m.txt_extraction_info import get_extraction_info
from m.video_extraction import extract_one_clip


def run_extractions(extract_path, orig_path, settings):
    fips = folder_digger_fips(orig_path)
    txt_ending = '.txt'
    txt_fips = [fip for fip in fips if fip[-len(txt_ending):]==txt_ending]

    extract_root = settings.extract_root
    previously_exported_fips = folder_digger_fips(extract_root)
    previously_exported_clips = [file_name_and_path(f)[0] for f in previously_exported_fips]
    
    for txt_fip in txt_fips:
        txt_file_name, file_path = file_name_and_path(txt_fip)
        video_file_name = get_video_name(txt_file_name)
        video_fip = file_path+'/'+video_file_name

        if os.path.isfile(video_fip):
            belonging_extractions = None
            #belonging_extractions = get_belonging_extractions( txt_file_name, core_name, extract_path)
            
            exported_extractions = extract_clips(settings, txt_fip, video_fip, extract_path, previously_exported_clips)
            #remove_old_extractions(belonging_extractions, exported_extractions, export_path)
        else:
            print 'Error: "' + video_file_name + '" does not exist.'


def extract_clips(settings, txt_fip, video_fip, extract_path, previously_exported_clips):
    list_of_extraction_dicts_for_video = get_extraction_info(txt_fip)
    video_file_name, p = file_name_and_path(video_fip)
    out_type = settings.out_type
    
    out_names = []
    for d in list_of_extraction_dicts_for_video:
        start = d['start']
        stop = d['stop']
        topic = d['topic']
        out_video_name = 'extr_'+video_file_name+'_'+start+'-'+stop
        if len(topic)>0:
            out_video_name += '_['+topic+']'
        out_video_name += out_type
        
        out_video_fip = extract_path+'/'+out_video_name

        if not out_video_name in previously_exported_clips:
            print 'out_video_name', out_video_name
            extract_one_clip(settings, video_fip, start, stop, out_video_fip)
        out_names.append(out_video_fip)
    return out_names


def main():
    main_dir = os.getcwd()
    settings = Settings(main_dir)
    extract_path = settings.extract_path
    orig_path = settings.orig_path
    
    run_extractions(extract_path, orig_path, settings)


if __name__ == '__main__':
    main()




