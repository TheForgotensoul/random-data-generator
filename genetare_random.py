import random
import string
import names


def phone(num):
    ph = []
    for i in range(int(num)):
        n = "0000000000"
        while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
            n = str(random.randint(10 ** 9, 10 ** 10 - 1))
        ph.append(n[:3] + '-' + n[3:6] + '-' + n[6:])
    return ph


def email(num):
    el = []
    for i in range(num):
        n = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 8)))
        d = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 8)))
        c = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 5)))
        el.append(f"{n}@{d}.{c}")
    return el


class Name:
    @staticmethod
    def firstname(num):
        f = []
        for i in range(num):
            gen = ["male", "female"]
            ft_name = names.get_first_name(gender=random.choices(gen))
            f.append(ft_name)
        return f

    @staticmethod
    def lastname(num):
        lt = []
        for i in range(num):
            lt_name = names.get_last_name()
            lt.append(lt_name)
        return lt

    @staticmethod
    def fullname(num):
        fl = []
        for i in range(num):
            gen = ["male", "female"]
            fl_name = names.get_full_name(gender=random.choices(gen))
            fl.append(fl_name)
        return fl


class Ind:
    @staticmethod
    def firstname(num):
        for i in range(int(num)):
            with open("Names.txt", "r") as f:
                first_names = f.read().splitlines()
                first_name = random.choice(first_names)
            return first_name

    @staticmethod
    def lastname(num):
        for i in range(int(num)):
            with open("Names.txt", "r") as f:
                last_names = f.read().splitlines()
                last_name = random.choice(last_names)
            return last_name

    @staticmethod
    def fullname(num):
        for i in range(int(num)):
            with open("Names.txt", "r") as f, open("last_name.txt", "r") as lt:
                first_names = f.read().splitlines()
                last_names = lt.read().splitlines()
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            return f"{first_name} {last_name}"

    @staticmethod
    def phone(num):
        ph = []
        for i in range(int(num)):
            n = str(random.randint(60 * 10 ** 8, 90 * 10 ** 8 - 1))
            ph.append(f"+91 {n}")
        return ph
