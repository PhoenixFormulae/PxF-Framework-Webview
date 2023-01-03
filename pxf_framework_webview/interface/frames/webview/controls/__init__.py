# Standard Imports
from typing import Union, List

# Local Imports
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.interface.view.event.interfaces import EventABC

# External Imports


class WebComponent(ControlABC):

    kind: str = "component"

    name: str
    width: int
    height: int
    global_position: tuple[int, int]
    required_properties: list[str]
    optional_properties: list[str]
    children: list[ControlABC]
    user_controls: list[UserControlABC]
    parent_cls: ControlABC

    def __init__(self):
        pass

    def __del__(self):
        pass

    def add_child(self, control: ControlABC):
        pass

    def add_children(self, controls: list[ControlABC]):
        pass

    def find_child(self, child_name: str) -> ControlABC | None:
        pass

    def add_user_control(self, user_control: Union[UserControlABC, List[UserControlABC]]):
        pass

    def set_parent(self, parent: ControlABC):
        pass

    def add_event(self, event: EventABC):
        pass

    def validated(self):
        pass

    def validate(self):
        pass

    def invalidate(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass


