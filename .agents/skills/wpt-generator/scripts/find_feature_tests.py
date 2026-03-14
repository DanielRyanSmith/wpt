#!/usr/bin/env python3
import os
import sys
import yaml
import glob
from pathlib import Path

def find_tests_for_feature(root_dir, target_feature):
    found_paths = []
    
    for root, dirs, files in os.walk(root_dir):
        if 'WEB_FEATURES.yml' in files:
            filepath = os.path.join(root, 'WEB_FEATURES.yml')
            try:
                with open(filepath, 'r') as f:
                    data = yaml.safe_load(f)
                    if not data or 'features' not in data:
                        continue
                        
                    for feature in data['features']:
                        if isinstance(feature, dict) and feature.get('name') == target_feature:
                            # Feature matches! We record the directory or files
                            files_pattern = feature.get('files', '**')
                            if isinstance(files_pattern, str):
                                found_paths.append((root, [files_pattern]))
                            elif isinstance(files_pattern, list):
                                found_paths.append((root, files_pattern))
            except Exception as e:
                # Silently ignore parsing errors or unreadable files
                pass
                
    return found_paths

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 find_feature_tests.py <web_feature_id> [root_dir]")
        sys.exit(1)
        
    target_feature = sys.argv[1]
    root_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    results = find_tests_for_feature(root_dir, target_feature)
    
    if not results:
        print(f"No tests found for feature '{target_feature}' in {root_dir}")
        sys.exit(0)
        
    print(f"Tests for feature '{target_feature}' found in:")
    for directory, patterns in results:
        print(f"\nDirectory: {directory}")
        print(f"  Patterns: {', '.join(patterns)}")
        
        # Briefly list up to 5 actual files to give context
        # Convert patterns to glob
        matched_files = []
        for pat in patterns:
            if pat == '**':
                matched_files.extend(list(Path(directory).rglob('*.html')))
                matched_files.extend(list(Path(directory).rglob('*.js')))
            else:
                for p in Path(directory).rglob(pat):
                    if p.is_file():
                        matched_files.append(p)
                        
        matched_files = list(set(matched_files)) # deduplicate
        if matched_files:
            print("  Example existing files:")
            for p in matched_files[:5]:
                try:
                    rel_p = p.relative_to(root_dir)
                    print(f"    - {rel_p}")
                except ValueError:
                    print(f"    - {p}")
            if len(matched_files) > 5:
                print(f"    ... and {len(matched_files) - 5} more files.")
