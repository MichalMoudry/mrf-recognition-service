"""
Module containing constructs for recognition service API metadata.
"""

GENERAL_TAG = "General"
DOCUMENT_PROCESSING = "Document processing"

tags = [
    {
        "name": GENERAL_TAG,
        "description": "A general operation with the recognition service.",
    },
    {
        "name": DOCUMENT_PROCESSING,
        "description": "A collection of operations for processing documents.",
    }
]
