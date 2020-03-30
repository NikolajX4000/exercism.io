def recite(start_verse, end_verse):
    ordinals = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
                9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
    lyrics = {'first': 'a Partridge in a Pear Tree', 'second': 'two Turtle Doves', 'third': 'three French Hens',
              'fourth': 'four Calling Birds', 'fifth': 'five Gold Rings', 'sixth': 'six Geese-a-Laying',
              'seventh': 'seven Swans-a-Swimming', 'eighth': 'eight Maids-a-Milking', 'ninth': 'nine Ladies Dancing',
              'tenth': 'ten Lords-a-Leaping', 'eleventh': 'eleven Pipers Piping', 'twelfth': 'twelve Drummers Drumming'}
    verses = []
    for i in range(start_verse, end_verse + 1):
        verse = f'On the {ordinals[i]} day of Christmas my true love gave to me: '
        while i > 1:
            verse += f'{lyrics[ordinals[i]]}, '
            i -= 1
        verse += f"{'and ' if ',' in verse else ''}{lyrics[ordinals[i]]}."
        verses.append(verse)
    return verses
