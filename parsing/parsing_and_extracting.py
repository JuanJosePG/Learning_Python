def parse_and_extract():
    data='My email is jjpg.code@gmail.com, bye!'
    comma_pos=data.find(' ',10)
    print(comma_pos)
    at_pos=data.find('@')
    print(at_pos)
    name_extracted=data[comma_pos+1:at_pos]
    print(name_extracted)

parse_and_extract()
