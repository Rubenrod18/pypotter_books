class DictHelper:
    @staticmethod
    def ignore_keys(data: dict, exclude: list) -> dict:
        return dict({item: data[item] for item in data if item not in exclude})
