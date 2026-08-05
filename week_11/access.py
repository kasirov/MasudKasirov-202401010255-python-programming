def check_access(registered, lab_open, comp_available):
    if registered and lab_open and comp_available:
        return "Access Granted!"
    else:
        return "Access Denied!"

def get_reason(registered, lab_open, comp_availabe):

    if not registered:
        return "Student is not registered!"
    elif not lab_open:
        return "Computer Lab is Closed!"
    elif not comp_availabe:
        return "No available computer!"
    else:
        return "Welcom to the lab!"