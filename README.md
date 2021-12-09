# Fruit inspection

## Dependencies

* Python v.2.7.x

Download dependencies from `requirements.txt`:
```bash
$ pip install -r requirements.txt
```

---

Image format:  Cx_yyyyyy.bmp
- x = 0 -> NIR
- x = 1 -> Color images
- yyyyyy -> Incremental number of pair

### Task 1

Outline the fruit by generating a binary mask:
- Remove the background
  - Threshold the image to remove the background
  - Flood-fill the mask