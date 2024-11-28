import xmltodict
import os


class SdtdModTranslator:

    def __init__(self, install_path):
        self._install_path = install_path

    def _get_mod_folders(self):
        outer_mod_folder = os.path.join(self._install_path, "Mods")
        mod_folders = [
            os.path.join(outer_mod_folder, name)
            for name in os.listdir(outer_mod_folder)
            if os.path.isdir(os.path.join(outer_mod_folder, name))
        ]
        return mod_folders

    def _get_keys(self, mod_folder):
        config_folder = os.path.join(mod_folder, "Config")
        if not os.path.exists(config_folder):
            return set()
        xml_files = [
            os.path.join(config_folder, i)
            for i in os.listdir(config_folder)
            if i.endswith(".xml")
        ]
        keys = set()
        for xml_file in xml_files:
            try:
                with open(xml_file, encoding="utf-8") as f:
                    xml_file_content = f.read()
                xml_content_obj = xmltodict.parse(xml_file_content)
                for obj in xml_content_obj["configs"]["append"]:
                    for key, value in obj.items():
                        if not key.startswith("@"):
                            keys.update(set([i["@name"] for i in value]))
                            break
            except:
                pass
        return keys


if __name__ == "__main__":
    pass
