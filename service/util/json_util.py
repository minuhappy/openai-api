import json
from types import SimpleNamespace
from typing import Any, Union


class JsonUtil:
    # 문자를 객체로 변환
    @staticmethod
    def json_to_object(json_string: str):
        return json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))

    @staticmethod
    def object_to_json(obj: Any):
        try:
            return json.dumps(obj)
        except:
            return JsonUtil.to_dict(obj=obj)

    @staticmethod
    def print_json(obj: Any):
        content = JsonUtil.object_to_json(obj)
        print(content)

    @staticmethod
    def to_dict(obj: Any):
        if isinstance(obj, list):
            return [JsonUtil.to_dict(e) for e in obj]

        if not hasattr(obj, '__dict__'):
            return obj if obj is not None else ''

        result = obj.__dict__
        if hasattr(obj, '__class__'):
            result = result.copy()  # create a copy to avoid modifying original obj
            result.update({'className': obj.__class__.__name__})

        new_result = {}
        for k, v in result.items():
            if hasattr(v, '__dict__') or isinstance(v, list):
                new_result[k] = JsonUtil.to_dict(v)
            elif v is None:
                pass
                # new_result[k] = ''
            else:
                new_result[k] = v

        return new_result
