#!/usr/bin/env python3
"""
Getting Started with Revenium Middleware for Anthropic

The simplest example to get you started with Revenium tracking.
Shows all optional metadata fields documented for reference.
"""

import os
from pathlib import Path

def load_env():
    """Load environment variables from .env file."""
    env_file = Path('.env')
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ[key] = value

def main():
    """Simple example showing automatic usage tracking."""
    # Load environment variables
    load_env()

    import anthropic
    import revenium_middleware_anthropic

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "Please verify you are ready to assist me."
            }
        ]

        # Optional metadata for advanced reporting, lineage tracking, and cost allocation
        # usage_metadata={
        #     # User identification
        #     "subscriber": {
        #         "id": "user-123",
        #         "email": "user@example.com",
        #         "credential": {
        #             "name": "api-key-prod",
        #             "value": "key-abc-123"
        #         }
        #     },
        #
        #     # Organization & billing
        #     "organization_id": "my-customers-name",
        #     "subscription_id": "plan-enterprise-2024",
        #
        #     # Product & task tracking
        #     "product_id": "my-product",
        #     "task_type": "doc-summary",
        #     "agent": "customer-support",
        #
        #     # Session tracking
        #     "trace_id": "session-abc123",
        #
        #     # Quality metrics
        #     "response_quality_score": 0.95  # 0.0-1.0 scale
        # }
    )

    print(f"Response: {message.content[0].text}")


if __name__ == "__main__":
    main()
