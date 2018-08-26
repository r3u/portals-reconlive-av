import pytest
import yaml
import os

from asset_metadata import AssetMetadata, AssetMetadataError, load_asset_metadata_from_path


def test_load_basic_metadata():
    file_contents = """
    type: audio
    tags:
      - Noise
      - Metal
    locations:
      - TestLocation
    """
    definition = yaml.safe_load(file_contents)
    metadata = AssetMetadata("test.yaml", definition)
    assert metadata.filename == "test.yaml"
    assert metadata.type == 'audio'
    assert len(metadata.tags) == 2
    assert 'noise' in metadata.tags
    assert 'metal' in metadata.tags
    assert len(metadata.locations) == 1
    assert 'TestLocation' in metadata.locations


def test_minimal_file():
    file_contents = """
    type: audio
    """
    definition = yaml.safe_load(file_contents)
    metadata = AssetMetadata("test.yaml", definition)
    assert metadata.filename == "test.yaml"
    assert metadata.type == 'audio'


def test_empty_input_file():
    file_contents = ""
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_validate_missing_type():
    file_contents = """
    tags:
      - noise
      - metal
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_invalid_tag_list():
    file_contents = """
    type: audio
    tags: noise
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_invalid_tag_type():
    file_contents = """
    type: audio
    tags:
      - noise
      - 42
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_invalid_location_list():
    file_contents = """
    type: audio
    locations: NotAList 
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_invalid_location_type():
    file_contents = """
    type: audio
    locations:
      - 42
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadata("test.yaml", definition)


def test_load_asset_metadata_path():
    root = os.path.dirname(os.path.realpath(__file__))
    test_assets_path = os.path.join(root, "test_assets")
    metadata = load_asset_metadata_from_path(test_assets_path)

    expected_file1 = os.path.join(test_assets_path, "TestLocation1", "sound", "testmacro.scd.yaml")
    expected_file2 = os.path.join(test_assets_path, "TestLocation2", "sound", "testmacro1.scd.yaml")
    expected_file3 = os.path.join(test_assets_path, "TestLocation2", "sound", "testmacro2.scd.yaml")
    expected_file4 = os.path.join(test_assets_path, "TestLocation2", "testimage.png.yaml")

    assert expected_file1 in metadata
    assert expected_file2 in metadata
    assert expected_file3 in metadata
    assert expected_file4 in metadata

    assert metadata[expected_file1].type == "supercollider"
    assert len(metadata[expected_file1].tags) == 4
    assert "deep" in metadata[expected_file1].tags
    assert "dark" in metadata[expected_file1].tags
    assert "forest" in metadata[expected_file1].tags
    assert "black" in metadata[expected_file1].tags
    assert len(metadata[expected_file1].locations) == 1
    assert "TestLocation1" in metadata[expected_file1].locations

    assert metadata[expected_file2].type == "supercollider"
    assert metadata[expected_file3].type == "supercollider"
    assert metadata[expected_file4].type == "image"
