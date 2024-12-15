
from utilities import helper as hp

#random valid data
def random_first_name():
    return hp.random_string_with_space(hp.random_number_in_range(1, 100))

def random_last_name():
    return hp.random_string_with_space(hp.random_number_in_range(1, 100))

def random_email():
    tail_domain = ["com", "net", "org"][hp.random_number_in_range(0,2)]
    domain = ["gmail", "yahoo","outlook","hotmail"][hp.random_number_in_range(0,3)]
    username = hp.random_string_and_digits(hp.random_number_in_range(1,243))
    return f"{username}@{domain}.{tail_domain}"

def random_phone():
    second_digit = hp.random_number_in_range(1,9)
    last_digits = hp.random_digits_len(hp.random_number_in_range(8,9))
    return f"0{second_digit}{last_digits}"

def random_password():
    return f"Aa#1{hp.random_string_and_digits(hp.random_number_in_range(4, 251))}"

def random_address():
    return hp.random_string_with_space(hp.random_number_in_range(1, 255))

def random_city():
    return hp.random_string_with_space(hp.random_number_in_range(1, 100))

def random_postal_code():
    return hp.random_digits_len(hp.random_number_in_range(3, 10))


