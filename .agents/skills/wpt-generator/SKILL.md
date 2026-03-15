---
name: wpt-generator
description: Generate Web Platform Tests (WPT) from minimal XML blueprints. The agent will autonomously determine the test type and implementation details by analyzing existing repository paradigms. Use when the user asks to generate a Web Platform Test based on a blueprint.
---
# Web Platform Test Generator

This skill enables Gemini CLI to generate Web Platform Tests (WPT) from minimal XML blueprints. Because the blueprint only contains high-level requirements, you must rely on existing codebase paradigms to determine how the test should be written.

## Workflow

When asked to generate a WPT from an XML blueprint, follow these steps:

### 1. Parse the Blueprint
Extract the following elements from the `<test_suggestion>` XML snippet provided by the user:
- `<web_feature_id>`: Used to find where the test should live.
- `<title>`: Descriptive title for the test.
- `<description>`: The underlying requirement or specification behavior to test.

### 2. Locate the Test Directory
Determine where this test belongs in the repository by finding the corresponding `WEB_FEATURES.yml` file.
1. Run the provided Python script:
   ```bash
   python3 scripts/find_feature_tests.py <web_feature_id> .
   ```
2. Review the output to determine the target directory.

### 3. Research Existing Paradigms & Determine Test Type
Since you are not provided with explicit steps or a test type, you MUST research how similar tests are written in this specific directory.
1. Use `run_shell_command` or `grep_search` to list existing tests in the target directory.
2. Read 1 or 2 existing tests that seem related to the `<description>`. Treat these as "Golden Examples".
3. Based on the requirement and the golden examples, decide on the best **Test Type**:
   - **Testharness test**: Best for JS APIs, parsing, DOM manipulation, or computed CSS values.
   - **Reftest**: Best for visual/rendering layout matching.
   - **Crashtest**: Best for ensuring no browser crash occurs.

### 4. Determine the Appropriate File & Name
Before creating a new file, rigorously check if the test logically belongs in an existing file.
1. If your research reveals an existing file that logically groups the exact same feature/behavior (e.g., a shared `parsing.html` file), read it. If it's a `testharness` test, append your new test block to it.
2. If no logical match is found, plan to create a new file. **Consult `references/wpt_style_guide.md` to determine the correct filename extension and suffixes** (e.g., `.html`, `.window.js`, `.any.js`) based on your chosen test type. Name the file logically based on the `<title>` or `<web_feature_id>`.

### 5. Load References & Generate the Test
**Before writing any code**, you MUST read the appropriate style guides to ensure correct formatting and syntax:
- For general guidelines (apply to all): See [wpt_style_guide.md](references/wpt_style_guide.md)
- If Testharness: See [testharness_style_guide.md](references/testharness_style_guide.md)
- If Reftest: See [reftest_style_guide.md](references/reftest_style_guide.md)
- If Crashtest: See [crashtest_style_guide.md](references/crashtest_style_guide.md)

Write the appropriate WPT test to strictly satisfy the `<description>`:
- **Deduce Expectations:** Carefully deduce the exact pass/fail condition and assertions from the `<description>`.
- **Domain-Specific Helpers:** Check if a built-in helper exists to avoid repetitive boilerplate. If testing CSS property animatability, interpolation, or discrete flips: See [css_animations.md](references/css_animations.md) and use helpers like `test_not_animatable()`.
- **Implementation:** Write the test logic, setup, and assertions autonomously. Mirror the style, structure, and imports of the "Golden Examples". *Note: If the target directory lacks examples of your chosen Test Type, rely heavily on the style guides.*

### 6. Final Checks
- Ensure standard WPT scripts are included properly (if applicable) using absolute paths from the root server.
- Ensure crashtests end with `-crash.html` if creating a new crashtest file.
- Do not check in or commit files unless explicitly requested.
