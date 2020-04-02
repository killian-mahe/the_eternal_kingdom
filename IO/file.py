# -*- coding: utf-8 -*-

class File(object):

    @staticmethod
    def read_as_array(file_name):
        assert type(file_name) is str

        # Read the file
        f = open(file_name, "r")
        txt = f.read()
        f.close()

        # Transform string into list of lists
        splited_txt = txt.splitlines()
        bg = list()
        for line in splited_txt :
            bg.append(list(line))
        
        return bg

    @staticmethod
    def read_frames(file_name):
        assert type(file_name) is str

        f = open(file_name, "r")
        txt = f.read()
        f.close

        animation = list()

        frames = txt.split("frame\n")
        
        for frame in frames:
            animation.append(frame.split("\n"))

        return animation

    pass