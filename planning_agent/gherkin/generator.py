def generate_gherkin(figma_data):
    gherkin_output = ""

    for feature in figma_data.get("features", []):
        feature_name = feature.get("feature_name", "Unknown Feature")

        # Feature header
        gherkin_output += f"\nFeature: {feature_name}\n"

        for screen in feature.get("screens", []):
            screen_name = screen.get("screen_name", "Unknown Screen")

            # -------------------------------
            # ELEMENT-BASED SCENARIOS
            # -------------------------------
            for element in screen.get("elements", []):
                label = element.get("label", "Unknown Element")
                element_type = element.get("type", "")

                # Button scenario
                if element_type == "button":
                    gherkin_output += f"""
  Scenario: Verify {label} button functionality
    Given user is on {screen_name} screen
    When user clicks {label}
    Then expected action should be performed
"""

                # Input scenario
                elif element_type == "input":
                    gherkin_output += f"""
  Scenario: Verify input for {label}
    Given user is on {screen_name} screen
    When user enters value in {label}
    Then value should be accepted
"""

            # -------------------------------
            # NAVIGATION SCENARIOS
            # -------------------------------
            for nav in screen.get("navigation", []):
                from_screen = nav.get("from", screen_name)
                to_screen = nav.get("to", "Next Screen")
                action = nav.get("action", "user performs action")

                gherkin_output += f"""
  Scenario: Verify navigation from {from_screen} to {to_screen}
    Given user is on {from_screen} screen
    When {action}
    Then user should navigate to {to_screen}
"""

    return gherkin_output.strip()