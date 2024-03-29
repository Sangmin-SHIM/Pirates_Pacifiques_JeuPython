import tkinter
from tkinter import Tk, Canvas, Event
from PIL import Image, ImageTk

from contract.icontroller import IController
from contract.imodel import IModel, IMobile, IBoard, ISquare, ISprite
from contract.iview import IView
from contract.action import Action


class View(IView):
    __model: IModel
    __controller: IController
    __zoom: int
    __screenWidth: int
    __screenHeight: int
    __blackImage: str

    def __init__(self):
        self.__zoom = 60
        self.__screenWidth = 20
        self.__screenHeight = 10
        self.__blackImage = "image/blacksquare.png"

    def setModel(self, model: IModel):
        self.__model = model
        self.__createWindow()

    def setController(self, controller: IController) -> None:
        self.__controller = controller

    def __onClosing(self):
        self.__controller.viewIsClosed()
        self.__window.destroy()

    def show(self):
        forest: IBoard
        squares: [[ISquare]]
        forest = self.__model.getBoard()
        squares = forest.getSquares()
        images = {}
        for y in range(self.transformYScreenToYBoard(0), self.transformYScreenToYBoard(self.__screenHeight)+1):
            for x in range(self.transformXScreenToXBoard(0), self.transformXScreenToXBoard(self.__screenWidth)+1):
                if 0 <= y < self.__model.getBoard().getHeight() and 0 <= x < self.__model.getBoard().getWidth():
                    imageName = squares[y][x].getSprite().getImageName()
                else:
                    imageName = self.__blackImage
                if imageName not in images:
                    image = Image.open(imageName).resize((self.__zoom, self.__zoom), Image.ANTIALIAS)
                    images[imageName] = ImageTk.PhotoImage(image)
                self.__canvas.create_image(self.transformXBoardToXScreen(x) * self.__zoom + self.__zoom / 2,
                                           self.transformYBoardToYScreen(y) * self.__zoom + self.__zoom / 2,
                                           image=images[imageName])
        mobile: IMobile
        for mobile in self.__model.getMobiles():
            imageName = mobile.getSprite().getImageName()
            if imageName not in images:
                image = Image.open(imageName).resize((self.__zoom, self.__zoom), Image.ANTIALIAS)
                images[imageName] = ImageTk.PhotoImage(image)
            self.__canvas.create_image(self.transformXBoardToXScreen(mobile.getX()) * self.__zoom + self.__zoom / 2,
                                       self.transformYBoardToYScreen(mobile.getY()) * self.__zoom + self.__zoom / 2,
                                       image=images[imageName])
        self.__window.update()

    def __createWindow(self):
        self.__window = Tk()
        self.__window.title("EPSI Project")
        self.__window.geometry(str(self.__screenWidth * self.__zoom)
                               + "x" + str(self.__screenHeight * self.__zoom))
        self.__canvas = Canvas(self.__window)
        self.__canvas.configure(bg="Black")
        self.__canvas.pack(fill="both", expand=True)
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.bind("<Key>", self.manageKeyEvent)
        self.__window.deiconify()
        self.__window.update()

    def manageKeyEvent(self, event: Event):
        if event.keysym == "Up":
            self.__controller.performAction(Action.UP)
        elif event.keysym == "Right":
            self.__controller.performAction(Action.RIGHT)
            # Down Interdit
        # elif event.keysym == "Down":
        # self.__controller.performAction(Action.DOWN)
        elif event.keysym == "Left":
            self.__controller.performAction(Action.LEFT)

    def transformXBoardToXScreen(self, xBoard: int) -> int:
        return int (xBoard - ((self.__model.getPlayer().getX()) - self.__screenWidth / 2))

    def transformYBoardToYScreen(self, yBoard: int) -> int:
        return int(yBoard - ((self.__model.getPlayer().getY()) - self.__screenHeight / 2))

    def transformXScreenToXBoard(self, xScreen: int) -> int:
        return int(xScreen + ((self.__model.getPlayer().getX()) - self.__screenWidth / 2))

    def transformYScreenToYBoard(self, yScreen: int) -> int:
        return int(yScreen + ((self.__model.getPlayer().getY()) - self.__screenHeight / 2))

    def showMessage(self, message: str):
        tkinter.messagebox.showinfo("Partie Terminée", message)

    def showGameOver(self, message: str):
        tkinter.messagebox.showinfo("Game Over", message)