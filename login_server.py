from database_manager import Database
import json
from hashlib import sha1
from models import login_character, login_response, vocation_to_name, load_config_json
import copy
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainHandler

class LoginServer:
    def __init__(self) -> None:
        load_config_json()

    def start(self) -> bool:
        self.db = Database()
        return self.db.open()
    
    def process_login(self, email: str, password: str, frame: "MainHandler") -> None:
        result = self.db.store_query("SELECT `id`, `premium_ends_at` FROM `accounts` WHERE `name` = {} AND `password` = {} LIMIT 1".format(self.db.escape_string(email), self.db.escape_string(LoginServer.sha1_string(password))))

        if not result:
            frame.write(json.dumps({"errorCode": 3, "errorMessage": "Account email address or password is not correct."}))
            return

        self.send_character_list(result[0], frame)

    def send_character_list(self, account_data: list, frame: "MainHandler") -> None:
        response = copy.deepcopy(login_response)

        response["session"]["premiumuntil"] = account_data[1]
        response["session"]["ispremium"] = account_data[1] >= datetime.datetime.now(datetime.timezone.utc).timestamp()
        #response["session"]["lastlogintime"] = account_data[2]

        result = self.db.store_query("SELECT `name`, `level`, `vocation`, `sex`, `looktype`, `lookhead`, `lookbody`, `looklegs`, `lookfeet`, `lookaddons` FROM `players` WHERE `account_id` = {}".format(account_data[0]))
        if result:
            for row in result:
                char_response = login_character.copy()
                char_response["name"] = row[0]
                char_response["level"] = row[1]
                char_response["vocation"] = vocation_to_name.get(row[2], "Unknown")
                char_response["ismale"] = row[3] == 1
                char_response["outfitid"] = row[4]
                char_response["headcolor"] = row[5]
                char_response["legscolor"] = row[6]
                char_response["detailcolor"] = row[7]
                char_response["addonsflags"] = row[8]
                # charResponse["ishidden"] = true not handled inside of database
                response["playdata"]["characters"].append(char_response)

        frame.write(response)

    @staticmethod
    def sha1_string(string: str) -> str:
        sha = sha1()
        sha.update(string.encode("utf-8"))
        return sha.hexdigest()
