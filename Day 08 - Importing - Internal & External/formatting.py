msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Ayush", website='ayush.com')

def format_msg(my_name="Ayush", my_website="ayush.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg