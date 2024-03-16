import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
 name ="snake",
 options ={"build_exe": {"packages":["snake"],
                           "include_files":["maxresdefault.jpg", "toby_fox_-_megalovania_original_60999331.mp3",
                                            "967b98f78113900.png", "12-нояб._-18.02_.mp3"]}},

 executables = executables

 )