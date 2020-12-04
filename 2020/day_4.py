import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


lines: List = [number for number in Path("inputs/4_1.txt").read_text().splitlines()]


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = "Northpole"
    validation: bool = True

    hcl_regex = re.compile(r"#[0-9abcdef]{6}")
    pid_regex = re.compile(r"[0-9]{9}")

    def _validate_height(self):
        if self.hgt.endswith("cm"):
            hgt = self.hgt.replace("cm", "")
            return 150 <= int(hgt) <= 193
        if self.hgt.endswith("in"):
            hgt = self.hgt.replace("in", "")
            return 59 <= int(hgt) <= 76
        return False

    def __post_init__(self):
        if self.validation:
            assert 1920 <= int(self.byr) <= 2002, f"byr {self.byr}"
            assert 2010 <= int(self.iyr) <= 2020, f"iyr {self.iyr}"
            assert 2020 <= int(self.eyr) <= 2030, f"eyr {self.eyr}"
            assert self.hcl_regex.match(self.hcl), f"hcl {self.hcl}"
            assert self.ecl in [
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ], f"ecl {self.ecl}"
            assert self.pid_regex.match(self.pid), f"pid {self.pid}"
            assert self._validate_height(), f"hgt {self.hgt}"


def validate_passport(passport, validation):
    try:
        Passport(validation=validation, **passport)
        return True
    except Exception as e:
        return False


def check_all_passports(validation: bool):
    valid_passport = 0
    passport = {}
    for line in lines:
        if line == "":
            if validate_passport(passport, validation):
                valid_passport += 1
            passport = {}
            continue

        parts = line.split(" ")
        for part in parts:
            sub = part.split(":")
            passport[sub[0]] = sub[1]
    validate_passport(passport, validation)
    print(valid_passport)


# part 1
check_all_passports(False)

# part 2
check_all_passports(True)
