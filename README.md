# Flying Toasters 2017
This is the co-processor openCV code for our FRC bot.

# VisionCore.py
Vision core is program that connects to the roboRIO over UDP. The roboRIO sends UDP requests for different info in the form of an int value. The program then runs the openCV function associated with that number.

# VisionTester.py
This is a program that does the exact same thing as VisionCore.py, but you change a variable to decide what function to run as opposed to taking UDP input.
