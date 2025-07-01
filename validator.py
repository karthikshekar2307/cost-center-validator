import re
from datetime import datetime

# Assumption: We check for the label under metadata.labels. If missing, resource is invalid.

def validate_cost_centre_label(resource: dict) -> bool:
    """
    Validates if a Kubernetes resource has a correct cost centre label.

    Returns True if valid, False otherwise.
    """
    current_year = datetime.now().year

    # Safely get labels
    metadata = resource.get("metadata", {})
    labels = metadata.get("labels", {})

    label_value = labels.get("metadata.megatech.inc/cost-centre")
    if not label_value:
        return False

    # Validate format: CC-NNN-YYYY
    pattern = r"^CC-(\d{3})-(\d{4})$"
    match = re.match(pattern, label_value)
    if not match:
        return False

    nnn = int(match.group(1))
    yyyy = int(match.group(2))

    # Validate NNN range
    if nnn < 50 or nnn > 150:
        return False

    # Validate year
    if yyyy != current_year:
        return False

    return True

