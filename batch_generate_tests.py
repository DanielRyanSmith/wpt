#!/usr/bin/env python3
import re
import subprocess
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Batch generate WPT tests from an audit file using Gemini CLI.")
    parser.add_argument("audit_file", help="Path to the markdown/XML file containing <test_suggestion> blocks.")
    parser.add_argument("--feature-id", required=True, help="The web_feature_id to inject into the blueprints.")
    parser.add_argument("--model", default="gemini-3.1-pro-preview", help="The Gemini model to use (default: gemini-3.1-pro-preview).")
    args = parser.parse_args()

    file_path = Path(args.audit_file)
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")

    # Extract all <test_suggestion> blocks
    suggestions = re.findall(r"(<test_suggestion>.*?</test_suggestion>)", content, re.DOTALL)

    if not suggestions:
        print("No <test_suggestion> blocks found in the file.")
        sys.exit(0)

    print(f"Found {len(suggestions)} test suggestions. Starting batch generation using model {args.model}...\n")

    for i, suggestion in enumerate(suggestions, 1):
        print(f"==================================================")
        print(f" Generating Test {i} of {len(suggestions)}")
        print(f"==================================================")

        # Inject web_feature_id if it's missing
        if "<web_feature_id>" not in suggestion:
            # Insert it right after the closing </title> tag
            suggestion = re.sub(
                r"(</title>)",
                f"\\1\n    <web_feature_id>{args.feature_id}</web_feature_id>",
                suggestion,
                count=1
            )

        # Construct the prompt for the CLI
        prompt = (
            "Use the wpt-generator skill to generate the following test. "
            "Rigorously follow all instructions in the skill. Do not ask for user confirmation, "
            "just perform the necessary research and write the final test file.\n\n"
            f"{suggestion}"
        )

        # Call the Gemini CLI in single-turn headless mode.
        try:
            # We use bash -ic to force an interactive shell so it loads aliases/nvm.
            # -p ensures the CLI exits automatically after completion.
            # --approval-mode=yolo ensures the agent does not hang waiting for manual tool confirmations.
            cmd = ['bash', '-ic', f'gemini --model {args.model} --approval-mode=yolo -p "$0"', prompt]

            subprocess.run(cmd, check=True)
            print(f"\n✓ Test {i} completed successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"\n✗ Error generating test {i}. Gemini CLI exited with code: {e.returncode}\n")
        except FileNotFoundError:
            print("\nError: 'gemini' CLI command not found. Ensure it is installed and in your PATH.")
            sys.exit(1)

    print("Batch generation complete!")

if __name__ == "__main__":
    main()
