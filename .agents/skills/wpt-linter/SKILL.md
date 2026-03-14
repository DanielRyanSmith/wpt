---
name: wpt-linter
description: Run the WPT lint tool (`./wpt lint`) on specified files or directories and automatically fix any reported lint errors. Use when the user asks to lint a file or fix linting issues in WPT.
---
# WPT Linter

This skill enables Gemini CLI to automatically run the WPT linting tool (`./wpt lint`) on specific files or directories and fix any reported errors, ensuring that tests conform to the WPT style guidelines.

## Workflow

When asked to lint a file or fix lint errors, follow these steps:

### 1. Run the Lint Command
Execute the WPT lint command on the target file or directory provided by the user.

```bash
./wpt lint <target_path>
```
*(Make sure to run this command from the root of the WPT repository).*

### 2. Analyze the Output
Review the output of the `./wpt lint` command. 
- If the output indicates that all checks passed (or there are no errors), report success to the user and stop.
- If the output contains errors, identify the specific file paths, line numbers, and error types.

**Common WPT Lint Errors:**
- `TRAILING WHITESPACE`: Remove spaces or tabs at the end of the specified lines.
- `INDENT TABS`: Replace tab characters with spaces (typically 2 or 4 spaces depending on the surrounding context).
- `CR AT EOL`: Replace Windows-style line endings (`\r\n`) with UNIX-style line endings (`\n`).
- `W3C-SPELLING`: Correct the spelling of specific words as mandated by W3C (e.g., changing "Webkit" to "WebKit").
- `MISSING LINK`: A CSS reftest is missing a `<link rel="match">`, `<link rel="mismatch">`, or `<link rel="help">`.

### 3. Fix the Errors
For each error reported, inspect the file and apply the necessary fix. 
- You can use the `read_file` or `grep_search` tools to pinpoint the exact lines containing the issues.
- Use the `replace` tool to fix small, targeted issues (like trailing whitespace or tabs).
- For repetitive issues (like fixing all trailing whitespace in a file), you may use a `run_shell_command` with `sed` if it is more efficient, e.g.:
  ```bash
  sed -i 's/[ \t]*$//' <file_path>  # Removes trailing whitespace
  sed -i 's/\t/    /g' <file_path>  # Replaces tabs with 4 spaces
  ```

### 4. Verify the Fixes
After applying the fixes, run the `./wpt lint <target_path>` command again to verify that all errors have been resolved.

- If errors remain, repeat the Analyze and Fix steps until the lint command passes without errors.
- Once the lint command passes, inform the user that the file has been successfully linted and fixed.

### 5. Final Checks
- Ensure that the fixes did not alter the fundamental behavior or logic of the test.
- Do not check in or commit the files unless explicitly requested by the user.
