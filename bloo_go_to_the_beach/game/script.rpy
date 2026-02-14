label start:

    # Scene 1 - Beach
    scene history_01
    with fade

    "Wide Bloo faces the beach"

    # Scene 2 - Surf
    scene history_02
    with dissolve

    "Bloo surf"

    scene history_03
    with hpunch

    "Bloo crashes!"

    # Scene 3 - Sandcastle
    scene history_04
    with dissolve

    "Bloo admire a sand castle"

    scene history_05
    with hpunch

    "Sand castle falls..."

    # Scene 4 - Crab
    scene history_06
    with dissolve

    "Bloo meets crab"


    menu:
        "Gentleman Bloo":
            jump kind
        "Rude Bloo":
            jump caos


label kind:

    "Bloo is happy"

    "Bloo wants to take the sun"

    return


label caos:

    scene history_07
    with vpunch

    "¡RAAAH!"

    "Crab ATTACKS!!!"

    return
