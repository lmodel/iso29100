"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import iso29100.datamodel.iso29100
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml')))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml')))


def _target_class_for(filepath):
    target_class_name = Path(filepath).stem.split("-")[0]
    return getattr(iso29100.datamodel.iso29100, target_class_name)


def test_valid_example_files_exist():
    """Test that valid example coverage exists."""
    assert VALID_EXAMPLE_FILES


def test_invalid_example_files_exist():
    """Test that invalid example coverage exists."""
    assert INVALID_EXAMPLE_FILES


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    tgt_class = _target_class_for(filepath)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test loading of all invalid data files fails."""
    tgt_class = _target_class_for(filepath)
    with pytest.raises(ValueError):
        yaml_loader.load(filepath, target_class=tgt_class)
