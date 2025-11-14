# E2E Tests - Baseline and Validation

This directory contains end-to-end tests that validate the middleware against the real Revenium API.

## Purpose

These tests verify that:
1. All required fields are sent to Revenium API
2. Metadata structure (nested vs flat) works correctly
3. Streaming is metered accurately
4. Provider detection works
5. Data appears in Revenium dashboard

## Running Tests

### Prerequisites

Create a `.env` file in project root with:
```bash
ANTHROPIC_API_KEY=sk-ant-api03-...
REVENIUM_METERING_API_KEY=hak_...
REVENIUM_METERING_BASE_URL=https://api.revenium.ai
```

### Run All Tests

```bash
python tests/e2e/run_all_baseline_tests.py
```

### Run Individual Tests

```bash
python tests/e2e/test_01_required_fields.py
python tests/e2e/test_02_nested_metadata.py
python tests/e2e/test_03_flat_metadata_current.py
python tests/e2e/test_04_streaming.py
```

## Manual Verification

Each test outputs instructions for manual verification in the Revenium dashboard.

Expected events with these organization IDs:
- `e2e-test-required-fields`
- `e2e-test-nested-subscriber`
- `e2e-test-flat-keys`
- `e2e-test-streaming`

## Test Descriptions

### test_01_required_fields.py
Verifies all 13 required API fields are sent correctly.

### test_02_nested_metadata.py
Tests CORRECT nested subscriber structure (what examples SHOULD show).

### test_03_flat_metadata_current.py
Tests CURRENT flat keys pattern (what examples DO show now).
Validates backward compatibility - middleware should convert flat→nested.

### test_04_streaming.py
Tests streaming token counting and metering.

## Baseline vs Post-Fix

- **Baseline**: Run before making fixes to establish current state
- **Post-Fix**: Run after fixes to verify improvements

Compare results to ensure fixes work correctly.
