# -*- coding: utf-8 -*-

class File(object):

    @staticmethod
    def readAsArray(file_name):
        assert type(file_name) is str

        # Read the file
        f = open(file_name, "r")
        txt = f.read()
        f.close()

        # Transform string into list of lists
        splitedTxt = txt.splitlines()
        bg = list()
        for line in splitedTxt :
            bg.append(list(line))
        
        return bg

    @staticmethod
    def readFrames(file_name):
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