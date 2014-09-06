#!/usr/bin/env python

import wx

from custom_button import CustomButton as CustomBtn


class Frame(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        sizer = wx.BoxSizer()

        pnl = wx.Panel(self)
        pnl_sizer = wx.GridBagSizer(10, 10)


        # Hand cursor.
        if 'phoenix' in wx.PlatformInfo:
            hand_cursor = wx.Cursor(wx.CURSOR_HAND)
        else:
            hand_cursor = wx.StockCursor(wx.CURSOR_HAND)


        # Button 1

        btn1 = CustomBtn(pnl, wx.ID_ANY, 'Button 1')

        btn1.set_bg_color('#dddddd')
        btn1.set_padding((5, 10, 5, 10))

        pnl_sizer.Add(btn1, flag=wx.ALIGN_CENTER, pos=(0, 0))


        # Button 2

        btn2 = CustomBtn(pnl, wx.ID_ANY, 'Button 2')

        btn2.set_bg_color('#ffffff', '#eeeeee', '#dddddd')
        btn2.set_border((1, '#666666', 5))
        btn2.set_padding((5, 10, 5, 10))
        btn2.set_cursor(hand_cursor)

        pnl_sizer.Add(btn2, flag=wx.ALIGN_CENTER, pos=(0, 1))


        # Button 3

        btn3 = CustomBtn(pnl, wx.ID_ANY, 'Button 3')

        btn3.set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'))
        btn3.set_border((1, '#666666', 3))
        btn3.set_padding((5, 10, 5, 10))

        pnl_sizer.Add(btn3, flag=wx.ALIGN_CENTER, pos=(0, 2))


        # Button 4

        btn4 = CustomBtn(pnl, wx.ID_ANY, 'Button 4')

        btn4.set_foreground_color('#ffffff')

        btn4.set_text_shadow((1, 1, '#286897'))
        btn4.set_bg_gradient(('#CEE3F2', '#438FC9'), ('#ABCEE9', '#3279AD'),
                             ('#8EBEE1', '#2C6A98'), ('#6DABD8', '#225275'))
        btn4.set_border((1, '#3076A9', 3))
        btn4.set_padding((5, 10, 5, 10))

        btn4.set_cursor(hand_cursor)

        pnl_sizer.Add(btn4, flag=wx.ALIGN_CENTER, pos=(1, 0))


        # Button 5

        btn5 = CustomBtn(pnl, wx.ID_ANY, 'Button 5')

        btn5.set_foreground_color('#ffffff')
        btn5.set_bg_color('#EE595E', '#F06C70', '#EC4A4F', '#EC3E42')
        btn5.set_border((1, '#DF151B', 0))
        btn5.set_padding((5, 10, 5, 10))

        pnl_sizer.Add(btn5, flag=wx.ALIGN_CENTER, pos=(1, 1))


        # Button 6

        btn6 = CustomBtn(pnl, wx.ID_ANY, 'Button 6')

        font_normal = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font_hover = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1)
        btn6.set_font(font_normal, hover=font_hover)

        btn6.set_foreground_color('#ffffff')
        btn6.set_bg_gradient(('#87CE6F', '#5E913C'))
        btn6.set_border((1, '#397126', 10))
        btn6.set_padding((5, 10, 5, 10))
        btn6.set_cursor(hand_cursor)

        pnl_sizer.Add(btn6, flag=wx.ALIGN_CENTER, pos=(1, 2))


        # Button 7

        btn7 = CustomBtn(pnl, wx.ID_ANY, 'Button 7')

        btn7.set_foreground_color('#ffffff')

        bg_normal = wx.Bitmap('img/bg1.png')
        bg_hover = wx.Bitmap('img/bg1_hover.png')
        btn7.set_bg_image(bg_normal, bg_hover)

        btn7.set_border((1, '#444444', 10))
        btn7.set_padding((5, 10, 5, 10))
        btn7.set_cursor(hand_cursor)

        pnl_sizer.Add(btn7, flag=wx.ALIGN_CENTER, pos=(2, 0))


        # Button 8

        btn8 = CustomBtn(pnl, wx.ID_ANY, 'Button 8')

        btn8.set_bmp((wx.Bitmap('img/icon2.png'), 'left'))
        btn8.set_foreground_color('#ffffff')
        btn8.set_bg_color('#1E425F', '#2B5C86')
        btn8.set_border((0, '#666666', 5))
        btn8.set_padding((5, 10, 5, 10))

        pnl_sizer.Add(btn8, flag=wx.ALIGN_CENTER, pos=(2, 1))


        # Button 9

        btn9 = CustomBtn(pnl, wx.ID_ANY, 'Button 9')

        btn9.set_bmp((wx.Bitmap('img/icon3.png'), 'right'))
        btn9.set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'))
        btn9.set_border((1, '#666666', 5))
        btn9.set_padding((5, 10, 5, 10))

        pnl_sizer.Add(btn9, flag=wx.ALIGN_CENTER, pos=(2, 2))


        # Button 10

        btn10 = CustomBtn(pnl, wx.ID_ANY, 'Button 10')

        btn10.set_bmp((wx.Bitmap('img/icon4.png'), 'top'))
        btn10.set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'),
                              ('#dddddd', '#bbbbbb'), ('#cccccc', '#aaaaaa'))
        btn10.set_border((1, '#666666', 5))
        btn10.set_padding((5, 10, 5, 10))
        btn10.set_cursor(hand_cursor)

        pnl_sizer.Add(btn10, flag=wx.ALIGN_CENTER, pos=(3, 0))


        # Button 11

        btn11 = CustomBtn(pnl, wx.ID_ANY, 'Button 11')

        btn11.set_bmp((wx.Bitmap('img/icon4.png'), 'bottom'))
        btn11.set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'),
                              ('#dddddd', '#bbbbbb'), ('#cccccc', '#aaaaaa'))
        btn11.set_border((1, '#666666', 5))
        btn11.set_padding((5, 10, 5, 10))
        btn11.set_cursor(hand_cursor)

        pnl_sizer.Add(btn11, flag=wx.ALIGN_CENTER, pos=(3, 1))


        # Button 12

        btn12 = CustomBtn(pnl, wx.ID_ANY, 'Button 12')

        btn12.set_font(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        btn12.set_bmp((wx.Bitmap('img/icon1.png'), 'top'))
        btn12.set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'),
                              ('#dddddd', '#bbbbbb'), ('#cccccc', '#aaaaaa'))
        btn12.set_border((1, '#666666', 34))

        btn12.set_size((70, 70))
        btn12.center_content()

        pnl_sizer.Add(btn12, flag=wx.ALIGN_CENTER, pos=(3, 2))


        # Button 13

        btn13 = CustomBtn(pnl, wx.ID_ANY, 'Button 13')

        btn13.set_foreground_color('#42662D')
        btn13.set_text_shadow((1, 1, '#BCD8A7'))
        btn13.set_bg_color('#9BC880', '#AAD093', mouse_down='#8BBF6C')

        normal = (4, '#639942', 0)
        hover = (4, '#71AF4B', 0)
        mouse_down = (4, '#538037', 0)
        btn13.set_border(normal, hover, mouse_down=mouse_down)

        btn13.set_padding((5, 0, 5, 0))
        btn13.set_cursor(hand_cursor)

        btn13.set_size((120, -1))
        btn13.center_content(True)

        pnl_sizer.Add(btn13, flag=wx.ALIGN_CENTER, pos=(4, 0))


        # Button 14

        btn14 = CustomBtn(pnl, wx.ID_ANY, 'Button 14')

        font_normal = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font_hover = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1)
        btn14.set_font(font_normal, hover=font_hover)

        btn14.set_bmp((wx.Bitmap('img/icon2.png'), 'left'))

        # Fix size.
        btn14.set_padding((0, 1, 0, 0))

        btn14.set_border(None)
        btn14.set_cursor(hand_cursor)

        pnl_sizer.Add(btn14, flag=wx.ALIGN_CENTER, pos=(4, 1))


        # Button 15

        btn15 = CustomBtn(pnl, wx.ID_ANY, 'Button 15')

        font_normal = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font_hover = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1)
        btn15.set_font(font_normal, hover=font_hover)

        btn15.set_foreground_color('#1A0DAB')

        # Fix size.
        btn15.set_padding((0, 1, 0, 0))

        btn15.set_border(None)
        btn15.set_cursor(hand_cursor)

        pnl_sizer.Add(btn15, flag=wx.ALIGN_CENTER, pos=(4, 2))


        # Button 16

        btn16 = CustomBtn(pnl, wx.ID_ANY, 'Button 16')

        btn16.set_foreground_color('#ffffff')

        bg_normal = wx.Bitmap('img/bg2.png')
        bg_hover = wx.Bitmap('img/bg2_hover.png')
        bg_mouse_down = wx.Bitmap('img/bg2_mouse_down.png')
        btn16.set_bg_image(bg_normal, bg_hover, mouse_down=bg_mouse_down)

        btn16.set_padding((5, 10, 5, 10))
        btn16.set_border((1, '#2B648E', 5))
        btn16.set_cursor(hand_cursor)

        btn16.set_size((-1, 26))

        pnl_sizer.Add(btn16, flag=wx.ALIGN_CENTER, pos=(5, 0))


        # Button 17

        btn17 = CustomBtn(pnl, wx.ID_ANY)

        normal = (wx.Bitmap('img/btn1.png'), 'left')
        focus = (wx.Bitmap('img/btn1_hover.png'), 'left')
        btn17.set_bmp(normal, focus)

        btn17.set_border(None)
        btn17.set_cursor(hand_cursor)

        pnl_sizer.Add(btn17, flag=wx.ALIGN_CENTER, pos=(5, 1))


        # Button 18

        btn18 = CustomBtn(pnl, wx.ID_ANY)

        normal = (wx.Bitmap('img/btn2.png'), 'left')
        focus = (wx.Bitmap('img/btn2_hover.png'), 'left')
        btn18.set_bmp(normal, focus)

        btn18.set_border(None)
        btn18.set_cursor(hand_cursor)

        pnl_sizer.Add(btn18, flag=wx.ALIGN_CENTER, pos=(5, 2))


        pnl.SetSizer(pnl_sizer)

        sizer.Add(pnl)
        self.SetSizerAndFit(sizer)


def main():
    app = wx.App(False)

    style = wx.DEFAULT_FRAME_STYLE ^\
        (wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX)
    frame = Frame(None, wx.ID_ANY, 'Examples', style=style)
    frame.Centre()
    frame.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()