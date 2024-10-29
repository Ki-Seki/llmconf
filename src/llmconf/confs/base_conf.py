from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseConf:
    def __repr__(self):
        fields = {}
        for key, value in self.__dict__.items():
            if value is not None:
                fields[key] = value
        return f"{type(self).__name__} {fields}"
