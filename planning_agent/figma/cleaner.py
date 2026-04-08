from planning_agent.figma.parser import extract_nodes, get_features_and_screens
from planning_agent.figma.mapper import map_to_ui_element
from planning_agent.figma.navigation import map_ids, extract_navigation


def process_screen(screen):
    elements = []
    seen = set()
    all_nodes = []

    extract_nodes(screen, all_nodes)

    for node in all_nodes:
        ui = map_to_ui_element(node)
        if ui:
            key = (ui["type"], ui["label"])
            if key not in seen:
                seen.add(key)
                elements.append(ui)

    return elements


def clean_figma_json(figma_json):
    features = get_features_and_screens(figma_json)

    id_to_name = {}
    map_ids(figma_json["document"], id_to_name)

    final = []

    for feature in features:
        screens_data = []

        for screen in feature["screens"]:
            name = screen.get("name", "Unknown")

            elements = process_screen(screen)
            navigation = extract_navigation(screen, name, id_to_name)

            if elements:
                screens_data.append({
                    "screen_name": name,
                    "elements": elements,
                    "navigation": navigation
                })

        if screens_data:
            final.append({
                "feature_name": feature["feature_name"],
                "screens": screens_data
            })

    return {"features": final}