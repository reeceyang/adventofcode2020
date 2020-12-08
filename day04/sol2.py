import re

#byr
#iyr
#eyr
is_year = re.compile(r"\d\d\d\d$")
#hgt
hgt_cm = re.compile(r"\d\d\dcm$")
hgt_in = re.compile(r"\d\din$")
#hcl
hcl = re.compile(r"#\w{6}$")
#ecl
ecl = re.compile(r"amb$|blu$|brn$|gry$|grn$|hzl$|oth")
#pid
pid = re.compile(r"\d{9}$")

line = input()

valids = 0
newPassport = True
passport = ""
while True:
    if newPassport and line == "":
        break
    elif (not newPassport) and line == "":
        tokens = passport.split()
        fields = {}
        for tok in tokens:
            x = tok.split(":")
            fields[x[0]] = x[1]
            print(x[0],x[1])
        valid = True
        #byr
        if "byr" in fields and is_year.match(fields["byr"]) and int(fields["byr"]) >= 1920 and int(fields["byr"]) <= 2002:
            pass
        else:
            print("byr failed")
            valid = False
        #iyr
        if "iyr" in fields and is_year.match(fields["iyr"]) and int(fields["iyr"]) >= 2010 and int(fields["iyr"]) <= 2020:
            pass
        else:
            print("iyr failed")
            valid = False
        #eyr
        if "eyr" in fields and is_year.match(fields["eyr"]) and int(fields["eyr"]) >= 2020 and int(fields["eyr"]) <= 2030:
            pass
        else:
            print("eyr failed")
            valid = False
        #hgt
        if "hgt" in fields and (hgt_cm.match(fields["hgt"]) or hgt_in.match(fields["hgt"])):
            pass
        else:
            print("hgt failed")
            valid = False
        #hcl
        if "hcl" in fields and hcl.match(fields["hcl"]):
            pass
        else:
            print("hcl failed")
            valid = False
        #ecl
        if "ecl" in fields and ecl.match(fields["ecl"]):
            pass
        else:
            print("ecl failed")
            valid = False
        #pid
        if "pid" in fields and pid.match(fields["pid"]):
            pass
        else:
            print("pid failed")
            valid = False
        newPassport = True
        passport = ""
        if valid:
            valids += 1
    else:
        newPassport = False
        passport += line + "\n"
    line = input()

print(valids)
