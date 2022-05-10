import sys
from tkinter import *
import random
import settings
import ctypes


# Cell class
class Cell:
    all = []
    cell_count = settings.grid_size**2
    cell_count_lbl = None
    def __init__(self, x, y, is_mine=False) -> None:
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_open = False
        self.is_marked = False

        # Append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location, 
            bg='white',
            width=12,
            height=4
        )

        btn.bind('<Button-1>', self.left_click)

        btn.bind('<Button-3>', self.right_click)

        self.cell_btn_object = btn


    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left:{Cell.cell_count}",
            font=("", 28)
        )
        Cell.cell_count_lbl = lbl

    # Get cell object based on the values of x and y
    def get_cell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def neighbour_cells(self):
        cells = [
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1),
            self.get_cell(self.x, self.y + 1)

        ]
        
        cells = [cell for cell in cells if cell is not None]
        

        return cells

    def show_mine(self):
        # Game over
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over!', 0)
        sys.exit()


    @property
    def mines_length(self):
        counter = 0
        for cell in self.neighbour_cells:
            if cell.is_mine:
                counter += 1

        return counter


    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.mines_length)

            # Update Cell count
            if Cell.cell_count_lbl:
                Cell.cell_count_lbl.configure(text=f"Cells left:{Cell.cell_count}")

            self.cell_btn_object.configure(bg='SystemButtonFace')


        self.is_open = True

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.mines_length == 0:
                for cell_obj in self.neighbour_cells:
                   cell_obj.show_cell()
            self.show_cell()


    def right_click(self, event):
        if not self.is_marked:
            self.cell_btn_object.configure(bg='orange')
            self.is_marked = True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_marked = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.mines)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"


# Window
root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper')
root.resizable(False, False)

# Top frame
top_frame = Frame(
    root,
    bg="red",
    width=settings.width,
    height=settings.height/4
    )

top_frame.place(x=0, y=0)


# Left frame
left_frame = Frame(
    root, 
    bg='blue',
    width=settings.width/4,
    height=3/4 * settings.height
    )

left_frame.place(x=0, y=1/4 * settings.height)


# Center frame
center_frame = Frame(
    root, 
    bg='green',
    width=3/4 * settings.width, 
    height= 3/4 * settings.height
)

center_frame.place(x=1/4 * settings.width, y=1/4 * settings.height)



for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)



Cell.create_cell_count_label(left_frame)
Cell.cell_count_lbl.place(x=0, y=0)
Cell.randomize_mines()


# Main loop
root.mainloop()