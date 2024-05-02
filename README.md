# ArtSnake

**Say no to art theft!** Robust and easy-to-use tool/API to protect digital art and photos from use without consent, combining context-aware watermarking and image poisoning.

## Current Scenario

Artists are often unable to protect their digital art from unauthorized use. No current solution combines the ease of use of traditional watermarking with the robustness of invisible watermarking and image poisoning techniques, and each has its own limitations.

Current watermark implementation tools are not context-aware. They can often be very easily removed by cropping or editing the image using modern image editing software and generative models, or obstruct the image in a way that is visually damaging to the art. 
**(For the prototype version of the project, this is the main concern)**

On the other side of the spectrum, current invisible watermarking techniques are often too complex for artists to use, and require a deep understanding of cryptography and image processing. And in the case of protection against generative models, they are often rely on the good faith of the model creators to respect the watermark, which does not provide a real solution to the problem. Anti-AI image poisoning techniques are, although powerful, not easily accessible in an easily integrable form for artists, especially those who do not possess computing resources or knowledge.

## References

### Technologies of Interest
[ArtShield](https://artshield.io/)

[Glaze](https://glaze.cs.uchicago.edu/index.html)

[Sanative AI](https://app.sanative.ai/)

### Papers

[Benchmarking the Robustness of Image Watermarks](https://arxiv.org/pdf/2401.08573.pdf)

[On the Effectiveness of Visible Watermarks](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dekel_On_the_Effectiveness_CVPR_2017_paper.pdf)

[Report on Watermarking Benchmarking And Steganalysis](http://omen.cs.uni-magdeburg.de/ecrypt/deliverables/DWVL16_final.pdf)

[Visible Watermark Detection in Images](https://cseweb.ucsd.edu//~sag043/static/pdfs/WatermarkDetection.pdf)

### Repositories of Interest

[umd-huang-lab/WAVES](https://github.com/umd-huang-lab/WAVES)

[rohitrango/automatic-watermark-detection](https://github.com/rohitrango/automatic-watermark-detection?tab=readme-ov-file)

[LAION-AI/watermark-detection](https://github.com/LAION-AI/watermark-detection)

[EspacioLatente/Glaze](https://github.com/EspacioLatente/Glaze)