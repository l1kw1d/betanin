def get_config():
    with open(BEETS_CONFIG_PATH, 'r') as file:
        return file.read()
