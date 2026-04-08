class PlanningAgent:
    def __init__(self, llm_enabled=True):
        self.llm_enabled = llm_enabled

    def run(self, figma_data=None, use_api=True):
        from planning_agent.figma.api import get_figma_data
        from planning_agent.figma.cleaner import clean_figma_json
        from planning_agent.gherkin.generator import generate_gherkin
        from planning_agent.llm.test_generator import generate_all_test_cases

        # Step 1: Get data
        if use_api:
            data = get_figma_data()
        else:
            data = figma_data

        # Step 2: Clean
        cleaned = clean_figma_json(data)

        # Step 3: Gherkin
        gherkin = generate_gherkin(cleaned)

        # Step 4: LLM
        test_cases = None
        if self.llm_enabled:
            test_cases = generate_all_test_cases(cleaned)

        return {
            "cleaned_data": cleaned,
            "gherkin": gherkin,
            "test_cases": test_cases
        }