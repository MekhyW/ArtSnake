.. Sphinx Documentation Project index file, created by ChatGPT

Welcome to My Project's Documentation!
======================================


Say no to art theft! Robust and easy-to-use tool/API to protect digital art and photos from use without consent, combining context-aware watermarking and image poisoning.

Current Scenario
-----------------

Artists are often unable to protect their digital art from unauthorized use. No current solution combines the ease of use of traditional watermarking with the robustness of invisible watermarking and image poisoning techniques, and each has its own limitations.

Current watermark implementation tools are not context-aware. They can often be very easily removed by cropping or editing the image using modern image editing software and generative models, or obstruct the image in a way that is visually damaging to the art. (For the prototype version of the project, this is the main concern)

On the other side of the spectrum, current invisible watermarking techniques are often too complex for artists to use, and require a deep understanding of cryptography and image processing. And in the case of protection against generative models, they are often rely on the good faith of the model creators to respect the watermark, which does not provide a real solution to the problem. Anti-AI image poisoning techniques are, although powerful, not easily accessible in an easily integrable form for artists, especially those who do not possess computing resources or knowledge.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage

* :ref:`search`

