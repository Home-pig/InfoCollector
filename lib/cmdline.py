#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""
import optparse
import sys
import random


def printBanner():
    banner = ['''
    
    
        88                  ad88                 ,ad8888ba,                88  88                                                            
        ""                 d8"                  d8"'    `"8b               88  88                            ,d                              
                           88                  d8'                         88  88                            88                              
        88  8b,dPPYba,   MM88MMM   ,adPPYba,   88              ,adPPYba,   88  88   ,adPPYba,   ,adPPYba,  MM88MMM   ,adPPYba,   8b,dPPYba,  
        88  88P'   `"8a    88     a8"     "8a  88             a8"     "8a  88  88  a8P_____88  a8"     ""    88     a8"     "8a  88P'   "Y8  
        88  88       88    88     8b       d8  Y8,            8b       d8  88  88  8PP"""""""  8b            88     8b       d8  88          
        88  88       88    88     "8a,   ,a8"   Y8a.    .a8P  "8a,   ,a8"  88  88  "8b,   ,aa  "8a,   ,aa    88,    "8a,   ,a8"  88          
        88  88       88    88      `"YbbdP"'     `"Y8888Y"'    `"YbbdP"'   88  88   `"Ybbd8"'   `"Ybbd8"'    "Y888   `"YbbdP"'   88          
        
        
    ''', '''
    
d888888b d8b   db d88888b  .d88b.   .o88b.  .d88b.  db      db      d88888b  .o88b. d888888b  .d88b.  d8888b. 
  `88'   888o  88 88'     .8P  Y8. d8P  Y8 .8P  Y8. 88      88      88'     d8P  Y8 `~~88~~' .8P  Y8. 88  `8D 
   88    88V8o 88 88ooo   88    88 8P      88    88 88      88      88ooooo 8P         88    88    88 88oobY' 
   88    88 V8o88 88~~~   88    88 8b      88    88 88      88      88~~~~~ 8b         88    88    88 88`8b   
  .88.   88  V888 88      `8b  d8' Y8b  d8 `8b  d8' 88booo. 88booo. 88.     Y8b  d8    88    `8b  d8' 88 `88. 
Y888888P VP   V8P YP       `Y88P'   `Y88P'  `Y88P'  Y88888P Y88888P Y88888P  `Y88P'    YP     `Y88P'  88   YD 
                                                                                                              
                                                                                                              
 
    ''', '''
    
 _          ___          ______         _  _                                   
(_)        / __)        / _____)       | || |               _                  
 _  ____  | |__   ___  | /        ___  | || |  ____   ____ | |_    ___    ____ 
| ||  _ \ |  __) / _ \ | |       / _ \ | || | / _  ) / ___)|  _)  / _ \  / ___)
| || | | || |   | |_| || \_____ | |_| || || |( (/ / ( (___ | |__ | |_| || |    
|_||_| |_||_|    \___/  \______) \___/ |_||_| \____) \____) \___) \___/ |_|    
                                                                               

    
    ''', '''
    
             ___         ___           _    _                  _                
 _         /'___)       (  _`\        (_ ) (_ )               ( )_              
(_)  ___  | (__     _   | ( (_)   _    | |  | |    __     ___ | ,_)   _    _ __ 
| |/' _ `\| ,__)  /'_`\ | |  _  /'_`\  | |  | |  /'__`\ /'___)| |   /'_`\ ( '__)
| || ( ) || |    ( (_) )| (_( )( (_) ) | |  | | (  ___/( (___ | |_ ( (_) )| |   
(_)(_) (_)(_)    `\___/'(____/'`\___/'(___)(___)`\____)`\____)`\__)`\___/'(_)   
                                                                                
                                                                                

    ''', '''
    
,-.  .-. .-.  ,---.  .---.     ,--,    .---.   ,-.     ,-.      ,---.     ,--,    _______  .---.   ,---.    
|(|  |  \| |  | .-' / .-. )  .' .')   / .-. )  | |     | |      | .-'   .' .')   |__   __|/ .-. )  | .-.\   
(_)  |   | |  | `-. | | |(_) |  |(_)  | | |(_) | |     | |      | `-.   |  |(_)    )| |   | | |(_) | `-'/   
| |  | |\  |  | .-' | | | |  \  \     | | | |  | |     | |      | .-'   \  \      (_) |   | | | |  |   (    
| |  | | |)|  | |   \ `-' /   \  `-.  \ `-' /  | `--.  | `--.   |  `--.  \  `-.     | |   \ `-' /  | |\ \   
`-'  /(  (_)  )\|    )---'     \____\  )---'   |( __.' |( __.'  /( __.'   \____\    `-'    )---'   |_| \)\  
    (__)     (__)   (_)               (_)      (_)     (_)     (__)                       (_)          (__) 
 
                                                                          
                                                                          

    ''', '''
    
  _____      __      _   _________     ____       ____     ____     _____       _____        _____     ____   ________     ____     ______    
 (_   _)    /  \    / ) (_   _____)   / __ \     / ___)   / __ \   (_   _)     (_   _)      / ___/    / ___) (___  ___)   / __ \   (   __ \   
   | |     / /\ \  / /    ) (___     / /  \ \   / /      / /  \ \    | |         | |       ( (__     / /         ) )     / /  \ \   ) (__) )  
   | |     ) ) ) ) ) )   (   ___)   ( ()  () ) ( (      ( ()  () )   | |         | |        ) __)   ( (         ( (     ( ()  () ) (    __/   
   | |    ( ( ( ( ( (     ) (       ( ()  () ) ( (      ( ()  () )   | |   __    | |   __  ( (      ( (          ) )    ( ()  () )  ) \ \  _  
  _| |__  / /  \ \/ /    (   )       \ \__/ /   \ \___   \ \__/ /  __| |___) ) __| |___) )  \ \___   \ \___     ( (      \ \__/ /  ( ( \ \_)) 
 /_____( (_/    \__/      \_/         \____/     \____)   \____/   \________/  \________/    \____\   \____)    /__\      \____/    )_) \__/  
                                                                                                                                              

    ''', '''
    
        ___  __   __   __             ___  __  ___  __   __  
| |\ | |__  /  \ /  ` /  \ |    |    |__  /  `  |  /  \ |__) 
| | \| |    \__/ \__, \__/ |___ |___ |___ \__,  |  \__/ |  \ 
                                                             

    ''', '''
    
  _            __            ____           _   _                 _                  
 (_)  _ __    / _|   ___    / ___|   ___   | | | |   ___    ___  | |_    ___    _ __ 
 | | | '_ \  | |_   / _ \  | |      / _ \  | | | |  / _ \  / __| | __|  / _ \  | '__|
 | | | | | | |  _| | (_) | | |___  | (_) | | | | | |  __/ | (__  | |_  | (_) | | |   
 |_| |_| |_| |_|    \___/   \____|  \___/  |_| |_|  \___|  \___|  \__|  \___/  |_|   
                                                                                     

    ''', '''
    
                                                                                                                   
  ,,                  ,...                                  ,,    ,,                                               
  db                .d' ""            .g8"""bgd           `7MM  `7MM                      mm                       
                    dM`             .dP'     `M             MM    MM                      MM                       
`7MM  `7MMpMMMb.   mMMmm   ,pW"Wq.  dM'       `  ,pW"Wq.    MM    MM   .gP"Ya   ,p6"bo  mmMMmm   ,pW"Wq.  `7Mb,od8 
  MM    MM    MM    MM    6W'   `Wb MM          6W'   `Wb   MM    MM  ,M'   Yb 6M'  OO    MM    6W'   `Wb   MM' "' 
  MM    MM    MM    MM    8M     M8 MM.         8M     M8   MM    MM  8M"""""" 8M         MM    8M     M8   MM     
  MM    MM    MM    MM    YA.   ,A9 `Mb.     ,' YA.   ,A9   MM    MM  YM.    , YM.    ,   MM    YA.   ,A9   MM     
.JMML..JMML  JMML..JMML.   `Ybmd9'    `"bmmmd'   `Ybmd9'  .JMML..JMML. `Mbmmd'  YMbmd'    `Mbmo  `Ybmd9'  .JMML.   
                                                                                                                   
                                                                                                                   

    ''', '''
    
                                                                                                      
                                                                                                      
                 __              ____             ___ ___                                             
68b             69MM            6MMMMb/           `MM `MM                                             
Y89            6M' `           8P    YM            MM  MM                     /                       
___ ___  __   _MM__   _____   6M      Y   _____    MM  MM   ____     ____    /M       _____   ___  __ 
`MM `MM 6MMb  MMMMM  6MMMMMb  MM         6MMMMMb   MM  MM  6MMMMb   6MMMMb. /MMMMM   6MMMMMb  `MM 6MM 
 MM  MMM9 `Mb  MM   6M'   `Mb MM        6M'   `Mb  MM  MM 6M'  `Mb 6M'   Mb  MM     6M'   `Mb  MM69 " 
 MM  MM'   MM  MM   MM     MM MM        MM     MM  MM  MM MM    MM MM    `'  MM     MM     MM  MM'    
 MM  MM    MM  MM   MM     MM MM        MM     MM  MM  MM MMMMMMMM MM        MM     MM     MM  MM     
 MM  MM    MM  MM   MM     MM YM      6 MM     MM  MM  MM MM       MM        MM     MM     MM  MM     
 MM  MM    MM  MM   YM.   ,M9  8b    d9 YM.   ,M9  MM  MM YM    d9 YM.   d9  YM.  , YM.   ,M9  MM     
_MM__MM_  _MM__MM_   YMMMMM9    YMMMM9   YMMMMM9  _MM__MM_ YMMMM9   YMMMM9    YMMM9  YMMMMM9  _MM_    
                                                                                                      
                                                                                                      
                                                                                                      

    '''
              ]
    print(random.choice(banner))


def parse_args():

    parser = optparse.OptionParser("usage: %prog [options] http://www.target.com", version="$prog 1.0")
    # parser.add_option("-u", "--url", dest="url",help="target url",type='string')

    options, args = parser.parse_args()
    # when didn't set url exit the system
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    printBanner()
    return options, args


if __name__ == "__main__":
    parse_args()
