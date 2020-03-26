from autoplay import play
import os
cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
print("cwd",cwd)
print("dirp",dir_path)

play()
