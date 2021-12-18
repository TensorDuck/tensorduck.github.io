import pathlib

from PIL import Image


if __name__ == "__main__":
    # input/output directory
    src_dir = "blog - taiwan2021"
    tar_dir = "blog_output"

    src_path = pathlib.Path(src_dir)
    tar_path = pathlib.Path(tar_dir)

    tar_path.mkdir(parents=True, exist_ok=True)

    # Pixel 3A camera produces a (3024, 4032) image
    # Shrink factor of 6 produces a (504, 672) image
    shrink_factor = 6

    for image_file in src_path.glob("**/*.jpg"):
        im = Image.open(image_file)
        new_im_dims = (im.size[0] / shrink_factor, im.size[1] / shrink_factor)
        im.thumbnail(size=new_im_dims)
        im.save(tar_dir / pathlib.Path(image_file.name), quality=95)