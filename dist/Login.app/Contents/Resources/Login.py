# from Cocoa import *
from AppKit import NSWindowController, NSApplication, NSApp, NSColor, NSMaxYEdge, NSMakeRect
from Cocoa import objc


class SimpleXibDemoController(NSWindowController):
    submit_button = objc.IBOutlet()
    popover = objc.IBOutlet()

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

    @objc.IBAction
    def submit_(self, sender):
        self.popover.showRelativeToRect_ofView_preferredEdge_(sender.bounds(), self.submit_button, NSMaxYEdge)

if __name__ == "__main__":
    app = NSApplication.sharedApplication()

    # Initiate the contrller with a XIB
    viewController = SimpleXibDemoController.alloc().initWithWindowNibName_("Login")

    # Show the window
    viewController.showWindow_(viewController)

    # Bring app to top
    NSApp.activateIgnoringOtherApps_(True)

    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()
