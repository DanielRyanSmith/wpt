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
- `<spec_url>` (can be multiple): A link to the specification. You MUST include these exact URLs in the generated test (using `<link rel="help" href="...">` for HTML tests, or as a single-line comment for `.js` tests).

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
3. **IDL Check:** If the `<description>` involves testing interface exposure, attributes, or methods, you MUST check the repository's `interfaces/` directory for a corresponding `.idl` file (e.g., `interfaces/crash-reporting.idl`). If it exists, this strongly indicates you should use `idlharness.js` instead of manual boolean assertions.
4. Read 1 or 2 existing tests that seem related to the `<description>`. Treat these as "Golden Examples", especially noting if they utilize shared helper scripts or array-driven testing loops.
5. Based on the requirement and the golden examples, decide on the best **Test Type**:
   - **Testharness test**: Best for JS APIs, parsing, DOM manipulation, or computed CSS values.
   - **Reftest**: Best for visual/rendering layout matching.
   - **Crashtest**: Best for ensuring no browser crash occurs.
   - **wdspec test**: Best for verifying WebDriver Classic or WebDriver BiDi protocols. Written in **Python** using pytest.
   - **Manual test (ABSOLUTE LAST RESORT)**: You MUST NOT write a manual test unless it is fundamentally impossible to test the behavior using current automated tooling (e.g., standard JS, `testharness.js`, or `testdriver.js`). This format is strictly reserved for behaviors that require unavoidable physical human interaction or OS-level interventions (e.g., forcefully crashing a browser process via the OS task manager). If automation is possible, you MUST automate it.

### 4. Determine the Appropriate File(s) & Name
Before creating a new file, rigorously check if the test logic belongs in existing files. **Minimize boilerplate by reusing existing files whenever possible.**
1. **Analyze Directory Paradigms:** Check if the target directory splits tests by category (e.g., separating valid vs. invalid values, or computed vs. parsing behavior).
2. **Split the Blueprint if Necessary:** A single XML blueprint might encompass multiple test categories. If the directory separates testing into distinct files (e.g., `feature-valid.html` and `feature-invalid.html`), **you MUST split the test logic across the respective existing files** rather than creating a single, monolithic new file.
3. **Append to Existing Files:** Read the logically matching file(s). If they are `testharness` tests, append your new test blocks to them.
4. **CRITICAL RULE - Manual Test Consolidation:** If you determine the test type must be `manual`, you MUST aggressively consolidate your test logic into existing manual tests whenever possible. Do not generate multiple manual test files that require identical user interventions (e.g., repeatedly clicking a button or crashing a process) across different files, even if the blueprint implies an isolated feature. Prioritize tester UX by testing multiple permutations in a single manual execution using data-driven loops. Furthermore, when appending to an existing data-driven loop in a manual test, check if the setup and intervention parameters overlap with an existing case. If they do, you MUST refactor the loop to evaluate multiple assertions against a single shared execution/intervention, rather than blindly adding a new row that forces an identical, redundant user intervention.
5. **Reftest Reference Search:** If you selected **Reftest**, you MUST search the target directory (and any `reference/` subdirectories) for existing reusable reference files (e.g., `ref-filled-green-100px-square.xht`) before deciding to create a new one. Do NOT generate a duplicate reference file if a suitable one exists.
6. **Create New Only When Necessary:** Only if no logical match is found (even after considering splitting and manual consolidation), plan to create a new file. **Consult `references/wpt_style_guide.md` to determine the correct filename extension and suffixes** (e.g., `.html`, `.window.js`, `.any.js`) based on your chosen test type. Name the file logically based on the `<title>` or `<web_feature_id>`.

### 5. Load References & Generate the Test
**Before writing any code**, you MUST read the appropriate style guides to ensure correct formatting and syntax:
- For general guidelines (apply to all): See [wpt_style_guide.md](references/wpt_style_guide.md)
- If Testharness: See [testharness_style_guide.md](references/testharness_style_guide.md)
- If Reftest: See [reftest_style_guide.md](references/reftest_style_guide.md)
- If Crashtest: See [crashtest_style_guide.md](references/crashtest_style_guide.md)
- If the test requires simulated user interaction (clicks, typing, gestures): See [automation_guide.md](references/automation_guide.md)
- If the test is a wdspec test (testing the WebDriver protocol itself): See [wdspec_guide.md](references/wdspec_guide.md)
- If the test strictly requires a human operator and cannot be automated: See [manual_test_style_guide.md](references/manual_test_style_guide.md)
- If the test involves Web IDL interfaces (e.g., testing `[Exposed]` attributes, method existence, or interface exposure): See [idlharness_guide.md](references/idlharness_guide.md)
- If the test requires cross-origin requests, custom HTTP headers, specific status codes, or dynamic server logic: See [server_features_guide.md](references/server_features_guide.md)

Write the appropriate WPT test to strictly satisfy the `<description>`:
- **CRITICAL RULE: Style Guides > Golden Examples:** Existing tests ("Golden Examples") often contain legacy code and violate current best practices. **You MUST prioritize the explicit rules in the style guides over the paradigms found in surrounding files.** Do not blindly copy outdated instantiation patterns (e.g., manual `AbortController` setups instead of `AbortSignal.abort()`, unbounded polling instead of sentinels) or generic assertion patterns (e.g., `assert_true('key' in obj)` instead of `assert_own_property(obj, 'key')`). Use existing files to understand the *domain logic*, but rely exclusively on the style guides for the *implementation syntax*.
- **Omit HTML Boilerplate:** Unless the test strictly requires attaching attributes to the root elements, you MUST omit standard `<html>`, `<head>`, and `<body>` tags in your generated `.html` files (including references) to keep tests focused and concise, even if "Golden Examples" include them. Start directly with `<!DOCTYPE html>` and `<meta charset="utf-8">`.
- **Deduce Expectations:** Carefully deduce the exact pass/fail condition and assertions from the `<description>`. If the requirement is highly complex or vague, use the `fetch_spec.py` script (found in your `<available_resources>` panel) to fetch the `<spec_url>` text to gain deeper context before writing the test.
   ```bash
   python3 <absolute_path_to_fetch_spec.py> "<spec_url>"
   ```
- **CRITICAL RULE: Minimize Specification Boilerplate:** Only use the APIs strictly required to trigger the behavior described in the `<description>`. Do not include optional features or initialization boilerplate from the spec unless explicitly required by the core assertion. For example, if a specification defines an implicit behavior (like dispatching a report when a process crashes), do not initialize optional JS APIs associated with that feature just to "set up" the environment.
- **CRITICAL RULE: Domain Helpers > Golden Examples:** Check if a built-in helper exists in the local `resources/` directory to avoid repetitive boilerplate. Even if your "Golden Example" writes out boilerplate logic manually (e.g., manually polling, fetching, resolving a sequence of events, or establishing positive controls), you MUST aggressively replace that boilerplate if a higher-level abstraction exists in a local helper file. **When you identify a helper file, you MUST perform an exhaustive audit of its entire exported API (e.g., reading the whole `helper.js` file) to discover all available utilities (like `wait()`, `delay()`, or custom assertions). Do not restrict your usage only to the specific functions the Golden Example used.**
   - If testing CSS property parsing, inheritance, computed values, or shorthands: See [css_testcommon.md](references/domain_helpers/css_testcommon.md)
   - If testing CSS property animatability, interpolation, or discrete flips: See [css_animations.md](references/domain_helpers/css_animations.md)
   - If testing cross-origin network or fetch behaviors via Javascript: See [get_host_info.md](references/domain_helpers/get_host_info.md)
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
   - **CRITICAL RULE - Manual Tests:** If the test you created or modified is a manual test (e.g., ends in `-manual.html` or requires human intervention), you **MUST SKIP** this execution step entirely. The WPT runner cannot execute manual tests headlessly and will incorrectly report `CRITICAL Unable to find any tests at the path(s)`. Rely strictly on the linter for manual tests.
   - **Analyze the Output:** Read the test runner's output carefully.
   - **Self-Correct:** If the runner reports a `Harness Error`, `SyntaxError`, a timeout, or a failure that indicates a flaw in your test logic (e.g., calling an undefined helper function or making an incorrect assertion), you MUST open the file, fix the bug, and re-run the test.
   - Repeat this execute-and-fix loop until the test executes successfully without syntax or harness errors. **Maximum 3 attempts.** If the test still fails after 3 correction attempts, stop debugging and proceed to finalize. *(Note: If the test fails because the browser genuinely does not support the feature, that is acceptable—your goal is to ensure the **test code** itself is valid.)*

### 7. Finalizing
- Ensure standard WPT scripts are included properly (if applicable) using absolute paths from the root server.
- Ensure crashtests end with `-crash.html` if creating a new crashtest file.
- **Clean Up:** Explicitly delete any temporary prototype files, scripts, or intermediate files you created during the research, testing, or debugging phases to keep the repository clean.
- Do not check in or commit files unless explicitly requested.
