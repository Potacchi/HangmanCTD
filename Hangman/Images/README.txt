Please put your images into this folder.

*The only image types that tkinter supports are GIF, PGM, PPM, and PNG.
Do NOT use JPG or JPEG.

**Guidelines for importing images:
# Ensure that image variable called is global
global var_name
var_name = PhotoImage(file="Images/filename.filetype")

# Put the image in a label
labelname = tk.label(root, image = var_name)

# Place the image into the tkinter window
labelname.place(x = 0-800, y = 0-800, anchor = 'center')
# Note that the tkinter window is 800x800; Just standardise anchor to be center
