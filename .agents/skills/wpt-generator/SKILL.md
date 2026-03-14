---
name: wpt-generator
description: Generate Web Platform Tests (WPT) from XML blueprints, discovering test locations via WEB_FEATURES.yml and formatting tests according to WPT conventions. Use when the user asks to generate a Web Platform Test based on a blueprint.
---
# Web Platform Test Generator

This skill enables Gemini CLI to generate Web Platform Tests (WPT) from provided XML blueprints. It locates the appropriate test directory by scanning `WEB_FEATURES.yml` files and generates the corresponding test based on the `<test_type>` defined in the blueprint.

## Workflow

When asked to generate a WPT from an XML blueprint, follow these steps:

### 1. Parse the Blueprint
Extract the following elements from the `<test_suggestion>` XML snippet provided by the user:
- `<web_feature_id>`: Used to find where the test should live.
- `<title>`: Descriptive title for the test.
- `<description>`: The underlying requirement.
- `<test_type>`: The category of the test (e.g., Testharness test, Reftest, Crashtest).
- `<pre_conditions>`: Necessary HTML/DOM setup.
- `<steps>`: Sequence of steps to reproduce the scenario.
- `<expected_result>`: The final assertion needed.

### 2. Locate the Test Directory
Determine where this test belongs in the repository by finding the corresponding `WEB_FEATURES.yml` file.

1. Run the provided Python script `scripts/find_feature_tests.py`:
   ```bash
   python3 scripts/find_feature_tests.py <web_feature_id> .
   ```
2. Review the output to determine the target directory. The output will also list existing files in that directory.

### 3. Determine the Appropriate File
Before creating a new file, you MUST rigorously check if the test logically belongs in an existing file.
1. Use `run_shell_command` or `grep_search` to find all existing tests in the target directory that match the requested `<test_type>` (e.g., search for `testharness.js` inclusions if generating a Testharness test).
2. Read the contents of those existing files to see if their scope matches the new test (e.g., looking for a `parsing/` directory if the new test is a parsing test, or an `animation/` directory for animation tests).
3. If there is an existing file that logically groups the exact same feature/behavior, read it. If it's a `testharness` test, append the new test block.
4. If no logical match is found (e.g., mixing complex animation subtests into a simple parsing test violates WPT principles), create a new file in the target directory named logically based on the `<title>` or `<web_feature_id>`.

### 4. Generate the Test
Write the appropriate WPT test using the specifications from the blueprint:
- Include `<pre_conditions>` in the body of the HTML file.
- **Domain-Specific Helpers:** Before writing out the `<steps>`, check if a built-in helper exists to avoid repetitive boilerplate.
  - If testing CSS property animatability, interpolation, or discrete flips: See [css_animations.md](references/css_animations.md). Use these helpers (e.g., `test_not_animatable()`) instead of manually setting up transitions or WAAPI.
- If no helper applies, follow the `<steps>` directly in the script block or test interactions.
- Ensure the `<expected_result>` is validated with the correct assertion method or rendering.

**For formatting requirements, style guidelines, and templates, consult the following references based on the `<test_type>`:**
- For general WPT file naming, metadata, and cross-platform guidelines: See [wpt_style_guide.md](references/wpt_style_guide.md)
- For `Testharness test`: See [testharness_style_guide.md](references/testharness_style_guide.md)
- For `Reftest`: See [reftest_style_guide.md](references/reftest_style_guide.md)
- For `Crashtest`: See [crashtest_style_guide.md](references/crashtest_style_guide.md)

Ensure you format the file appropriately according to the loaded reference.

### 5. Final Checks
- Ensure standard WPT scripts are included properly (if applicable) using absolute paths from the root server.
- Ensure crashtests end with `-crash.html` if creating a new crashtest file.
- Do not check in or commit files unless explicitly requested.
