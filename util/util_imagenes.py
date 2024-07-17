from PIL import ImageTk, Image

def lee_imagen( path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))