import random
import requests
import pandas
import uuid
import time


init_url = "http://royal-mail.delivery"
mail_domains = ["yahoo.com", "gmail.com", "outlook.co.uk", "hotmail.co.uk", "hotmail.com"]
f_names = pandas.read_csv('babies-first-names-all-names-all-years.csv').FirstForename.to_list()
l_names = pandas.read_csv('surnames.csv').name.to_list()
cities = pandas.read_csv('uk-towns-sample.csv').name.to_list()


def generate_payloads():
    post_code = f"{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(1, 9)} " \
                f"{random.randint(1, 9)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}"
    phone = f"07{random.randint(112323242, 879687698)}"
    dob = f"{random.randint(11, 30)}/{random.randint(1, 12)}/{random.randint(1923, 2021)}"
    house_number = f"{random.randint(1, 200)}"
    name = f"{random.choice(f_names)} {random.choice(l_names).capitalize()}"
    email = f"{name.replace(' ', '').lower()}{random.randint(12, 9999)}" \
            f"@{random.choice(mail_domains)}"
    city = random.choice(cities)
    address = f"{house_number} {city}"

    card_number = f"{random.randint(1234123412341234, 9876987698769876)}"
    acc_number = f"{random.randint(12233223, 98789786)}"
    sort_code = f"{random.randint(11, 99)}-{random.randint(11, 99)}-{random.randint(11, 99)}"
    cvc = f"{random.randint(111, 999)}"
    exp = f"{random.randint(1, 12)}/{random.randint(22, 24)}"

    return ({'name': name, 'dob': dob, 'email': email, 'phone': phone, 'address': address, 'city': city,
             'postcode': post_code}, {'card_holderName': name, 'card_number': card_number, 'cardExpiry': exp,
                                      'cardCVC': cvc, 'account_number': acc_number, 'sort_code': sort_code})


def fire_payloads(base_url, p1, p2, session):
    res1 = requests.post(f"{base_url}/payment.php?ssl=true&session={session}", data=p1)
    res2 = requests.post(f"{base_url}/loading.php?ssl=true&session={session}", data=p2)
    print(res1, res2)


def generate_random_session():
    s = str(uuid.uuid4()).replace('-', '')
    return s * 2


if __name__ == "__main__":
    while True:
        payload = generate_payloads()
        print("Firing!")
        print(payload[0])
        print(payload[1])
        fire_payloads(init_url, payload[0], payload[1], generate_random_session())
        print()
        time.sleep(5)
