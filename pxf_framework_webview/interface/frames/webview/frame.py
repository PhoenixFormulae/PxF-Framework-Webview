# Standard Imports

# Local Imports
from pxf_framework_webview.interface.frames.webview import controls, user_controls, events
from pxf_framework_webview.interface.frames.webview.config import WindowConfig
from pxf_framework_webview.interface.frames.webview.controls import WebComponent

# External Imports
from pxf_framework_core.framework.interface.frame.base import BaseFrame
from pxf_framework_core.framework.interface.frame.window.abc import FrameWindowABC
from pxf_framework_core.framework.interface.frame.window.data import FrameWindowConfig
from pxf_framework_core.framework.interface.set.interfaces import InterfaceSetABC
from pxf_framework_core.framework.interface.view.control.container import ControlContainer
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.event.container import EventContainer
from pxf_framework_core.framework.interface.view.user_control.container import UserControlContainer


class WebviewFrame(BaseFrame):

    kind: str = "webview"
    static_window: bool = False

    @property
    def assets_dir(self) -> str:
        raise NotImplementedError

    InterfaceSets: list[InterfaceSetABC] = []

    WindowConfiguration: FrameWindowConfig = WindowConfig
    Window: FrameWindowABC | None = None

    base_control_type: ControlABC = WebComponent
    control_types: ControlContainer = ControlContainer(controls.__path__)
    control_types += base_control_type

    user_control_types: UserControlContainer = UserControlContainer(user_controls.__path__)
    event_types: EventContainer = EventContainer(events.__path__)

    @classmethod
    def loop(cls):
        pass
