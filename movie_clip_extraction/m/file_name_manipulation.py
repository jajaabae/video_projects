def get_core_name(file_name):
    return file_name.split('.')[0]

def get_video_name(txt_file_name):
    return '.'.join( txt_file_name.split('.')[0:-1] )

def replace_slashes(path):
    return path.replace('\\','/')

def file_name_and_path(fip):
    fip = replace_slashes(fip)
    fip_list = fip.split('/')
    file_name = fip_list[-1]
    path = '/'.join(fip_list[0:-1])
    return file_name, path

def name_without_last_ending(txt_file_name):
    return '.'.join(txt_file_name.split('.')[0:-1])


def main_test():
    file_name = 'something.jpg.txt'
    print get_core_name(file_name)

    fip = r'S:\fileFolder_128GB\Media\Zouk\tmp.txt'
    print file_name_and_path(fip)

if __name__ == '__main__':
    main_test()
