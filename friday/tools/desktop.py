"""
Desktop tools — control the Windows host (opening websites, applications).
"""

import os
import webbrowser

def register(mcp):

    @mcp.tool()
    def open_website(url: str) -> str:
        """
        Opens a specific website in the default browser. 
        Use this when the user asks to open YouTube, Google, or any other website.
        Provide the full URL, e.g., 'https://www.youtube.com' or 'https://www.google.com'.
        """
        try:
            webbrowser.open(url)
            return f"Opening {url} on your screen now."
        except Exception as e:
            return f"Failed to open website: {str(e)}"

    @mcp.tool()
    def launch_application(app_name: str) -> str:
        """
        Launches a local desktop application by its executable name.
        Use this when the user asks to open Notepad, Calculator, Spotify, etc.
        Only use common executable names (e.g. 'notepad', 'calc', 'mspaint').
        """
        try:
            # On Windows, 'start' can open registered executables.
            os.system(f"start {app_name}")
            return f"Launched application: {app_name}."
        except Exception as e:
            return f"Failed to launch {app_name}: {str(e)}"
