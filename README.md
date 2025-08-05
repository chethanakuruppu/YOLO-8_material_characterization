Scientific Project I - EL060A- **“Advanced Materials
Characterization Using X-ray Imaging and YOLOv8:
A Scientific Exploration”**

X-ray-based materials characterization techniques play a critical role in both scientific research
and industrial applications. By analyzing how materials absorb X-rays, these techniques provide
insight into their electronic and atomic structures, informing assessments of composition, oxida-
tion states, and coordination environments. Although X-ray absorption spectroscopy (XAS)1 is
a powerful method in this domain, it is not applicable in our laboratory setting due to its spe-
cialized requirements. Instead, this study employed a more accessible X-ray imaging technique
using a laboratory X-ray tube setup to investigate material absorption characteristics.
We examined wedge and samples made of various material compositions, focusing on three
thickness levels: 1mm, 2mm, and 5mm. A 5cm long wedge was used in Project 01. The X-ray
tube operated at 50keV with a current of 240μA, and each exposure was standardized to 25
seconds to ensure consistent imaging conditions. The goal was to observe how X-ray absorption
varies with material type and thickness.
For image classification and interpretation, we implemented deep learning techniques, specif-
ically the YOLO2 model, due to its high accuracy and real-time processing capability. Training
the model on Dataset 5, which included a significantly larger number of images, resulted in
markedly improved classification performance.
Although this study did not use XAS directly, we highlight how AI3 methods particularly
deep learning can be leveraged in materials characterization tasks, including automated in-
terpretation of X-ray imaging data. AI techniques contribute to improved efficiency, reduced
manual analysis, and improved consistency, offering scalable solutions for research, quality
control, and industrial inspection[13, 14].
Keywords: XAS, deep learning, image classification, Material Characterization, Alloys,
Wedge Absorption Study, AI, YOLO

**Summary of “Training and Validation Loss Curves for YOLOv8n”**

The model performed best when trained on the 5mm thickness dataset, achieving the highest stability and validation accuracy. Training on the 1mm dataset resulted in the poorest performance, while the 2mm dataset produced better, but still suboptimal, results.

Combining datasets showed mixed outcomes. Merging the 1mm and 2mm datasets was unsatisfactory, but combining the 2mm and 5mm datasets noticeably improved performance, though it did not surpass the results from the exclusive 5mm dataset.

These findings suggest that increased material thickness and larger wedge sizes are key factors for achieving more accurate and stable training results. The 5mm dataset consistently yielded the best performance metrics, including high precision, recall, and mAP, proving to be the most effective for this model.
| Thickness (mm) | Precision (P) | Recall (R) | mAP@50 | mAP@50-95 |
|---|---|---|---|---|
| 1 mm | 0.675 | 0.890 | 0.884 | 0.884 |
| 2 mm | 0.870 | 1.000 | 0.920 | 0.995 |
| 5 mm | 1.000 | 1.000 | 1.000 | 0.996 |
| 1 mm + 2 mm | 0.799 | 1.000 | 0.984 | 0.984 |
| 2 mm + 5 mm | 1.000 | 1.000 | 0.995 | 0.995 |

As seen in the table above, the dataset for 5mm thickness achieved the highest overall performance. Although combining data sets (e.g., 2mm + 5mm) improved generalization, the data set of only 5mm consistently produced the most stable and accurate results.
