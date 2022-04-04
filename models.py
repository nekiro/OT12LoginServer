import yaml

login_response = {
     "session": {
        "sessionkey": "sessionKey",
        "lastlogintime": 0,
        "ispremium": False,
        "premiumuntil": 0,
        "status": "active",
        "returnernotification": False,
        "showrewardnews": True,
        "isreturner": True,
        "fpstracking": False,
        "optiontracking": False,
        "tournamentticketpurchasestate": 0,
    },
    "playdata": {
        "worlds": [],
        "characters": []
    }
}

game_world_template = {
    "id": 0,
    "name": "World 1",
    "externaladdress": "127.0.0.1",
    "externalport": 7172,
    "externaladdressunprotected": "127.0.0.1",
    "externaladdressprotected": "127.0.0.1",
    "externalportunprotected": 7172,
    "externalportprotected": 7172,
    "previewstate": 0,
    "location": "EUR",
    "anticheatprotection": False,
    "pvptype": 0,
    "istournamentworld": False,
    "restrictedstore": False
}

login_character = {
    "worldid": 0,
    "name": "Name",
    "level": 38,
    "vocation": "Knight",
    "ismale": False,
    "ishidden": False,
    "ismaincharacter": False,
    "tutorial": False,
    "outfitid": 139,
    "headcolor": 95,
    "torsocolor": 38,
    "legscolor": 94,
    "detailcolor": 115,
    "addonsflags": 0,
    "istournamentparticipant": False,
    "remainingdailytournamentplaytime": 0
}

vocation_to_name = {
    0: "None",
    1: "Sorcerer",
    2: "Druid",
    3: "Paladin",
    4: "Knight",
    5: "Master Sorcerer",
    6: "Elder Druid",
    7: "Royal Paladin",
    8: "Elite Knight",
}

config_key_to_world_key = {
    "id": "id",
    "name": "name",
    "ip-protected": "externaladdressprotected",
    "ip-unprotected": "externaladdressunprotected",
    "port-protected": "externalportprotected",
    "port-unprotected": "externalportunprotected",
    "location": "location",
    "pvp-type": "pvptype"
}

def load_config_json() -> None:
    try:
        stream = open("config.yaml", 'r')
        global config
        config = yaml.safe_load(stream)
        stream.close()
    except yaml.YAMLError as exc:
        print(exc)
        exit()

    if not config:
        print("invalid config.yml")
        exit()

    if not "worlds" in config:
        print("missing worlds configuration in config.yml")
        exit()

    # worlds
    for world_config in config["worlds"]:
        game_world = game_world_template.copy()

        for key, val in world_config.items():
            if key in config_key_to_world_key:
                game_world[config_key_to_world_key[key]] = val

        login_response["playdata"]["worlds"].append(game_world)

    print("Loaded config")
