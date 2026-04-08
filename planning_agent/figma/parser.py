def extract_nodes(node, elements):
    if not isinstance(node, dict):
        return

    if not node.get("visible", True):
        return

    elements.append(node)

    for child in node.get("children", []):
        extract_nodes(child, elements)


def get_features_and_screens(figma_json):
    features = []

    pages = figma_json.get("document", {}).get("children", [])

    for page in pages:
        for section in page.get("children", []):
            if section.get("type") not in ["SECTION", "FRAME"]:
                continue

            feature_name = section.get("name", "Unknown Feature")
            screens = []

            for node in section.get("children", []):
                if node.get("type") == "FRAME":
                    screens.append(node)

            if screens:
                features.append({
                    "feature_name": feature_name,
                    "screens": screens
                })

    return features