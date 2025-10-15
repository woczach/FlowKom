import win32gui
import win32con

def is_taskbar_window(hwnd):
    # Must be visible
    if not win32gui.IsWindowVisible(hwnd):
        return False

    # Must not be a child window
    if win32gui.GetParent(hwnd):
        return False

    # Skip tool windows and invisible owner windows
    exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    if exstyle & win32con.WS_EX_TOOLWINDOW:
        return False
    if exstyle & win32con.WS_EX_APPWINDOW:
        return True

    # Check if has no owner (ownerless top-level window)
    owner = win32gui.GetWindow(hwnd, win32con.GW_OWNER)
    if owner == 0:
        return True

    return False


def enum_taskbar_windows():
    result = []

    def callback(hwnd, _):
        if is_taskbar_window(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:  # skip blank titles
                result.append((hwnd, title))
        return True

    win32gui.EnumWindows(callback, None)
    return result


if __name__ == "__main__":
    for hwnd, title in enum_taskbar_windows():
        print(f"{hwnd:10d} | {title}")
