=====================================
Usage Documentation
=====================================

This document provides an overview and description of the functions available in the ArtSnake library. The focus of this guide is on functions for calculating differences and similarities between images.

.. contents::
    :local:
    :depth: 2

Watermark Insertion Functions
=====================================

insert_watermark
-----------------

**Description:**

The `insert_watermark` function inserts a watermark into an image. This is the main function and uses multiple sub-functions to detect, remove, and insert watermarks. You can create your custom functions and pass them as arguments to this function, but the standard versions of each function are listed below.

**Function Signature:**

.. code-block:: python

    insert_watermark(img, watermark, n, measure_diff=measure_diff_padrao, watermark_remover=watermark_remover_padrao, watermark_detector=watermark_detector_padrao)

**Arguments:**

- `img` (numpy.ndarray): The image to insert the watermark into.
- `watermark` (numpy.ndarray): The watermark image.
- `n` (int): The number of iterations to perform the watermark random insertion process.
- `measure_diff` (function, optional): The function to use for measuring differences between images. Defaults to `measure_diff_padrao`.
- `watermark_remover` (function, optional): The function to use for removing watermarks from images. Defaults to `watermark_remover_padrao`.
- `watermark_detector` (function, optional): The function to use for detecting watermarks in images. Defaults to `watermark_detector_padrao`.

**Returns:**

- `img` (numpy.ndarray): The image with the watermark inserted.
- `score` (float): The score of the quality of the inserted watermark. 

**Example Usage:**

.. code-block:: python

    import cv2 
    from ArtSnake import *

    imagem1_path = "../image.jpeg"
    imagem2_path = "../praia.jpg"

    img1 = cv2.imread(imagem1_path)
    img2 = cv2.imread(imagem2_path)

    result, score = insert_watermark(img2, img1, 10)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



Image Comparison Functions
============================

The following functions are designed to compare images by calculating differences and similarities.

measure_diff_simple
--------------------

**Description:**

The `measure_diff_simple` function calculates the simple pixel-wise difference between two images.

**Function Signature:**

.. code-block:: python

    measure_diff_simple(img1, img2, show_diff=False)

**Arguments:**

- `img1` (numpy.ndarray): The first image.
- `img2` (numpy.ndarray): The second image.
- `show_diff` (bool, optional): Whether to display the difference image. Defaults to `False`.

**Returns:**

- `diff` (float): The calculated difference value.

**Example Usage:**

.. code-block:: python

    from ArtSnake import measure_diff_simple

    diff = measure_diff_simple(image1, image2, show_diff=True)

measure_similarity_psnr
------------------------

**Description:**

The `measure_similarity_psnr` function calculates the Peak Signal-to-Noise Ratio (PSNR) between two images.

**Function Signature:**

.. code-block:: python

    measure_similarity_psnr(img1, img2, show_diff=False)

**Arguments:**

- `img1` (numpy.ndarray): The first image.
- `img2` (numpy.ndarray): The second image.
- `show_diff` (bool, optional): Whether to display the difference image. Defaults to `False`.

**Returns:**

- `psnr` (float): The calculated PSNR value.

**Example Usage:**

.. code-block:: python

    from ArtSnake import measure_similarity_psnr

    psnr = measure_similarity_psnr(image1, image2, show_diff=True)

measure_similarity_ssim
------------------------

**Description:**

The `measure_similarity_ssim` function calculates the Structural Similarity Index (SSIM) between two images.

**Function Signature:**

.. code-block:: python

    measure_similarity_ssim(img1, img2, show_similarity=False)

**Arguments:**

- `img1` (numpy.ndarray): The first image.
- `img2` (numpy.ndarray): The second image.
- `show_similarity` (bool, optional): Whether to print the SSIM value. Defaults to `False`.

**Returns:**

- `ssim_value` (float): The calculated SSIM value.

**Example Usage:**

.. code-block:: python

    from ArtSnake import measure_similarity_ssim

    ssim_value = measure_similarity_ssim(image1, image2, show_similarity=True)


Watermark Detection Functions
=====================================

watermark_proba_prebuilt_from_opencv
------------------------------------

**Description:**

The `watermark_proba_prebuilt_from_opencv` function calculates the probability that an image contains a watermark using a prebuilt model.

**Function Signature:**

.. code-block:: python

    watermark_proba_prebuilt_from_opencv(img_path)

**Arguments:**

- `img_path` (str): The path to the image file.

**Returns:**

- `proba` (float): The probability that the image contains a watermark.

**Example Usage:**

.. code-block:: python

    from ArtSnake import watermark_proba_prebuilt_from_opencv

    proba = watermark_proba_prebuilt_from_opencv('path/to/image.jpg')


Watermark Removal Functions
=====================================

remove_watermark_from_opencv
--------------------------

**Description:**

The `remove_watermark_prebuilt_from_path` function removes a watermark from an image file.

**Function Signature:**

.. code-block:: python

    remove_watermark_from_opencv(img_path)

**Arguments:**

- `img_path` (str): The path to the image file.

**Returns:**

- `img` (numpy.ndarray): The image with the watermark removed.

**Example Usage:**

.. code-block:: python

    from ArtSnake import remove_watermark_from_opencv

    img = remove_watermark_from_opencv('path/to/image.jpg')