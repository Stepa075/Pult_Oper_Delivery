from tkinter import *
import tkintermapview

window = Tk()
window.title("Test_Map")
window.geometry("800x800+300+50")
map_widget = tkintermapview.TkinterMapView(window, width=800, height=800, corner_radius=0)
map_widget.place(x=0, y=0)

map_widget.set_position(49.9341676, 36.3787474)
map_widget.set_zoom(15)
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=18)
marker1 = map_widget.set_address("Пушкинская, 7, Харьков, Украина", text="Пушкинская, 7, Харьков, Украина", marker=True)
# marker_1.set_text("Пушкинская, 7, Харьков, Украина")








window.mainloop()