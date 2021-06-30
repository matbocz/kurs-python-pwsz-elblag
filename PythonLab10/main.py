import os.path
from os import listdir

import wx
import wx.xrc


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(756, 575), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.main_menuBar = wx.MenuBar(0)
        self.main_menu = wx.Menu()
        self.load_menuItem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Otwórz plik", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.load_menuItem)

        # self.save_menuItem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Zapisz plik", wx.EmptyString, wx.ITEM_NORMAL)
        # self.main_menu.Append(self.save_menuItem)

        self.help_menuItem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Pomoc", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.help_menuItem)

        self.quit_menuItem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Wyjście", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.quit_menuItem)

        self.main_menuBar.Append(self.main_menu, u"Menu")

        self.SetMenuBar(self.main_menuBar)

        box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.name_staticText = wx.StaticText(self, wx.ID_ANY, u"Nazwa", wx.DefaultPosition, wx.DefaultSize, 0)
        self.name_staticText.Wrap(-1)

        box_sizer.Add(self.name_staticText, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.image_staticBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        box_sizer.Add(self.image_staticBitmap, 5, wx.ALL | wx.EXPAND, 5)

        grid_sizer = wx.GridSizer(0, 2, 0, 0)

        self.prev_button = wx.Button(self, wx.ID_ANY, u"Poprzednie", wx.DefaultPosition, wx.DefaultSize, 0)
        grid_sizer.Add(self.prev_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.next_button = wx.Button(self, wx.ID_ANY, u"Następne", wx.DefaultPosition, wx.DefaultSize, 0)
        grid_sizer.Add(self.next_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        box_sizer.Add(grid_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(box_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.load_menuItem_click, id=self.load_menuItem.GetId())
        # self.Bind(wx.EVT_MENU, self.save_menuItem_click, id=self.save_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self.help_menuItem_click, id=self.help_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self.quit_menuItem_click, id=self.quit_menuItem.GetId())
        self.prev_button.Bind(wx.EVT_LEFT_DOWN, self.prev_button_click)
        self.next_button.Bind(wx.EVT_LEFT_DOWN, self.next_button_click)

        # Set images folder
        self.currentImage = 0
        self.path = "./images"
        self.images = [img for img in listdir(self.path)]

        # Load start image
        self.load_image()

    def load_menuItem_click(self, event):
        with wx.FileDialog(self, "Open XYZ file", wildcard="JPG files (*.jpg)|*.jpg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            path_to_image = fileDialog.GetPath()
            bitmap = wx.Bitmap()
            wx.Bitmap.LoadFile(bitmap, path_to_image)
            self.image_staticBitmap.SetBitmap(bitmap)
            self.name_staticText.SetLabel(os.path.basename(path_to_image))

    # def save_menuItem_click(self, event):
    #     event.Skip()

    def help_menuItem_click(self, event):
        wx.MessageBox('Tutaj znajduje się pomoc.', 'Pomoc',
                      wx.OK | wx.ICON_INFORMATION)

    def quit_menuItem_click(self, event):
        self.Close()

    def prev_button_click(self, event):
        if self.currentImage == 0:
            self.currentImage = len(self.images) - 1
        else:
            self.currentImage -= 1

        self.load_image()

    def next_button_click(self, event):
        if self.currentImage == len(self.images) - 1:
            self.currentImage = 0
        else:
            self.currentImage += 1

        self.load_image()

    def load_image(self):
        bitmap = wx.Bitmap()
        wx.Bitmap.LoadFile(bitmap, f"images/{self.images[self.currentImage]}")
        self.image_staticBitmap.SetBitmap(bitmap)
        self.name_staticText.SetLabel(str(self.images[self.currentImage]))


class App(wx.App):
    def OnInit(self):
        main_frame = MainFrame(None)
        main_frame.Show(True)

        return True


if __name__ == "__main__":
    App().MainLoop()
