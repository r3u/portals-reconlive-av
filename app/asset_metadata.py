import yaml
import glob
import os

from pathlib import Path
from typing import FrozenSet, Dict, List


class AssetMetadataError(Exception):
    def __init__(self, filename, message):
        full_msg = "Error in file {0}: {1}".format(filename, message)
        super().__init__(full_msg)


class AssetMetadataDef:
    def __init__(self, filename: str, definition: dict):
        self.__filename: str = filename
        self.__asset_filename:str = Path(filename).stem
        self.__definition: dict = definition
        self.__tags: FrozenSet[str] = None
        self.__locations: FrozenSet[str] = None
        self.__type: str = None
        self.__init(definition)

    def __repr__(self):
        return 'AssetMetadata("{0}", {1})'.format(self.__filename, self.__definition)

    def __eq__(self, other: 'AssetMetadataDef'):
        return other is not None and other.__filename == self.__filename

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
                normalized_location = location.strip()
                normalized_locations.append(normalized_location)
            self.__locations = frozenset(normalized_locations)

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def asset_filename(self) -> str:
        return self.__asset_filename

    @property
    def type(self) -> str:
        return self.__type

    @property
    def locations(self) -> FrozenSet[str]:
        return self.__locations

    @property
    def tags(self) -> FrozenSet[str]:
        return self.__tags

    @staticmethod
    def from_file(filename: str) -> 'AssetMetadataDef':
        with open(filename) as fp:
            metadata = yaml.safe_load(fp)
        return AssetMetadataDef(filename, metadata)


class AssetMetadata:
    def __init__(self, definitions: Dict[str, AssetMetadataDef],
                 by_location_cache: Dict[str, List['AssetMetadataDef']]):
        self.__definitions = definitions
        self.__by_location_cache: Dict[str, List['AssetMetadataDef']] = by_location_cache

    @staticmethod
    def load_from_path(path: str) -> 'AssetMetadata':
        by_location_cache: Dict[str, List['AssetMetadataDef']] = {}
        pattern = os.path.join(path, '**', '*.yaml')
        metadata: Dict[str, AssetMetadataDef] = {}
        for filename in glob.glob(pattern, recursive=True):
            asset_metadata_def = AssetMetadataDef.from_file(filename)
            for location in asset_metadata_def.locations:
                if location not in by_location_cache:
                    by_location_cache[location] = []
                by_location_cache[location].append(asset_metadata_def)
            metadata[filename] = asset_metadata_def
        return AssetMetadata(metadata, by_location_cache)

    def by_filename(self, filename):
        return self.__definitions.get(filename)

    def by_location(self, location_name: str) -> List['AssetMetadataDef']:
        if location_name not in self.__by_location_cache:
            return []
        return list(self.__by_location_cache[location_name])


