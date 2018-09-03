import pytest
import yaml
import os

from asset_metadata import AssetMetadata, AssetMetadataDef, AssetMetadataError


def test_load_basic_metadata(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    tags:
      - Noise
      - Metal
    locations:
      - TestLocation
    """
    definition = yaml.safe_load(file_contents)
    metadata = AssetMetadataDef("test.wav.yaml", definition)
    assert metadata.filename == "test.wav.yaml"
    assert metadata.asset_filename == "test.wav"
    assert metadata.type == 'audio'
    assert len(metadata.tags) == 2
    assert 'noise' in metadata.tags
    assert 'metal' in metadata.tags
    assert len(metadata.locations) == 1
    assert 'TestLocation' in metadata.locations


def test_minimal_file(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    """
    definition = yaml.safe_load(file_contents)
    metadata = AssetMetadataDef("test.wav.yaml", definition)
    assert metadata.filename == "test.wav.yaml"
    assert metadata.type == 'audio'


def test_empty_input_file(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = ""
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_validate_missing_type(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    tags:
      - noise
      - metal
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_invalid_tag_list(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    tags: noise
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_invalid_tag_type(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    tags:
      - noise
      - 42
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_invalid_location_list(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    locations: NotAList 
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_invalid_location_type(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return True
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    locations:
      - 42
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_missing_asset_file(monkeypatch):
    def mock_isfile(filename):
        assert filename == "test.wav"
        return False
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    file_contents = """
    type: audio
    """
    definition = yaml.safe_load(file_contents)
    with pytest.raises(AssetMetadataError):
        AssetMetadataDef("test.wav.yaml", definition)


def test_load_asset_metadata_path():
    root = os.path.dirname(os.path.realpath(__file__))
    test_assets_path = os.path.join(root, "test_assets_good")
    metadata = AssetMetadata()
    metadata.load_from_path(test_assets_path)

    expected_file1 = os.path.join(test_assets_path, "TestLocation1", "sound", "testmacro.scd.yaml")
    expected_file2 = os.path.join(test_assets_path, "TestLocation2", "sound", "testmacro1.scd.yaml")
    expected_file3 = os.path.join(test_assets_path, "TestLocation2", "sound", "testmacro2.scd.yaml")
    expected_file4 = os.path.join(test_assets_path, "testimage.jpg.yaml")

    assert metadata.by_filename(expected_file1) is not None
    assert metadata.by_filename(expected_file2) is not None
    assert metadata.by_filename(expected_file3) is not None
    assert metadata.by_filename(expected_file4) is not None

    assert metadata.by_filename(expected_file1).type == "supercollider"
    assert len(metadata.by_filename(expected_file1).tags) == 4
    assert "deep" in metadata.by_filename(expected_file1).tags
    assert "dark" in metadata.by_filename(expected_file1).tags
    assert "forest" in metadata.by_filename(expected_file1).tags
    assert "black" in metadata.by_filename(expected_file1).tags
    assert len(metadata.by_filename(expected_file1).locations) == 1
    assert "TestLocation1" in metadata.by_filename(expected_file1).locations

    assert metadata.by_filename(expected_file2).type == "supercollider"
    assert metadata.by_filename(expected_file3).type == "supercollider"
    assert metadata.by_filename(expected_file4).type == "image"

    loc1_assets = metadata.by_location("TestLocation1")
    assert len(loc1_assets) == 2
    for asset in loc1_assets:
        assert "TestLocation1" in asset.locations

    loc2_assets = metadata.by_location("TestLocation2")
    assert len(loc2_assets) == 3
    for asset in loc2_assets:
        assert "TestLocation2" in asset.locations


def test_find_by_non_existing_location():
    root = os.path.dirname(os.path.realpath(__file__))
    test_assets_path = os.path.join(root, "test_assets_good")
    metadata = AssetMetadata()
    metadata.load_from_path(test_assets_path)
    assert len(metadata.by_location("blah")) == 0
