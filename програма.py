#import Tkinter as tk # Python 2
import tkinter as tk # Python 3
root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = tk.PhotoImage(file='1.png')
label = tk.Label(root, image=root.image, bg='white')
#root.overrideredirect(True)#Ховає верзн
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True) #Закріплює в 1 місці
root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()
