# Description
# In the following, every capital letter represents some hexadecimal digit from 0 to f.
#
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
#
# Now, say the similarity between two colors
# "#ABCDEF" and "#UVWXYZ" is abs((AB - UV)^2 + (CD - WX)^2 + (EF - YZ)^2).
#
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
# and has a shorthand (that is, it can be represented as some "#XYZ")
#
#
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.
# Example
# Example 1:
#
# Input:
#
# color = "#09f166"
# Output:
#
# "#11ee66"
# Explanation:
#
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.
#
# Example 2:
#
# Input:
#
# color = "#010000"
# Output:
#
# "#000000"
# Explanation:
#
# The similarity is -(0x01 - 0x00)^2 -(0x00 - 0x00)^2 - (0x00 - 0x00)^2 = -1 -0 -0 = -1.
# This is the highest among any shorthand color.


def similar_rgb(color: str) -> str:
    def closest_hex(hex_str):
        num = int(hex_str, 16)

        candidates = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
        closest = min(candidates, key=lambda x: abs(x - num))
        return f"{closest:02x}"

    # Process each component
    r = color[1:3]
    g = color[3:5]
    b = color[5:7]

    closest_r = closest_hex(r)
    closest_g = closest_hex(g)
    closest_b = closest_hex(b)

    return f"#{closest_r[0]}{closest_r[0]}{closest_g[0]}{closest_g[0]}{closest_b[0]}{closest_b[0]}"