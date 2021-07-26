import wx
import wx.xrc

from PIL import Image


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Przetwarzanie obrazu", pos=wx.DefaultPosition,
                          size=wx.Size(823, 549), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.main_menubar = wx.MenuBar(0)
        self.main_menu = wx.Menu()
        self.open_menuitem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Otwórz", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.open_menuitem)

        self.save_menuitem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Zapisz", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.save_menuitem)

        self.quit_menuitem = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Wyjdź", wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.Append(self.quit_menuitem)

        self.main_menubar.Append(self.main_menu, u"Menu")

        self.SetMenuBar(self.main_menubar)

        main_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.name_statictext = wx.StaticText(self, wx.ID_ANY, u"Mateusz Boczarski", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.name_statictext.Wrap(-1)

        main_box_sizer.Add(self.name_statictext, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.image_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        main_box_sizer.Add(self.image_bitmap, 10, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        buttons_grid_sizer = wx.GridSizer(1, 3, 0, 0)

        self.sobel_button = wx.Button(self, wx.ID_ANY, u"Sobel", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons_grid_sizer.Add(self.sobel_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.roberts_button = wx.Button(self, wx.ID_ANY, u"Roberts", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons_grid_sizer.Add(self.roberts_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                               5)

        self.prewitt_button = wx.Button(self, wx.ID_ANY, u"Prewitt", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons_grid_sizer.Add(self.prewitt_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                               5)

        main_box_sizer.Add(buttons_grid_sizer, 1, wx.EXPAND, 5)

        main_grid_sizer = wx.GridSizer(1, 2, 0, 0)

        left_box_sizer = wx.BoxSizer(wx.VERTICAL)

        progowanie_radioboxChoices = [u"Proste", u"Adaptacyjne"]
        self.progowanie_radiobox = wx.RadioBox(self, wx.ID_ANY, u"Wybór sposobu progowania", wx.DefaultPosition,
                                               wx.DefaultSize, progowanie_radioboxChoices, 1, wx.RA_SPECIFY_COLS)
        self.progowanie_radiobox.SetSelection(0)
        left_box_sizer.Add(self.progowanie_radiobox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        main_grid_sizer.Add(left_box_sizer, 1, wx.EXPAND, 5)

        right_grid_sizer = wx.GridSizer(0, 3, 0, 0)

        settings1_radioboxChoices = [u"Opcja 1", u"Opcja 2"]
        self.settings1_radiobox = wx.RadioBox(self, wx.ID_ANY, u"Ustawienia 1", wx.DefaultPosition, wx.DefaultSize,
                                              settings1_radioboxChoices, 1, wx.RA_SPECIFY_COLS)
        self.settings1_radiobox.SetSelection(0)
        right_grid_sizer.Add(self.settings1_radiobox, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
                             5)

        settings2_radioboxChoices = [u"Opcja 1", u"Opcja 2"]
        self.settings2_radiobox = wx.RadioBox(self, wx.ID_ANY, u"Ustawienia 2", wx.DefaultPosition, wx.DefaultSize,
                                              settings2_radioboxChoices, 1, wx.RA_SPECIFY_COLS)
        self.settings2_radiobox.SetSelection(0)
        right_grid_sizer.Add(self.settings2_radiobox, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
                             5)

        settings3_radioboxChoices = [u"Opcja 1", u"Opcja 2"]
        self.settings3_radiobox = wx.RadioBox(self, wx.ID_ANY, u"Ustawienia 3", wx.DefaultPosition, wx.DefaultSize,
                                              settings3_radioboxChoices, 1, wx.RA_SPECIFY_COLS)
        self.settings3_radiobox.SetSelection(0)
        right_grid_sizer.Add(self.settings3_radiobox, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
                             5)

        main_grid_sizer.Add(right_grid_sizer, 1, wx.EXPAND, 5)

        main_box_sizer.Add(main_grid_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(main_box_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Image
        self.path_to_image = None
        self.path_to_save = None
        self.image = None

        # Connect Events
        self.Bind(wx.EVT_MENU, self.open_menuitem_click, id=self.open_menuitem.GetId())
        self.Bind(wx.EVT_MENU, self.save_menuitem_item, id=self.save_menuitem.GetId())
        self.Bind(wx.EVT_MENU, self.quit_menuitem_click, id=self.quit_menuitem.GetId())

    def __del__(self):
        pass

    def open_menuitem_click(self, event):
        with wx.FileDialog(self, "Open JPG file", wildcard="JPG files (*.jpg)|*.jpg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.path_to_image = fileDialog.GetPath()
            self.image = Image.open(self.path_to_image)

            bitmap = wx.Bitmap()
            wx.Bitmap.LoadFile(bitmap, self.path_to_image)
            self.image_bitmap.SetBitmap(bitmap)

    def save_menuitem_item(self, event):
        with wx.FileDialog(self, "Save JPG file", wildcard="JPG files (*.jpg)|*.jpg",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.path_to_save = fileDialog.GetPath()

            self.image = self.image.save(self.path_to_save)

    def quit_menuitem_click(self, event):
        self.Close()


class App(wx.App):
    def OnInit(self):
        main_frame = MainFrame(None)
        main_frame.Show(True)

        return True


if __name__ == "__main__":
    App().MainLoop()
