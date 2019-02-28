# -*- coding: utf-8 -*-
import sys
from os import listdir
from os.path import isfile, isdir, join, dirname, splitext, basename
import xml.etree.ElementTree as ET


class XMLReader:
    def __init__(self, path):
        file = open(path, 'r')

        self.path = path
        self.content = file.read()
        self.root = ET.fromstring(self.content)
        self.template = "{name} 0.00 0 0.0 {xmin}.00 {ymin}.00 {xmax}.00 {ymax}.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"

    def get_filename(self):
        return splitext(basename(self.path))[0]

    def get_dir(self):
        return dirname(self.path)

    def get_objects(self):
        objects = []

        for object in self.root.findall("object"):
            objects.append({
                "name" : object.find("name").text,
                "xmin" : object.find("bndbox").find("xmin").text,
                "ymin" : object.find("bndbox").find("ymin").text,
                "xmax" : object.find("bndbox").find("xmax").text,
                "ymax" : object.find("bndbox").find("ymax").text
            })

        return objects

    def fill_template(self, object):
        return self.template.format(**object)

    def export_kitti(self):
        objects = self.get_objects()

        #Skip empty
        if len(objects) == 0: return False

        file = open(join(self.get_dir(), self.get_filename()) + ".txt", 'w')

        for object in objects[:-1]:
            file.write(self.fill_template(object) + "\n")
        # Write last without '\n'
        file.write(self.fill_template(objects[-1]))

        file.close()

        return True


def process_file(path):
    xml_reader = XMLReader(path)

    return xml_reader.export_kitti()


def get_directory_xml_files(dir):
    return [join(dir, f) for f in listdir(dir) if isfile(join(dir, f)) and splitext(f)[1].lower() == ".xml"]


def check_argv(argv):
    return len(argv) > 1


def main():
    if not check_argv(sys.argv):
        print("Wrong arguments. You should specify xml files or directory with xml files")

    # remove script name
    args = sys.argv[1:]
    processed_file_count = 0

    for path in args:
        files = []

        if isfile(path):
            files.append(path)
        elif isdir(path):
            files += get_directory_xml_files(path)

        for file in files:
            if process_file(file): processed_file_count += 1

    print("Finished. {0} Files are processed".format(processed_file_count))

if __name__ == "__main__":
    main()
