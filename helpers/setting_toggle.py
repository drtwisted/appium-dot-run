__author__ = 'twisted'
from PyQt4.QtGui import QCheckBox


def __get_widgets_by_name(_obj, name, exclude_type):
    _dict = _obj.__dict__
    _res = list()
    for widget_name in list(_dict):
        if name in widget_name and \
                not isinstance(_dict[widget_name], exclude_type):
            _res.append(_dict[widget_name])

    return _res


def set_widgets_visible_state(ui, name, state):
    for widget in __get_widgets_by_name(ui, name, QCheckBox):
        widget.setEnabled(state)
