import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key = "files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")

output_label = sg.Text(key = "output", text_color="green")

zip_name_label = sg.Text("Enter name of the zip file: ")
zip_name = sg.Input(key = "compressed_name")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor", 
                   layout = [[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [zip_name_label, zip_name],
                             [compress_button, output_label]])

while True:

    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    compressed_folder_name = values["compressed_name"] + ".zip"
    make_archive(filepaths, folder, compressed_folder_name)
    window["output"].update("Compressed succesfully!")

    print(compressed_folder_name)

window.close()