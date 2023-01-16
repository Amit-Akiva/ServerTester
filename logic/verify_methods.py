
def unique_names(names_in):
    return len(names_in) == len(set(names_in))


def fields_exist(pair_values_in, desired_field):
    if desired_field in pair_values_in.keys():
        return True
    else:
        return False
