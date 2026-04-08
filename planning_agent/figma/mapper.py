def normalize_label(name):
    return name.replace(":", " ").replace("-", " ").title()


def map_to_ui_element(node):
    name = node.get("name", "").lower()

    if any(x in name for x in ["login", "submit", "pay"]):
        return {"type": "button", "label": normalize_label(node["name"])}

    if any(x in name for x in ["email", "password"]):
        return {"type": "input", "label": normalize_label(node["name"])}

    return None