from ..color import color
from ..clear import clear


def banner ():
    # Specify the path to the ASCII banner file
    banner = """
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██║███████╗███████║    ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚════██║██╔══██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║██║███████║██║  ██║    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                      
"""
    clear.TerminalClear.clear()
    print(color.ColorPrinter.magenta(banner))

def print_banner():
  banner()
  print(color.ColorPrinter.cyan("-------------------------------------------------------------------------------------------"))
  print(color.ColorPrinter.blue("                 Welcome to Phish Master - A user-friendly phishing tool."))
  print()
  print(color.ColorPrinter.blue("                                Author: Armoghan-ul-Mohmin"))
  print(color.ColorPrinter.cyan("-------------------------------------------------------------------------------------------"))

#############################################
#                 Usage                     #
#############################################
# from banner import print_banner
# print_banner()