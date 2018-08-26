import yaml
import glob
import os

from typing import List, Dict


class AssetMetadataError(Exception):
    def __init__(self, filename, message):
        full_msg = "Error in file {0}: {1}".format(filename, message)
        super().__init__(full_msg)


class AssetMetadata:
    def __init__(self, filename: str, definition: dict):
        self.__filename: str = filename
        self.__definition: dict = definition
        self.__tags: List[str] = []
        self.__locations: List[str] = []
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
            if type(tags) != list:
                return self.__init_fail("'tags' is not a list")
            for tag in tags:
                if type(tag) != str:
                    return self.__init_fail("Invalid tag: {0}".format(tag))
                self.__tags.append(tag.strip().lower())
            self.__tags = tags

    @property
    def filename(self):
        return self.__filename

    @property
    def type(self):
        return self.__type

    @property
    def tags(self):
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
