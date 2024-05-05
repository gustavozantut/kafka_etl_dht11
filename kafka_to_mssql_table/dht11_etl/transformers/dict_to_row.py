from typing import Dict, List

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(messages: List[Dict], *args, **kwargs):
    """
    Template code for a transformer block.

    Args:
        messages: List of messages in the stream.

    Returns:
        Transformed messages
    """
    # Specify your transformation logic here

    for i, message in enumerate(messages):

        # Create a dictionary for DataFrame
        flat_result = {
            "Temperature": message["Temperature"],
            "Humidity": message["Humidity"],
            "Timestamp": message["Timestamp"]
        }
        messages[i] = flat_result


    return messages
