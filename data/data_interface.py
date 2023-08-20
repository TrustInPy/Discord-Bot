import json
import logging
import os

_logger = logging.getLogger("main")


_DATA_FILE = "data/data.json"
_data = {}


def _init():
    if not os.path.exists(_DATA_FILE):
        _logger.debug(
            f"data_interface: Data file does not exist. Creating {_DATA_FILE}"
        )
        with open(_DATA_FILE, "w") as file:
            file.write(json.dumps(_data))


def _load():
    _logger.debug(f"data_interface: Loading data from {_DATA_FILE}")
    with open(_DATA_FILE) as file:
        global _data
        _data = json.load(file)


def _save():
    _logger.debug(f"data_interface: Saving data to {_DATA_FILE}")
    with open(_DATA_FILE, "w") as file:
        file.write(json.dumps(_data, indent=4, sort_keys=True))


_init()
_load()


def get_subscriptions():
    subscriptions = {}
    servers: dict = _data.get("servers")
    if not servers:
        return subscriptions
    for server_id in servers.keys():
        subscriptions[server_id] = servers[server_id]["active"]
    return subscriptions


def get_server(guild_id):
    servers: dict = _data.get("servers")
    if not servers:
        return None
    return servers.get(str(guild_id))


def add_server(name, id):
    server = get_server(id)
    if server:
        return "The server is already registered."

    if not _data.get("servers"):
        _data["servers"] = {}

    _data["servers"][id] = {
        "name": name,
        "active": True,
    }
    _save()
    return id


def edit_server(id, active):
    server = get_server(id)
    if not server:
        return "No server found with this id."

    server["active"] = active
    _save()
    return id


def remove_server(id):
    server = get_server(id)
    if not server:
        return "No server found with this id."

    _data["servers"].pop(str(id))
    _save()
    return id


def set_welcome_channel_id(guild_id, channel_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["welcome_channel_id"] = channel_id
        _save()
        return channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set welcome_channel_id "
            + f"({channel_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_welcome_channel_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("welcome_channel_id")


def set_welcome_message(guild_id, message):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["welcome_message"] = message
        _save()
        return message
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set welcome_message "
            + f"({message}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_welcome_message(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("welcome_message")


def set_epic_games_channel_id(guild_id, channel_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["epic_games_channel_id"] = channel_id
        _save()
        return channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set epic_games_channel_id"
            + f"channel id ({channel_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_epic_games_channel_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("epic_games_channel_id")


def set_klei_links_channel_id(guild_id, channel_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["klei_links_channel_id"] = channel_id
        _save()
        return channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set klei_links_channel_id"
            + f"channel id ({channel_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_klei_links_channel_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("klei_links_channel_id")


def set_free_games_role_id(guild_id, role_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["free_games_role_id"] = role_id
        _save()
        return role_id
    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set free games role id ({role_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_free_games_role_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("free_games_role_id")


def set_dst_role_id(guild_id, role_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["dst_role_id"] = role_id
        _save()
        return role_id
    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set DST role id ({role_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_dst_role_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("dst_role_id")


def set_epic_games_names(guild_id, games):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["epic_games"] = games
        _save()
        return games
    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set free games names ({games}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_epic_games_names(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    games = server.get("epic_games")
    if games:
        return games
    return []


def set_klei_links(guild_id, links):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["klei_links"] = links
        _save()
        return links
    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set klei links ({links}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_klei_links(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    links = server.get("klei_links")
    if links:
        return links
    return []


def set_member_count_channel_id(guild_id, channel_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["member_count_channel_id"] = channel_id
        _save()
        return channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set member count channel id "
            + f"({channel_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_member_count_channel_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("member_count_channel_id")


def set_role_message_id(guild_id, message_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["set_role_message_id"] = message_id
        _save()
        return message_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to set set-role message id "
            + f"({message_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_role_message_id(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("set_role_message_id")


def set_role_emoji(guild_id, emoji_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        server["set_role_emoji"] = emoji_id
        _save()
        return emoji_id
    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set role emoji id ({emoji_id}) for guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_role_emoji(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("set_role_emoji")


def add_yt_notif_rule(
    guild_id,
    yt_channel_id,
    yt_channel_name,
    discord_channel_id,
    last_video_id,
    custom_message=None,
):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        if not server.get("yt_notif_rules"):
            server["yt_notif_rules"] = {}

        rules = server["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id in rules:
            if rules[yt_channel_id].get("name") != yt_channel_name:
                rules[yt_channel_id]["name"] = yt_channel_name
                _save()
            if (
                rules[yt_channel_id]["discord_channel_id"] == discord_channel_id
                and rules[yt_channel_id]["custom_text_message"] == custom_message
            ):
                return "This rule already exists."
            else:
                rules[yt_channel_id]["discord_channel_id"] = discord_channel_id
                rules[yt_channel_id]["custom_text_message"] = custom_message
                _save()
                return "Updated."

        rules[yt_channel_id] = {
            "name": yt_channel_name,
            "discord_channel_id": discord_channel_id,
            "last_video_id": last_video_id,
            "custom_text_message": custom_message,
        }
        _save()
        return yt_channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to add youtube notification rule with these parameters: "
            + f"yt_channel_id ({yt_channel_id}), yt_channel_name ({yt_channel_name}), "
            + f"discord_channel_id ({discord_channel_id}), last_video_id ({last_video_id}), "
            + f"custom_message ({custom_message}) "
            + f"in guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def get_yt_notif_rules(guild_id):
    server = get_server(guild_id)
    if not server:
        return None
    return server.get("yt_notif_rules")


def set_yt_last_video_id(guild_id, yt_channel_id, yt_channel_name, video_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        if not server.get("yt_notif_rules"):
            return "The server has no Youtube notification rules defined."

        rules = server["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id not in rules:
            return "The server has no rules defined for this Youtube channel."

        if rules[yt_channel_id].get("name") != yt_channel_name:
            rules[yt_channel_id]["name"] = yt_channel_name
            _save()
        if rules[yt_channel_id]["last_video_id"] == video_id:
            return "Unchanged."
        else:
            rules[yt_channel_id]["last_video_id"] = video_id
            _save()
            return video_id

    except Exception as e:
        _logger.exception(
            f"data_interface: Failed to set last youtube video id ({video_id}) "
            + f"for yt_channel_id ({yt_channel_id}), yt_channel_name ({yt_channel_name}), "
            + f"in guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"


def remove_yt_notif_rule(guild_id, yt_channel_id):
    try:
        server = get_server(guild_id)
        if not server:
            return "No server found with this id."

        if not server.get("yt_notif_rules"):
            server["yt_notif_rules"] = {}

        rules = server["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id not in rules:
            return "No rule is set for this Youtube channel."

        server["yt_notif_rules"].pop(yt_channel_id)
        _save()
        return yt_channel_id
    except Exception as e:
        _logger.exception(
            "data_interface: Failed to remove youtube notification rule of yt_channel_id "
            + f"({yt_channel_id}) from guild ({guild_id})"
        )
        return f"Error happened: {str(e)}"
