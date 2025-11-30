"""
Basic structure tests
"""
import pytest


def test_package_structure():
    """Test that package structure exists"""
    import src.customer_analytics
    assert hasattr(src.customer_analytics, '__path__')


def test_config_module():
    """Test config module exists"""
    from src.customer_analytics import config
    assert config is not None


def test_utils_module():
    """Test utils module exists"""
    from src.customer_analytics import utils
    assert utils is not None


def test_constants():
    """Test constants are accessible"""
    from src.customer_analytics.utils.constants import ROOT, DATA_DIR
    assert ROOT is not None
    assert DATA_DIR is not None
