"""Sanity tests for MIR Medical Intelligence."""
import pytest
import mir_medical

def test_package_import():
    assert mir_medical.__version__ == "2.2.0"
