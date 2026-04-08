from planning_agent.llm.parser import extract_json


def build_prompt(screen_data):
    return f"""
You are a QA automation expert.

STRICT RULES:
- Return ONLY valid JSON
- No explanation

Format:
[
  {{
    "scenario": "",
    "steps": [],
    "expected_result": ""
  }}
]

Generate:
- Positive test cases
- Negative test cases
- Edge cases
- Navigation test cases

Screen Data:
{screen_data}
"""


def generate_all_test_cases(cleaned_data, llm):
    results = []

    for feature in cleaned_data.get("features", []):
        for screen in feature.get("screens", []):

            screen_data = {
                "screen_name": screen["screen_name"],
                "elements": screen["elements"],
                "navigation": screen.get("navigation", [])
            }

            prompt = build_prompt(screen_data)

            # 🔥 Safe LLM call
            try:
                raw_output = llm.generate(prompt)
            except Exception as e:
                print(f"❌ LLM failed: {e}")
                raw_output = "[]"

            parsed_output = extract_json(raw_output)

            if not parsed_output:
                print("⚠️ Invalid JSON from LLM")

            results.append({
                "feature": feature["feature_name"],
                "screen": screen["screen_name"],
                "test_cases": parsed_output
            })

    return results