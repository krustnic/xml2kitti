import unittest
from xml2kitti import get_directory_xml_files, check_argv, XMLReader

class TestUtil(unittest.TestCase):
    def test_get_directory_xml_files(self):
        files = get_directory_xml_files("sample/labels")

        self.assertEqual(len(files), 3)


    def test_check_argv(self):
        self.assertEqual(check_argv([]), False)
        self.assertEqual(check_argv([""]), False)
        self.assertEqual(check_argv(["", ""]), True)


class TestXmlReader(unittest.TestCase):
    def setUp(self):
        self.xml_reader = XMLReader("sample/labels/IMAG0113.xml")


    def test_get_filename(self):
        self.assertEqual(self.xml_reader.get_filename(), "IMAG0113")

    def test_get_dir(self):
        dir = self.xml_reader.get_dir()

        self.xml_reader = XMLReader("sample/labels/IMAG0113.xml")
        self.assertEqual(dir, "sample/labels")

    def test_get_objects(self):
        objects = self.xml_reader.get_objects()
        self.assertEqual(len(objects), 5)
        self.assertEqual(objects[0]["name"], "car")
        self.assertEqual(objects[0]["xmin"], "869")
        self.assertEqual(objects[0]["ymin"], "843")
        self.assertEqual(objects[0]["xmax"], "1055")
        self.assertEqual(objects[0]["ymax"], "1108")

    def test_fill_template(self):
        objects = self.xml_reader.get_objects()

        self.assertEqual(self.xml_reader.fill_template(objects[0]), "car 0.00 0 0.0 869.00 843.00 1055.00 1108.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0")


if __name__ == '__main__':
    unittest.main()
