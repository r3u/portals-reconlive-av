import yaml
import glob
import os

from typing import FrozenSet, Dict


class AssetMetadataError(Exception):
    def __init__(self, filename, message):
        full_msg = "Error in file {0}: {1}".format(filename, message)
        super().__init__(full_msg)


class AssetMetadata:
    def __init__(self, filename: str, definition: dict):
        self.__filename: str = filename
        self.__definition: dict = definition
        self.__tags: FrozenSet[str] = None
        self.__locations: FrozenSet[str] = None
        self.__type: str = None
        self.__init(definition)

    def __repr__(self):
        return 'AssetMetadata("{0}", {1})'.format(self.__filename, self.__definition)

    def __init_fail(self, msg: str):
        raise AssetMetadataError(self.__filename, msg)

    def __init(self, definition: dict):
        if definition is None:
            return self.__init_fail("Empty input file")
        if 'type' not in definition:
            return self.__init_fail("Missing 'type' property")
        self.__type = definition['type']
        if 'tags' in definition:
            tags = definition['tags']
            normalized_tags = []
            if type(tags) != list:
                return self.__init_fail("'tags' is not a list")
            for tag in tags:
                if type(tag) != str:
                    return self.__init_fail("Invalid tag: {0}".format(tag))
                normalized_tags.append(tag.strip().lower())
            self.__tags = frozenset(normalized_tags)
        if 'locations' in definition:
            locations = definition['locations']
            normalized_locations = []
            if type(locations) != list:
                return self.__init_fail("'locations' is not a list")
            for location in locations:
                if type(location) != str:
                    return self.__init_fail("Invalid location: {0}".format(location))
                normalized_locations.append(location.strip())
            self.__locations = frozenset(normalized_locations)

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def type(self) -> str:
        return self.__type

    @property
    def locations(self) -> FrozenSet[str]:
        return self.__locations

    @property
    def tags(self) -> FrozenSet[str]:
        return self.__tags


def load_asset_metadata(filename: str) -> AssetMetadata:
    with open(filename) as fp:
        metadata = yaml.safe_load(fp)
    return AssetMetadata(filename, metadata)


def load_asset_metadata_from_path(path: str) -> Dict[str, AssetMetadata]:
    pattern = os.path.join(path, '**', '*.yaml')
    metadata: Dict[str, AssetMetadata] = {}
    for filename in glob.glob(pattern, recursive=True):
        metadata[filename] = load_asset_metadata(filename)
    return metadata
