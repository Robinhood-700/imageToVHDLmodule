#!/usr/bin/env python3
import sys
import os
import math
from PIL import Image
from PIL import UnidentifiedImageError

print("Args: ", sys.argv)


def getImagePath():
    while (True):
        path = input("Please input the name of the file: ")
        if os.path.isfile(path):
            return path
        else:
            print("Invalid file. Please try again.")


if len(sys.argv) - 1 > 1:
    print("Only provide one image at a time.")
    exit()

if ((len(sys.argv) - 1) == 1):
    imagePath = sys.argv[1]
else:
    imagePath = getImagePath()

try:
    image = Image.open(imagePath)
except UnidentifiedImageError:
    print("Image could not be processed.")
    exit()

print("Image size: (", image.width, ", ", image.height, ")")
bitmap = list(image.get_flattened_data())
print(bitmap)
print("Obtaining RGB values")

RGB = []
str_prefix = "x\""
str_postfix = "\""

for val in bitmap:
    R = val[0]
    G = val[1]
    B = val[2]
    print("Decimal RGB: (", R, ", ", G, ", ", B, ")")
    print("Hex values =(",
          hex(R >> 4),
          ",",
          hex(G >> 4),
          ", ",
          hex(B >> 4),
          ")")
    RGB.append(str_prefix +
               format(R >> 4, 'x') +
               format(G >> 4, 'x') +
               format(B >> 4, 'x') +
               str_postfix)
print("RGB values: ", RGB)

outputString = """----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    12:03:30 03/17/2026 
-- Design Name: 
-- Module Name:    img_rom - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

--for conv_integer
--use ieee.std_logic_unsigned.all;

entity img_rom is
    Port ( clk : in  STD_LOGIC;
           reset : in  STD_LOGIC;
           enable : in  STD_LOGIC;
           dout : out  STD_LOGIC_VECTOR (11 downto 0));
end img_rom;

architecture Behavioral of img_rom is \n"""

outputString += ("\t type rom_type is array (0 to " + str((len(RGB) - 1)) + ") of std_logic_vector(11 downto 0);\n")

outputString += "\tsignal ROM : rom_type ( "

for i in range(0, len(RGB) - 1):
    outputString += RGB[i]
    if i != (len(RGB) - 1):
        outputString += ", "

outputString += ");\n"

outputString += "signal addr : unsigned(" + str(math.ceil(math.log2(len(RGB)))) +" downto 0);"
outputString += """ begin
    
    process(clk, reset)
    begin
		if (reset = '1') then
				addr <= (others => '0');
		elsif (clk'event and clk='1') then
			if (enable = '1') then """
outputString += ("if (addr >= " + str((len(RGB) - 1)) + ") then\n")
outputString += """	addr <= (others => '0');
				else
					addr <= addr + 1;
				end if;
			end if;
		end if;
    end process;
	 
	 dout <= ROM(to_integer(addr));

end Behavioral; """

print("ROM generado")
outFile = input("Write the name of the VHDL module: ") + ".vhd"

with open(outFile, "w") as file:
    file.write(outputString)

print("File: ", outFile, " created.")
