lines_string = "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

lines = lines_string.split(', ')

lines.reverse()

days = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

def recite(start_verse, end_verse):
    recitation = [f'On the {days[start_verse]} day of Christmas my true love gave to me: ']
    i = start_verse
    while i >= end_verse:
        recitation.append(lines[i-1]+', ')
        i -= 1
    return recitation
