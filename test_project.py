from project import allowed_file, index, new, ALLOWED_EXTENSIONS, filename, render_template

def test_allowed_file():
    assert allowed_file() == r"." in filename and filename.rsplit(".", 1) in ALLOWED_EXTENSIONS


def test_index():
  assert index() == render_template('index.html')


def test_new():
  assert new() == 5