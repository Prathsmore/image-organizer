from image_organizer.organizer import get_resolution
from PIL import Image
import tempfile

def test_get_resolution():
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
        img = Image.new("RGB", (640, 480))
        img.save(tmp.name)
        assert get_resolution(tmp.name) == "640x480"
