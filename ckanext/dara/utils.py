import random


def author_name_split(name):
    """
    as long as we don't have an author implementation, we have to hack ;-)
    we simply assume (for now) that name is given as FirstName (Middlename)
    LastName. It's ugly...
    """

    #XXX leaving middlename out for now
    all = name.split()
    firstname = all[0]
    lastname = 'None'
    if len(all) >=2:
        lastname = all[-1]

    return dict(
            firstname = firstname,
            lastname = lastname
            )


