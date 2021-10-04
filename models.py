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
        "tournamentcyclephase": 2
    },
    "playdata": {
        "worlds": [],
        "characters": []
    }
}

game_world_template = {
    "id": 0,
    "name": "World 1",
    "externaladdressprotected": "127.0.0.1",
    "externalportprotected": 7171,
    "externaladdressunprotected": "127.0.0.1",
    "externalportunprotected": 7171,
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
    "istournamentparticipant": False
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

def load_config_json() -> None:
    try:
        stream = open("config.yaml", 'r')
        global config
        config = yaml.safe_load(stream)
        stream.close()
    except yaml.YAMLError as exc:
        print(exc)
        return

    # update default values in response model
    for world_config in config["worlds"]:
        game_world = game_world_template.copy()
        game_world["id"] = world_config["id"]
        game_world["name"] = world_config["name"]
        game_world["externaladdressprotected"] = world_config["ip"]
        game_world["externaladdressunprotected"] = world_config["ip"]
        game_world["externalportprotected"] = world_config["port"]
        game_world["externalportunprotected"] = world_config["port"]
        game_world["location"] = world_config["location"]
        game_world["pvptype"] = world_config["pvp-type"]
        login_response["playdata"]["worlds"].append(game_world)

    print("Loaded config")
