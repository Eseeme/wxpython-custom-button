wxPython Custom Button
======================

Español:

Clase para crear botones personalizados en wxPython. Pueden usarla libremente en sus proyectos. Compatible con Python 2.7 y 3.x, inclusive con la versión Phoenix de wxPython.

-

Português:

Classe pra criar botões personalizados no wxPython. Podem usar livremente nos seus projetos. Compatível com Python 2.7 e 3.x, inclusive com a versão Phoenix do wxPython.

Examples
--------

    CustomButton(parent, wx.ID_ANY, 'Press me!')
-
    set_label(label)
    
    Example:
    set_label('Press me!')
-
    set_bmp(normal, [hover], [focus], [mouse_down])
    
    Example:
    set_bmp(wx.Bitmap('normal.png'), wx.Bitmap('hover.png'), ... etc)
-
    set_foreground_color(normal, [hover], [focus], [mouse_down])
    
    Example:
    set_foreground_color('#333333', '#666666', mouse_down='#111111')
-
    set_text_shadow(normal (x, y, colour), [hover], [focus], [mouse_down])
    
    Example:
    set_text_shadow((1, 1, '#dddddd'), (1, 1, '#eeeeee'), ... etc)
-
    set_padding(padding (top, left, bottom, right))
    
    Example:
    set_padding((5, 10, 5, 10))
-
    set_bg_color(normal, [hover], [focus], [mouse_down])
    
    Example:
    set_bg_color('#ffffff', '#eeeeee', '#dddddd', '#cccccc')
-
    set_bg_gradient(normal (init_colour, end_colour), [hover], [focus], [mouse_down])
    
    Example:
    set_bg_gradient(('#ffffff', '#dddddd'), ('#eeeeee', '#cccccc'), ('#dddddd', '#bbbbbb'), ('#cccccc', '#aaaaaa'))
-
    set_bg_image(normal, [hover], [focus], [mouse_down])
    
    Example:
    set_bg_image(wx.Bitmap('normal.png'), wx.Bitmap('hover.png'), ... etc)
-
    set_border(normal (px, color, radius), [hover], [focus], [mouse_down])
    
    Examples:
    set_border(None)
    set_border((1, '#333333', 5), (1, '#666666', 5), ... etc)
-
    set_font(normal, [hover], [focus], [mouse_down])
    
    Example:
    set_font(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL), ... etc)
-
    set_cursor(cursor)
    
    Examples:
    
    Phoenix:
    set_cursor(wx.Cursor(wx.CURSOR_HAND))
    
    Old versions:
    set_cursor(wx.StockCursor(wx.CURSOR_HAND))
-
    center_content([center=True])
    
    Examples:
    center_content()
    center_content(True)
    center_content(False)
-
    set_size(size (w, h))
    
    Example:
    set_size((100, 40))
