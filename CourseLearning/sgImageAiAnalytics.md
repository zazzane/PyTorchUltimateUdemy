# Image AI Analytics Learnings
_For all documentation of learnings when using PyTorch for Computer Vision and Image Classification_

## Torch
### Torchvision.Tranforms
1. `.RandomVerticalFlips(p)` or `.RandomHorizontallFlips(p)`
    * use real world context and application to decide if vert/hori flipping is natural and/or expected
    * based on context, we can also determine the probability `p`
    * flipping should only be applied to the training data

2. `.Resize((target_y_pixels, target_x_pixels), interpolation)`
    * resize input image to new dimension for de-resolution or standardising size
    * the `interpolation` parameter controls the algorithm used for resampling the image when scaling it to new dimensions. Possible values:
        - BILINEAR: Uses a `2x2` pixel neighborhood for linear interpolation
        - BICUBIC: Uses a `4x4` pixel neighborhood for cubic interpolation
        - NEAREST: Uses the nearest neighbor pixel value **(no interpolation)**
        - NEAREST_EXACT: A more precise version of nearest neighbor interpolation
        - Others like LANCZOS, BOX, and HAMMING are also available
    * High-Level Understanding: Think of interpolation as the method used to "fill in the gaps" when an image is resized. When you're making an image larger or smaller, you need to create new pixel values that didn't exist in the original image.

