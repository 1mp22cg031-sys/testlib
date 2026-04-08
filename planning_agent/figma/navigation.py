def map_ids(node, id_to_name):
    if not isinstance(node, dict):
        return

    if "id" in node and "name" in node:
        id_to_name[node["id"]] = node["name"]

    for child in node.get("children", []):
        map_ids(child, id_to_name)


def extract_navigation(node, current_screen, id_to_name):
    nav = []

    for interaction in node.get("interactions", []):
        for action in interaction.get("actions", []):
            dest = action.get("destinationId")

            if dest in id_to_name:
                nav.append({
                    "from": current_screen,
                    "to": id_to_name[dest],
                    "action": f"Click {node.get('name')}"
                })

    for child in node.get("children", []):
        nav.extend(extract_navigation(child, current_screen, id_to_name))

    return nav