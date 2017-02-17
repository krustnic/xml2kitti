# XML2KITTI

Python script for conversion annotations saved as XML files in PASCAL VOC format (created by [labelImg](https://github.com/tzutalin/labelImg))
to KITTI file format:

```
Car 0.00 0 0.0 470.00 199.00 877.00 414.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
```

## Usage

Directory source:
```
python xml2kitti sample/labels
```

### or

File source:
```
python xml2kitti sample/labels/IMAG0113.xml
```

Results are saved as `.txt` files at the same directory with the same filename.
