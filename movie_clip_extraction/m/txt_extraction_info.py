def read_valid_lines(txt_fip):
    f = open(txt_fip,'r')
    lines = [l.replace('\n','') for l in f.readlines() if len(l)>0 and not l[0] == '#']
    f.close()
    return lines

def get_extraction_info(txt_fip):
    lines = read_valid_lines(txt_fip)
    split_lines = [l.split('\t') for l in lines]

    list_of_extraction_dicts_for_video = []
    for l in split_lines:
        try:
            extraction_dict = {}
            extraction_dict['start'] = l[0]
            extraction_dict['stop'] = l[1]
            if len(l)>2:
                topic = l[2]
            else:
                topic = ''
            extraction_dict['topic'] = topic
            list_of_extraction_dicts_for_video.append(extraction_dict)
        except:
            print 'Error: '+txt_fip, '\n'+' '.join(l)
    return list_of_extraction_dicts_for_video




