# week07_07.py

def get_formatted_name(firstname, lastname):
    return f"{firstname} {lastname}".title()

def build_person(firstname, lastname, age=None):
    person = {'firstname':firstname, 'lastname':lastname}
    if age:
        if isinstance(age, int):
            person['age'] = age
    return person

musician_list = []
musician_list.append(build_person('jimi', 'hendrix'))
musician_list.append(build_person('sukjin', 'kim', age=27))
musician_list.append(build_person('jaemin', 'kim', age=20))
for musician in musician_list:
    #print(musician)
    print(get_formatted_name(musician['firstname'], musician['lastname']))
print("############################")
def get_formatted_name(firstname, lastname):
    return f"{firstname} {lastname}".title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(firstname, lastname, opt =''):
    if opt == "kor":
        return f"{lastname} {firstname}".title()
    else:
        return f"{firstname} {lastname}".title()
musician = get_formatted_name('jimi', 'hendrix',"kor")
print(musician)
musician = get_formatted_name(lastname='장', firstname='인하', opt="kor")
print(musician)
