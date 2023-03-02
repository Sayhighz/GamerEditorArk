import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


# select type ini
def ini_selection():
    
    # change from old button
    buttonini.configure(text='PVP INI',
                        command=pvp_ini)
    buttonwater.configure(text='Pretty INI',
                          command=pretty_ini)
    buttonpretty.configure(text='FARM INI',
                           command=farm_ini)
    buttonpretty.place(x=205, y=70)
    # crate more button
    global defualtini
    defualtini = Button(
        MainWindow, text='Default INI', height=1, width=11, command=default_ini)
    defualtini.place(x=5, y=105)
    # create backbutton
    global backbtn
    backbtn = Button(MainWindow, text="Back", height=1,
                     width=11, fg='red', command=back_page)
    backbtn.place(x=205, y=105)
    # path of ini
    ini = '\Engine\Config\\'
    global path_ini
    path_ini = textBoxGamepath.get().replace('\\', '/')
    path_ini = textBoxGamepath.get() + ini

    global check_file
    check_file = path_ini + 'BaseDeviceProfiles.ini'


# Remove water surface
def delete_topwater():

    # path file
    deleteWater = '\ShooterGame\Content\PrimalEarth\Effects\Textures\Generic\\'
    path_water = textBoxGamepath.get().replace('\\', '/')
    path_water = textBoxGamepath.get() + deleteWater
    check_filewater = path_water + 'SoftEdgeGradient.uasset' and path_water + \
        'SoftEdgeGradient_Linear.uasset'

    # check old file if have will rename
    if os.path.exists(check_filewater):
        new_name1 = path_water + 'SoftEdgeGradient.uasset1'
        old_name1 = path_water + 'SoftEdgeGradient.uasset'
        os.rename(old_name1, new_name1)

        new_name2 = path_water + 'SoftEdgeGradient_Linear.uasset1'
        old_name2 = path_water + 'SoftEdgeGradient_Linear.uasset'
        os.rename(old_name2, new_name2)

        messagebox.showinfo("Clear Topwater", "Done!")

    else:
        messagebox.showerror("Clear Topwater", "It's clear now.")


# install pvp ini
def pvp_ini():

    mainfile = 'ini/PVP INI.ini'
    igfile = check_file
    # if have oldfile remove it
    if os.path.exists(check_file):
        os.remove(igfile)

    shutil.copyfile(mainfile, check_file)
    messagebox.showinfo("Change to pvp ini", "Done!")


# install pretty ini
def pretty_ini():

    mainfile = 'ini/Pretty INI.ini'
    igfile = check_file
    # if have oldfile remove it
    if os.path.exists(check_file):
        os.remove(igfile)

    shutil.copyfile(mainfile, check_file)
    messagebox.showinfo("Change to pretty ini", "Done!")


# install farm ini
def farm_ini():

    mainfile = 'ini/FARM INI.ini'
    igfile = check_file
    # if have oldfile remove it
    if os.path.exists(check_file):
        os.remove(igfile)

    shutil.copyfile(mainfile, check_file)
    messagebox.showinfo("Change to farm ini", "Done!")


# install default ini
def default_ini():

    mainfile = 'ini/Default INI.ini'
    igfile = check_file
    # if have oldfile remove it
    if os.path.exists(check_file):
        os.remove(igfile)

    shutil.copyfile(mainfile, check_file)
    messagebox.showinfo("Change to default ini", "Done!")


# make pretty map
def pretty_map():
    # path file
    prettymap = '\Engine\Content\EngineResources\\'
    path_map = textBoxGamepath.get().replace('\\', '/')
    path_map = textBoxGamepath.get() + prettymap
    check_filemap = path_map + 'DefaultTexture.uasset'
    # if have file will rename it
    if os.path.exists(check_filemap):
        new_name = path_map + 'DefaultTexture.uasset1'
        old_name = path_map + 'DefaultTexture.uasset'
        os.rename(old_name, new_name)
        messagebox.showinfo("PrettyMap", "Done!")

    else:
        messagebox.showerror("PrettyMap", "It's pretty now.")


# back first page
def back_page():
    buttonini.configure(
        text='INI', command=ini_selection)
    buttonwater.configure(
        text='ClearTopwater', command=delete_topwater)
    buttonpretty.configure(
        text='PrettyMap', command=pretty_map)
    buttonpretty.place(x=205, y=70)
    # delete default ini button whenclick
    defualtini.destroy()
    backbtn.destroy()


# resetbuttton
def reset():

    # path file map
    prettymap = '\Engine\Content\EngineResources\\'
    path_map = textBoxGamepath.get().replace('\\', '/')
    path_map = textBoxGamepath.get() + prettymap
    check_filemap = path_map + 'DefaultTexture.uasset1'

    # path file water
    deleteWater = '\ShooterGame\Content\PrimalEarth\Effects\Textures\Generic\\'
    path_water = textBoxGamepath.get().replace('\\', '/')
    path_water = textBoxGamepath.get() + deleteWater
    check_filewater = path_water + 'SoftEdgeGradient.uasset1' and path_water + \
        'SoftEdgeGradient_Linear.uasset1'

    # if have file will rename it
    if os.path.exists(check_filemap):
        new_namemap = path_map + 'DefaultTexture.uasset'
        old_namemap = path_map + 'DefaultTexture.uasset1'
        os.rename(old_namemap, new_namemap)

        messagebox.showinfo("PrettyMap", "Reset done!")

    else:
        messagebox.showerror("PrettyMap", "still default")

    if os.path.exists(check_filewater):
        new_namewater1 = path_water + 'SoftEdgeGradient.uasset'
        old_namewater1 = path_water + 'SoftEdgeGradient.uasset1'
        os.rename(old_namewater1, new_namewater1)

        new_namewater2 = path_water + 'SoftEdgeGradient_Linear.uasset'
        old_namewater2 = path_water + 'SoftEdgeGradient_Linear.uasset1'
        os.rename(old_namewater2, new_namewater2)

        messagebox.showinfo("Topwater", "Reset done!")

    else:
        messagebox.showerror("Topwater", "still default")


# write location user
def Savelocation():
    with open("gamelocation.txt", "w") as file:
        file.write(textBoxGamepath.get())


# getfilelocation
def getfilepath():

    global file_path, buttonini, buttonwater, buttonpretty, folder_check
    file_path = filedialog.askdirectory(initialdir="/", title="Select a file")
    folder_check = file_path + '/ShooterGame/'
    
    # check game path
    if os.path.exists(folder_check):
        textBoxGamepath.delete(0, END)
        textBoxGamepath.insert(0, (file_path))
        Savelocation()

        # show menu
        MainWindow.geometry("300x150")
    else:
        messagebox.showerror("Path", "Not found\nplease change directory")
        getfilepath()


#read location user
with open('gamelocation.txt', 'r') as file:
    gamelocation = file.read()
    print(gamelocation)

# ui
MainWindow = Tk()
MainWindow.title("Gamer EditorArk")
MainWindow.geometry("300x70")

# input area user path
lablePath = Label(
    MainWindow, text="(change to ur path)\n*Example* (.../steamapps/common/ARK)")
lablePath.place(x=40, y=1)
textBoxGamepath = Entry(MainWindow, width=39, justify=CENTER,)
textBoxGamepath.place(x=5, y=40)
textBoxGamepath.insert(0, gamelocation)

#menu button
browsepath = Button(
    MainWindow, text="Browse", width=5, command=getfilepath)
browsepath.place(x=247, y=38)
buttonini = Button(
    MainWindow, text='INI', height=1, width=11, command=ini_selection)
buttonini.place(x=5, y=70)
buttonwater = Button(
    MainWindow, text='ClearTopwater', height=1, width=11, command=delete_topwater)
buttonwater.place(x=105, y=70)
buttonpretty = Button(
    MainWindow, text='PrettyMap', height=1, width=11, command=pretty_map)
buttonpretty.place(x=205, y=70)
resetbtn = Button(
    MainWindow, text="Reset", height=1, width=11, fg='red', command=reset)
resetbtn.place(x=205, y=105)


# get data from file txt and check if
checkdirectory = textBoxGamepath.get() + ('/ShooterGame/')
if os.path.exists(checkdirectory):
    MainWindow.geometry("300x150")

MainWindow.mainloop()