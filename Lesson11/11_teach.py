with open("hr_system.txt") as hr_system:
    for line in hr_system:
        newline = line.split()
        one_newline = newline[0].strip()
        id_newline = newline[1].strip()
        two_newline = newline[2].strip()
        pay_newline = int(newline[3].strip())
        if two_newline == "Engineer":
            pay_newline += 24000
        print(f"{one_newline} (ID: {id_newline}), {two_newline} - ${pay_newline/24:.2f}")