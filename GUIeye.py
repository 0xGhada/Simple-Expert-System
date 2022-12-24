import tkinter as tk
from PIL import ImageTk, Image
import eyeDisease as rules
from experta import Fact
import tkinter.font as tkFont

# Function to declare the Rules and Search in it ()
def detectDisease():
    # Starting the engine
    expertSystem = rules.eyeDisease()
    expertSystem.reset()
    expertSystem.declare(Fact(itching=str(itching.get())))
    expertSystem.declare(Fact(blurring=str(blurring.get())))
    expertSystem.declare(Fact(redness = str(redness.get())))
    expertSystem.declare(Fact(night=str(night.get())))
    expertSystem.declare(Fact(mucus=str(mucus.get())))
    expertSystem.declare(Fact(tear=str(tear.get())))
    expertSystem.declare(Fact(yellowing=str(yellowing.get())))
    expertSystem.declare(Fact(headache=str(headache.get())))
    expertSystem.declare(Fact(cough=str(cough.get())))
    expertSystem.declare(Fact(pain=str(pain.get())))
    expertSystem.declare(Fact(overstrain=str(overstrain.get())))
    expertSystem.declare(Fact(sensitivity=str(sensitivity.get())))
    expertSystem.declare(Fact(rainbow=str(rainbow.get())))
    expertSystem.declare(Fact(double=str(double.get())))
    expertSystem.declare(Fact(sightedness=str(sightedness.get())))
    expertSystem.declare(Fact(sight=str(sight.get())))
    expertSystem.declare(Fact(nausea=str(nausea.get())))
    expertSystem.declare(Fact(dilated=str(dilated.get())))
    expertSystem.declare(Fact(eyelid=str(eyelid.get())))
    expertSystem.declare(Fact(redness=str(vision.get())))
    expertSystem.run()

    return expertSystem.diseases, expertSystem.description, expertSystem.photo

# the window that is responsible about  showing  eye disease
def openNewWindow():

    newWindow = tk.Toplevel()
    newWindow.title("Eye disease")
     # sets the geometry of toplevel
    newWindow.geometry("900x700")

    # A Label widget to show in toplevel
    tk.Label(newWindow, text ="Eye diseases",font=('Times',18,'bold')).pack()
    name, description, photo = detectDisease()
    if name == description == photo == '':
        name = 'Unfortunately, we could not find your eye diseases.'
        photo = r'.\photo\no.jpg'

    img = ImageTk.PhotoImage(Image.open(photo).resize((500, 300)))
    canvas = tk.Canvas(newWindow, width=1500, height=900)
    canvas.pack()
    canvas.create_image(500, 300, anchor=tk.CENTER, image=img)
    canvas.img = img
    # name diesease
    tk.Label(newWindow, text =str(name),font=('Times',14,'bold')).place(relx=0.5,
                       rely=0.7,
                       anchor='center')
    # description
    tk.Label(newWindow, text =str(description),font=('Times',11,'bold') ).place(relx=0.5,
                       rely=0.8,
                       anchor='center')

# the main window for selecting Symptoms
background = "#C6E2FF"
source = tk.Tk()
source.title("Eye Disease")
source.geometry("1500x900")
source.config(bg=background)
source.resizable(True, True)

#declare the variables that use in the selection button
itching = tk.IntVar()
blurring= tk.IntVar()
redness= tk.IntVar()
night= tk.IntVar()
mucus = tk.IntVar()
tear= tk.IntVar()
yellowing= tk.IntVar()
headache= tk.IntVar()
cough = tk.IntVar()
pain= tk.IntVar()
overstrain= tk.IntVar()
sensitivity= tk.IntVar()
rainbow = tk.IntVar()
double= tk.IntVar()
sightedness= tk.IntVar()
sight= tk.IntVar()
nausea = tk.IntVar()
dilated= tk.IntVar()
eyelid= tk.IntVar()
vision= tk.IntVar()



# declare fonts that use in Interface  
fontStyle = tkFont.Font(family="Helvetica", size=14, weight="bold")
l1 = tk.Label(source, text="Welcome to The Expert System ", width=40,
              fg='#DE2132', bg=background,  font=fontStyle)
l1.grid(row = 0, column = 1, pady = 0, padx=3 )

l1 = tk.Label(source, text="  For Diagnosing Eye Diseases", width=40,
              fg='#cd2731',    bg=background,  font=fontStyle)
l1.grid(row = 1, column = 1, pady = 0, padx=3 )

fontTipo = tkFont.Font(family="Helvetica", size=10,weight="bold")
tk.Label(source, text="Check the options", width=30, bg=background,
         font=("Helvetica", 10, "bold")).grid(row = 3, column = 1, pady = 0)


#--------------------------------------" Part  1 "---------------------------------------------------- 
#Q1 itching
tk.Label(source, text="Do you experience itching and burning on your eyes? ",
           width=45, bg=background, font=fontTipo).grid(row = 2, column = 0)

c1 = tk.Checkbutton(source, text = "No", variable= itching,  onvalue=0 ,bg= background)
c1.grid(row = 3, column = 0)
# c1.deselect()
c2= tk.Checkbutton(source, text = "Yes", variable = itching,
                   onvalue=1,
bg=background)
c2.grid(row = 4, column = 0)
# c2.deselect()
#Q2 blurring
tk.Label(source, text="Do you experience a blurring vision? ",
         width=40, bg=background, font=fontTipo).grid(row = 5, column = 0)

c3 = tk.Checkbutton(source, text = "No", variable= blurring,
                    onvalue=0,
                    bg= background)
c3.grid(row = 6, column = 0)

c4 = tk.Checkbutton(source, text = "Yes", variable = blurring,
                    onvalue=1,
                    bg=background)
c4.grid(row = 7, column = 0)

#Q3 redness
tk.Label(source, text="Do you experience redness in your eye color? ",
         width=40, bg=background, font=fontTipo).grid(row = 8, column = 0)

c5 = tk.Checkbutton(source, text = "No", variable= redness,
                    onvalue=0,   bg= background)
c5.grid(row = 9, column = 0)

c6 = tk.Checkbutton(source, text = "Yes", variable = redness,
                    onvalue=1,    bg=background)
c6.grid(row = 10, column = 0)


#Q4 night
tk.Label(source, text="Do you experience difficulty in seeing while driving at night? ",
         width=50, bg=background, font=fontTipo).grid(row = 11, column = 0)


c7 = tk.Checkbutton(source, text = "No", variable= night,
                    onvalue=0,
                    bg= background)
c7.grid(row = 12, column = 0)

c8 = tk.Checkbutton(source, text = "Yes", variable = night,
                    onvalue=1,
                    bg=background)
c8.grid(row = 13, column = 0)

#Q5 mucus
tk.Label(source, text="Do you experience a discharge of sticky mucus in your eyes? ",
         width=50, bg=background, font=fontTipo).grid(row = 14, column = 0)


c9= tk.Checkbutton(source, text = "No", variable= mucus,
                   onvalue=0,
bg= background)
c9.grid(row = 15, column = 0)

c10 = tk.Checkbutton(source, text = "Yes", variable = mucus,
                     onvalue=1,
bg=background)
c10.grid(row = 16, column = 0)


#Q6 tear
tk.Label(source, text="Do you have a tear in both eyes?",
         width=50, bg=background, font=fontTipo).grid(row = 17, column = 0)


c11= tk.Checkbutton(source, text = "No", variable= tear,
                    onvalue=0,
bg= background)
c11.grid(row = 18, column = 0)

c12 = tk.Checkbutton(source, text = "Yes", variable = tear,
                     onvalue=1,
bg=background)
c12.grid(row = 19, column = 0)

#Q7 yellowing
tk.Label(source, text="Do you experience yellowing of colors in your eyes?",
         width=50, bg=background, font=fontTipo).grid(row = 20, column = 0)


c13= tk.Checkbutton(source, text = "No", variable= yellowing,
                    onvalue=0,
bg= background)
c13.grid(row = 21, column = 0)

c14 = tk.Checkbutton(source, text = "Yes", variable = yellowing,
                     onvalue=1,
bg=background)
c14.grid(row = 22, column = 0)

#Q8 headache
tk.Label(source, text="Do you experience severe headache?",
         width=40, bg=background, font=fontTipo).grid(row = 23, column = 0)


c15= tk.Checkbutton(source, text = "No", variable= headache,
                    onvalue=0,
bg= background)
c15.grid(row =24, column = 0)

c16 = tk.Checkbutton(source, text = "Yes", variable = headache,
                     onvalue=1,
bg=background)
c16.grid(row = 25, column = 0)


#--------------------------------------" Part  2 "---------------------------------------------------- 

#Q9 cough
tk.Label(source, text="Do you experience cough, running nose and scratching throat?",
         width=50, bg=background, font=fontTipo).grid(row = 5, column = 1)


c17= tk.Checkbutton(source, text = "No", variable= cough,
                    onvalue=0, bg= background)
c17.grid(row = 6, column = 1)

c18 = tk.Checkbutton(source, text = "Yes", variable = cough,
                     onvalue=1,bg=background)
c18.grid(row = 7, column = 1)

#Q10 pain
tk.Label(source, text="Do you experience eye pain and swollen eyelid?",
         width=50, bg=background, font=fontTipo).grid(row = 8, column = 1)


c19= tk.Checkbutton(source, text = "No", variable= pain,
                    onvalue=0,   bg= background)
c19.grid(row = 9, column = 1)

c20 = tk.Checkbutton(source, text = "Yes", variable = pain,
                     onvalue=1,
                     bg=background)
c20.grid(row = 10, column = 1)


#Q11 overstrain
tk.Label(source, text="Does your eyes constantly overstrain you?",
         width=50, bg=background, font=fontTipo).grid(row = 11, column = 1)


c21= tk.Checkbutton(source, text = "No", variable= overstrain,
                    onvalue=0,
                    bg= background)
c21.grid(row = 12, column = 1)

c22 = tk.Checkbutton(source, text = "Yes", variable = overstrain,
                     onvalue=1,
                     bg=background)
c22.grid(row = 13, column =1)

#Q12 sensitivity
tk.Label(source, text="Do you experience an increased sensitivity to light?",
         width=50, bg=background, font=fontTipo).grid(row = 14, column = 1)


c23= tk.Checkbutton(source, text = "No", variable= sensitivity,
                    onvalue=0,
                    bg= background)
c23.grid(row = 15, column = 1)

c24 = tk.Checkbutton(source, text = "Yes", variable = sensitivity,
                     onvalue=1,
                     bg=background)
c24.grid(row = 16, column = 1)


#--------------------------------------" Part  3 "---------------------------------------------------- 


#Q13 rainbow
tk.Label(source, text="Do you see halos or rainbow colored cirle around light?",
         width=50, bg=background, font=fontTipo).grid(row = 2, column = 2)


c25= tk.Checkbutton(source, text = "No", variable= rainbow,
                    onvalue=0,
                    bg= background)
c25.grid(row = 3, column = 2)

c26 = tk.Checkbutton(source, text = "Yes", variable = rainbow,
                     onvalue=1,
                     bg=background)
c26.grid(row = 4, column = 2)

#Q14  double
tk.Label(source, text="Do you experience double vision in a single eye?",
         width=50, bg=background, font=fontTipo).grid(row = 5, column = 2)


c27= tk.Checkbutton(source, text = "No", variable= double,
                    onvalue=0,
                    bg= background)
c27.grid(row = 6, column = 2)

c28 = tk.Checkbutton(source, text = "Yes", variable = double,
                     onvalue=1,
                     bg=background)
c28.grid(row = 7, column = 2)

#Q15  sightedness
tk.Label(source, text="Do you experience near sightedness?",
         width=50, bg=background, font=fontTipo).grid(row = 8, column = 2)


c29= tk.Checkbutton(source, text = "No", variable= sightedness,
                    onvalue=0,
                    bg= background)
c29.grid(row = 9, column = 2)

c30 = tk.Checkbutton(source, text = "Yes", variable = sightedness,
                     onvalue=1,
                     bg=background)
c30.grid(row = 10, column = 2)


#Q16   sight
tk.Label(source, text="Do you experience sudden loss of sight?",
         width=50, bg=background, font=fontTipo).grid(row = 11, column = 2)


c31= tk.Checkbutton(source, text = "No", variable= sight,
                    onvalue=0,
                    bg= background)
c31.grid(row =12, column = 2)

c32 = tk.Checkbutton(source, text = "Yes", variable = sight,
                     onvalue=1,
                     bg=background)
c32.grid(row = 13, column = 2)

#Q17 nausea
tk.Label(source, text="Do you constant nausea and vomiting?",
         width=50, bg=background, font=fontTipo).grid(row = 14, column = 2)


c33= tk.Checkbutton(source, text = "No", variable= nausea,
                    onvalue=0,
                    bg= background)
c33.grid(row = 15, column = 2)

c34 = tk.Checkbutton(source, text = "Yes", variable = nausea,
                     onvalue=1,
                     bg=background)
c34.grid(row = 16, column = 2)

#Q18 dilated
tk.Label(source, text="Do you have a dilated pupil?",
         width=50, bg=background, font=fontTipo).grid(row = 17, column = 2)


c35= tk.Checkbutton(source, text = "No", variable= dilated,
                    onvalue=0,
                    bg= background)
c35.grid(row =18 , column = 2)

c36 = tk.Checkbutton(source, text = "Yes", variable = dilated,
                     onvalue=1,
                     bg=background)
c36.grid(row = 19, column = 2)

#Q19 eyelid
tk.Label(source, text="Do you need to partially close your eyelid to see clearly?",
         width=50, bg=background, font=fontTipo).grid(row = 20, column = 2)


c37= tk.Checkbutton(source, text = "No", variable= eyelid,
                    onvalue=0,
                    bg= background)
c37.grid(row =21 , column = 2)

c38 = tk.Checkbutton(source, text = "Yes", variable = eyelid,
                     onvalue=1,
                     bg=background)
c38.grid(row =22, column = 2)

#Q20 vision
tk.Label(source, text="Do you need experience a sudden decrease in vision?",
         width=50, bg=background, font=fontTipo).grid(row = 23, column = 2)


c39= tk.Checkbutton(source, text = "No", variable= vision,
                    onvalue=0,
                    bg= background)
c39.grid(row =24 , column = 2)

c40 = tk.Checkbutton(source, text = "Yes", variable = vision,
                     onvalue=1,
                     bg=background)
c40.grid(row = 25, column = 2)



#button of confirm

b1 = tk.Button(source, text="        Confirm        ", command=openNewWindow,
               bg='#05A0C8', fg='white', font=('Times', 14, 'bold'))
b1.grid(row=23, column=1, padx=10, pady=0)

#the main function that is responsible about run the windows of program
source.mainloop()