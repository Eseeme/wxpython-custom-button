#### wxPython Custom Button ####
#
# File: custom_button.py
# Creation date: 2014-09-02
# Author: Daniel Ramos
# Email: daniel_p_em@outlook.com
#
# This Program Is Freeware And Distributed Under The wxPython License.

import wx


class CustomButton(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, label='', *args, **kwargs):
        wx.Panel.__init__(self, parent, id, *args, **kwargs)

        self.parent = parent
        self.label = label

        self.bmp_normal = None
        self.bmp_hover = None
        self.bmp_focus = None
        self.bmp_mouse_down = None

        self.foreground_color_normal = '#000000'
        self.foreground_color_hover = None
        self.foreground_color_focus = None
        self.foreground_color_mouse_down = None

        # txt_shadow = (x, y, colour)
        self.txt_shadow_normal = None
        self.txt_shadow_hover = None
        self.txt_shadow_focus = None
        self.txt_shadow_mouse_down = None

        # border = (px, colour, radius)
        self.border = (1, '#333333', 0)
        self.border_hover = None
        self.border_focus = None
        self.border_mouse_down = None

        # padding = (top, right, bottom, left)
        self.padding = (0, 0, 0, 0)

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font_normal = font
        self.font_hover = None
        self.font_focus = None
        self.font_mouse_down = None

        self.bg_type = 'color'
        parent_bg = self.parent.GetBackgroundColour()
        self.bg_color_normal = parent_bg
        self.bg_color_hover = None
        self.bg_color_focus = None
        self.bg_color_mouse_down = None

        if 'phoenix' in wx.PlatformInfo:
            self.cursor = wx.Cursor(wx.CURSOR_ARROW)
        else:
            self.cursor = wx.StockCursor(wx.CURSOR_ARROW)

        self.center = False
        self.size = None

        self.mouse_in = False
        self.mouse_down = False
        self.focus = False

        self.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
        self.Bind(wx.EVT_KILL_FOCUS, self._on_kill_focus)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_mouse_leave)
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_mouse_enter)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_mouse_up)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self._on_erase_background)
        self.Bind(wx.EVT_SIZE, self._on_size)
        self.Bind(wx.EVT_PAINT, self._on_paint)

    def set_label(self, label):
        self.label = label
        self.Refresh()

    def set_bmp(self, normal, bmp_hover=None, bmp_focus=None,
                bmp_mouse_down=None):

        # bmp = (bmp, position)
        # position: 'top', 'right', 'bottom', 'left'.
        self.bmp_normal = normal
        self.bmp_hover = bmp_hover
        self.bmp_focus = bmp_focus
        self.bmp_mouse_down = bmp_mouse_down

        self.Refresh()

    def set_foreground_color(self, normal, hover=None, focus=None,
                             mouse_down=None):
        self.foreground_color_normal = normal
        self.foreground_color_hover = hover
        self.foreground_color_focus = focus
        self.foreground_color_mouse_down = mouse_down

        self.Refresh()

    def set_text_shadow(self, normal, hover=None, focus=None, mouse_down=None):

        # shadow = (x, y, colour)
        self.txt_shadow_normal = normal
        self.txt_shadow_hover = hover
        self.txt_shadow_focus = focus
        self.txt_shadow_mouse_down = mouse_down

        self.Refresh()

    def set_padding(self, padding):

        # padding = (top, right, bottom, left)
        self.padding = padding

        self.Refresh()

    def set_bg_color(self, normal, hover=None, focus=None, mouse_down=None):
        self.bg_type = 'color'

        self.bg_color_normal = normal
        self.bg_color_hover = hover
        self.bg_color_focus = focus
        self.bg_color_mouse_down = mouse_down

        self.Refresh()

    def set_bg_gradient(self, normal, hover=None, focus=None, mouse_down=None):
        self.bg_type = 'gradient'

        # bg_gradient = (init_color, end_color)
        self.bg_gradient_normal = normal
        self.bg_gradient_hover = hover
        self.bg_gradient_focus = focus
        self.bg_gradient_mouse_down = mouse_down

        self.Refresh()

    def set_bg_image(self, normal, hover=None, focus=None, mouse_down=None):
        self.bg_type = 'image'

        self.bg_image_normal = normal
        self.bg_image_hover = hover
        self.bg_image_focus = focus
        self.bg_image_mouse_down = mouse_down

        self.Refresh()

    def set_border(self, normal=None, hover=None, focus=None, mouse_down=None):
        # Border: px, colour, radius.
        self.border = normal
        self.border_hover = hover
        self.border_focus = focus
        self.border_mouse_down = mouse_down

        self.Refresh()

    def set_font(self, normal, hover=None, focus=None, mouse_down=None):
        self.font_normal = normal
        self.font_hover = hover
        self.font_focus = focus
        self.font_mouse_down = mouse_down

        self.Refresh()

    def set_cursor(self, cursor):
        self.cursor = cursor

    def center_content(self, center=True):
        self.center = center
        self.Refresh()

    def set_size(self, size):
        self.size = size
        self.Refresh()

    def _on_set_focus(self, event):
        self.focus = True
        self.Refresh()

    def _on_kill_focus(self, event):
        self.focus = False
        self.Refresh()

    def _on_mouse_enter(self, event):
        self.SetCursor(self.cursor)
        self.mouse_in = True
        self.Refresh()

    def _on_mouse_leave(self, event):
        self.mouse_in = False
        self.Refresh()

    def _on_mouse_down(self, event):
        self.mouse_down = True
        self.SetFocus()
        self.Refresh()

    def _on_mouse_up(self, event):
        self.mouse_down = False
        self.send_button_event()
        self.Refresh()

    def send_button_event(self):
        evt = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
        evt.SetInt(0)
        evt.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(evt)

    def _on_erase_background(self, event):
        pass

    def _on_size(self, event):
        dc = wx.ClientDC(self)
        bdc = wx.BufferedDC(dc)
        self._redraw(bdc)
        self.Refresh()

    def _on_paint(self, event):
        bdc = wx.BufferedPaintDC(self)
        self._redraw(bdc)

    def _redraw(self, bdc):
        bdc.Clear()
        gcdc = wx.GCDC(bdc)
        gc = gcdc.GetGraphicsContext()


        # Set font.
        if self.mouse_down and self.font_mouse_down is not None:
            gcdc.SetFont(self.font_mouse_down)
        elif self.mouse_in and self.font_hover is not None:
            gcdc.SetFont(self.font_hover)
        elif self.focus and self.font_focus is not None:
            gcdc.SetFont(self.font_focus)
        else:
            gcdc.SetFont(self.font_normal)


        # Get txt_w, txt_h, bmp_w, bmp_h and bmp position.
        txt_w, txt_h = gcdc.GetTextExtent(self.label)

        if self.mouse_down and self.bmp_mouse_down is not None:
            bmp = self.bmp_normal
            bmp_w, bmp_h = bmp[0].GetSize()
            position = bmp[1]
        elif self.focus and self.bmp_focus is not None:
            bmp = self.bmp_focus
            bmp_w, bmp_h = bmp[0].GetSize()
            position = bmp[1]
        elif self.mouse_in and self.bmp_hover is not None:
            bmp = self.bmp_hover
            bmp_w, bmp_h = bmp[0].GetSize()
            position = bmp[1]
        elif self.bmp_normal is not None:
            bmp = self.bmp_normal
            bmp_w, bmp_h = bmp[0].GetSize()
            position = bmp[1]
        else:
            bmp = False


        # Set minimum size.

        if bmp:
            if position == 'left' or position == 'right':
                if bmp_h > txt_h:
                    size = (self.padding[3] + bmp_w + txt_w + self.padding[1],
                            self.padding[0] + bmp_h + self.padding[2])
                else:
                    size = (self.padding[3] + bmp_w + txt_w + self.padding[1],
                            self.padding[0] + txt_h + self.padding[2])
            else:
                if bmp_w > txt_w:
                    size = (self.padding[3] + bmp_w + self.padding[1],
                            self.padding[0] + bmp_h + txt_h + self.padding[2])
                else:
                    size = (self.padding[3] + txt_w + self.padding[1],
                            self.padding[0] + bmp_h + txt_h + self.padding[2])
        else:
            size = (self.padding[3] + txt_w + self.padding[1],
                    self.padding[0] + txt_h + self.padding[2])

        if self.size is None:
            self.SetMinSize(size)
        else:
            if self.size[0] > 0 and self.size[1] == -1:
                self.SetMinSize((self.size[0], size[1]))
            elif self.size[0] == -1 and self.size[1] > 0:
                self.SetMinSize((size[0], self.size[1]))
            elif self.size[0] == -1 and self.size[1] == -1:
                self.SetMinSize(size)
            else:
                self.SetMinSize(self.size)


        # Get button size.
        w, h = self.GetSize()


        # Set background (brush).

        if self.bg_type == 'color':

            # Mouse down
            if self.mouse_down and self.bg_color_mouse_down is not None:
                gcdc.SetBrush(wx.Brush(self.bg_color_mouse_down))

            # Focus
            elif self.focus and self.bg_color_focus is not None:
                gcdc.SetBrush(wx.Brush(self.bg_color_focus))

            # Hover
            elif self.mouse_in and self.bg_color_hover is not None:
                gcdc.SetBrush(wx.Brush(self.bg_color_hover))

            # Normal
            else:
                gcdc.SetBrush(wx.Brush(self.bg_color_normal))

        elif self.bg_type == 'gradient':

            # Mouse down
            if self.mouse_down and self.bg_gradient_mouse_down is not None:
                gradbrush = gc.CreateLinearGradientBrush(
                    0, 0, 0, h,
                    self.bg_gradient_mouse_down[0],
                    self.bg_gradient_mouse_down[1])

            # Focus
            elif self.focus and self.bg_gradient_focus is not None:
                gradbrush = gc.CreateLinearGradientBrush(
                    0, 0, 0, h,
                    self.bg_gradient_focus[0], self.bg_gradient_focus[1])

            # Hover
            elif self.mouse_in and self.bg_gradient_hover is not None:
                gradbrush = gc.CreateLinearGradientBrush(
                    0, 0, 0, h,
                    self.bg_gradient_hover[0], self.bg_gradient_hover[1])

            # Normal
            else:
                gradbrush = gc.CreateLinearGradientBrush(
                    0, 0, 0, h,
                    self.bg_gradient_normal[0], self.bg_gradient_normal[1])

            gc.SetBrush(gradbrush)

        elif self.bg_type == 'image':

            # Mouse down
            if self.mouse_down and self.bg_image_mouse_down is not None:
                if 'phoenix' in wx.PlatformInfo:
                    brush = wx.Brush(self.bg_image_mouse_down)
                else:
                    brush = wx.BrushFromBitmap(self.bg_image_mouse_down)
                gcdc.SetBrush(brush)

            # Focus
            elif self.focus and self.bg_image_focus is not None:
                if 'phoenix' in wx.PlatformInfo:
                    brush = wx.Brush(self.bg_image_focus)
                else:
                    brush = wx.BrushFromBitmap(self.bg_image_focus)
                gcdc.SetBrush(brush)

            # Hover
            elif self.mouse_in and self.bg_image_hover is not None:
                if 'phoenix' in wx.PlatformInfo:
                    brush = wx.Brush(self.bg_image_hover)
                else:
                    brush = wx.BrushFromBitmap(self.bg_image_hover)
                gcdc.SetBrush(brush)

            # Normal
            else:
                if 'phoenix' in wx.PlatformInfo:
                    brush = wx.Brush(self.bg_image_normal)
                else:
                    brush = wx.BrushFromBitmap(self.bg_image_normal)
                gcdc.SetBrush(brush)

        else:
            gcdc.SetBrush(wx.Brush(self.parent.GetBackgroundColour()))


        # Set border (pen).

        # Mouse down
        if self.mouse_down and self.border_mouse_down is not None:
            if self.border_mouse_down[0] == 0:
                gcdc.SetPen(wx.TRANSPARENT_PEN)
            else:
                gcdc.SetPen(wx.Pen(self.border_mouse_down[1],
                                   self.border_mouse_down[0],
                            wx.SOLID))
            radius = self.border_mouse_down[2]

        # Focus
        elif self.focus and self.border_focus is not None:
            if self.border_focus[0] == 0:
                gcdc.SetPen(wx.TRANSPARENT_PEN)
            else:
                gcdc.SetPen(wx.Pen(self.border_focus[1], self.border_focus[0],
                            wx.SOLID))
            radius = self.border_focus[2]

        # Hover
        elif self.mouse_in and self.border_hover is not None:
            if self.border_hover[0] == 0:
                gcdc.SetPen(wx.TRANSPARENT_PEN)
            else:
                gcdc.SetPen(wx.Pen(self.border_hover[1], self.border_hover[0],
                            wx.SOLID))
            radius = self.border_hover[2]

        # Normal
        elif self.border is not None:
            if self.border[0] == 0:
                gcdc.SetPen(wx.TRANSPARENT_PEN)
            else:
                gcdc.SetPen(wx.Pen(self.border[1], self.border[0],
                            wx.SOLID))
            radius = self.border[2]

        # No border
        else:
            gcdc.SetPen(wx.TRANSPARENT_PEN)
            radius = 0

        gcdc.DrawRoundedRectangle(0, 0, w, h, radius)


        # Draw text and bmp.

        if bmp:

            if position == 'left':
                if self.center:
                    bmp_x = (w - txt_w - bmp_w) / 2
                    bmp_y = (h - bmp_h) / 2

                    txt_x = (w - txt_w - bmp_w) / 2 + bmp_w
                    txt_y = (h - txt_h) / 2
                else:
                    bmp_x = self.padding[3]
                    bmp_y = self.padding[0]

                    txt_x = self.padding[3] + bmp_w
                    if bmp_h > txt_h:
                        txt_y = (bmp_h - txt_h) / 2 + self.padding[0]
                    else:
                        txt_y = self.padding[0]

            if position == 'right':
                if self.center:
                    bmp_x = (w - txt_w - bmp_w) / 2 + txt_w
                    bmp_y = (h - bmp_h) / 2

                    txt_x = (w - txt_w - bmp_w) / 2
                    txt_y = (h - txt_h) / 2
                else:
                    bmp_x = self.padding[3] + txt_w
                    bmp_y = self.padding[0]

                    txt_x = self.padding[3]
                    if bmp_h > txt_h:
                        txt_y = (bmp_h - txt_h) / 2 + self.padding[0]
                    else:
                        txt_y = self.padding[0]

            elif position == 'top':
                if self.center:
                    bmp_x = (w - bmp_w) / 2
                    bmp_y = (h - bmp_h - txt_h) / 2

                    txt_x = (w - txt_w) / 2
                    txt_y = (h - bmp_h - txt_h) / 2 + bmp_h
                else:
                    if bmp_w > txt_w:
                        bmp_x = self.padding[3]
                        bmp_y = self.padding[0]

                        txt_x = (bmp_w - txt_w) / 2 + self.padding[3]
                        txt_y = self.padding[0] + bmp_h
                    else:
                        bmp_x = (txt_w - bmp_w) / 2 + self.padding[3]
                        bmp_y = self.padding[0]

                        txt_x = self.padding[3]
                        txt_y = self.padding[0] + bmp_h

            elif position == 'bottom':
                if self.center:
                    bmp_x = (w - bmp_w) / 2
                    bmp_y = (h - txt_h - bmp_h) / 2 + txt_h

                    txt_x = (w - txt_w) / 2
                    txt_y = (h - txt_h - bmp_h) / 2
                else:
                    if bmp_w > txt_w:
                        bmp_x = self.padding[3]
                        bmp_y = self.padding[0] + txt_h

                        txt_x = (bmp_w - txt_w) / 2 + self.padding[3]
                        txt_y = self.padding[0]
                    else:
                        bmp_x = (txt_w - bmp_w) / 2 + self.padding[3]
                        bmp_y = self.padding[0] + txt_h

                        txt_x = self.padding[3]
                        txt_y = self.padding[0]

            gcdc.DrawBitmap(bmp[0], bmp_x, bmp_y)
        else:
            if self.center:
                txt_x = (w - txt_w) / 2
                txt_y = (h - txt_h) / 2
            else:
                txt_x = self.padding[3]
                txt_y = self.padding[0]

        # Text shadow
        if self.mouse_down and self.txt_shadow_mouse_down is not None:
            gcdc.SetTextForeground(self.txt_shadow_mouse_down[2])
            gcdc.DrawText(self.label,
                          txt_x + self.txt_shadow_mouse_down[0],
                          txt_y + self.txt_shadow_mouse_down[1])
        elif self.focus and self.txt_shadow_focus is not None:
            gcdc.SetTextForeground(self.txt_shadow_focus[2])
            gcdc.DrawText(self.label,
                          txt_x + self.txt_shadow_focus[0],
                          txt_y + self.txt_shadow_focus[1])
        elif self.mouse_in and self.txt_shadow_hover is not None:
            gcdc.SetTextForeground(self.txt_shadow_hover[2])
            gcdc.DrawText(self.label,
                          txt_x + self.txt_shadow_hover[0],
                          txt_y + self.txt_shadow_focus[1])
        elif self.txt_shadow_normal is not None:
            gcdc.SetTextForeground(self.txt_shadow_normal[2])
            gcdc.DrawText(self.label,
                          txt_x + self.txt_shadow_normal[0],
                          txt_y + self.txt_shadow_normal[1])

        # Text color
        if self.mouse_down and self.foreground_color_normal is not None:
            gcdc.SetTextForeground(self.foreground_color_normal)
        elif self.focus and self.foreground_color_focus is not None:
            gcdc.SetTextForeground(self.foreground_color_focus)
        elif self.mouse_in and self.foreground_color_hover is not None:
            gcdc.SetTextForeground(self.foreground_color_hover)
        elif self.foreground_color_normal is not None:
            gcdc.SetTextForeground(self.foreground_color_normal)

        # Draw text
        gcdc.DrawText(self.label, txt_x, txt_y)