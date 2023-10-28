from typing import Dict, Optional


def owner_params(owner: Optional[str]) -> Dict[str, str]:
    if owner is None:
        return {}
    owner_split = owner.split("/")
    params = {"owner_name": owner_split[0]}
    if len(owner_split) >= 2:
        params["project_name"] = owner_split[1]
    return params
