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
1. Run the `find_feature_tests.py` script. **Important:** Do not run `python3 scripts/...` from the repository root. You must use the absolute path to `find_feature_tests.py` provided in the `<available_resources>` panel of your activated skill:
   ```bash
   python3 <absolute_path_to_find_feature_tests.py> <web_feature_id> .
   ```
2. Review the output to determine the target directory.

### 3. Research Existing Paradigms & Determine Test Type
Since you are not provided with explicit steps or a test type, you MUST research how similar tests are written for this feature, both in the target directory and across the broader codebase. **Avoid "Tunnel Vision":** Do not restrict your research solely to the output of `find_feature_tests.py`.
1. Use `run_shell_command` or `grep_search` to list existing tests in the target directory.
2. Broaden your search: Grep the entire repository (or related parent directories) for the API name or feature (e.g., `fetchLater`) to find existing test ecosystems, helper files (`resources/`), or data-driven testing paradigms that might live in adjacent directories.
3. Read 1 or 2 existing tests that seem related to the `<description>`. Treat these as "Golden Examples", especially noting if they utilize shared helper scripts or array-driven testing loops.
4. Based on the requirement and the golden examples, decide on the best **Test Type**:
   - **Testharness test**: Best for JS APIs, parsing, DOM manipulation, or computed CSS values.
   - **Reftest**: Best for visual/rendering layout matching.
   - **Crashtest**: Best for ensuring no browser crash occurs.

### 4. Determine the Appropriate File(s) & Name
Before creating a new file, rigorously check if the test logic belongs in existing files. **Minimize boilerplate by reusing existing files whenever possible.**
1. **Analyze Directory Paradigms:** Check if the target directory splits tests by category (e.g., separating valid vs. invalid values, or computed vs. parsing behavior).
2. **Split the Blueprint if Necessary:** A single XML blueprint might encompass multiple test categories. If the directory separates testing into distinct files (e.g., `feature-valid.html` and `feature-invalid.html`), **you MUST split the test logic across the respective existing files** rather than creating a single, monolithic new file.
3. **Append to Existing Files:** Read the logically matching file(s). If they are `testharness` tests, append your new test blocks to them.
4. **Create New Only When Necessary:** Only if no logical match is found (even after considering splitting), plan to create a new file. **Consult `references/wpt_style_guide.md` to determine the correct filename extension and suffixes** (e.g., `.html`, `.window.js`, `.any.js`) based on your chosen test type. Name the file logically based on the `<title>` or `<web_feature_id>`.

### 5. Load References & Generate the Test
**Before writing any code**, you MUST read the appropriate style guides to ensure correct formatting and syntax:
- For general guidelines (apply to all): See [wpt_style_guide.md](references/wpt_style_guide.md)
- If Testharness: See [testharness_style_guide.md](references/testharness_style_guide.md)
- If Reftest: See [reftest_style_guide.md](references/reftest_style_guide.md)
- If Crashtest: See [crashtest_style_guide.md](references/crashtest_style_guide.md)

Write the appropriate WPT test to strictly satisfy the `<description>`:
- **CRITICAL RULE: Style Guides > Golden Examples:** Existing tests ("Golden Examples") often contain legacy code and violate current best practices. **You MUST prioritize the explicit rules in the style guides over the paradigms found in surrounding files.** Do not blindly copy outdated instantiation patterns (e.g., manual `AbortController` setups instead of `AbortSignal.abort()`, unbounded polling instead of sentinels). Use existing files to understand the *domain logic*, but rely exclusively on the style guides for the *implementation syntax*.
- **Deduce Expectations:** Carefully deduce the exact pass/fail condition and assertions from the `<description>`.
- **CRITICAL RULE: Domain Helpers > Golden Examples:** Check if a built-in helper exists in the local `resources/` directory to avoid repetitive boilerplate. Even if your "Golden Example" writes out boilerplate logic manually (e.g., manually polling, fetching, resolving a sequence of events, or establishing positive controls), you MUST aggressively replace that boilerplate if a higher-level abstraction exists in a local helper file. Read and fully comprehend the helper functions imported by your Golden Examples. If testing CSS property animatability, interpolation, or discrete flips: See [css_animations.md](references/css_animations.md) and use helpers like `test_not_animatable()`.
- **Implementation:** Write the test logic, setup, and assertions autonomously. **CRITICAL:** When generating tests for multiple permutations or variations of an API, you MUST NOT write flat, repetitive test blocks. You MUST adhere to the Data-Driven Testing mandate in `testharness_style_guide.md` using arrays and loops. *Note: If the target directory lacks examples of your chosen Test Type, rely entirely on the style guides.*

### 6. Validation & Self-Correction (CRITICAL)
Before completing the task, you MUST validate that the code you generated is syntactically correct, properly formatted, and functions as intended.

1. **Linting:** Run the WPT linter on the file you created/modified:
   ```bash
   ./wpt lint <path_to_file>
   ```
   - If the linter reports errors (e.g., `TRAILING WHITESPACE`, `INDENT TABS`), you MUST use `replace` or `sed` to fix the errors and re-run the linter until it passes cleanly.

2. **Execution:** You MUST run it using the headless browser runner:
   ```bash
   ./wpt run chrome <path_to_file> --headless
   ```
   - **Analyze the Output:** Read the test runner's output carefully.
   - **Self-Correct:** If the runner reports a `Harness Error`, `SyntaxError`, a timeout, or a failure that indicates a flaw in your test logic (e.g., calling an undefined helper function or making an incorrect assertion), you MUST open the file, fix the bug, and re-run the test.
   - Repeat this execute-and-fix loop until the test executes successfully without syntax or harness errors. **Maximum 3 attempts.** If the test still fails after 3 correction attempts, stop debugging and proceed to finalize. *(Note: If the test fails because the browser genuinely does not support the feature, that is acceptable—your goal is to ensure the **test code** itself is valid.)*

### 7. Finalizing
- Ensure standard WPT scripts are included properly (if applicable) using absolute paths from the root server.
- Ensure crashtests end with `-crash.html` if creating a new crashtest file.
- **Clean Up:** Explicitly delete any temporary prototype files, scripts, or intermediate files you created during the research, testing, or debugging phases to keep the repository clean.
- Do not check in or commit files unless explicitly requested.
