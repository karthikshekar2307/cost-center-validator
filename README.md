# Kubernetes Cost Centre Validator

A simple CLI tool to validate Kubernetes manifests for a required cost centre label.

## Problem

At MegaTech, all Kubernetes resources must include a cost centre label:


metadata.megatech.inc/cost-centre: CC-NNN-YYYY

Where:
- `NNN` is a 3-digit number between 050 and 150.
- `YYYY` is the current year.

## Features

- Accepts Kubernetes manifests from stdin.
- Supports multi-document YAML (separated by `---`).
- Prints a summary of valid and invalid resources.

## Usage

Install dependencies:

```bash
pip install -r requirements.txt

Validate manifests:

cat your-manifests.yaml | python main.py

Example output:
Valid resources: 2
Invalid resources: 2

Files
***** main.py: CLI entrypoint.

***** validator.py: Contains validation logic.

***** requirements.txt: Dependencies.

***** README.md: Documentation.


