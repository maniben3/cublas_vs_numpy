import ctypes

beach = "./a.out"
seashell = ctypes.cdll.LoadLibrary(beach)

seashell.main()
