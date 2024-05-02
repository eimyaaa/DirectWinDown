import argparse
from preq import webbrowser as wb

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to DirectWinDown!!, A direct mirror link of Windows Installers!")

    parser.add_argument(
        "-en", "--enterprise", 
        action="store_true", 
        help="Selects Enterprise Edition", 
        dest="ent"
    )
    parser.add_argument(
        "-c1", "--consumer1", 
        action="store_true", 
        help="Selects 64-bit Consumer Edition", 
        dest="con1"
    )
    parser.add_argument(
        "-c2", "--consumer2", 
        action="store_true", 
        help="Selects 32-bit Consumer Edition", 
        dest="con2"
    )
    parser.add_argument(
        "-c3", "--consumer3", 
        action="store_true", 
        help="Selects Both 32 and 64bit Consumer Edition", 
        dest="con3"
    )
    args = parser.parse_args()


    if args.con1:
        print("You selected 64-bit Consumer Edition of Windows, Enjoy!")
        wb.open_new("https://archive.org/download/windows-10-22-h-2-english-us-multi/Windows%2010%2022H2%20English%20US%20x64.iso")
    
    if args.con2:
        print("You selected 32-bit Consumer Edition of Windows, Enjoy!")
        wb.open_new("https://archive.org/download/windows-10-22-h-2-english-us-multi/Windows%2010%2022H2%20English%20US%20x86.iso")

    if args.con3:
        print("You selected 32 and 64 bit Consumer Edition of Windows, Enjoy!")
        wb.open_new("https://archive.org/download/windows-10-22-h-2-english-us-multi/Windows%2010%2022H2%20English%20US%20Multi.iso")

    if args.ent:
        print("You selected 64-bit Enterprise Edition of Windows, Enjoy!")
        wb.open_new("https://drive.massgrave.dev/en-us_windows_10_iot_enterprise_ltsc_2021_x64_dvd_257ad90f.iso")
