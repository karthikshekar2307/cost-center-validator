import sys
import yaml
import click
from validator import validate_cost_centre_label

@click.command()
def validate():
    """
    CLI tool to validate Kubernetes manifests for cost centre labels.
    Reads from stdin.
    """
    input_text = sys.stdin.read()

    # Split into multiple YAML documents
    docs = list(yaml.safe_load_all(input_text))

    valid_count = 0
    invalid_count = 0

    for doc in docs:
        if doc is None:
            continue  # Skip empty docs

        if validate_cost_centre_label(doc):
            valid_count += 1
        else:
            invalid_count += 1

    click.echo(f"Valid resources: {valid_count}")
    click.echo(f"Invalid resources: {invalid_count}")

if __name__ == '__main__':
    validate()

