#GUI
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from time import strftime

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
            
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (HomePage, attack_detector, about_us, contact_us):

                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):

        fg = 'white'
        bg =  '#3c3c3b'#'#4b4646'
        bar_bg =  '#38AEE6'
        top_bar_bg = '#ECEBEB' 

        tk.Frame.__init__(self, parent, bg = bg, highlightbackground = bg)

        photo = PhotoImage(file = r"home_black.png")
        photo = photo.subsample(1, 1)

        label = Label(image=photo)
        label.image = photo # keep a reference!
                    
        title_bg = ttk.Label(self, text = '                        ', font = LARGEFONT, width = 200)
        title_bg.config(background = top_bar_bg)
        title_bg.place(relx = 0, rely = 0)


        photo4 = PhotoImage(file = r"home_active.png")
        photo4 = photo4.subsample(1, 1)

        label4 = Label(image=photo4)
        label4.image = photo4

        button4 = tk.Button(self, text ="Home", image = photo4, command = lambda : None, compound = TOP,
                            cursor = 'hand2')
        button4.place(relx = 0.20, rely = 0)
        button4.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

        photo1 = PhotoImage(file = r"aboutus_final.png")
        photo1 = photo1.subsample(1, 1)

        label1 = Label(image=photo1)
        label1.image = photo1 # keep a reference!

        button1 = tk.Button(self, text ="  about us", image = photo1, command = lambda : controller.show_frame(about_us),
                         compound = TOP, cursor = 'hand2')
        button1.place(relx = 0.40, rely = 0.0)
        button1.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

       
        photo2 = PhotoImage(file = r"contactus_final.png")
        photo2 = photo2.subsample(1, 1)

        label2 = Label(image=photo2)
        label2.image = photo2 # keep a reference!

        button2 = tk.Button(self, text ="  contact us", image = photo2, command = lambda : controller.show_frame(contact_us),
                            compound = TOP, cursor = 'hand2')
        button2.place(relx = 0.60, rely = 0.0)
        button2.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        
        photo3 = PhotoImage(file = r"attackdetector_final.png")
        photo3 = photo3.subsample(1, 1)

        label3 = Label(image=photo3)
        label3.image = photo3 # keep a reference!
        
        button3 = tk.Button(self, text ="  attack detector", image = photo3, command = lambda : controller.show_frame(attack_detector),
                            compound = TOP, cursor = 'hand2')
        button3.place(relx = 0.80, rely = 0.0)
        button3.config(bg = top_bar_bg, activebackground = 'white', bd = 0)

        lo1 = tk.Label(self, text = "Denial of Service(DoS) attack detection system")
        lo2 = tk.Label(self, text = "What is a Denial of Service(DoS) attack?")
        lo3 = tk.Label(self, text = "--> Denial of service is a type of cyber attack that is a topic of great concern today.")
        lo4 = tk.Label(self, text = "--> When the Denial of service attack occurs, the system becomes inaccessible to its legitimate users.")
        lo5 = tk.Label(self, text = "--> The attack is successfully achieved by directing the traffic to the target server.")
        lo6 = tk.Label(self, text = "--> The attacker sends a lot of requests to the server that it cannot handle which makes the system inaccessible to its users.")
        lo7 = tk.Label(self, text = "--> These attacks are dangerous for organizations because they can cause huge financial as well as reputational losses.")
        
        relx = 0.15
    
        lo1.place(relx = relx, rely = 0.30)
        lo2.place(relx = relx, rely = 0.38)
        lo3.place(relx = relx, rely = 0.44)
        lo4.place(relx = relx, rely = 0.49)
        lo5.place(relx = relx, rely = 0.54)
        lo6.place(relx = relx, rely = 0.59)
        lo7.place(relx = relx, rely = 0.64)

        
        lo1.config(bg = bg, fg = fg, font = ("segoe ui", 25))
        lo2.config(bg = bg, fg = fg, font = ("segoe ui", 20))
        lo3.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo4.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo5.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo6.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo7.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        
		

class attack_detector(tk.Frame):

    def __init__(self, parent, controller):

        #but_bg="70%, #576064, #dddedd, 30%"
        but_bg = '#576064'
        but_font = 'times new roman'
        bfont_size = 10
        
        fg = 'white'
        bg = '#3c3c3b'
        bar_bg =  '#38AEE6'
        top_bar_bg = '#ECEBEB' 

        tk.Frame.__init__(self, parent, bg = bg, highlightbackground = bg)

        photo = PhotoImage(file = r"home_black.png")
        photo = photo.subsample(1, 1)

        label = Label(image=photo)
        label.image = photo # keep a reference!
                    
        title_bg = ttk.Label(self, text = '                        ', font = LARGEFONT, width = 200)
        title_bg.config(background = top_bar_bg)
        title_bg.place(relx = 0, rely = 0)


        photo4 = PhotoImage(file = r"home_final.png")
        photo4 = photo4.subsample(1, 1)

        label4 = Label(image=photo4)
        label4.image = photo4

        button4 = tk.Button(self, text ="Home", image = photo4, command = lambda : controller.show_frame(HomePage), compound = TOP,
                            cursor = 'hand2')
        button4.place(relx = 0.20, rely = 0.0)
        button4.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

        photo1 = PhotoImage(file = r"aboutus_final.png")
        photo1 = photo1.subsample(1, 1)

        label1 = Label(image=photo1)
        label1.image = photo1 # keep a reference!

        button1 = tk.Button(self, text ="  about us", image = photo1, command = lambda : controller.show_frame(about_us),
                         compound = TOP, cursor = 'hand2')
        button1.place(relx = 0.40, rely = 0.0)
        button1.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

       
        photo2 = PhotoImage(file = r"contactus_final.png")
        photo2 = photo2.subsample(1, 1)

        label2 = Label(image=photo2)
        label2.image = photo2 # keep a reference!

        button2 = tk.Button(self, text ="  contact us", image = photo2, command = lambda : controller.show_frame(contact_us),
                            compound = TOP, cursor = 'hand2')
        button2.place(relx = 0.60, rely = 0.0)
        button2.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        
        photo3 = PhotoImage(file = r"attackdetector_active.png")
        photo3 = photo3.subsample(1, 1)

        label3 = Label(image=photo3)
        label3.image = photo3 # keep a reference!
        
        button3 = tk.Button(self, text ="  attack detector", image = photo3, command = lambda : controller.show_frame(attack_detector),
                            compound = TOP, cursor = 'hand2')
        button3.place(relx = 0.80, rely = 0.0)
        button3.config(bg = top_bar_bg, activebackground = 'white', bd = 0)


        lo1 = tk.Label(self, text = "Instructions:")
        lo2 = tk.Label(self, text = "You must have .csv file containing the details about the traffic.")
        lo3 = tk.Label(self, text = "Your .csv file must be in the same folder as the application.")
        lo4 = tk.Label(self, text = "The .csv file must contain following fields:")
        lo5 = tk.Label(self, text = "1. Source IPs")
        lo6 = tk.Label(self, text = "2. Time Duration")
        lo7 = tk.Label(self, text = "3. Destination IPs")
        lo8 = tk.Label(self, text = "4. Frame Length")
        lo9 = tk.Label(self, text = "5. Protocol type")


        relx = 0.15

        lo1.place(relx = relx, rely = 0.30)
        lo2.place(relx = relx, rely = 0.35)
        lo3.place(relx = relx, rely = 0.40)
        lo4.place(relx = relx, rely = 0.50)
        lo5.place(relx = relx, rely = 0.55)
        lo6.place(relx = relx, rely = 0.60)
        lo7.place(relx = relx, rely = 0.65)
        lo8.place(relx = relx, rely = 0.70)
        lo9.place(relx = relx, rely = 0.75)


        fg = "white"
        bg = "#3c3c3b"
        
        lo1.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo2.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo3.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo4.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo5.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo6.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo7.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo8.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo9.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        
        
        from pandas import read_csv
        import math
        import matplotlib.pyplot as plt
        import csv
        import pandas as pd


        #Input text box
        itext_box = tk.Text(self, height = 1, width = 40, font = ("segoe ui", 15))
        itext_box.place(relx = 0.60, rely = 0.20)
        itext_box.config(bg = "#c6c6c6", fg = 'black')


        def getcsv():
            text = itext_box.get(1.0, 500.0).strip()
            csvfile = text
            file = csvfile
            dataset = read_csv(file, low_memory = False)
            return dataset

        photo_i = PhotoImage(file = r"import.png")
        photo_i = photo_i.subsample(1, 1)
        label_i = Label(image=photo_i)
        label_i.image = photo_i

        #button for import csv
        buttoncsv = tk.Button(self, text ="   Import file  ", cursor = 'hand2', image = photo_i, compound = TOP,
                             command = getcsv, font = (but_font, bfont_size))
        buttoncsv.place(relx = 0.74, rely = 0.50)
        buttoncsv.config(bg = '#a8a8a8', fg = 'black', activebackground = 'white')

        
        
        prob_source_ip = []

        def findDistinct(field):
            distinct = []
            for i in field:
                if i in distinct:
                    continue
                distinct += [i]
            return(distinct)

        def findProbs_of_all_elem(field, array):
            probabilities = {}
            for i in array:
                p = (list(field).count(i))/len(field)
                probabilities[i] = p
            return probabilities

        def calculate_normalized_entropy(field):
            prob = findProbs_of_all_elem(field, findDistinct(field))
            entropy = []
            j = 0
            counter = 1
            for i in field:
                x = len(findDistinct(list(field)[:counter]))
                
                if x == 1:
                    entropy += [(-(prob[i] * math.log(prob[i]))) + j]
                    j = (-(prob[i] * math.log(prob[i])))
                else:
                    entropy += [(-(prob[i] * math.log(prob[i])))/math.log(x) + j]
                    j = (-(prob[i] * math.log(prob[i])))/math.log(x)
                counter += 1
            return entropy


        def find_attack():
            dataset = getcsv()
            destip_field = dataset.Source_ip
            frame_length_field = dataset.Frame_length
            my_data = dict(dataset)
            threshold_dip = 0.3
            
            threshold_fl = 0.3
            
            ans = "Woo! hoo! \nYou are Safe\n"
            attack_f = 0
            for i in range(len(destip_field)):
                if calculate_normalized_entropy(dataset.Source_ip)[i] < threshold_dip and calculate_normalized_entropy(dataset.Frame_length)[i] < threshold_fl:
                    if attack_f == 10:
                        ans = "Oops!!! \nYour system is under attack !!!\n"
                    attack_f += 1
                    my_data['Attack'][i] = "Attacked" 
                else:
                    my_data['Attack'][i] = "Benign"
                    
            df = pd.DataFrame.from_dict(my_data)
            df.to_csv("utsav3.csv")
            
            otext_box.insert(tk.END, ans)

        def classify_traffic():
            df2 = pd.read_csv("utsav3.csv")

            attacked = 0
            benign = 0
            for i in dict(df2)["Attack"]:
                if i == "Attacked":
                    attacked += 1
                else:
                    benign += 1
                    
            attack_data = [attacked, benign]
            labels = ["Suspicious", "Benign"]
            colors = ["#ff7f0e", "green"]
            fig, ax = plt.subplots(1)
            fig.set_facecolor('#79BEEB')
            ax.pie(attack_data, labels=labels , colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            ax.set_title("Traffic Classification", fontweight = 'bold')
            manager = plt.get_current_fig_manager()
            manager.window.state('normal')
            otext_box.insert(tk.END, plt.show())


        def visualize_traffic():
            dataset = getcsv()
            y1 = calculate_normalized_entropy(dataset.Source_ip)
            x1 = list(range(len(dataset)))
            y2 = calculate_normalized_entropy(dataset.Frame_length)
            fig, ax = plt.subplots(2)
            fig.set_facecolor('#79BEEB')
            ax[0].plot(x1, y1, color = 'green', linewidth = 3)
            #ax[0].set_facecolor(but_bg)
            ax[0].set_ylabel("Source IP Entropy")
            ax[0].set_title("Source IP Entropy vs number of requests", fontweight = 'bold')
            ax[1].plot(x1, y2, color = 'red', linewidth = 3)
            ax[1].set_title("Frame Length Entropy vs number of requests", fontweight = 'bold')
            #ax[1].set_facecolor(but_bg)
            ax[1].set_ylabel("Frame Length Entropy")
            ax[1].set_xlabel("number of requests")
            fig.tight_layout()
            manager = plt.get_current_fig_manager()
            manager.window.state('normal')
            otext_box.insert(tk.END, plt.show())
		
        #image for buttons
        photo_d = PhotoImage(file = r"detect.png")
        photo_d = photo_d.subsample(1, 1)
        label_d = Label(image=photo_d)
        label_d.image = photo_d

        photo_c = PhotoImage(file = r"classify.png")
        photo_c = photo_c.subsample(1, 1)
        label_c = Label(image=photo_c)
        label_c.image = photo_c

        photo_v = PhotoImage(file = r"visualize.png")
        photo_v = photo_v.subsample(1, 1)
        label_v = Label(image=photo_v)
        label_v.image = photo_v

        #Import a button for detection, classification and Visualization of the traffic
        button_d = tk.Button(self, text = "      Detect     ", image = photo_d, compound = TOP, command = find_attack)
        button_c = tk.Button(self, text = "    Classify    ", image = photo_c, compound = TOP, command = classify_traffic)
        button_v = tk.Button(self, text = "   Visualize    ", image = photo_v, compound = TOP, command = visualize_traffic)

        

        #instruction for input
        inst = tk.Label(self, text = "Enter the name of csv file to be examined :---> ")
        inst.place(relx = relx, rely = 0.20)
        inst.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        
        #Output text box
        otext_box = tk.Text(self, height = 3, width = 40, font = ("segoe ui", 15))
        otext_box.place(relx = 0.60, rely = 0.30)
        otext_box.config(bg = "#c6c6c6", fg = 'black')
        # #1f2122 


        #Place the button at desired position
        button_d.place(relx = 0.74, rely = 0.60)
        button_c.place(relx = 0.74, rely = 0.70)
        button_v.place(relx = 0.74, rely = 0.80)

        #Add color to buttons
        button_d.config(bg = '#a8a8a8', fg = 'black', activebackground = "white", cursor = 'hand2', font = (but_font, bfont_size))
        button_c.config(bg = '#a8a8a8', fg = 'black', activebackground = "white", cursor = 'hand2', font = (but_font, bfont_size))
        button_v.config(bg = '#a8a8a8', fg = 'black', activebackground = "white", cursor = 'hand2', font = (but_font, bfont_size))		


# second window frame page1
class about_us(tk.Frame):
    def __init__(self, parent, controller):
            
        fg = 'white'
        bg = '#3c3c3b'
        bar_bg =  '#38AEE6'
        top_bar_bg = '#ECEBEB' 

        tk.Frame.__init__(self, parent, bg = bg, highlightbackground = bg)

        photo = PhotoImage(file = r"home_black.png")
        photo = photo.subsample(1, 1)

        label = Label(image=photo)
        label.image = photo # keep a reference!
                    
        title_bg = ttk.Label(self, text = '                        ', font = LARGEFONT, width = 200)
        title_bg.config(background = top_bar_bg)
        title_bg.place(relx = 0, rely = 0)


        photo4 = PhotoImage(file = r"home_final.png")
        photo4 = photo4.subsample(1, 1)

        label4 = Label(image=photo4)
        label4.image = photo4

        button4 = tk.Button(self, text ="Home", image = photo4, command = lambda : controller.show_frame(HomePage), compound = TOP,
                            cursor = 'hand2')
        button4.place(relx = 0.20, rely = 0.0)
        button4.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

        photo1 = PhotoImage(file = r"aboutus_active.png")
        photo1 = photo1.subsample(1, 1)

        label1 = Label(image=photo1)
        label1.image = photo1 # keep a reference!

        button1 = tk.Button(self, text ="  about us", image = photo1, command = lambda : controller.show_frame(about_us),
                         compound = TOP, cursor = 'hand2')
        button1.place(relx = 0.40, rely = 0.0)
        button1.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

       
        photo2 = PhotoImage(file = r"contactus_final.png")
        photo2 = photo2.subsample(1, 1)

        label2 = Label(image=photo2)
        label2.image = photo2 # keep a reference!

        button2 = tk.Button(self, text ="  contact us", image = photo2, command = lambda : controller.show_frame(contact_us),
                            compound = TOP, cursor = 'hand2')
        button2.place(relx = 0.60, rely = 0.0)
        button2.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        
        photo3 = PhotoImage(file = r"attackdetector_final.png")
        photo3 = photo3.subsample(1, 1)

        label3 = Label(image=photo3)
        label3.image = photo3 # keep a reference!
        
        button3 = tk.Button(self, text ="  attack detector", image = photo3, command = lambda : controller.show_frame(attack_detector),
                            compound = TOP, cursor = 'hand2')
        button3.place(relx = 0.80, rely = 0.0)
        button3.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        
        lo1 = tk.Label(self, text = "We are students of Ahmedabad university.")
        lo2 = tk.Label(self, text = "This is our group project for the course ENR200: Design, Innovation, and Making.")
        lo2_1 = tk.Label(self, text = "We have worked together to design and create a Denial of services(DoS) attack detection system under the guidance")
        lo3 = tk.Label(self, text = "of professor Jaina Mehta.")
        lo4 = tk.Label(self, text = "There are 7 members in our team with different skill sets and we have put all our skills together to create this project.")
        lo5 = tk.Label(self, text = "Team")
        lo6 = tk.Label(self, text = "AU2040255	Utsav Vithlani	B.Tech CSE")
        lo7 = tk.Label(self, text = "AU2040226	Tushar Vaghela	B.Tech CSE")
        lo8 = tk.Label(self, text = "AU2040183	Nand Patel	B.Tech CSE")
        lo9 = tk.Label(self, text = "AU2040042	Aditi Thakar	B.Tech Chem")
        lo10 = tk.Label(self, text = "AU2040118	Jatin Parmar 	B.Tech CSE")
        lo11 = tk.Label(self, text = "AU2040199	Akshay Parmar	B.Tech CSE")
        lo12 = tk.Label(self, text = "AU2040237	Milap Chaudhari	B.Tech CSE")
        
        lo1.place(relx = 0.15, rely = 0.22)
        lo2.place(relx = 0.15, rely = 0.27)
        lo2_1.place(relx = 0.15, rely = 0.32) 
        lo3.place(relx = 0.15, rely = 0.37)
        lo4.place(relx = 0.15, rely = 0.42)
        lo5.place(relx = 0.15, rely = 0.50)
        lo6.place(relx = 0.15, rely = 0.55)
        lo7.place(relx = 0.15, rely = 0.60)
        lo8.place(relx = 0.15, rely = 0.65)
        lo9.place(relx = 0.15, rely = 0.70)
        lo10.place(relx = 0.15, rely = 0.75)
        lo11.place(relx = 0.15, rely = 0.80)
        lo12.place(relx = 0.15, rely = 0.85)

        fg = "white"
        bg = "#3c3c3b"
        
        lo1.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo2.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo2_1.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo3.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo4.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo5.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo6.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo7.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo8.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo9.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo10.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo11.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo12.config(bg = bg, fg = fg, font = ("segoe ui", 15))



class contact_us(tk.Frame):
    def __init__(self, parent, controller):

        fg = 'white'
        bg = '#3c3c3b'
        bar_bg =  '#38AEE6'
        top_bar_bg = '#ECEBEB' 

        tk.Frame.__init__(self, parent, bg = bg, highlightbackground = bg)

        photo = PhotoImage(file = r"home_black.png")
        photo = photo.subsample(1, 1)

        label = Label(image=photo)
        label.image = photo # keep a reference!
                    
        title_bg = ttk.Label(self, text = '                        ', font = LARGEFONT, width = 200)
        title_bg.config(background = top_bar_bg)
        title_bg.place(relx = 0, rely = 0)


        photo4 = PhotoImage(file = r"home_final.png")
        photo4 = photo4.subsample(1, 1)

        label4 = Label(image=photo4)
        label4.image = photo4

        button4 = tk.Button(self, text ="Home", image = photo4, command = lambda : controller.show_frame(HomePage), compound = TOP,
                            cursor = 'hand2')
        button4.place(relx = 0.20, rely = 0.0)
        button4.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

        photo1 = PhotoImage(file = r"aboutus_final.png")
        photo1 = photo1.subsample(1, 1)

        label1 = Label(image=photo1)
        label1.image = photo1 # keep a reference!

        button1 = tk.Button(self, text ="  about us", image = photo1, command = lambda : controller.show_frame(about_us),
                         compound = TOP, cursor = 'hand2')
        button1.place(relx = 0.40, rely = 0.0)
        button1.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        

       
        photo2 = PhotoImage(file = r"contactus_active.png")
        photo2 = photo2.subsample(1, 1)

        label2 = Label(image=photo2)
        label2.image = photo2 # keep a reference!

        button2 = tk.Button(self, text ="  contact us", image = photo2, command = lambda : controller.show_frame(contact_us),
                            compound = TOP, cursor = 'hand2')
        button2.place(relx = 0.60, rely = 0.0)
        button2.config(bg = top_bar_bg, activebackground = 'white', bd = 0)
        
        photo3 = PhotoImage(file = r"attackdetector_final.png")
        photo3 = photo3.subsample(1, 1)

        label3 = Label(image=photo3)
        label3.image = photo3 # keep a reference!
        
        button3 = tk.Button(self, text ="  attack detector", image = photo3, command = lambda : controller.show_frame(attack_detector),
                            compound = TOP, cursor = 'hand2')
        button3.place(relx = 0.80, rely = 0.0)
        button3.config(bg = top_bar_bg, activebackground = 'white', bd = 0)

        lo1 = tk.Label(self, text = "Contact us:")
        lo2 = tk.Label(self, text = "Akshay Parmar		akshay.p@ahduni.edu.in")
        lo3 = tk.Label(self, text = "Tushar Vaghela		tusharkumar.v@ahduni.edu.in")
        lo4 = tk.Label(self, text = "Nand Patel	         	nand.p@ahduni.edu.in")
        lo5 = tk.Label(self, text = "Aditi Thakar	   	thaker.b@ahduni.edu.in")
        lo6 = tk.Label(self, text = "Jatin Parmar 		jatin.p@ahduni.edu.in")
        lo7 = tk.Label(self, text = "Utsav Vithlani		utsav.v@ahduni.edu.in")
        lo8 = tk.Label(self, text = "Milap Chaudhari		milap.c@ahduni.edu.in")

        lo1.place(relx = 0.15, rely = 0.30)
        lo2.place(relx = 0.15, rely = 0.35)
        lo3.place(relx = 0.15, rely = 0.40)
        lo4.place(relx = 0.15, rely = 0.45)
        lo5.place(relx = 0.15, rely = 0.50)
        lo6.place(relx = 0.15, rely = 0.55)
        lo7.place(relx = 0.15, rely = 0.60)
        lo8.place(relx = 0.15, rely = 0.65)

        fg = "white"
        bg = "#3c3c3b"
        
        lo1.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo2.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo3.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo4.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo5.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo6.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo7.config(bg = bg, fg = fg, font = ("segoe ui", 15))
        lo8.config(bg = bg, fg = fg, font = ("segoe ui", 15))

# Driver Code
#app.title('DoS Attack Detector')
app = tkinterApp()
app.title('DoS Attack Detector')
app.state('normal')
app.mainloop()
