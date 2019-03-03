# returning number into a string


def number_to_string(num):
    return str(num)

# #reversing words


def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)


# ''' підглянуто у solutions в CodeWars'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# ''' підглянуто у solutions в CodeWars'''
