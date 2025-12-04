def find_combos(kipelov, kinchev):
    kipelov.sort()
    shevchuk = []

    for i in range(len(kipelov)):
        if kipelov[i] == kinchev:
            if [kipelov[i]] not in shevchuk:
                shevchuk.append([kipelov[i]])

        for j in range(i + 1, len(kipelov)):
            if kipelov[i] + kipelov[j] == kinchev:
                lindemann = [kipelov[i], kipelov[j]]
                if lindemann not in shevchuk:
                    shevchuk.append(lindemann)

            for k in range(j + 1, len(kipelov)):
                if kipelov[i] + kipelov[j] + kipelov[k] == kinchev:
                    broden = [kipelov[i], kipelov[j], kipelov[k]]
                    if broden not in shevchuk:
                        shevchuk.append(broden)

    return shevchuk

kipelov = [2, 5, 2, 1, 2]
kinchev = 5
print(find_combos(kipelov, kinchev))
