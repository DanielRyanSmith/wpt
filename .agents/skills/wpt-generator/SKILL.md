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
- **Domain-Specific Helpers & Idioms:** Before writing out the `<steps>`, check if a built-in helper exists to avoid repetitive boilerplate.
  - If testing CSS property animatability, interpolation, or discrete flips: See [css_animations.md](references/css_animations.md). Use these helpers (e.g., `test_not_animatable()`) instead of manually setting up transitions or WAAPI.
  - **Local Feature Helpers:** Deeply inspect the local `resources/` directory (e.g., `fetch-later-helper.js`) or sibling `.js` tests for existing helper functions and structural patterns (like `parallelPromiseTest`, `loadScriptAsIframe`, `expectBeacon`). Read existing tests in the same directory to identify and reuse these idiomatic testing patterns instead of writing manual DOM manipulation (like raw `iframe` boilerplate) from scratch.
- **Optimize and Modernize (Crucial First Step):** The blueprint `<steps>` are behavioral guidelines, not literal code. You MUST prioritize idiomatic WPT patterns, helper functions, and modern primitives over a line-by-line translation of the `<steps>`.
  - Look for opportunities to reduce boilerplate using modern web platform primitives (e.g., using `AbortSignal.abort()` instead of an `AbortController` if only a signal is needed).
  - Use the most precise `testharness.js` assertions available (e.g., `assert_throws_exactly`).
  - **Data-Driven / Parameterized Tests:** If appending a new scenario to an existing test file that tests a very similar scenario (e.g., throwing a standard `DOMException` vs a custom `Error`), refactor the test to use an array of inputs and a `for...of` loop rather than copying and pasting an entire `test()` block.
  - **Contextual Simplification (Avoid Cargo Culting):** When appending a new test block to an existing file, do not blindly copy the structural boilerplate (like `iframe` wrappers, worker instantiation, or event listener setups) from sibling tests unless the new test logically requires it. Evaluate the specific trigger mechanism of your new test (e.g., a timeout vs. a document unload) and strip out unnecessary scaffolding to make the test as direct and minimal as possible.
  - **File-Level Conventions:** Look at sibling files. If they universally use `'use strict';`, ensure your new or appended test file uses it.
  - **CRITICAL:** You must only apply optimizations if they strictly preserve the exact behavior and feature being tested by the blueprint. Do not alter the intent of the test.
- If no helper applies, follow the `<steps>` directly in the script block or test interactions.
- Ensure the `<expected_result>` is validated with the correct assertion method or rendering.

**For formatting requirements, style guidelines, and templates, consult the following references based on the `<test_type>`:**
- For general WPT file naming, metadata, and cross-platform guidelines: See [wpt_style_guide.md](references/wpt_style_guide.md)
- For `Testharness test`: See [testharness_style_guide.md](references/testharness_style_guide.md)
- For `Reftest`: See [reftest_style_guide.md](references/reftest_style_guide.md)
- For `Crashtest`: See [crashtest_style_guide.md](references/crashtest_style_guide.md)

Ensure you format the file appropriately according to the loaded reference.

### 5. Validate and Fix (Mandatory)
A test is not complete until it has been empirically validated to run without framework errors and to conform to WPT style guidelines.

1. **Linting:** Run the WPT linter on the newly created or modified file:
   ```bash
   ./wpt lint <path_to_test_file>
   ```
   If the linter reports errors (like `TRAILING WHITESPACE` or `CR AT EOL`), you MUST fix the file and re-run the linter until it passes cleanly.

2. **Headless Execution:** Verify the structural and syntactical integrity of the test by running it in a headless browser:
   ```bash
   ./wpt run chrome <path_to_test_file> --headless
   ```
   - **Analyze the Output:** Look for `Harness Error`, `SyntaxError`, or timeouts.
   - **Iterate:** If the test fails to run due to a syntax error, bad import, or malformed HTML, read the error output, fix the code, and run it again. (Note: A test failing because the browser doesn't support the feature yet is acceptable, but a test failing because of bad JavaScript syntax is not).

### 6. Final Checks
- **Cleanup:** Ensure that any temporary files, utility scripts, or scaffolding files created during the generation, optimization, or validation process (e.g., `temp.js`, `patch.js`) are completely deleted from the workspace.
- Do not check in or commit files unless explicitly requested.