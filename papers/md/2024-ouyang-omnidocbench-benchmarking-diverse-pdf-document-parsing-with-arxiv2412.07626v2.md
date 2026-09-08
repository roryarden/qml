---
title: "OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"
authors:
  - "Linke Ouyang"
  - "Yuan Qu"
  - "Hongbin Zhou"
  - "Jiawei Zhu"
  - "Rui Zhang"
  - "Qunshu Lin"
  - "Bin Wang"
  - "Zhiyuan Zhao"
  - "Man Jiang"
  - "Xiaomeng Zhao"
  - "Jin Shi"
  - "Fan Wu"
  - "Pei Chu"
  - "Minghao Liu"
  - "Zhenxiang Li"
  - "Chao Xu"
  - "Bo Zhang"
  - "Botian Shi"
  - "Zhongying Tu"
  - "Conghui He"
arxiv: "2412.07626v2"
published: 2024-12-10
updated: 2025-03-25
primary_category: cs.CV
categories: [cs.CV, cs.AI, cs.IR]
comment: "Accepted by CVPR2025"
abs_url: "http://arxiv.org/abs/2412.07626v2"
pdf_url: "https://arxiv.org/pdf/2412.07626v2"
abstract: >
  Document content extraction is a critical task in computer vision, underpinning the data needs of large language models (LLMs) and retrieval-augmented generation (RAG) systems. Despite recent progress, current document parsing methods have not been fairly and comprehensively evaluated due to the narrow coverage of document types and the simplified, unrealistic evaluation procedures in existing benchmarks. To address these gaps, we introduce OmniDocBench, a novel benchmark featuring high-quality annotations across nine document sources, including academic papers, textbooks, and more challenging cases such as handwritten notes and densely typeset newspapers. OmniDocBench supports flexible, multi-level evaluations--ranging from an end-to-end assessment to the task-specific and attribute--based analysis using 19 layout categories and 15 attribute labels. We conduct a thorough evaluation of both pipeline-based methods and end-to-end vision-language models, revealing their strengths and weaknesses across different document types. OmniDocBench sets a new standard for the fair, diverse, and fine-grained evaluation in document parsing. Dataset and code are available at https://github.com/opendatalab/OmniDocBench.
---

# OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations

Linke Ouyang    Yuan Qu    Hongbin Zhou    Jiawei Zhu    Rui Zhang    Qunshu Lin    Bin Wang    Zhiyuan Zhao Man Jiang Xiaomeng Zhao Jin Shi Fan Wu Pei Chu Minghao Liu Affiliation: Shanghai AI Laboratory Abaka AI 2077AI     Zhenxiang Li Chao Xu Bo Zhang Botian Shi Zhongying Tu Conghui He

###### Abstract

Document content extraction is a critical task in computer vision, underpinning the data needs of large language models (LLMs) and retrieval-augmented generation (RAG) systems. Despite recent progress, current document parsing methods have not been fairly and comprehensively evaluated due to the narrow coverage of document types and the simplified, unrealistic evaluation procedures in existing benchmarks. To address these gaps, we introduce OmniDocBench, a novel benchmark featuring high-quality annotations across nine document sources, including academic papers, textbooks, and more challenging cases such as handwritten notes and densely typeset newspapers. OmniDocBench supports flexible, multi-level evaluations—ranging from an end-to-end assessment to the task-specific and attribute-based analysis—using 19 layout categories and 15 attribute labels. We conduct a thorough evaluation of both pipeline-based methods and end-to-end vision-language models, revealing their strengths and weaknesses across different document types. OmniDocBench sets a new standard for the fair, diverse, and fine-grained evaluation in document parsing. Dataset and code are available at <https://github.com/opendatalab/OmniDocBench>.

<sup>††</sup>footnotetext: <sup>∗</sup> The authors contributed equally.<sup>††</sup>footnotetext: <sup>†</sup> Project lead.<sup>††</sup>footnotetext: <sup>‡</sup> Corresponding author (heconghui@pjlab.org.cn).

## 1 Introduction

<figure id="S1.F1" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/radar_0324_new.png" id="S1.F1.g1" class="ltx_graphics ltx_centering ltx_img_square" style="aspect-ratio:596/590;" width="596" height="590" alt="Refer to caption" />
<figcaption>Figure 1: Results of End-to-End Text Recognition on OmniDocBench across 9 PDF page types.</figcaption>
</figure>

<figure id="S1.F2" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/Data_diversity.png" id="S1.F2.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:617/345;" width="617" height="345" alt="Refer to caption" />
<figcaption>Figure 2: Overview of OmniDocBench Data Diversity. The benchmark includes 9 diverse PDF document types. It supports rich annotation types, including layout annotations (e.g., title, table, figure) and recognition annotations (e.g., text spans, equations, tables). Each page is annotated with 6 page-level attributes (e.g., PDF type, layout type), along with fine-grained 3 text attributes (e.g., language) and 6 tables attributes (Items under “special issues” are treated as individual binary attributes (yes/no)), enabling detailed and robust evaluation.</figcaption>
</figure>

As large language models \[[1](#bib.bib1), [39](#bib.bib39), [44](#bib.bib44), [28](#bib.bib28)\] increasingly rely on high-quality, knowledge-rich data, the importance of accurate document parsing has grown substantially. Document parsing, a core task in computer vision and document intelligence, aims to extract structured, machine-readable content from unstructured documents such as PDFs. This task is particularly critical for ingesting academic papers, technical reports, textbooks, and other rich textual sources into large language models, thereby enhancing their factual accuracy and knowledge grounding \[[19](#bib.bib19), [42](#bib.bib42), [45](#bib.bib45), [47](#bib.bib47), [52](#bib.bib52)\]. Moreover, with the emergence of retrieval-augmented generation (RAG) systems \[[22](#bib.bib22), [12](#bib.bib12)\], which retrieve and generate answers conditionally with external documents, the demand for precise document understanding has further intensified.

To address this challenging task, two main paradigms have emerged: 1) Pipeline-based approaches that decompose the task into layout analysis, OCR, formula/table recognition, and reading order estimation \[[42](#bib.bib42), [34](#bib.bib34)\]; and 2) End-to-end vision-language models (VLMs) that directly output structured representations (e.g., Markdown) \[[7](#bib.bib7), [46](#bib.bib46), [29](#bib.bib29), [45](#bib.bib45), [3](#bib.bib3), [8](#bib.bib8), [48](#bib.bib48)\]. Although both approaches have demonstrated promising results, conducting a broad comparison of their effectiveness remains challenging due to the absence of a comprehensive and unified evaluation benchmark.

As shown in Table [1](#S2.T1 "Table 1 ‣ 2 Related Work ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), for pipeline-based document parsing systems, dedicated benchmarks \[[26](#bib.bib26), [54](#bib.bib54), [10](#bib.bib10)\] have been developed to target specific sub-tasks. For end-to-end evaluation, works like Nougat \[[7](#bib.bib7)\] and GOT-OCR \[[45](#bib.bib45)\] provide relatively small validation sets and assess predictions using page-level metrics such as Edit Distance \[[21](#bib.bib21)\].

However, these benchmarks present several key limitations: 1) Limited document diversity: Existing datasets primarily focus on academic papers, overlooking other real-world document types such as textbooks, exams, financial reports, and newspapers; 2) Inconsistent evaluation metrics: Current benchmarks rely heavily on generic text similarity metrics (e.g., Edit Distance \[[21](#bib.bib21)\] and BLEU \[[33](#bib.bib33)\]), which fail to fairly assess the accuracy of formulas and tables in LaTeX or HTML formats that allow for diverse syntactic expressions; and 3) Lack of fine-grained evaluation: Most evaluations report only an overall score, lacking insights into specific weaknesses, such as element-level score (e.g., text vs. formula) or per document-type performance (e.g., magazine or notes).

To address these limitations, we introduce OmniDocBench, a new benchmark designed to provide a rigorous and comprehensive evaluation for document parsing models across both pipeline-based and end-to-end paradigms. In summary, our benchmark introduces the following key contributions:

- <span id="S1.I1.i1">•</span>

  High-quality, diverse evaluation set: We include pages from 9 distinct document types, ranging from textbooks to newspapers, annotated using a combination of automated tools, manual verification, and expert review.

- <span id="S1.I1.i2">•</span>

  Flexible, multi-dimensional evaluation: We support comprehensive evaluation at three levels—end-to-end, task-specific, and attribute-based. End-to-end evaluation measures the overall quality of full-page parsing results. Task-specific evaluation allows users to assess individual components such as layout detection, OCR, table recognition, or formula parsing. Attribute-based evaluation provides fine-grained analysis across 9 document types, 6 page-level attributes and 9 bbox-level attributes.

- <span id="S1.I1.i3">•</span>

  Comprehensive benchmarking of state-of-the-art methods: We systematically evaluate a suite of representative document parsing systems, including both pipeline-based tools and VLMs, providing the most comprehensive comparison and identifying performance bottlenecks across document types and content structures.

## 2 Related Work

<figure id="S2.T1" class="ltx_table">
<table id="S2.T1.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S2.T1.3.1.1" class="ltx_tr">
<td rowspan="2" id="S2.T1.3.1.1.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Benchmark</td>
<td rowspan="2" id="S2.T1.3.1.1.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Document Domain</td>
<td colspan="5" id="S2.T1.3.1.1.3" class="ltx_td ltx_align_center ltx_border_tt">Annotaion Type</td>
<td colspan="4" id="S2.T1.3.1.1.4" class="ltx_td ltx_align_center ltx_border_tt">Single-Task Eval</td>
<td colspan="4" id="S2.T1.3.1.1.5" class="ltx_td ltx_align_center ltx_border_tt">End-to-End Eval</td>
</tr>
<tr id="S2.T1.3.1.2" class="ltx_tr">
<td id="S2.T1.3.1.2.1" class="ltx_td ltx_align_center">BBox</td>
<td id="S2.T1.3.1.2.2" class="ltx_td ltx_align_center">Text</td>
<td id="S2.T1.3.1.2.3" class="ltx_td ltx_align_center">Table</td>
<td id="S2.T1.3.1.2.4" class="ltx_td ltx_align_center">Formula</td>
<td id="S2.T1.3.1.2.5" class="ltx_td ltx_align_center ltx_border_r">Attributes</td>
<td id="S2.T1.3.1.2.6" class="ltx_td ltx_align_center">OCR</td>
<td id="S2.T1.3.1.2.7" class="ltx_td ltx_align_center">DLA</td>
<td id="S2.T1.3.1.2.8" class="ltx_td ltx_align_center">TR</td>
<td id="S2.T1.3.1.2.9" class="ltx_td ltx_align_center ltx_border_r">MFR</td>
<td id="S2.T1.3.1.2.10" class="ltx_td ltx_align_center">OCR</td>
<td id="S2.T1.3.1.2.11" class="ltx_td ltx_align_center">TR</td>
<td id="S2.T1.3.1.2.12" class="ltx_td ltx_align_center">MFR</td>
<td id="S2.T1.3.1.2.13" class="ltx_td ltx_align_center">ROD</td>
</tr>
<tr id="S2.T1.3.1.3" class="ltx_tr">
<td colspan="15" id="S2.T1.3.1.3.1" class="ltx_td ltx_align_left ltx_border_t">Single-Task Eval Benchmark</td>
</tr>
<tr id="S2.T1.3.1.4" class="ltx_tr">
<td id="S2.T1.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">Robust Reading [<a href="#bib.bib20">20</a>]</td>
<td id="S2.T1.3.1.4.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">1</td>
<td id="S2.T1.3.1.4.3" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.4.4" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.4.5" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.6" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.7" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.4.8" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.4.9" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.10" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.11" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.4.12" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.13" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.14" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.4.15" class="ltx_td ltx_border_t"></td>
</tr>
<tr id="S2.T1.3.1.5" class="ltx_tr">
<td id="S2.T1.3.1.5.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">PubLayNet [<a href="#bib.bib49">49</a>], DocBank [<a href="#bib.bib26">26</a>], DocLayNet [<a href="#bib.bib35">35</a>], M<sup>6</sup>Doc [<a href="#bib.bib9">9</a>]</td>
<td id="S2.T1.3.1.5.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">1, 1, 5, 6</td>
<td id="S2.T1.3.1.5.3" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.5.4" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.5" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.6" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.7" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.5.8" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.9" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.5.10" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.11" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.5.12" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.13" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.14" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.5.15" class="ltx_td ltx_border_t"></td>
</tr>
<tr id="S2.T1.3.1.6" class="ltx_tr">
<td id="S2.T1.3.1.6.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">PubTabNet [<a href="#bib.bib54">54</a>],TableX [<a href="#bib.bib11">11</a>]</td>
<td id="S2.T1.3.1.6.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">1, 1</td>
<td id="S2.T1.3.1.6.3" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.4" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.5" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.6.6" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.7" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.6.8" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.9" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.10" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.6.11" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.6.12" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.13" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.14" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.6.15" class="ltx_td ltx_border_t"></td>
</tr>
<tr id="S2.T1.3.1.7" class="ltx_tr">
<td id="S2.T1.3.1.7.1" class="ltx_td ltx_align_left ltx_border_r">TableBank [<a href="#bib.bib25">25</a>]</td>
<td id="S2.T1.3.1.7.2" class="ltx_td ltx_align_center ltx_border_r">1</td>
<td id="S2.T1.3.1.7.3" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.7.4" class="ltx_td"></td>
<td id="S2.T1.3.1.7.5" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.7.6" class="ltx_td"></td>
<td id="S2.T1.3.1.7.7" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.7.8" class="ltx_td"></td>
<td id="S2.T1.3.1.7.9" class="ltx_td"></td>
<td id="S2.T1.3.1.7.10" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.7.11" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.7.12" class="ltx_td"></td>
<td id="S2.T1.3.1.7.13" class="ltx_td"></td>
<td id="S2.T1.3.1.7.14" class="ltx_td"></td>
<td id="S2.T1.3.1.7.15" class="ltx_td"></td>
</tr>
<tr id="S2.T1.3.1.8" class="ltx_tr">
<td id="S2.T1.3.1.8.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">Im2Latex-100K [<a href="#bib.bib10">10</a>],UniMER-Test [<a href="#bib.bib40">40</a>]</td>
<td id="S2.T1.3.1.8.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">1</td>
<td id="S2.T1.3.1.8.3" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.4" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.5" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.6" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.8.7" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.8.8" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.9" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.10" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.11" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">✔</td>
<td id="S2.T1.3.1.8.12" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.13" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.14" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.8.15" class="ltx_td ltx_border_t"></td>
</tr>
<tr id="S2.T1.3.1.9" class="ltx_tr">
<td colspan="15" id="S2.T1.3.1.9.1" class="ltx_td ltx_align_left ltx_border_t">End-to-end Eval Benchmarks</td>
</tr>
<tr id="S2.T1.3.1.10" class="ltx_tr">
<td id="S2.T1.3.1.10.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">Fox [<a href="#bib.bib29">29</a>]</td>
<td id="S2.T1.3.1.10.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">2</td>
<td id="S2.T1.3.1.10.3" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.10.4" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.10.5" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.6" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.7" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.10.8" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.10.9" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.10" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.11" class="ltx_td ltx_border_r ltx_border_t"></td>
<td id="S2.T1.3.1.10.12" class="ltx_td ltx_align_center ltx_border_t">✔</td>
<td id="S2.T1.3.1.10.13" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.14" class="ltx_td ltx_border_t"></td>
<td id="S2.T1.3.1.10.15" class="ltx_td ltx_border_t"></td>
</tr>
<tr id="S2.T1.3.1.11" class="ltx_tr">
<td id="S2.T1.3.1.11.1" class="ltx_td ltx_align_left ltx_border_r">Nougat [<a href="#bib.bib7">7</a>]</td>
<td id="S2.T1.3.1.11.2" class="ltx_td ltx_align_center ltx_border_r">1</td>
<td id="S2.T1.3.1.11.3" class="ltx_td"></td>
<td id="S2.T1.3.1.11.4" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.5" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.6" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.7" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.11.8" class="ltx_td"></td>
<td id="S2.T1.3.1.11.9" class="ltx_td"></td>
<td id="S2.T1.3.1.11.10" class="ltx_td"></td>
<td id="S2.T1.3.1.11.11" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.11.12" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.13" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.14" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.11.15" class="ltx_td"></td>
</tr>
<tr id="S2.T1.3.1.12" class="ltx_tr">
<td id="S2.T1.3.1.12.1" class="ltx_td ltx_align_left ltx_border_r">GOT OCR 2.0 [<a href="#bib.bib45">45</a>]</td>
<td id="S2.T1.3.1.12.2" class="ltx_td ltx_align_center ltx_border_r">2</td>
<td id="S2.T1.3.1.12.3" class="ltx_td"></td>
<td id="S2.T1.3.1.12.4" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.5" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.6" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.7" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.12.8" class="ltx_td"></td>
<td id="S2.T1.3.1.12.9" class="ltx_td"></td>
<td id="S2.T1.3.1.12.10" class="ltx_td"></td>
<td id="S2.T1.3.1.12.11" class="ltx_td ltx_border_r"></td>
<td id="S2.T1.3.1.12.12" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.13" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.14" class="ltx_td ltx_align_center">✔</td>
<td id="S2.T1.3.1.12.15" class="ltx_td"></td>
</tr>
<tr id="S2.T1.3.1.13" class="ltx_tr" style="--ltx-bg-color:#F2F2F2;">
<td id="S2.T1.3.1.13.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r ltx_border_t">OmniDocBench</td>
<td id="S2.T1.3.1.13.2" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">9</td>
<td id="S2.T1.3.1.13.3" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.4" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.5" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.6" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.7" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.8" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.9" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.10" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.11" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.12" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.13" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.14" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
<td id="S2.T1.3.1.13.15" class="ltx_td ltx_align_center ltx_border_bb ltx_border_t">✔</td>
</tr>
</tbody>
</table>
<figcaption>Table 1: A Comparison between OmniDocBench and existing benchmarks. BBox: Bounding boxes. Text: Text in Unicode. Table: Table in LaTeX/HTML/Markdown. Formula: Formula in LaTeX. Attributes: Page- and BBox-Level Attributes. OCR: Optical Character Recognition; DLA: Document Layout Analysis; TR: Table Recognition; MFR: Math Formula Recognition; ROD: Reading Order Detection</figcaption>
</figure>

### 2.1 Pipeline-based Document Content Extraction

Pipeline-based methods treat the document content extraction task as a collection of single modules, such as document layout detection \[[17](#bib.bib17), [53](#bib.bib53), [36](#bib.bib36), [13](#bib.bib13)\], optical character recognition \[[38](#bib.bib38), [23](#bib.bib23), [30](#bib.bib30), [15](#bib.bib15), [43](#bib.bib43)\], formula recognition \[[51](#bib.bib51), [27](#bib.bib27), [6](#bib.bib6), [40](#bib.bib40)\], and table recognition \[[16](#bib.bib16), [18](#bib.bib18), [23](#bib.bib23)\]. In this sense, such methods can utilize different expert models to address each specific task. Marker \[[34](#bib.bib34)\] integrates open-source models to parse documents into structured formats such as Markdown, JSON, and HTML. To get higher accuracy, an optional LLM-enabled version can also be integrated to merge tables across pages, handle inline math, and so on. Similarly, MinerU \[[42](#bib.bib42)\] first utilizes a layout detection model to segment the document page into different regions, then applies task-specific models for corresponding regions. Finally, it outputs the complete content in Markdown format with a reading order algorithm. By leveraging lightweight models and parallelized operations, pipeline-based methods can achieve efficient parsing speeds.

### 2.2 VLM-based Document Content Extraction

Document understanding and optical character recognition (OCR) are crucial tasks for evaluating the perception capabilities of vision-language models (VLMs). By incorporating extensive OCR corpus into the pretraining stage, VLMs like GPT4o \[[2](#bib.bib2)\] and Qwen2-VL \[[3](#bib.bib3)\] have demonstrated comparable performance in document content extraction tasks. Unlike pipeline-based methods, VLMs perform document parsing in an end-to-end manner. Furthermore, without requiring specialized data fine-tuning, these models are able to deal with diverse and even unseen document types for their generalization capabilities.

To integrate the efficiency of lightweight models and the generalizability of VLMs, many works \[[7](#bib.bib7), [46](#bib.bib46), [29](#bib.bib29), [45](#bib.bib45), [14](#bib.bib14), [32](#bib.bib32)\] have focus on training specialized end-to-end expert models for document parsing. These VLM-driven models excel at comprehending both visual layouts and textual contents, balancing a trade-off between accuracy and efficiency.

### 2.3 Benchmarks for Document Content Extraction

Document content extraction requires the ability to understand document layouts and recognize various types of content. However, current benchmarks fall short of a comprehensive page-level evaluation, as they focus solely on evaluating the model’s performance on module-level recognition. PubLayNet \[[49](#bib.bib49)\] and concurrent benchmarks \[[26](#bib.bib26), [35](#bib.bib35), [9](#bib.bib9)\] specialize in evaluating a model’s ability to detect document page layouts. OCRBench \[[31](#bib.bib31)\] proposes five OCR-related tasks with a greater emphasis on evaluating the model’s visual understanding and reasoning capabilities. Only line-level assessments are provided for text recognition and handwritten mathematical expression recognition (HMER). Similarly, single-module benchmarks \[[20](#bib.bib20), [54](#bib.bib54), [26](#bib.bib26), [40](#bib.bib40)\] disentangle the task into different dimensions and focus narrowly on specific parts. Such paradigm overlooks the importance of structural and semantic information like the reading order and fails to evaluate the model’s overall ability when processing the full-page documents as a whole.

Page-level benchmarks have been proposed alongside some recent VLM-driven expert models \[[29](#bib.bib29), [7](#bib.bib7), [45](#bib.bib45)\]. However, the robustness of these benchmarks is compromised by limitations in data size, language, document type, and annotation. For example, Nougat \[[7](#bib.bib7)\] evaluates models using only printed English documents collected from arXiv while the page-level benchmark introduced by GOT-OCR \[[45](#bib.bib45)\] consists of only 90 pages of Chinese and English documents in total. Commonly-seen document types like handwritten notes, newspapers, and exam papers are further neglected. Lacking detailed annotations, the benchmarks can only conduct naive evaluation between the full-page results of Ground Truths and predictions without special handling for different output formats and specialized metrics for different content types. The evaluation of the model performance can be severely biased due to limited document domains, unaligned output format and mismatched metrics. Therefore, there is an urgent need for a more finely annotated, diverse, and reasonable page-level document content extraction benchmark.

## 3 OmniDocBench Dataset

Constructing a diverse and comprehensive document parsing benchmark with precise annotations is a significant challenge. As illustrated in Figure [3](#S3.F3 "Figure 3 ‣ 3.1 Data Acquisition ‣ 3 OmniDocBench Dataset ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), we have designed a systematic and professional annotation framework for OmniDocBench, encompassing data acquisition, intelligent pre-annotation, and manual refinement. This ensures that OmniDocBench possesses the following key attributes:

- <span id="S3.I1.i1">•</span>

  Page Diversity. We sourced document pages from a variety of origins to ensure a wide range of document types.

- <span id="S3.I1.i2">•</span>

  Comprehensive Annotation. We meticulously annotated all elements on the pages, including bounding boxes, specific contents, and various potential attributes.

- <span id="S3.I1.i3">•</span>

  Annotation Accuracy. By integrating semi-automated annotation processes, annotator corrections, and expert quality checks, we ensure the reliability of all annotations.

The following sections detail the data acquisition process, the annotation methodology, and a statistical analysis of the final annotated dataset.

### 3.1 Data Acquisition

During the data acquisition phase, we sourced document pages from diverse origins and used clustering algorithms to initially select visually diverse pages, followed by manual annotation of page attributes to finalize the OmniDocBench pages. Specifically, we collected over 200,000 initial PDF documents from Common Crawl, Google, Baidu search engines, and internal data. Subsequently, we extracted visual features from these document pages using ResNet-50 and performed clustering using Faiss <sup>11</sup> 1 <https://github.com/facebookresearch/faiss>, sampling 6,000 visually diverse pages from 10 cluster centers. Finally, annotators provided page-level attribute annotations, including page type, layout type, and language type, and further balanced the selection to 981 samples for the final dataset. The OmniDocBench dataset includes pages from nine distinct types, multiple layout categories, and various attribute annotations, covering a wide range of real-world scenarios.

<figure id="S3.F3" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/annotation_pipeline.png" id="S3.F3.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:343/159;" width="343" height="159" alt="Refer to caption" />
<figcaption>Figure 3: Overview of the OmniDocBench dataset construction.</figcaption>
</figure>

### 3.2 Data Annotation

To ensure the comprehensiveness of OmniDocBench’s annotations, we conducted detailed annotations for layout detection and content recognition.

#### 3.2.1 Annotation Types

Layout Detection Annotations: Unlike typical layout detection tasks, OmniDocBench includes four comprehensive types of annotations: (1) Layout Bounding Box Annotations: Positioanl information for 19 distinct region categories such as titles, text paragraphs, tables, and images. (2) Layout Attribute Annotations: Detailed attribute annotations for detected boxes, including 3 text box attribute categories, 6 table attribute categories, 9 bbox-level attribute labels in total. (3) Reading Order Annotations: Annotating the reading sequence of detected boxes. (4) Affiliation Annotations: For images, tables, formulas, and code blocks, we annotate captions and titles to distinguish them from main text. Similarly, for cross-page paragraphs, we annotate affiliation relationships.

Content Recognition Annotations: Based on the content type within each region, we conduct the following three types of annotations: (1) Text Annotations: Pure text annotations for titles, text paragraphs, and other plain text content. (2) Formula Annotations: LaTeX format annotations for inline formulas, display formulas, and subscripts. (3) Table Annotations: Providing both HTML and LaTeX annotations for table data.

#### 3.2.2 Annotation Process

For these annotation tasks on diverse pages, we design a standardized process to ensure quality and efficiency, comprising intelligent automatic annotation, annotator correction, and expert quality inspection.

Automatic Annotation. Manually annotating entire documents is time-consuming and costly. To enhance efficiency, we employ state-of-the-art detection and recognition models for pre-annotation of layout detection and content recognition. Specifically, we use fine-tuned LayoutLMv3 \[[17](#bib.bib17)\] for layout detection annotations and PaddleOCR \[[23](#bib.bib23)\], UniMERNet \[[40](#bib.bib40)\], and GPT-4o \[[2](#bib.bib2)\] for text, formula, and table annotations, respectively.

Annotator Correction. After the layout detection phase, annotators refine the detection boxes and enhance annotations with reading order and affiliation details. Each character is verified to ensure accuracy in content recognition. For complex annotations of tables and formulas, requiring LaTeX and HTML formats, annotators use tools like Tables Generator <sup>22</sup> 2 <https://www.tablesgenerator.com/> and latexlive <sup>33</sup> 3 <https://www.latexlive.com/> for verification and correction.

Expert Quality Inspection. Despite thorough annotator corrections, the complexity of formulas and tables may result in residual issues. To address these, we use CDM’s rendering techniques \[[41](#bib.bib41)\] to identify unrenderable elements. These elements are then reviewed and corrected by three researchers to ensure accuracy in the final annotations.

### 3.3 Dataset Statistics

Page Diversity. OmniDocBench comprises a total of 981 PDF pages across 9 distinct types. Each page is annotated with global attributes, including text language, column layout type, and indicators for blurred scans, watermarks, and colored backgrounds.

Annotation Diversity: OmniDocBench contains over 100,000 annotations for page detection and recognition: (1) More than 20,000 block-level annotations across 15 categories, including over 15,979 text paragraphs, 989 image boxes, 428 table boxes, and so on. All document components except headers, footers, and page notes are labeled with reading order information, totaling over 16,000 annotations. (2) The dataset also includes more than 70,000 span-level annotations across 4 categories, with 4,009 inline formulas and 357 footnote markers represented in LaTeX format, while the remaining annotations are in text format.

Annotation Attribute Diversity: (1) Text Attributes: All block-level annotations, except for tables and images, include text attribute tags. In addition to standard Chinese and English text, there are over 2,000 blocks with complex backgrounds and 493 with rotated text. (2) Table Attributes: In addition to standard Chinese and English tables, there are 142 tables with complex backgrounds, 81 containing formulas, 150 with merged cells, and 7 vertical tables.

## 4 OmniDocBench Evaluation Methodology

To provide a fair and comprehensive evaluation for various models, we proposed an end-to-end evaluation pipeline consisting of several modules, including extraction, matching algorithm, and metric calculation, as shown in Figure [4](#S4.F4 "Figure 4 ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"). It ensures that OmniDocBench automatically performs unified evaluation on document parsing, thereby producing reliable and effective evaluation results.

<figure id="S4.F4" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/Eval_pipeline_small.png" id="S4.F4.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:329/204;" width="329" height="204" alt="Refer to caption" />
<figcaption>Figure 4: OmniDocBench Evaluation Pipeline.</figcaption>
</figure>

### 4.1 Extraction

Preprocessing. The model-generated markdown text should be preprocessed, which includes removing images, eliminating markdown tags at the beginning of the document, and standardizing the number of repeated characters.

Elements Extraction. Extraction is primarily carried out using regular expression matching. To ensure that the extraction of elements does not interfere with each other, it is necessary to follow a specific order. The extraction sequence is as follows: LaTeX tables, HTML tables, display formulas, markdown tables (which are then converted into HTML format), and code blocks.

Pure Text Extraction. After extracting special components, the remaining content is considered pure text. Paragraphs are separated by double line breaks, allowing them to participate in subsequent matching processes, thus aligning with reading order annotation units in the GTs. If no double line break exists, single line breaks are used for paragraph separation. Additionally, previously extracted code blocks are merged into the text category for processing.

Inline Formula Format Converting. We standardized inline formulas within paragraphs to Unicode format. This was necessary because different models produce inconsistent outputs for inline formulas. For formulas originally written in Unicode, it is hard to extract them using regular expressions. Therefore, to ensure a fair comparison, we do not extract inline formulas for separate evaluation. Instead, we include them in their Unicode format alongside the text paragraphs for evaluation.

Reading Order Extraction. Upon completion of the extraction, the start and end positions of the extracted content in the original markdown are recorded for subsequent reading order calculation.

<figure id="S4.T2" class="ltx_table">
<table id="S4.T2.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T2.3.1.1" class="ltx_tr">
<td rowspan="2" id="S4.T2.3.1.1.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Method Type</td>
<td rowspan="2" id="S4.T2.3.1.1.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Methods</td>
<td colspan="2" id="S4.T2.3.1.1.3" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Text<sup>Edit</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↓</mo><annotation encoding="application/x-tex">\downarrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.4" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Formula<sup>Edit</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↓</mo><annotation encoding="application/x-tex">\downarrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.5" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Formula<sup>CDM</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↑</mo><annotation encoding="application/x-tex">\uparrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.6" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Table<sup>TEDS</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↑</mo><annotation encoding="application/x-tex">\uparrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.7" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Table<sup>Edit</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↓</mo><annotation encoding="application/x-tex">\downarrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.8" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Read Order<sup>Edit</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↓</mo><annotation encoding="application/x-tex">\downarrow</annotation></semantics></math></td>
<td colspan="2" id="S4.T2.3.1.1.9" class="ltx_td ltx_align_center ltx_border_tt">Overall<sup>Edit</sup><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>↓</mo><annotation encoding="application/x-tex">\downarrow</annotation></semantics></math></td>
</tr>
<tr id="S4.T2.3.1.2" class="ltx_tr">
<td id="S4.T2.3.1.2.1" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.2" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.3" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.4" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.5" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.6" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.7" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.8" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.9" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.10" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.11" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">ZH</td>
<td id="S4.T2.3.1.2.13" class="ltx_td ltx_align_center ltx_border_t">EN</td>
<td id="S4.T2.3.1.2.14" class="ltx_td ltx_align_center ltx_border_t">ZH</td>
</tr>
<tr id="S4.T2.3.1.3" class="ltx_tr">
<td rowspan="3" id="S4.T2.3.1.3.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Pipeline Tools</td>
<td id="S4.T2.3.1.3.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">MinerU [<a href="#bib.bib42">42</a>]</td>
<td id="S4.T2.3.1.3.3" class="ltx_td ltx_align_center ltx_border_t">0.061</td>
<td id="S4.T2.3.1.3.4" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.215</td>
<td id="S4.T2.3.1.3.5" class="ltx_td ltx_align_center ltx_border_t">0.278</td>
<td id="S4.T2.3.1.3.6" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.577</td>
<td id="S4.T2.3.1.3.7" class="ltx_td ltx_align_center ltx_border_t">57.3</td>
<td id="S4.T2.3.1.3.8" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">42.9</td>
<td id="S4.T2.3.1.3.9" class="ltx_td ltx_align_center ltx_border_t">78.6</td>
<td id="S4.T2.3.1.3.10" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">62.1</td>
<td id="S4.T2.3.1.3.11" class="ltx_td ltx_align_center ltx_border_t">0.18</td>
<td id="S4.T2.3.1.3.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.344</td>
<td id="S4.T2.3.1.3.13" class="ltx_td ltx_align_center ltx_border_t">0.079</td>
<td id="S4.T2.3.1.3.14" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.292</td>
<td id="S4.T2.3.1.3.15" class="ltx_td ltx_align_center ltx_border_t">0.15</td>
<td id="S4.T2.3.1.3.16" class="ltx_td ltx_align_center ltx_border_t">0.357</td>
</tr>
<tr id="S4.T2.3.1.4" class="ltx_tr">
<td id="S4.T2.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r">Marker [<a href="#bib.bib34">34</a>]</td>
<td id="S4.T2.3.1.4.2" class="ltx_td ltx_align_center">0.08</td>
<td id="S4.T2.3.1.4.3" class="ltx_td ltx_align_center ltx_border_r">0.315</td>
<td id="S4.T2.3.1.4.4" class="ltx_td ltx_align_center">0.53</td>
<td id="S4.T2.3.1.4.5" class="ltx_td ltx_align_center ltx_border_r">0.883</td>
<td id="S4.T2.3.1.4.6" class="ltx_td ltx_align_center">17.6</td>
<td id="S4.T2.3.1.4.7" class="ltx_td ltx_align_center ltx_border_r">11.7</td>
<td id="S4.T2.3.1.4.8" class="ltx_td ltx_align_center">67.6</td>
<td id="S4.T2.3.1.4.9" class="ltx_td ltx_align_center ltx_border_r">49.2</td>
<td id="S4.T2.3.1.4.10" class="ltx_td ltx_align_center">0.619</td>
<td id="S4.T2.3.1.4.11" class="ltx_td ltx_align_center ltx_border_r">0.685</td>
<td id="S4.T2.3.1.4.12" class="ltx_td ltx_align_center">0.114</td>
<td id="S4.T2.3.1.4.13" class="ltx_td ltx_align_center ltx_border_r">0.34</td>
<td id="S4.T2.3.1.4.14" class="ltx_td ltx_align_center">0.336</td>
<td id="S4.T2.3.1.4.15" class="ltx_td ltx_align_center">0.556</td>
</tr>
<tr id="S4.T2.3.1.5" class="ltx_tr">
<td id="S4.T2.3.1.5.1" class="ltx_td ltx_align_left ltx_border_r">Mathpix <sup>44</sup> 4 <a href="https://mathpix.com/">https://mathpix.com/</a></td>
<td id="S4.T2.3.1.5.2" class="ltx_td ltx_align_center">0.105</td>
<td id="S4.T2.3.1.5.3" class="ltx_td ltx_align_center ltx_border_r">0.384</td>
<td id="S4.T2.3.1.5.4" class="ltx_td ltx_align_center">0.306</td>
<td id="S4.T2.3.1.5.5" class="ltx_td ltx_align_center ltx_border_r">0.454</td>
<td id="S4.T2.3.1.5.6" class="ltx_td ltx_align_center">62.7</td>
<td id="S4.T2.3.1.5.7" class="ltx_td ltx_align_center ltx_border_r">62.1</td>
<td id="S4.T2.3.1.5.8" class="ltx_td ltx_align_center">77.0</td>
<td id="S4.T2.3.1.5.9" class="ltx_td ltx_align_center ltx_border_r">67.1</td>
<td id="S4.T2.3.1.5.10" class="ltx_td ltx_align_center">0.243</td>
<td id="S4.T2.3.1.5.11" class="ltx_td ltx_align_center ltx_border_r">0.32</td>
<td id="S4.T2.3.1.5.12" class="ltx_td ltx_align_center">0.108</td>
<td id="S4.T2.3.1.5.13" class="ltx_td ltx_align_center ltx_border_r">0.304</td>
<td id="S4.T2.3.1.5.14" class="ltx_td ltx_align_center">0.191</td>
<td id="S4.T2.3.1.5.15" class="ltx_td ltx_align_center">0.365</td>
</tr>
<tr id="S4.T2.3.1.6" class="ltx_tr">
<td rowspan="2" id="S4.T2.3.1.6.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Expert VLMs</td>
<td id="S4.T2.3.1.6.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T2.3.1.6.3" class="ltx_td ltx_align_center ltx_border_t">0.189</td>
<td id="S4.T2.3.1.6.4" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.315</td>
<td id="S4.T2.3.1.6.5" class="ltx_td ltx_align_center ltx_border_t">0.360</td>
<td id="S4.T2.3.1.6.6" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.528</td>
<td id="S4.T2.3.1.6.7" class="ltx_td ltx_align_center ltx_border_t">74.3</td>
<td id="S4.T2.3.1.6.8" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">45.3</td>
<td id="S4.T2.3.1.6.9" class="ltx_td ltx_align_center ltx_border_t">53.2</td>
<td id="S4.T2.3.1.6.10" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">47.2</td>
<td id="S4.T2.3.1.6.11" class="ltx_td ltx_align_center ltx_border_t">0.459</td>
<td id="S4.T2.3.1.6.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.52</td>
<td id="S4.T2.3.1.6.13" class="ltx_td ltx_align_center ltx_border_t">0.141</td>
<td id="S4.T2.3.1.6.14" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.28</td>
<td id="S4.T2.3.1.6.15" class="ltx_td ltx_align_center ltx_border_t">0.287</td>
<td id="S4.T2.3.1.6.16" class="ltx_td ltx_align_center ltx_border_t">0.411</td>
</tr>
<tr id="S4.T2.3.1.7" class="ltx_tr">
<td id="S4.T2.3.1.7.1" class="ltx_td ltx_align_left ltx_border_r">Nougat [<a href="#bib.bib7">7</a>]</td>
<td id="S4.T2.3.1.7.2" class="ltx_td ltx_align_center">0.365</td>
<td id="S4.T2.3.1.7.3" class="ltx_td ltx_align_center ltx_border_r">0.998</td>
<td id="S4.T2.3.1.7.4" class="ltx_td ltx_align_center">0.488</td>
<td id="S4.T2.3.1.7.5" class="ltx_td ltx_align_center ltx_border_r">0.941</td>
<td id="S4.T2.3.1.7.6" class="ltx_td ltx_align_center">15.1</td>
<td id="S4.T2.3.1.7.7" class="ltx_td ltx_align_center ltx_border_r">16.8</td>
<td id="S4.T2.3.1.7.8" class="ltx_td ltx_align_center">39.9</td>
<td id="S4.T2.3.1.7.9" class="ltx_td ltx_align_center ltx_border_r">0.0</td>
<td id="S4.T2.3.1.7.10" class="ltx_td ltx_align_center">0.572</td>
<td id="S4.T2.3.1.7.11" class="ltx_td ltx_align_center ltx_border_r">1.000</td>
<td id="S4.T2.3.1.7.12" class="ltx_td ltx_align_center">0.382</td>
<td id="S4.T2.3.1.7.13" class="ltx_td ltx_align_center ltx_border_r">0.954</td>
<td id="S4.T2.3.1.7.14" class="ltx_td ltx_align_center">0.452</td>
<td id="S4.T2.3.1.7.15" class="ltx_td ltx_align_center">0.973</td>
</tr>
<tr id="S4.T2.3.1.8" class="ltx_tr">
<td rowspan="3" id="S4.T2.3.1.8.1" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">General VLMs</td>
<td id="S4.T2.3.1.8.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T2.3.1.8.3" class="ltx_td ltx_align_center ltx_border_t">0.144</td>
<td id="S4.T2.3.1.8.4" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.409</td>
<td id="S4.T2.3.1.8.5" class="ltx_td ltx_align_center ltx_border_t">0.425</td>
<td id="S4.T2.3.1.8.6" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.606</td>
<td id="S4.T2.3.1.8.7" class="ltx_td ltx_align_center ltx_border_t">72.8</td>
<td id="S4.T2.3.1.8.8" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">42.8</td>
<td id="S4.T2.3.1.8.9" class="ltx_td ltx_align_center ltx_border_t">72.0</td>
<td id="S4.T2.3.1.8.10" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">62.9</td>
<td id="S4.T2.3.1.8.11" class="ltx_td ltx_align_center ltx_border_t">0.234</td>
<td id="S4.T2.3.1.8.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.329</td>
<td id="S4.T2.3.1.8.13" class="ltx_td ltx_align_center ltx_border_t">0.128</td>
<td id="S4.T2.3.1.8.14" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.251</td>
<td id="S4.T2.3.1.8.15" class="ltx_td ltx_align_center ltx_border_t">0.233</td>
<td id="S4.T2.3.1.8.16" class="ltx_td ltx_align_center ltx_border_t">0.399</td>
</tr>
<tr id="S4.T2.3.1.9" class="ltx_tr">
<td id="S4.T2.3.1.9.1" class="ltx_td ltx_align_left ltx_border_r">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T2.3.1.9.2" class="ltx_td ltx_align_center">0.096</td>
<td id="S4.T2.3.1.9.3" class="ltx_td ltx_align_center ltx_border_r">0.218</td>
<td id="S4.T2.3.1.9.4" class="ltx_td ltx_align_center">0.404</td>
<td id="S4.T2.3.1.9.5" class="ltx_td ltx_align_center ltx_border_r">0.487</td>
<td id="S4.T2.3.1.9.6" class="ltx_td ltx_align_center">82.2</td>
<td id="S4.T2.3.1.9.7" class="ltx_td ltx_align_center ltx_border_r">61.2</td>
<td id="S4.T2.3.1.9.8" class="ltx_td ltx_align_center">76.8</td>
<td id="S4.T2.3.1.9.9" class="ltx_td ltx_align_center ltx_border_r">76.4</td>
<td id="S4.T2.3.1.9.10" class="ltx_td ltx_align_center">0.387</td>
<td id="S4.T2.3.1.9.11" class="ltx_td ltx_align_center ltx_border_r">0.408</td>
<td id="S4.T2.3.1.9.12" class="ltx_td ltx_align_center">0.119</td>
<td id="S4.T2.3.1.9.13" class="ltx_td ltx_align_center ltx_border_r">0.193</td>
<td id="S4.T2.3.1.9.14" class="ltx_td ltx_align_center">0.252</td>
<td id="S4.T2.3.1.9.15" class="ltx_td ltx_align_center">0.327</td>
</tr>
<tr id="S4.T2.3.1.10" class="ltx_tr">
<td id="S4.T2.3.1.10.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T2.3.1.10.2" class="ltx_td ltx_align_center ltx_border_bb">0.353</td>
<td id="S4.T2.3.1.10.3" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.290</td>
<td id="S4.T2.3.1.10.4" class="ltx_td ltx_align_center ltx_border_bb">0.543</td>
<td id="S4.T2.3.1.10.5" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.701</td>
<td id="S4.T2.3.1.10.6" class="ltx_td ltx_align_center ltx_border_bb">67.4</td>
<td id="S4.T2.3.1.10.7" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">44.1</td>
<td id="S4.T2.3.1.10.8" class="ltx_td ltx_align_center ltx_border_bb">63.0</td>
<td id="S4.T2.3.1.10.9" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">60.2</td>
<td id="S4.T2.3.1.10.10" class="ltx_td ltx_align_center ltx_border_bb">0.547</td>
<td id="S4.T2.3.1.10.11" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.555</td>
<td id="S4.T2.3.1.10.12" class="ltx_td ltx_align_center ltx_border_bb">0.317</td>
<td id="S4.T2.3.1.10.13" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.228</td>
<td id="S4.T2.3.1.10.14" class="ltx_td ltx_align_center ltx_border_bb">0.44</td>
<td id="S4.T2.3.1.10.15" class="ltx_td ltx_align_center ltx_border_bb">0.443</td>
</tr>
</tbody>
</table>
<figcaption>Table 2: Comprehensive evaluation of document parsing algorithms on OmniDocBench: performance metrics for text, formula, table, and reading order extraction, with overall scores derived from ground truth comparisons.</figcaption>
</figure>

<figure id="S4.T3" class="ltx_table">
<table id="S4.T3.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T3.3.1.1" class="ltx_tr">
<td id="S4.T3.3.1.1.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Model Type</td>
<td id="S4.T3.3.1.1.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Models</td>
<td id="S4.T3.3.1.1.3" class="ltx_td ltx_align_center ltx_border_tt">Book</td>
<td id="S4.T3.3.1.1.4" class="ltx_td ltx_align_center ltx_border_tt">Slides</td>
<td id="S4.T3.3.1.1.5" class="ltx_td ltx_align_center ltx_border_tt">Financial Report</td>
<td id="S4.T3.3.1.1.6" class="ltx_td ltx_align_center ltx_border_tt">Textbook</td>
<td id="S4.T3.3.1.1.7" class="ltx_td ltx_align_center ltx_border_tt">Exam Paper</td>
<td id="S4.T3.3.1.1.8" class="ltx_td ltx_align_center ltx_border_tt">Magazine</td>
<td id="S4.T3.3.1.1.9" class="ltx_td ltx_align_center ltx_border_tt">Academic Papers</td>
<td id="S4.T3.3.1.1.10" class="ltx_td ltx_align_center ltx_border_tt">Notes</td>
<td id="S4.T3.3.1.1.11" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Newspaper</td>
<td id="S4.T3.3.1.1.12" class="ltx_td ltx_align_center ltx_border_tt">Overall</td>
</tr>
<tr id="S4.T3.3.1.2" class="ltx_tr">
<td rowspan="3" id="S4.T3.3.1.2.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Pipeline Tools</td>
<td id="S4.T3.3.1.2.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">MinerU [<a href="#bib.bib42">42</a>]</td>
<td id="S4.T3.3.1.2.3" class="ltx_td ltx_align_center ltx_border_t">0.055</td>
<td id="S4.T3.3.1.2.4" class="ltx_td ltx_align_center ltx_border_t">0.124</td>
<td id="S4.T3.3.1.2.5" class="ltx_td ltx_align_center ltx_border_t">0.033</td>
<td id="S4.T3.3.1.2.6" class="ltx_td ltx_align_center ltx_border_t">0.102</td>
<td id="S4.T3.3.1.2.7" class="ltx_td ltx_align_center ltx_border_t">0.159</td>
<td id="S4.T3.3.1.2.8" class="ltx_td ltx_align_center ltx_border_t">0.072</td>
<td id="S4.T3.3.1.2.9" class="ltx_td ltx_align_center ltx_border_t">0.025</td>
<td id="S4.T3.3.1.2.10" class="ltx_td ltx_align_center ltx_border_t">0.984</td>
<td id="S4.T3.3.1.2.11" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.171</td>
<td id="S4.T3.3.1.2.12" class="ltx_td ltx_align_center ltx_border_t">0.206</td>
</tr>
<tr id="S4.T3.3.1.3" class="ltx_tr">
<td id="S4.T3.3.1.3.1" class="ltx_td ltx_align_left ltx_border_r">Marker [<a href="#bib.bib34">34</a>]</td>
<td id="S4.T3.3.1.3.2" class="ltx_td ltx_align_center">0.074</td>
<td id="S4.T3.3.1.3.3" class="ltx_td ltx_align_center">0.34</td>
<td id="S4.T3.3.1.3.4" class="ltx_td ltx_align_center">0.089</td>
<td id="S4.T3.3.1.3.5" class="ltx_td ltx_align_center">0.319</td>
<td id="S4.T3.3.1.3.6" class="ltx_td ltx_align_center">0.452</td>
<td id="S4.T3.3.1.3.7" class="ltx_td ltx_align_center">0.153</td>
<td id="S4.T3.3.1.3.8" class="ltx_td ltx_align_center">0.059</td>
<td id="S4.T3.3.1.3.9" class="ltx_td ltx_align_center">0.651</td>
<td id="S4.T3.3.1.3.10" class="ltx_td ltx_align_center ltx_border_r">0.192</td>
<td id="S4.T3.3.1.3.11" class="ltx_td ltx_align_center">0.274</td>
</tr>
<tr id="S4.T3.3.1.4" class="ltx_tr">
<td id="S4.T3.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r">Mathpix <sup><a href="#footnote4" title="Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations">4</a></sup></td>
<td id="S4.T3.3.1.4.2" class="ltx_td ltx_align_center">0.131</td>
<td id="S4.T3.3.1.4.3" class="ltx_td ltx_align_center">0.22</td>
<td id="S4.T3.3.1.4.4" class="ltx_td ltx_align_center">0.202</td>
<td id="S4.T3.3.1.4.5" class="ltx_td ltx_align_center">0.216</td>
<td id="S4.T3.3.1.4.6" class="ltx_td ltx_align_center">0.278</td>
<td id="S4.T3.3.1.4.7" class="ltx_td ltx_align_center">0.147</td>
<td id="S4.T3.3.1.4.8" class="ltx_td ltx_align_center">0.091</td>
<td id="S4.T3.3.1.4.9" class="ltx_td ltx_align_center">0.634</td>
<td id="S4.T3.3.1.4.10" class="ltx_td ltx_align_center ltx_border_r">0.69</td>
<td id="S4.T3.3.1.4.11" class="ltx_td ltx_align_center">0.3</td>
</tr>
<tr id="S4.T3.3.1.5" class="ltx_tr">
<td rowspan="2" id="S4.T3.3.1.5.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Expert VLMs</td>
<td id="S4.T3.3.1.5.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T3.3.1.5.3" class="ltx_td ltx_align_center ltx_border_t">0.111</td>
<td id="S4.T3.3.1.5.4" class="ltx_td ltx_align_center ltx_border_t">0.222</td>
<td id="S4.T3.3.1.5.5" class="ltx_td ltx_align_center ltx_border_t">0.067</td>
<td id="S4.T3.3.1.5.6" class="ltx_td ltx_align_center ltx_border_t">0.132</td>
<td id="S4.T3.3.1.5.7" class="ltx_td ltx_align_center ltx_border_t">0.204</td>
<td id="S4.T3.3.1.5.8" class="ltx_td ltx_align_center ltx_border_t">0.198</td>
<td id="S4.T3.3.1.5.9" class="ltx_td ltx_align_center ltx_border_t">0.179</td>
<td id="S4.T3.3.1.5.10" class="ltx_td ltx_align_center ltx_border_t">0.388</td>
<td id="S4.T3.3.1.5.11" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.771</td>
<td id="S4.T3.3.1.5.12" class="ltx_td ltx_align_center ltx_border_t">0.267</td>
</tr>
<tr id="S4.T3.3.1.6" class="ltx_tr">
<td id="S4.T3.3.1.6.1" class="ltx_td ltx_align_left ltx_border_r">Nougat [<a href="#bib.bib7">7</a>]</td>
<td id="S4.T3.3.1.6.2" class="ltx_td ltx_align_center">0.734</td>
<td id="S4.T3.3.1.6.3" class="ltx_td ltx_align_center">0.958</td>
<td id="S4.T3.3.1.6.4" class="ltx_td ltx_align_center">1.000</td>
<td id="S4.T3.3.1.6.5" class="ltx_td ltx_align_center">0.820</td>
<td id="S4.T3.3.1.6.6" class="ltx_td ltx_align_center">0.930</td>
<td id="S4.T3.3.1.6.7" class="ltx_td ltx_align_center">0.83</td>
<td id="S4.T3.3.1.6.8" class="ltx_td ltx_align_center">0.214</td>
<td id="S4.T3.3.1.6.9" class="ltx_td ltx_align_center">0.991</td>
<td id="S4.T3.3.1.6.10" class="ltx_td ltx_align_center ltx_border_r">0.871</td>
<td id="S4.T3.3.1.6.11" class="ltx_td ltx_align_center">0.806</td>
</tr>
<tr id="S4.T3.3.1.7" class="ltx_tr">
<td rowspan="3" id="S4.T3.3.1.7.1" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">General VLMs</td>
<td id="S4.T3.3.1.7.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T3.3.1.7.3" class="ltx_td ltx_align_center ltx_border_t">0.157</td>
<td id="S4.T3.3.1.7.4" class="ltx_td ltx_align_center ltx_border_t">0.163</td>
<td id="S4.T3.3.1.7.5" class="ltx_td ltx_align_center ltx_border_t">0.348</td>
<td id="S4.T3.3.1.7.6" class="ltx_td ltx_align_center ltx_border_t">0.187</td>
<td id="S4.T3.3.1.7.7" class="ltx_td ltx_align_center ltx_border_t">0.281</td>
<td id="S4.T3.3.1.7.8" class="ltx_td ltx_align_center ltx_border_t">0.173</td>
<td id="S4.T3.3.1.7.9" class="ltx_td ltx_align_center ltx_border_t">0.146</td>
<td id="S4.T3.3.1.7.10" class="ltx_td ltx_align_center ltx_border_t">0.607</td>
<td id="S4.T3.3.1.7.11" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.751</td>
<td id="S4.T3.3.1.7.12" class="ltx_td ltx_align_center ltx_border_t">0.316</td>
</tr>
<tr id="S4.T3.3.1.8" class="ltx_tr">
<td id="S4.T3.3.1.8.1" class="ltx_td ltx_align_left ltx_border_r">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T3.3.1.8.2" class="ltx_td ltx_align_center">0.096</td>
<td id="S4.T3.3.1.8.3" class="ltx_td ltx_align_center">0.061</td>
<td id="S4.T3.3.1.8.4" class="ltx_td ltx_align_center">0.047</td>
<td id="S4.T3.3.1.8.5" class="ltx_td ltx_align_center">0.149</td>
<td id="S4.T3.3.1.8.6" class="ltx_td ltx_align_center">0.195</td>
<td id="S4.T3.3.1.8.7" class="ltx_td ltx_align_center">0.071</td>
<td id="S4.T3.3.1.8.8" class="ltx_td ltx_align_center">0.085</td>
<td id="S4.T3.3.1.8.9" class="ltx_td ltx_align_center">0.168</td>
<td id="S4.T3.3.1.8.10" class="ltx_td ltx_align_center ltx_border_r">0.676</td>
<td id="S4.T3.3.1.8.11" class="ltx_td ltx_align_center">0.179</td>
</tr>
<tr id="S4.T3.3.1.9" class="ltx_tr">
<td id="S4.T3.3.1.9.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T3.3.1.9.2" class="ltx_td ltx_align_center ltx_border_bb">0.216</td>
<td id="S4.T3.3.1.9.3" class="ltx_td ltx_align_center ltx_border_bb">0.098</td>
<td id="S4.T3.3.1.9.4" class="ltx_td ltx_align_center ltx_border_bb">0.162</td>
<td id="S4.T3.3.1.9.5" class="ltx_td ltx_align_center ltx_border_bb">0.184</td>
<td id="S4.T3.3.1.9.6" class="ltx_td ltx_align_center ltx_border_bb">0.247</td>
<td id="S4.T3.3.1.9.7" class="ltx_td ltx_align_center ltx_border_bb">0.150</td>
<td id="S4.T3.3.1.9.8" class="ltx_td ltx_align_center ltx_border_bb">0.419</td>
<td id="S4.T3.3.1.9.9" class="ltx_td ltx_align_center ltx_border_bb">0.226</td>
<td id="S4.T3.3.1.9.10" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.903</td>
<td id="S4.T3.3.1.9.11" class="ltx_td ltx_align_center ltx_border_bb">0.3</td>
</tr>
</tbody>
</table>
<figcaption>Table 3: End-to-end text recognition performance on OmniDocBench: evaluation using edit distance across 9 PDF page types.</figcaption>
</figure>

<figure id="S4.T4" class="ltx_table">
<table id="S4.T4.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T4.3.1.1" class="ltx_tr">
<td id="S4.T4.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Models</td>
<td id="S4.T4.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Fuzzy</td>
<td id="S4.T4.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Water</td>
<td id="S4.T4.3.1.1.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Color</td>
<td id="S4.T4.3.1.1.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">None</td>
</tr>
<tr id="S4.T4.3.1.2" class="ltx_tr">
<td id="S4.T4.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">MinerU [<a href="#bib.bib42">42</a>]</td>
<td id="S4.T4.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.15/0.048</td>
<td id="S4.T4.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.151/0.031</td>
<td id="S4.T4.3.1.2.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.107/0.052</td>
<td id="S4.T4.3.1.2.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.079/0.035</td>
</tr>
<tr id="S4.T4.3.1.3" class="ltx_tr">
<td id="S4.T4.3.1.3.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Marker [<a href="#bib.bib34">34</a>]</td>
<td id="S4.T4.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.333/0.092</td>
<td id="S4.T4.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.484/0.126</td>
<td id="S4.T4.3.1.3.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.319/0.127</td>
<td id="S4.T4.3.1.3.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.062/0.125</td>
</tr>
<tr id="S4.T4.3.1.4" class="ltx_tr">
<td id="S4.T4.3.1.4.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Mathpix <sup><a href="#footnote4" title="Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations">4</a></sup></td>
<td id="S4.T4.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.294/0.064</td>
<td id="S4.T4.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.290/0.059</td>
<td id="S4.T4.3.1.4.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.216/0.09</td>
<td id="S4.T4.3.1.4.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.135/0.043</td>
</tr>
<tr id="S4.T4.3.1.5" class="ltx_tr">
<td id="S4.T4.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T4.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.175/0.05</td>
<td id="S4.T4.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.190/0.056</td>
<td id="S4.T4.3.1.5.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.186/0.097</td>
<td id="S4.T4.3.1.5.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.177/0.081</td>
</tr>
<tr id="S4.T4.3.1.6" class="ltx_tr">
<td id="S4.T4.3.1.6.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Nougat [<a href="#bib.bib7">7</a>]</td>
<td id="S4.T4.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.934/0.051</td>
<td id="S4.T4.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.915/0.071</td>
<td id="S4.T4.3.1.6.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.873/0.096</td>
<td id="S4.T4.3.1.6.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.615/0.208</td>
</tr>
<tr id="S4.T4.3.1.7" class="ltx_tr">
<td id="S4.T4.3.1.7.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T4.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.263/0.078</td>
<td id="S4.T4.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.195/0.057</td>
<td id="S4.T4.3.1.7.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.184/0.078</td>
<td id="S4.T4.3.1.7.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.186/0.072</td>
</tr>
<tr id="S4.T4.3.1.8" class="ltx_tr">
<td id="S4.T4.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T4.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.082 /0.01</td>
<td id="S4.T4.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.172/ 0.078</td>
<td id="S4.T4.3.1.8.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.104/0.05</td>
<td id="S4.T4.3.1.8.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.084/0.042</td>
</tr>
<tr id="S4.T4.3.1.9" class="ltx_tr">
<td id="S4.T4.3.1.9.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T4.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.120/0.013</td>
<td id="S4.T4.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.197/0.042</td>
<td id="S4.T4.3.1.9.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.155/0.059</td>
<td id="S4.T4.3.1.9.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.261/0.082</td>
</tr>
</tbody>
</table>
<figcaption>Table 4: End-to-end text recognition on OmniDocBench: evaluation under various page attributes using the edit distance metric. The value is Mean/Variance of scores in the attribute group. Columns represent: Fuzzy (Fuzzy scan), Water (Watermark), Color (Colorful background). None (No special issue)</figcaption>
</figure>

<figure id="S4.T5" class="ltx_table">
<table id="S4.T5.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T5.3.1.1" class="ltx_tr">
<td id="S4.T5.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Models</td>
<td id="S4.T5.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Single</td>
<td id="S4.T5.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Double</td>
<td id="S4.T5.3.1.1.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Three</td>
<td id="S4.T5.3.1.1.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Complex</td>
</tr>
<tr id="S4.T5.3.1.2" class="ltx_tr">
<td id="S4.T5.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">MinerU [<a href="#bib.bib42">42</a>]</td>
<td id="S4.T5.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.311/0.187</td>
<td id="S4.T5.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.101/0.013</td>
<td id="S4.T5.3.1.2.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.117/0.046</td>
<td id="S4.T5.3.1.2.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.385/0.057</td>
</tr>
<tr id="S4.T5.3.1.3" class="ltx_tr">
<td id="S4.T5.3.1.3.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Marker [<a href="#bib.bib34">34</a>]</td>
<td id="S4.T5.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.299/0.143</td>
<td id="S4.T5.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.299/0.299</td>
<td id="S4.T5.3.1.3.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.149/0.063</td>
<td id="S4.T5.3.1.3.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.363/0.086</td>
</tr>
<tr id="S4.T5.3.1.4" class="ltx_tr">
<td id="S4.T5.3.1.4.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Mathpix <sup><a href="#footnote4" title="Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations">4</a></sup></td>
<td id="S4.T5.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.207/0.123</td>
<td id="S4.T5.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.188/0.07</td>
<td id="S4.T5.3.1.4.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.225/0.029</td>
<td id="S4.T5.3.1.4.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.452/0.177</td>
</tr>
<tr id="S4.T5.3.1.5" class="ltx_tr">
<td id="S4.T5.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T5.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.163/0.106</td>
<td id="S4.T5.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.145/0.059</td>
<td id="S4.T5.3.1.5.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.257/0.072</td>
<td id="S4.T5.3.1.5.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.468/0.185</td>
</tr>
<tr id="S4.T5.3.1.6" class="ltx_tr">
<td id="S4.T5.3.1.6.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Nougat [<a href="#bib.bib7">7</a>]</td>
<td id="S4.T5.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.852/0.084</td>
<td id="S4.T5.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.601/0.224</td>
<td id="S4.T5.3.1.6.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.662/0.093</td>
<td id="S4.T5.3.1.6.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.873/0.09</td>
</tr>
<tr id="S4.T5.3.1.7" class="ltx_tr">
<td id="S4.T5.3.1.7.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T5.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.109/0.112</td>
<td id="S4.T5.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.204/0.076</td>
<td id="S4.T5.3.1.7.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.254/0.046</td>
<td id="S4.T5.3.1.7.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.426/0.188</td>
</tr>
<tr id="S4.T5.3.1.8" class="ltx_tr">
<td id="S4.T5.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T5.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.066/0.048</td>
<td id="S4.T5.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.145/0.049</td>
<td id="S4.T5.3.1.8.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.204/0.055</td>
<td id="S4.T5.3.1.8.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.394/0.203</td>
</tr>
<tr id="S4.T5.3.1.9" class="ltx_tr">
<td id="S4.T5.3.1.9.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T5.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.082/0.052</td>
<td id="S4.T5.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.312/0.069</td>
<td id="S4.T5.3.1.9.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.682/0.098</td>
<td id="S4.T5.3.1.9.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.444/0.174</td>
</tr>
</tbody>
</table>
<figcaption>Table 5: End-to-end reading order evaluation on OmniDocBench: results across different column layout types using Normalized Edit Distance. The value is Mean/Variance of scores in the attribute group.</figcaption>
</figure>

### 4.2 Matching Algorithm

Adjacency Search Match. To avoid the impact of paragraph splitting on the final results, we proposed Adjacency Search Match, that merges and splits paragraphs in both GTs and Preds to achieve the best possible match. The specific strategy involves: i) Calculate a metrix of Normalized Edit Distance between GTs and Preds. The Pred and GT pairs whose similarity exceeds a specific threshold are considered as successful match. ii) For the rest, we apply fuzzy matching to determine whether one string is a subset of another string. If so, we further apply the merging algorithm which would try to merge adjacent paragraph. This process would continue to merge more paragraph until the Normalized Edit Distance starts to decrease. After this process, the best match will be found for GTs and Preds.

Ignore Handling. We implement an ignore logic for certain components in PDF page content, meaning they participate in matching but are excluded from metric calculations. This is mainly because of inconsistent output standards among models, which should not affect the validation results. For fairness, we ignore: (1) Headers, footers, page numbers, and page footnotes, which are handled inconsistently by different models. (2) Captions for figures, tables, and footnotes often have uncertain placements, thus complicating the reading order. Additionally, some models embed table captions in HTML or LaTeX tables, while others treat them as plain text.

<figure id="S4.T6" class="ltx_table">
<table id="S4.T6.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T6.3.1.1" class="ltx_tr">
<td id="S4.T6.3.1.1.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Model</td>
<td id="S4.T6.3.1.1.2" class="ltx_td ltx_align_center ltx_border_tt">Backbone</td>
<td id="S4.T6.3.1.1.3" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Params</td>
<td id="S4.T6.3.1.1.4" class="ltx_td ltx_align_center ltx_border_tt">Book</td>
<td id="S4.T6.3.1.1.5" class="ltx_td ltx_align_center ltx_border_tt">Slides</td>
<td id="S4.T6.3.1.1.6" class="ltx_td ltx_align_center ltx_border_tt">Research Report</td>
<td id="S4.T6.3.1.1.7" class="ltx_td ltx_align_center ltx_border_tt">Textbook</td>
<td id="S4.T6.3.1.1.8" class="ltx_td ltx_align_center ltx_border_tt">Exam Paper</td>
<td id="S4.T6.3.1.1.9" class="ltx_td ltx_align_center ltx_border_tt">Magazine</td>
<td id="S4.T6.3.1.1.10" class="ltx_td ltx_align_center ltx_border_tt">Academic Literature</td>
<td id="S4.T6.3.1.1.11" class="ltx_td ltx_align_center ltx_border_tt">Notes</td>
<td id="S4.T6.3.1.1.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Newspaper</td>
<td id="S4.T6.3.1.1.13" class="ltx_td ltx_align_center ltx_border_tt">Average</td>
</tr>
<tr id="S4.T6.3.1.2" class="ltx_tr">
<td id="S4.T6.3.1.2.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">DiT-L [<a href="#bib.bib24">24</a>]</td>
<td id="S4.T6.3.1.2.2" class="ltx_td ltx_align_center ltx_border_t">ViT-L</td>
<td id="S4.T6.3.1.2.3" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">361.6M</td>
<td id="S4.T6.3.1.2.4" class="ltx_td ltx_align_center ltx_border_t">43.44</td>
<td id="S4.T6.3.1.2.5" class="ltx_td ltx_align_center ltx_border_t">13.72</td>
<td id="S4.T6.3.1.2.6" class="ltx_td ltx_align_center ltx_border_t">45.85</td>
<td id="S4.T6.3.1.2.7" class="ltx_td ltx_align_center ltx_border_t">15.45</td>
<td id="S4.T6.3.1.2.8" class="ltx_td ltx_align_center ltx_border_t">3.40</td>
<td id="S4.T6.3.1.2.9" class="ltx_td ltx_align_center ltx_border_t">29.23</td>
<td id="S4.T6.3.1.2.10" class="ltx_td ltx_align_center ltx_border_t">66.13</td>
<td id="S4.T6.3.1.2.11" class="ltx_td ltx_align_center ltx_border_t">0.21</td>
<td id="S4.T6.3.1.2.12" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">23.65</td>
<td id="S4.T6.3.1.2.13" class="ltx_td ltx_align_center ltx_border_t">26.90</td>
</tr>
<tr id="S4.T6.3.1.3" class="ltx_tr">
<td id="S4.T6.3.1.3.1" class="ltx_td ltx_align_left ltx_border_r">LayoutLMv3 [<a href="#bib.bib17">17</a>]</td>
<td id="S4.T6.3.1.3.2" class="ltx_td ltx_align_center">RoBERTa-B</td>
<td id="S4.T6.3.1.3.3" class="ltx_td ltx_align_center ltx_border_r">138.4M</td>
<td id="S4.T6.3.1.3.4" class="ltx_td ltx_align_center">42.12</td>
<td id="S4.T6.3.1.3.5" class="ltx_td ltx_align_center">13.63</td>
<td id="S4.T6.3.1.3.6" class="ltx_td ltx_align_center">43.22</td>
<td id="S4.T6.3.1.3.7" class="ltx_td ltx_align_center">21.00</td>
<td id="S4.T6.3.1.3.8" class="ltx_td ltx_align_center">5.48</td>
<td id="S4.T6.3.1.3.9" class="ltx_td ltx_align_center">31.81</td>
<td id="S4.T6.3.1.3.10" class="ltx_td ltx_align_center">64.66</td>
<td id="S4.T6.3.1.3.11" class="ltx_td ltx_align_center">0.80</td>
<td id="S4.T6.3.1.3.12" class="ltx_td ltx_align_center ltx_border_r">30.84</td>
<td id="S4.T6.3.1.3.13" class="ltx_td ltx_align_center">28.84</td>
</tr>
<tr id="S4.T6.3.1.4" class="ltx_tr">
<td id="S4.T6.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r">DocLayout-YOLO [<a href="#bib.bib53">53</a>]</td>
<td id="S4.T6.3.1.4.2" class="ltx_td ltx_align_center">v10m</td>
<td id="S4.T6.3.1.4.3" class="ltx_td ltx_align_center ltx_border_r">19.6M</td>
<td id="S4.T6.3.1.4.4" class="ltx_td ltx_align_center">43.71</td>
<td id="S4.T6.3.1.4.5" class="ltx_td ltx_align_center">48.71</td>
<td id="S4.T6.3.1.4.6" class="ltx_td ltx_align_center">72.83</td>
<td id="S4.T6.3.1.4.7" class="ltx_td ltx_align_center">42.67</td>
<td id="S4.T6.3.1.4.8" class="ltx_td ltx_align_center">35.40</td>
<td id="S4.T6.3.1.4.9" class="ltx_td ltx_align_center">51.44</td>
<td id="S4.T6.3.1.4.10" class="ltx_td ltx_align_center">64.64</td>
<td id="S4.T6.3.1.4.11" class="ltx_td ltx_align_center">9.54</td>
<td id="S4.T6.3.1.4.12" class="ltx_td ltx_align_center ltx_border_r">57.54</td>
<td id="S4.T6.3.1.4.13" class="ltx_td ltx_align_center">47.38</td>
</tr>
<tr id="S4.T6.3.1.5" class="ltx_tr">
<td id="S4.T6.3.1.5.1" class="ltx_td ltx_align_left ltx_border_r">SwinDocSegmenter [<a href="#bib.bib4">4</a>]</td>
<td id="S4.T6.3.1.5.2" class="ltx_td ltx_align_center">Swin-L</td>
<td id="S4.T6.3.1.5.3" class="ltx_td ltx_align_center ltx_border_r">223M</td>
<td id="S4.T6.3.1.5.4" class="ltx_td ltx_align_center">42.91</td>
<td id="S4.T6.3.1.5.5" class="ltx_td ltx_align_center">28.20</td>
<td id="S4.T6.3.1.5.6" class="ltx_td ltx_align_center">47.29</td>
<td id="S4.T6.3.1.5.7" class="ltx_td ltx_align_center">32.44</td>
<td id="S4.T6.3.1.5.8" class="ltx_td ltx_align_center">20.81</td>
<td id="S4.T6.3.1.5.9" class="ltx_td ltx_align_center">52.35</td>
<td id="S4.T6.3.1.5.10" class="ltx_td ltx_align_center">48.54</td>
<td id="S4.T6.3.1.5.11" class="ltx_td ltx_align_center">12.38</td>
<td id="S4.T6.3.1.5.12" class="ltx_td ltx_align_center ltx_border_r">38.06</td>
<td id="S4.T6.3.1.5.13" class="ltx_td ltx_align_center">35.89</td>
</tr>
<tr id="S4.T6.3.1.6" class="ltx_tr">
<td id="S4.T6.3.1.6.1" class="ltx_td ltx_align_left ltx_border_r">GraphKD [<a href="#bib.bib5">5</a>]</td>
<td id="S4.T6.3.1.6.2" class="ltx_td ltx_align_center">R101</td>
<td id="S4.T6.3.1.6.3" class="ltx_td ltx_align_center ltx_border_r">44.5M</td>
<td id="S4.T6.3.1.6.4" class="ltx_td ltx_align_center">39.03</td>
<td id="S4.T6.3.1.6.5" class="ltx_td ltx_align_center">16.18</td>
<td id="S4.T6.3.1.6.6" class="ltx_td ltx_align_center">39.92</td>
<td id="S4.T6.3.1.6.7" class="ltx_td ltx_align_center">22.82</td>
<td id="S4.T6.3.1.6.8" class="ltx_td ltx_align_center">14.31</td>
<td id="S4.T6.3.1.6.9" class="ltx_td ltx_align_center">37.61</td>
<td id="S4.T6.3.1.6.10" class="ltx_td ltx_align_center">44.43</td>
<td id="S4.T6.3.1.6.11" class="ltx_td ltx_align_center">5.71</td>
<td id="S4.T6.3.1.6.12" class="ltx_td ltx_align_center ltx_border_r">23.86</td>
<td id="S4.T6.3.1.6.13" class="ltx_td ltx_align_center">27.10</td>
</tr>
<tr id="S4.T6.3.1.7" class="ltx_tr">
<td id="S4.T6.3.1.7.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r">DOCX-Chain [<a href="#bib.bib50">50</a>]</td>
<td id="S4.T6.3.1.7.2" class="ltx_td ltx_align_center ltx_border_bb">-</td>
<td id="S4.T6.3.1.7.3" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">-</td>
<td id="S4.T6.3.1.7.4" class="ltx_td ltx_align_center ltx_border_bb">30.86</td>
<td id="S4.T6.3.1.7.5" class="ltx_td ltx_align_center ltx_border_bb">11.71</td>
<td id="S4.T6.3.1.7.6" class="ltx_td ltx_align_center ltx_border_bb">39.62</td>
<td id="S4.T6.3.1.7.7" class="ltx_td ltx_align_center ltx_border_bb">19.23</td>
<td id="S4.T6.3.1.7.8" class="ltx_td ltx_align_center ltx_border_bb">10.67</td>
<td id="S4.T6.3.1.7.9" class="ltx_td ltx_align_center ltx_border_bb">23.00</td>
<td id="S4.T6.3.1.7.10" class="ltx_td ltx_align_center ltx_border_bb">41.60</td>
<td id="S4.T6.3.1.7.11" class="ltx_td ltx_align_center ltx_border_bb">1.80</td>
<td id="S4.T6.3.1.7.12" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">16.96</td>
<td id="S4.T6.3.1.7.13" class="ltx_td ltx_align_center ltx_border_bb">21.27</td>
</tr>
</tbody>
</table>
<figcaption>Table 6: Component-level layout detection evaluation on OmniDocBench layout subset: mAP results by PDF page type.</figcaption>
</figure>

<figure id="S4.T7" class="ltx_table">
<table id="S4.T7.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T7.3.1.1" class="ltx_tr">
<td rowspan="2" id="S4.T7.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Model Type</td>
<td rowspan="2" id="S4.T7.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Model</td>
<td colspan="3" id="S4.T7.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Language</td>
<td colspan="4" id="S4.T7.3.1.1.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Table Frame Type</td>
<td colspan="4" id="S4.T7.3.1.1.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Special Situation</td>
<td rowspan="2" id="S4.T7.3.1.1.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_tt" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Overall</td>
</tr>
<tr id="S4.T7.3.1.2" class="ltx_tr">
<td id="S4.T7.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">EN</td>
<td id="S4.T7.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">ZH</td>
<td id="S4.T7.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Mixed</td>
<td id="S4.T7.3.1.2.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Full</td>
<td id="S4.T7.3.1.2.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Omission</td>
<td id="S4.T7.3.1.2.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Three</td>
<td id="S4.T7.3.1.2.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Zero</td>
<td id="S4.T7.3.1.2.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Merge Cell(+/-)</td>
<td id="S4.T7.3.1.2.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Formula(+/-)</td>
<td id="S4.T7.3.1.2.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Colorful (+/-)</td>
<td id="S4.T7.3.1.2.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Rotate(+/-)</td>
</tr>
<tr id="S4.T7.3.1.3" class="ltx_tr">
<td rowspan="2" id="S4.T7.3.1.3.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">OCR-based Models</td>
<td id="S4.T7.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">PaddleOCR[<a href="#bib.bib23">23</a>]</td>
<td id="S4.T7.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">76.8</td>
<td id="S4.T7.3.1.3.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.8</td>
<td id="S4.T7.3.1.3.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">80.1</td>
<td id="S4.T7.3.1.3.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">67.9</td>
<td id="S4.T7.3.1.3.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">74.3</td>
<td id="S4.T7.3.1.3.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">81.1</td>
<td id="S4.T7.3.1.3.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">74.5</td>
<td id="S4.T7.3.1.3.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.6/75.2</td>
<td id="S4.T7.3.1.3.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.3/74.1</td>
<td id="S4.T7.3.1.3.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.7/74.0</td>
<td id="S4.T7.3.1.3.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">23.3/74.6</td>
<td id="S4.T7.3.1.3.14" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">73.6</td>
</tr>
<tr id="S4.T7.3.1.4" class="ltx_tr">
<td id="S4.T7.3.1.4.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">RapidTable[<a href="#bib.bib37">37</a>]</td>
<td id="S4.T7.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">80.0</td>
<td id="S4.T7.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">83.2</td>
<td id="S4.T7.3.1.4.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">91.2</td>
<td id="S4.T7.3.1.4.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">83.0</td>
<td id="S4.T7.3.1.4.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">79.7</td>
<td id="S4.T7.3.1.4.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">83.4</td>
<td id="S4.T7.3.1.4.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">78.4</td>
<td id="S4.T7.3.1.4.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">77.1/85.4</td>
<td id="S4.T7.3.1.4.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">76.7/83.9</td>
<td id="S4.T7.3.1.4.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">77.6/84.9</td>
<td id="S4.T7.3.1.4.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">25.2/83.7</td>
<td id="S4.T7.3.1.4.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">82.5</td>
</tr>
<tr id="S4.T7.3.1.5" class="ltx_tr">
<td rowspan="2" id="S4.T7.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Expert VLMs</td>
<td id="S4.T7.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">StructEqTable[<a href="#bib.bib55">55</a>]</td>
<td id="S4.T7.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.8</td>
<td id="S4.T7.3.1.5.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">75.9</td>
<td id="S4.T7.3.1.5.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">83.4</td>
<td id="S4.T7.3.1.5.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.9</td>
<td id="S4.T7.3.1.5.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">76.2</td>
<td id="S4.T7.3.1.5.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">76.9</td>
<td id="S4.T7.3.1.5.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">88.0</td>
<td id="S4.T7.3.1.5.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">64.5/81.0</td>
<td id="S4.T7.3.1.5.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">69.2/76.6</td>
<td id="S4.T7.3.1.5.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.8/76.4</td>
<td id="S4.T7.3.1.5.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">30.5/76.2</td>
<td id="S4.T7.3.1.5.14" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">75.8</td>
</tr>
<tr id="S4.T7.3.1.6" class="ltx_tr">
<td id="S4.T7.3.1.6.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T7.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.2</td>
<td id="S4.T7.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">75.5</td>
<td id="S4.T7.3.1.6.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">85.4</td>
<td id="S4.T7.3.1.6.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">73.1</td>
<td id="S4.T7.3.1.6.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">72.7</td>
<td id="S4.T7.3.1.6.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">78.2</td>
<td id="S4.T7.3.1.6.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">75.7</td>
<td id="S4.T7.3.1.6.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">65.0/80.2</td>
<td id="S4.T7.3.1.6.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">64.3/77.3</td>
<td id="S4.T7.3.1.6.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.8/76.9</td>
<td id="S4.T7.3.1.6.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">8.5/76.3</td>
<td id="S4.T7.3.1.6.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.1pt; padding-bottom: -0.1pt">74.9</td>
</tr>
<tr id="S4.T7.3.1.7" class="ltx_tr">
<td rowspan="2" id="S4.T7.3.1.7.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">General VLMs</td>
<td id="S4.T7.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">Qwen2-VL-7B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T7.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.2</td>
<td id="S4.T7.3.1.7.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.7</td>
<td id="S4.T7.3.1.7.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">82.4</td>
<td id="S4.T7.3.1.7.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.2</td>
<td id="S4.T7.3.1.7.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">62.8</td>
<td id="S4.T7.3.1.7.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">74.5</td>
<td id="S4.T7.3.1.7.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">80.3</td>
<td id="S4.T7.3.1.7.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">60.8/76.5</td>
<td id="S4.T7.3.1.7.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">63.8/72.6</td>
<td id="S4.T7.3.1.7.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.4/70.8</td>
<td id="S4.T7.3.1.7.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">20.0/72.1</td>
<td id="S4.T7.3.1.7.14" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.0</td>
</tr>
<tr id="S4.T7.3.1.8" class="ltx_tr">
<td id="S4.T7.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">InternVL2-8B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T7.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">70.9</td>
<td id="S4.T7.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.5</td>
<td id="S4.T7.3.1.8.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">77.4</td>
<td id="S4.T7.3.1.8.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">69.5</td>
<td id="S4.T7.3.1.8.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">69.2</td>
<td id="S4.T7.3.1.8.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">74.8</td>
<td id="S4.T7.3.1.8.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">75.8</td>
<td id="S4.T7.3.1.8.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">58.7/78.4</td>
<td id="S4.T7.3.1.8.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">62.4/73.6</td>
<td id="S4.T7.3.1.8.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">68.2/73.1</td>
<td id="S4.T7.3.1.8.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.1pt; padding-bottom: -0.1pt">20.4/72.6</td>
<td id="S4.T7.3.1.8.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.1pt; padding-bottom: -0.1pt">71.5</td>
</tr>
</tbody>
</table>
<figcaption>Table 7: Component-level Table Recognition evaluation on OmniDocBench table subset. (+/-) means with/without special situation.</figcaption>
</figure>

<figure id="S4.T8" class="ltx_table">
<table id="S4.T8.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T8.3.1.1" class="ltx_tr">
<td rowspan="2" id="S4.T8.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Model Type</td>
<td rowspan="2" id="S4.T8.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_tt" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Model</td>
<td colspan="3" id="S4.T8.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Language</td>
<td colspan="3" id="S4.T8.3.1.1.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Text background</td>
<td colspan="4" id="S4.T8.3.1.1.5" class="ltx_td ltx_nopad_l ltx_align_center ltx_border_tt" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Text Rotate</td>
</tr>
<tr id="S4.T8.3.1.2" class="ltx_tr">
<td id="S4.T8.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">EN</td>
<td id="S4.T8.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">ZH</td>
<td id="S4.T8.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Mixed</td>
<td id="S4.T8.3.1.2.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">White</td>
<td id="S4.T8.3.1.2.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Single</td>
<td id="S4.T8.3.1.2.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Multi</td>
<td id="S4.T8.3.1.2.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Normal</td>
<td id="S4.T8.3.1.2.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Rotate90</td>
<td id="S4.T8.3.1.2.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Rotate270</td>
<td id="S4.T8.3.1.2.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Horizontal</td>
</tr>
<tr id="S4.T8.3.1.3" class="ltx_tr">
<td rowspan="5" id="S4.T8.3.1.3.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Expert Vision Models</td>
<td id="S4.T8.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">PaddleOCR [<a href="#bib.bib23">23</a>]</td>
<td id="S4.T8.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.071</td>
<td id="S4.T8.3.1.3.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.055</td>
<td id="S4.T8.3.1.3.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.118</td>
<td id="S4.T8.3.1.3.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.060</td>
<td id="S4.T8.3.1.3.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.038</td>
<td id="S4.T8.3.1.3.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.085</td>
<td id="S4.T8.3.1.3.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.060</td>
<td id="S4.T8.3.1.3.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.015</td>
<td id="S4.T8.3.1.3.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.285</td>
<td id="S4.T8.3.1.3.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.021</td>
</tr>
<tr id="S4.T8.3.1.4" class="ltx_tr">
<td id="S4.T8.3.1.4.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Tesseract OCR <sup>55</sup> 5 <a href="https://github.com/tesseract-ocr/tesseract">https://github.com/tesseract-ocr/tesseract</a></td>
<td id="S4.T8.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.179</td>
<td id="S4.T8.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.553</td>
<td id="S4.T8.3.1.4.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.553</td>
<td id="S4.T8.3.1.4.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.453</td>
<td id="S4.T8.3.1.4.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.463</td>
<td id="S4.T8.3.1.4.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.394</td>
<td id="S4.T8.3.1.4.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.448</td>
<td id="S4.T8.3.1.4.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.369</td>
<td id="S4.T8.3.1.4.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.979</td>
<td id="S4.T8.3.1.4.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.982</td>
</tr>
<tr id="S4.T8.3.1.5" class="ltx_tr">
<td id="S4.T8.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Surya <sup>66</sup> 6 <a href="https://github.com/VikParuchuri/surya">https://github.com/VikParuchuri/surya</a></td>
<td id="S4.T8.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.057</td>
<td id="S4.T8.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.123</td>
<td id="S4.T8.3.1.5.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.164</td>
<td id="S4.T8.3.1.5.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.093</td>
<td id="S4.T8.3.1.5.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.186</td>
<td id="S4.T8.3.1.5.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.235</td>
<td id="S4.T8.3.1.5.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.104</td>
<td id="S4.T8.3.1.5.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.634</td>
<td id="S4.T8.3.1.5.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.767</td>
<td id="S4.T8.3.1.5.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.255</td>
</tr>
<tr id="S4.T8.3.1.6" class="ltx_tr">
<td id="S4.T8.3.1.6.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T8.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.041</td>
<td id="S4.T8.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.112</td>
<td id="S4.T8.3.1.6.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.135</td>
<td id="S4.T8.3.1.6.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.092</td>
<td id="S4.T8.3.1.6.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.052</td>
<td id="S4.T8.3.1.6.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.155</td>
<td id="S4.T8.3.1.6.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.091</td>
<td id="S4.T8.3.1.6.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.562</td>
<td id="S4.T8.3.1.6.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.966</td>
<td id="S4.T8.3.1.6.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.097</td>
</tr>
<tr id="S4.T8.3.1.7" class="ltx_tr">
<td id="S4.T8.3.1.7.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Mathpix <sup><a href="#footnote4" title="Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations">4</a></sup></td>
<td id="S4.T8.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.033</td>
<td id="S4.T8.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.240</td>
<td id="S4.T8.3.1.7.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.261</td>
<td id="S4.T8.3.1.7.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.185</td>
<td id="S4.T8.3.1.7.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.121</td>
<td id="S4.T8.3.1.7.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.166</td>
<td id="S4.T8.3.1.7.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.180</td>
<td id="S4.T8.3.1.7.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.038</td>
<td id="S4.T8.3.1.7.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.185</td>
<td id="S4.T8.3.1.7.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.638</td>
</tr>
<tr id="S4.T8.3.1.8" class="ltx_tr">
<td rowspan="3" id="S4.T8.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Vision Language Models</td>
<td id="S4.T8.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T8.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.072</td>
<td id="S4.T8.3.1.8.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.274</td>
<td id="S4.T8.3.1.8.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.286</td>
<td id="S4.T8.3.1.8.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.234</td>
<td id="S4.T8.3.1.8.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.155</td>
<td id="S4.T8.3.1.8.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.148</td>
<td id="S4.T8.3.1.8.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.223</td>
<td id="S4.T8.3.1.8.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.273</td>
<td id="S4.T8.3.1.8.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.721</td>
<td id="S4.T8.3.1.8.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.067</td>
</tr>
<tr id="S4.T8.3.1.9" class="ltx_tr">
<td id="S4.T8.3.1.9.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T8.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.074</td>
<td id="S4.T8.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.155</td>
<td id="S4.T8.3.1.9.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.242</td>
<td id="S4.T8.3.1.9.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.113</td>
<td id="S4.T8.3.1.9.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.352</td>
<td id="S4.T8.3.1.9.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.269</td>
<td id="S4.T8.3.1.9.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.132</td>
<td id="S4.T8.3.1.9.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.610</td>
<td id="S4.T8.3.1.9.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.907</td>
<td id="S4.T8.3.1.9.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.595</td>
</tr>
<tr id="S4.T8.3.1.10" class="ltx_tr">
<td id="S4.T8.3.1.10.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T8.3.1.10.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.020</td>
<td id="S4.T8.3.1.10.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.224</td>
<td id="S4.T8.3.1.10.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.125</td>
<td id="S4.T8.3.1.10.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.167</td>
<td id="S4.T8.3.1.10.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.140</td>
<td id="S4.T8.3.1.10.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.220</td>
<td id="S4.T8.3.1.10.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.168</td>
<td id="S4.T8.3.1.10.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.115</td>
<td id="S4.T8.3.1.10.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.718</td>
<td id="S4.T8.3.1.10.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.35pt; padding-bottom: -0.35pt">0.132</td>
</tr>
</tbody>
</table>
<figcaption>Table 8: Component-level evaluation on OmniDocBench OCR subset: results grouped by text attributes using the edit distance metric.</figcaption>
</figure>

<figure id="S4.T9" class="ltx_table">
<table id="S4.T9.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S4.T9.3.1.1" class="ltx_tr">
<td id="S4.T9.3.1.1.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Models</td>
<td id="S4.T9.3.1.1.2" class="ltx_td ltx_align_center ltx_border_tt">CDM</td>
<td id="S4.T9.3.1.1.3" class="ltx_td ltx_align_center ltx_border_tt">ExpRate@CDM</td>
<td id="S4.T9.3.1.1.4" class="ltx_td ltx_align_center ltx_border_tt">BLEU</td>
<td id="S4.T9.3.1.1.5" class="ltx_td ltx_align_center ltx_border_tt">Norm Edit</td>
</tr>
<tr id="S4.T9.3.1.2" class="ltx_tr">
<td id="S4.T9.3.1.2.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GOT-OCR [<a href="#bib.bib45">45</a>]</td>
<td id="S4.T9.3.1.2.2" class="ltx_td ltx_align_center ltx_border_t">74.1</td>
<td id="S4.T9.3.1.2.3" class="ltx_td ltx_align_center ltx_border_t">28.0</td>
<td id="S4.T9.3.1.2.4" class="ltx_td ltx_align_center ltx_border_t">55.07</td>
<td id="S4.T9.3.1.2.5" class="ltx_td ltx_align_center ltx_border_t">0.290</td>
</tr>
<tr id="S4.T9.3.1.3" class="ltx_tr">
<td id="S4.T9.3.1.3.1" class="ltx_td ltx_align_left ltx_border_r">Mathpix <sup><a href="#footnote4" title="Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations">4</a></sup></td>
<td id="S4.T9.3.1.3.2" class="ltx_td ltx_align_center">86.6</td>
<td id="S4.T9.3.1.3.3" class="ltx_td ltx_align_center">2.8</td>
<td id="S4.T9.3.1.3.4" class="ltx_td ltx_align_center">66.56</td>
<td id="S4.T9.3.1.3.5" class="ltx_td ltx_align_center">0.322</td>
</tr>
<tr id="S4.T9.3.1.4" class="ltx_tr">
<td id="S4.T9.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r">Pix2Tex <sup>77</sup> 7 <a href="https://github.com/lukas-blecher/LaTeX-OCR">https://github.com/lukas-blecher/LaTeX-OCR</a></td>
<td id="S4.T9.3.1.4.2" class="ltx_td ltx_align_center">73.9</td>
<td id="S4.T9.3.1.4.3" class="ltx_td ltx_align_center">39.5</td>
<td id="S4.T9.3.1.4.4" class="ltx_td ltx_align_center">46.00</td>
<td id="S4.T9.3.1.4.5" class="ltx_td ltx_align_center">0.337</td>
</tr>
<tr id="S4.T9.3.1.5" class="ltx_tr">
<td id="S4.T9.3.1.5.1" class="ltx_td ltx_align_left ltx_border_r">UniMERNet-B [<a href="#bib.bib40">40</a>]</td>
<td id="S4.T9.3.1.5.2" class="ltx_td ltx_align_center">85.0</td>
<td id="S4.T9.3.1.5.3" class="ltx_td ltx_align_center">60.2</td>
<td id="S4.T9.3.1.5.4" class="ltx_td ltx_align_center">60.84</td>
<td id="S4.T9.3.1.5.5" class="ltx_td ltx_align_center">0.238</td>
</tr>
<tr id="S4.T9.3.1.6" class="ltx_tr">
<td id="S4.T9.3.1.6.1" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GPT4o [<a href="#bib.bib2">2</a>]</td>
<td id="S4.T9.3.1.6.2" class="ltx_td ltx_align_center ltx_border_t">86.8</td>
<td id="S4.T9.3.1.6.3" class="ltx_td ltx_align_center ltx_border_t">65.5</td>
<td id="S4.T9.3.1.6.4" class="ltx_td ltx_align_center ltx_border_t">45.17</td>
<td id="S4.T9.3.1.6.5" class="ltx_td ltx_align_center ltx_border_t">0.282</td>
</tr>
<tr id="S4.T9.3.1.7" class="ltx_tr">
<td id="S4.T9.3.1.7.1" class="ltx_td ltx_align_left ltx_border_r">InternVL2-76B [<a href="#bib.bib8">8</a>]</td>
<td id="S4.T9.3.1.7.2" class="ltx_td ltx_align_center">67.4</td>
<td id="S4.T9.3.1.7.3" class="ltx_td ltx_align_center">54.5</td>
<td id="S4.T9.3.1.7.4" class="ltx_td ltx_align_center">47.63</td>
<td id="S4.T9.3.1.7.5" class="ltx_td ltx_align_center">0.308</td>
</tr>
<tr id="S4.T9.3.1.8" class="ltx_tr">
<td id="S4.T9.3.1.8.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r">Qwen2-VL-72B [<a href="#bib.bib44">44</a>]</td>
<td id="S4.T9.3.1.8.2" class="ltx_td ltx_align_center ltx_border_bb">83.8</td>
<td id="S4.T9.3.1.8.3" class="ltx_td ltx_align_center ltx_border_bb">55.4</td>
<td id="S4.T9.3.1.8.4" class="ltx_td ltx_align_center ltx_border_bb">53.71</td>
<td id="S4.T9.3.1.8.5" class="ltx_td ltx_align_center ltx_border_bb">0.285</td>
</tr>
</tbody>
</table>
<figcaption>Table 9: Component-level formula recognition evaluation on OmniDocBench formula subset.</figcaption>
</figure>

### 4.3 Metric Calculation

Pure Text. We calculate Normalized Edit Distance \[[21](#bib.bib21)\], averaging these metrics at the sample level to obtain the final scores.

Tables. All tables are converted to HTML format before calculating the Tree-Edit-Distance-based Similarity (TEDS) \[[54](#bib.bib54)\] metric and Normalized Edit Distance.

Formulas. Formulas are currently evaluated using the Character Detection Matching (CDM) metric \[[41](#bib.bib41)\], Normalized Edit Distance, and BLEU \[[33](#bib.bib33)\].

Reading Order. Reading order is evaluated using the Normalized Edit Distance as metric. It only involves text components, with tables, images, and ignored components excluded from the final reading order calculation.

## 5 Benchmarks

Based on the distinct characteristics of these algorithms, we categorize document content extraction methods into three main classes:

- <span id="S5.I1.i1">•</span>

  Pipeline Tools: These methods integrate layout detection and various content recognition tasks (such as OCR, table recognition, and formula recognition) into a document parsing pipeline for content extraction. Prominent examples include MinerU \[[42](#bib.bib42)\] (v0.9.3), Marker \[[34](#bib.bib34)\] (v1.2.3), and Mathpix<sup>[4](#footnote4 "Footnote 4 ‣ Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")</sup>.

- <span id="S5.I1.i2">•</span>

  Expert VLMs: These are large multimodal models specifically trained for document parsing tasks. Representative models include GOT-OCR2.0 \[[45](#bib.bib45)\] and Nougat \[[7](#bib.bib7)\].

- <span id="S5.I1.i3">•</span>

  General VLMs: These are general-purpose large multimodal models inherently capable of document parsing. Leading models in this category include GPT-4o \[[2](#bib.bib2)\], Qwen2-VL-72B \[[44](#bib.bib44)\], and InternVL2-76B \[[8](#bib.bib8)\].

### 5.1 End-to-End Evaluation Results

Overall Evaluation Results. As illustrated in Table [2](#S4.T2 "Table 2 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), pipeline tools such as MinerU and Mathpix, demonstrate superior performance across sub-tasks like text recognition, formula recognition, and table recognition. Moreover, the general Vision Language Models (VLMs), Qwen2-VL, and GPT4o, also exhibit competitive performance. Almost all algorithms score higher on English than on Chinese pages.

Performance Across Diverse Page Types. To gain deeper insights into model performance on diverse document types, we evaluated text recognition tasks across different page types. Intriguingly, as shown in Table [3](#S4.T3 "Table 3 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), pipeline tools perform well for commonly used data, such as academic papers and financial reports. Meanwhile, for more specialized data, such as slides and handwritten notes, general VLMs demonstrate stronger generalization. Notably, most VLMs fail to recognize when dealing with the Newspapers, while pipeline tools achieve significantly better performance.

Performance on Pages with Visual Degradations. In Table [4](#S4.T4 "Table 4 ‣ 4.1 Extraction ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), we further analyze performance on pages containing common document-specific challenges, including fuzzy scans, watermarks, and colorful backgrounds. VLMs like InternVL2 and Qwen2-VL exhibit higher robustness in these scenarios despite visual noise. Among pipeline tools, MinerU remains competitive due to its strong layout segmentation and preprocessing capabilities.

Performance on Different Layout Types. Page layout is a critical factor in document understanding, especially for tasks involving reading order. OmniDocBench annotates layout attributes such as single-column, multi-column, and complex custom formats. Across all models, we observe a clear drop in accuracy on multi-column and complex layouts. MinerU shows the most consistent reading order prediction, though its performance dips on handwritten single-column pages due to recognition noise.

Discussion on End-to-End Results. 1) While general VLMs often lag behind specialized pipelines and expert models on standard documents (e.g., academic papers), they generalize better to unconventional formats (e.g., notes) and perform more robustly under degraded conditions (e.g., fuzzy scans). This is largely due to their broader training data, enabling better handling of long-tail scenarios compared to models trained on narrow domains. 2) VLMs, however, struggle with high-density documents like newspapers due to limitations in input resolution and token length. In contrast, pipeline tools leverage layout-based segmentation to process components individually, maintaining accuracy in complex layouts. Enhancing VLMs with layout-aware designs and domain-specific fine-tuning offers a promising path forward. OmniDocBench facilitates this by providing detailed annotations for layout, text, formulas, and tables, enabling comprehensive benchmarking and modular tool development for diverse document parsing tasks.

### 5.2 Single Task Evaluation Results

Layout Detection Results. Layout detection is the first step in document parsing using pipeline tools. A robust layout detection algorithm should perform well across a variety of document types. Table [6](#S4.T6 "Table 6 ‣ 4.2 Matching Algorithm ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") presents an evaluation of leading layout detection models. The DocLayout-YOLO method, which is pre-trained on diverse synthetic document data, significantly outperforms other approaches. This superiority is a key factor in MinerU’s integration of DocLayout-YOLO, contributing to its outstanding overall performance. Other methods perform well on books and academic literature but struggle with more diverse formats due to limited training data.

Table Recognition Results. In Table [7](#S4.T7 "Table 7 ‣ 4.2 Matching Algorithm ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), We evaluate table recognition models across three dimensions on our OmniDocBench table subset: language diversity, table frame types, and special situations. Among all models, OCR-based models demonstrate superior overall performance, with RapidTable achieving the highest scores in language diversity and maintaining stable performance across different frame types. Expert VLMs show competitive results in specific scenarios, with StructEqTable \[[55](#bib.bib55)\] excelling in no-frame tables and showing better rotation robustness. General VLMs (Qwen2-VL-7B and InternVL2-8B) exhibit relatively lower but consistent performance, suggesting that while general-purpose VLMs have made progress in table understanding, they still lag behind specialized solutions.

Text Recognition Results. Table [8](#S4.T8 "Table 8 ‣ 4.2 Matching Algorithm ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") compares OCR tools across languages, backgrounds, and rotations using Edit Distance. PaddleOCR outperforms all competitors, followed by GOT-OCR and Mathpix. General VLMs struggle to handle text rotation or mixed-language scenarios.

Formula Recognition Results. Table [9](#S4.T9 "Table 9 ‣ 4.2 Matching Algorithm ‣ 4 OmniDocBench Evaluation Methodology ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") presents results on formula parsing, using CDM, BLEU, and normalized Edit Distance. GPT-4o, Mathpix, and UniMERNet achieve results of 86.8%, 86.6%, and 85.0%, respectively. Notably, GPT-4o excels with a recall rate of 65.5% under strict conditions requiring perfect character accuracy. Although Mathpix shows high character-level precision, it occasionally omits punctuation, such as commas, leading to a lower overall correctness rate. Nonetheless, all three models are strong candidates for formula recognition tasks.

## 6 Conclusion

This paper addresses the lack of diverse and realistic benchmarks in document parsing research by introducing OmniDocBench, a dataset featuring a variety of page types with comprehensive annotations, along with a flexible and reliable evaluation framework. OmniDocBench enables systematic and fair assessments of document parsing methods, providing crucial insights for advancing the field. Its task-specific and attribute-level evaluations facilitate targeted model optimization, promoting more robust and effective parsing solutions.

## References

- <span id="bib.bib1">\[1\] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. *arXiv:2303.08774*, 2023.</span>
- <span id="bib.bib2">\[2\] Open AI. Hello gpt 4o, 2024. Accessed July 24, 2024.</span>
- <span id="bib.bib3">\[3\] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv:2308.12966*, 2024.</span>
- <span id="bib.bib4">\[4\] Ayan Banerjee, Sanket Biswas, Josep Lladós, and Umapada Pal. Swindocsegmenter: An end-to-end unified domain adaptive transformer for document instance segmentation. In *ICDAR*, 2023.</span>
- <span id="bib.bib5">\[5\] Ayan Banerjee, Sanket Biswas, Josep Lladós, and Umapada Pal. Graphkd: Exploring knowledge distillation towards document object detection with structured graph creation. In *ICDAR*, 2024.</span>
- <span id="bib.bib6">\[6\] Lukas Blecher. pix2tex - latex ocr. <https://github.com/lukas-blecher/LaTeX-OCR>, 2022. Accessed: 2024-2-29.</span>
- <span id="bib.bib7">\[7\] Lukas Blecher, Guillem Cucurull, Thomas Scialom, and Robert Stojnic. Nougat: Neural optical understanding for academic documents. *arXiv:2308.13418*, 2024.</span>
- <span id="bib.bib8">\[8\] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, Bin Li, Ping Luo, Tong Lu, Yu Qiao, and Jifeng Dai. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 24185–24198, 2024.</span>
- <span id="bib.bib9">\[9\] Hiuyi Cheng, Peirong Zhang, Sihang Wu, Jiaxin Zhang, Qiyuan Zhu, Zecheng Xie, Jing Li, Kai Ding, and Lianwen Jin. M6doc: A large-scale multi-format, multi-type, multi-layout, multi-language, multi-annotation category dataset for modern document layout analysis. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 15138–15147, 2023.</span>
- <span id="bib.bib10">\[10\] Yuntian Deng, Anssi Kanervisto, Jeffrey Ling, and Alexander M Rush. Image-to-markup generation with coarse-to-fine attention. In *International Conference on Machine Learning*, pages 980–989. PMLR, 2017.</span>
- <span id="bib.bib11">\[11\] Harsh Desai, Pratik Kayal, and Mayank Singh. Tablex: a benchmark dataset for structure and content information extraction from scientific tables. In *Document Analysis and Recognition–ICDAR 2021: 16th International Conference*, pages 554–569, 2021.</span>
- <span id="bib.bib12">\[12\] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and Haofen Wang. Retrieval-augmented generation for large language models: A survey. *arXiv:2312.10997*, 2023.</span>
- <span id="bib.bib13">\[13\] Jiuxiang Gu, Jason Kuen, Vlad I Morariu, Handong Zhao, Rajiv Jain, Nikolaos Barmpalios, Ani Nenkova, and Tong Sun. Unidoc: Unified pretraining framework for document understanding. *Advances in Neural Information Processing Systems*, 34:39–50, 2021.</span>
- <span id="bib.bib14">\[14\] Anwen Hu, Haiyang Xu, Liang Zhang, Jiabo Ye, Ming Yan, Ji Zhang, Qin Jin, Fei Huang, and Jingren Zhou. mplug-docowl2: High-resolution compressing for ocr-free multi-page document understanding. *arXiv preprint arXiv:2409.03420*, 2024.</span>
- <span id="bib.bib15">\[15\] Mingxin Huang, Yuliang Liu, Zhenghao Peng, Chongyu Liu, Dahua Lin, Shenggao Zhu, Nicholas Yuan, Kai Ding, and Lianwen Jin. Swintextspotter: Scene text spotting via better synergy between text detection and text recognition. In *proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 4593–4603, 2022a.</span>
- <span id="bib.bib16">\[16\] Xin Huang, Ashish Khetan, Milan Cvitkovic, and Zohar Karnin. Tabtransformer: Tabular data modeling using contextual embeddings. arxiv 2020. *arXiv preprint arXiv:2012.06678*, 2012.</span>
- <span id="bib.bib17">\[17\] Yupan Huang, Tengchao Lv, Lei Cui, Yutong Lu, and Furu Wei. Layoutlmv3: Pre-training for document ai with unified text and image masking, 2022b.</span>
- <span id="bib.bib18">\[18\] Yongshuai Huang, Ning Lu, Dapeng Chen, Yibo Li, Zecheng Xie, Shenggao Zhu, Liangcai Gao, and Wei Peng. Improving table structure recognition with visual-alignment sequential coordinate modeling. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 11134–11143, 2023.</span>
- <span id="bib.bib19">\[19\] Wonseok Hwang, Jinyeong Yim, Seunghyun Park, Sohee Yang, and Minjoon Seo. Spatial dependency parsing for semi-structured document information extraction. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP*, pages 330–343. Association for Computational Linguistics (ACL), 2021.</span>
- <span id="bib.bib20">\[20\] Dimosthenis Karatzas, Lluis Gomez-Bigorda, Anguelos Nicolaou, Suman Ghosh, Andrew Bagdanov, Masakazu Iwamura, Jiri Matas, Lukas Neumann, Vijay Ramaseshan Chandrasekhar, Shijian Lu, Faisal Shafait, Seiichi Uchida, and Ernest Valveny. Icdar 2015 competition on robust reading. In *2015 13th International Conference on Document Analysis and Recognition*, pages 1156–1160, 2015.</span>
- <span id="bib.bib21">\[21\] Vladimir I Levenshtein et al. Binary codes capable of correcting deletions, insertions, and reversals. In *Doklady Physics*, pages 707–710. Soviet Union, 1966.</span>
- <span id="bib.bib22">\[22\] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. *Advances in Neural Information Processing Systems*, 33:9459–9474, 2020.</span>
- <span id="bib.bib23">\[23\] Chenxia Li, Weiwei Liu, Ruoyu Guo, Xiaoting Yin, Kaitao Jiang, Yongkun Du, Yuning Du, Lingfeng Zhu, Baohua Lai, Xiaoguang Hu, Dianhai Yu, and Yanjun Ma. Pp-ocrv3: More attempts for the improvement of ultra lightweight ocr system, 2022a.</span>
- <span id="bib.bib24">\[24\] Junlong Li, Yiheng Xu, Tengchao Lv, Lei Cui, Cha Zhang, and Furu Wei. Dit: Self-supervised pre-training for document image transformer. In *ACMMM*, 2022b.</span>
- <span id="bib.bib25">\[25\] Minghao Li, Lei Cui, Shaohan Huang, Furu Wei, Ming Zhou, and Zhoujun Li. Tablebank: Table benchmark for image-based table detection and recognition. In *Proceedings of the Twelfth Language Resources and Evaluation Conference*, pages 1918–1925, 2020a.</span>
- <span id="bib.bib26">\[26\] Minghao Li, Yiheng Xu, Lei Cui, Shaohan Huang, Furu Wei, Zhoujun Li, and Ming Zhou. Docbank: A benchmark dataset for document layout analysis. *arXiv:2006.01038*, 2020b.</span>
- <span id="bib.bib27">\[27\] Zhe Li, Lianwen Jin, Songxuan Lai, and Yecheng Zhu. Improving attention-based handwritten mathematical expression recognition with scale augmentation and drop attention. In *2020 17th International Conference on Frontiers in Handwriting Recognition (ICFHR)*, pages 175–180. IEEE, 2020c.</span>
- <span id="bib.bib28">\[28\] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024a.</span>
- <span id="bib.bib29">\[29\] Chenglong Liu, Haoran Wei, Jinyue Chen, Lingyu Kong, Zheng Ge, Zining Zhu, Liang Zhao, Jianjian Sun, Chunrui Han, and Xiangyu Zhang. Focus anywhere for fine-grained multi-page document understanding. *arXiv:2405.14295*, 2024b.</span>
- <span id="bib.bib30">\[30\] Yuliang Liu, Hao Chen, Chunhua Shen, Tong He, Lianwen Jin, and Liangwei Wang. Abcnet: Real-time scene text spotting with adaptive bezier-curve network. In *proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 9809–9818, 2020.</span>
- <span id="bib.bib31">\[31\] Yuliang Liu, Zhang Li, Mingxin Huang, Biao Yang, Wenwen Yu, Chunyuan Li, Xu-Cheng Yin, Cheng-Lin Liu, Lianwen Jin, and Xiang Bai. Ocrbench: on the hidden mystery of ocr in large multimodal models. *Science China Information Sciences*, 67(12), 2024c.</span>
- <span id="bib.bib32">\[32\] Tengchao Lv, Yupan Huang, Jingye Chen, Yuzhong Zhao, Yilin Jia, Lei Cui, Shuming Ma, Yaoyao Chang, Shaohan Huang, Wenhui Wang, Li Dong, Weiyao Luo, Shaoxiang Wu, Guoxin Wang, Cha Zhang, and Furu Wei. Kosmos-2.5: A multimodal literate model, 2024.</span>
- <span id="bib.bib33">\[33\] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. pages 311–318, 2002.</span>
- <span id="bib.bib34">\[34\] Vik Paruchuri. Marker, 2024.</span>
- <span id="bib.bib35">\[35\] Birgit Pfitzmann, Christoph Auer, Michele Dolfi, Ahmed S Nassar, and Peter Staar. Doclaynet: A large human-annotated dataset for document-layout segmentation. In *Proceedings of the 28th ACM SIGKDD conference on knowledge discovery and data mining*, pages 3743–3751, 2022.</span>
- <span id="bib.bib36">\[36\] Subhojeet Pramanik, Shashank Mujumdar, and Hima Patel. Towards a multi-modal, multi-task learning based pre-training framework for document representation learning. *arXiv preprint arXiv:2009.14457*, 2020.</span>
- <span id="bib.bib37">\[37\] RapidAI. Rapidtable. <https://github.com/RapidAI/RapidTable>, 2023.</span>
- <span id="bib.bib38">\[38\] Ray Smith, Daria Antonova, and Dar-Shyang Lee. Adapting the tesseract open source ocr engine for multilingual ocr. In *Proceedings of the International Workshop on Multilingual OCR*, 2009.</span>
- <span id="bib.bib39">\[39\] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.</span>
- <span id="bib.bib40">\[40\] Bin Wang, Zhuangcheng Gu, Guang Liang, Chao Xu, Bo Zhang, Botian Shi, and Conghui He. Unimernet: A universal network for real-world mathematical expression recognition, 2024a.</span>
- <span id="bib.bib41">\[41\] Bin Wang, Fan Wu, Linke Ouyang, Zhuangcheng Gu, Rui Zhang, Renqiu Xia, Bo Zhang, and Conghui He. Cdm: A reliable metric for fair and accurate formula recognition evaluation. *arXiv:2409.03643*, 2024b.</span>
- <span id="bib.bib42">\[42\] Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, Fan Wu, Zhiyuan Zhao, Rui Xu, Kaiwen Liu, Yuan Qu, Fukai Shang, Bo Zhang, Liqun Wei, Zhihao Sui, Wei Li, Botian Shi, Yu Qiao, Dahua Lin, and Conghui He. Mineru: An open-source solution for precise document content extraction. *arXiv:2409.18839*, 2024c.</span>
- <span id="bib.bib43">\[43\] Pengfei Wang, Chengquan Zhang, Fei Qi, Shanshan Liu, Xiaoqiang Zhang, Pengyuan Lyu, Junyu Han, Jingtuo Liu, Errui Ding, and Guangming Shi. Pgnet: Real-time arbitrarily-shaped text spotting with point gathering network. In *Proceedings of the AAAI Conference on Artificial Intelligence*, pages 2782–2790, 2021.</span>
- <span id="bib.bib44">\[44\] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution. *arXiv preprint arXiv:2409.12191*, 2024d.</span>
- <span id="bib.bib45">\[45\] Haoran Wei, Chenglong Liu, Jinyue Chen, Jia Wang, Lingyu Kong, Yanming Xu, Zheng Ge, Liang Zhao, Jianjian Sun, Yuang Peng, et al. General ocr theory: Towards ocr-2.0 via a unified end-to-end model. *arXiv:2409.01704*, 2024.</span>
- <span id="bib.bib46">\[46\] Haoran Wei, Lingyu Kong, Jinyue Chen, Liang Zhao, Zheng Ge, Jinrong Yang, Jianjian Sun, Chunrui Han, and Xiangyu Zhang. Vary: Scaling up the vision vocabulary for large vision-language model. In *European Conference on Computer Vision*, pages 408–424. Springer, 2025.</span>
- <span id="bib.bib47">\[47\] Renqiu Xia, Song Mao, Xiangchao Yan, Hongbin Zhou, Bo Zhang, Haoyang Peng, Jiahao Pi, Daocheng Fu, Wenjie Wu, Hancheng Ye, et al. Docgenome: An open large-scale scientific document benchmark for training and testing multi-modal large language models. *arXiv preprint arXiv:2406.11633*, 2024a.</span>
- <span id="bib.bib48">\[48\] Renqiu Xia, Bo Zhang, Hancheng Ye, Xiangchao Yan, Qi Liu, Hongbin Zhou, Zijun Chen, Min Dou, Botian Shi, Junchi Yan, et al. Chartx & chartvlm: A versatile benchmark and foundation model for complicated chart reasoning. *arXiv preprint arXiv:2402.12185*, 2024b.</span>
- <span id="bib.bib49">\[49\] Zhong Xu, Jianbin Tang, and Antonio Jimeno Yepes. Publaynet: largest dataset ever for document layout analysis. In *2019 International conference on document analysis and recognition*, pages 1015–1022, 2019.</span>
- <span id="bib.bib50">\[50\] Cong Yao. DocXChain: A Powerful Open-Source Toolchain for Document Parsing and Beyond. *ArXiv*, 2023.</span>
- <span id="bib.bib51">\[51\] Jianshu Zhang, Jun Du, and Lirong Dai. Multi-scale attention with dense encoder for handwritten mathematical expression recognition. In *2018 24th international conference on pattern recognition (ICPR)*, pages 2245–2250. IEEE, 2018.</span>
- <span id="bib.bib52">\[52\] Qintong Zhang, Victor Shea-Jay Huang, Bin Wang, Junyuan Zhang, Zhengren Wang, Hao Liang, Shawn Wang, Matthieu Lin, Wentao Zhang, and Conghui He. Document parsing unveiled: Techniques, challenges, and prospects for structured information extraction. *arXiv preprint arXiv:2410.21169*, 2024.</span>
- <span id="bib.bib53">\[53\] Zhiyuan Zhao, Hengrui Kang, Bin Wang, and Conghui He. Doclayout-yolo: Enhancing document layout analysis through diverse synthetic data and global-to-local adaptive perception, 2024.</span>
- <span id="bib.bib54">\[54\] Xu Zhong, Elaheh ShafieiBavani, and Antonio Jimeno Yepes. Image-based table recognition: data, model, and evaluation. In *European conference on computer vision*, pages 564–580, 2020.</span>
- <span id="bib.bib55">\[55\] Hongbin Zhou, Xiangchao Yan, and Bo Zhang. Structeqtable-deploy: A high-efficiency open-source toolkit for table-to-latex transformation. <https://github.com/UniModal4Reasoning/StructEqTable-Deploy>, 2024.</span>

\

Supplementary Material\

## I More End-to-End Evaluation Results

[Table S1](#S1.T1 "In I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") presents the evaluation results of End2End Tables grouped by Table Attributes. As it shows, most of the models perform better in English Tables rather than Chinese ones. Most models perform relatively poorly with Full Frame and No Frame tables. The accuracy of most models is affected by special conditions. Merged cells and formulas mainly test the breadth of data the model can recognize, while colored backgrounds and table rotation test their robustness. The results show that table rotation significantly impacts the accuracy of all models. Pipeline Tools’ performance would not be affected by more challenging tables (e.g., merge cell), but colored backgrounds can affect recognition accuracy. Several Vision Language Models (VLMs) tend to perform worse on tables with merged cells, but colored backgrounds do not significantly impact table recognition accuracy.

[Table S2](#S1.T2 "In I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") shows the evaluation results of End2End Text blocks grouped by Text Attributes. Almost all models have lower recognition accuracy in Chinese compared to English. Some models, such as MinerU and Marker, experience a further decrease in accuracy when recognizing mixed Chinese and English content. The main reason is that minerU’s text recognition module is PaddleOCR model. According to the performance of the PaddleOCR model in text recognition module, its accuracy will decline in the case of mixed language. Moreover, complex background colors significantly affect the recognition accuracy of pipeline tools, but it has only little impact on accuracy for VLMs.

<figure id="S1.T1" class="ltx_table">
<table id="S1.T1.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T1.3.1.1" class="ltx_tr">
<td rowspan="2" id="S1.T1.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Model Type</td>
<td rowspan="2" id="S1.T1.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Model</td>
<td colspan="3" id="S1.T1.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Language</td>
<td colspan="4" id="S1.T1.3.1.1.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Table Frame Type</td>
<td colspan="4" id="S1.T1.3.1.1.5" class="ltx_td ltx_nopad_l ltx_align_center ltx_border_tt" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Special Situation</td>
</tr>
<tr id="S1.T1.3.1.2" class="ltx_tr">
<td id="S1.T1.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">EN</td>
<td id="S1.T1.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">ZH</td>
<td id="S1.T1.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Mixed</td>
<td id="S1.T1.3.1.2.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Full</td>
<td id="S1.T1.3.1.2.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Omission</td>
<td id="S1.T1.3.1.2.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Three</td>
<td id="S1.T1.3.1.2.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Zero</td>
<td id="S1.T1.3.1.2.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Merge Cell(+/-)</td>
<td id="S1.T1.3.1.2.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Formula(+/-)</td>
<td id="S1.T1.3.1.2.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Colorful (+/-)</td>
<td id="S1.T1.3.1.2.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Rotate(+/-)</td>
</tr>
<tr id="S1.T1.3.1.3" class="ltx_tr">
<td rowspan="3" id="S1.T1.3.1.3.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Pipeline Tools</td>
<td id="S1.T1.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">MinerU</td>
<td id="S1.T1.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">75.1</td>
<td id="S1.T1.3.1.3.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">59.3</td>
<td id="S1.T1.3.1.3.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">79.1</td>
<td id="S1.T1.3.1.3.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">59.4</td>
<td id="S1.T1.3.1.3.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">71.6</td>
<td id="S1.T1.3.1.3.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">69.7</td>
<td id="S1.T1.3.1.3.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">60.0</td>
<td id="S1.T1.3.1.3.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">63.6/65.3</td>
<td id="S1.T1.3.1.3.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">66.0/64.4</td>
<td id="S1.T1.3.1.3.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">59.2/67.5</td>
<td id="S1.T1.3.1.3.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">3.0/65.8</td>
</tr>
<tr id="S1.T1.3.1.4" class="ltx_tr">
<td id="S1.T1.3.1.4.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Marker</td>
<td id="S1.T1.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">64.9</td>
<td id="S1.T1.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">47.3</td>
<td id="S1.T1.3.1.4.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">49.8</td>
<td id="S1.T1.3.1.4.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">44.5</td>
<td id="S1.T1.3.1.4.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">61.8</td>
<td id="S1.T1.3.1.4.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">59.0</td>
<td id="S1.T1.3.1.4.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">63.6</td>
<td id="S1.T1.3.1.4.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">52.6/52.7</td>
<td id="S1.T1.3.1.4.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">53.2/52.5</td>
<td id="S1.T1.3.1.4.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">48.0/54.9</td>
<td id="S1.T1.3.1.4.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">35.5/52.9</td>
</tr>
<tr id="S1.T1.3.1.5" class="ltx_tr">
<td id="S1.T1.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Mathpix</td>
<td id="S1.T1.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">75.4</td>
<td id="S1.T1.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">63.2</td>
<td id="S1.T1.3.1.5.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">71.3</td>
<td id="S1.T1.3.1.5.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">67.4</td>
<td id="S1.T1.3.1.5.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">77.3</td>
<td id="S1.T1.3.1.5.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">66.3</td>
<td id="S1.T1.3.1.5.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">25.5</td>
<td id="S1.T1.3.1.5.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">70.3/65.4</td>
<td id="S1.T1.3.1.5.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">68.7/66.7</td>
<td id="S1.T1.3.1.5.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">59.7/70.8</td>
<td id="S1.T1.3.1.5.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">19.2/67.9</td>
</tr>
<tr id="S1.T1.3.1.6" class="ltx_tr">
<td rowspan="2" id="S1.T1.3.1.6.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Expert Vision Models</td>
<td id="S1.T1.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GOT-OCR</td>
<td id="S1.T1.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">51.7</td>
<td id="S1.T1.3.1.6.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">46.2</td>
<td id="S1.T1.3.1.6.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">49.0</td>
<td id="S1.T1.3.1.6.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">45.5</td>
<td id="S1.T1.3.1.6.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">48.3</td>
<td id="S1.T1.3.1.6.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">51.3</td>
<td id="S1.T1.3.1.6.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">46.2</td>
<td id="S1.T1.3.1.6.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">46.0/48.9</td>
<td id="S1.T1.3.1.6.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">45.7/48.4</td>
<td id="S1.T1.3.1.6.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">39.8/51.9</td>
<td id="S1.T1.3.1.6.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.0/48.7</td>
</tr>
<tr id="S1.T1.3.1.7" class="ltx_tr">
<td id="S1.T1.3.1.7.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Nougat</td>
<td id="S1.T1.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">36.2</td>
<td id="S1.T1.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.3</td>
<td id="S1.T1.3.1.7.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.0</td>
<td id="S1.T1.3.1.7.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">6.1</td>
<td id="S1.T1.3.1.7.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">3.5</td>
<td id="S1.T1.3.1.7.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">22.1</td>
<td id="S1.T1.3.1.7.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.0</td>
<td id="S1.T1.3.1.7.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">15.0/8.9</td>
<td id="S1.T1.3.1.7.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">21/8.7</td>
<td id="S1.T1.3.1.7.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">2.6/15.2</td>
<td id="S1.T1.3.1.7.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">0.0/11.2</td>
</tr>
<tr id="S1.T1.3.1.8" class="ltx_tr">
<td rowspan="3" id="S1.T1.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Vision Language Models</td>
<td id="S1.T1.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">GPT4o</td>
<td id="S1.T1.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">71.1</td>
<td id="S1.T1.3.1.8.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">58.0</td>
<td id="S1.T1.3.1.8.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">57.3</td>
<td id="S1.T1.3.1.8.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">62.5</td>
<td id="S1.T1.3.1.8.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">68.7</td>
<td id="S1.T1.3.1.8.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">61.3</td>
<td id="S1.T1.3.1.8.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">31.2</td>
<td id="S1.T1.3.1.8.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">56.8/64.7</td>
<td id="S1.T1.3.1.8.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">60.8/62.2</td>
<td id="S1.T1.3.1.8.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">61.4/62.2</td>
<td id="S1.T1.3.1.8.13" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_t" style="padding-top: -0.45pt; padding-bottom: -0.45pt">14.2/62.7</td>
</tr>
<tr id="S1.T1.3.1.9" class="ltx_tr">
<td id="S1.T1.3.1.9.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">Qwen2-VL-72B</td>
<td id="S1.T1.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">73.2</td>
<td id="S1.T1.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">75.1</td>
<td id="S1.T1.3.1.9.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">76.1</td>
<td id="S1.T1.3.1.9.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">72.0</td>
<td id="S1.T1.3.1.9.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">79.0</td>
<td id="S1.T1.3.1.9.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">77.5</td>
<td id="S1.T1.3.1.9.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">63.2</td>
<td id="S1.T1.3.1.9.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">67.9/78.1</td>
<td id="S1.T1.3.1.9.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">71.6/75.3</td>
<td id="S1.T1.3.1.9.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">77.9/72.9</td>
<td id="S1.T1.3.1.9.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center" style="padding-top: -0.45pt; padding-bottom: -0.45pt">42.7/75.1</td>
</tr>
<tr id="S1.T1.3.1.10" class="ltx_tr">
<td id="S1.T1.3.1.10.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">InterVL2-76B</td>
<td id="S1.T1.3.1.10.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">60.9</td>
<td id="S1.T1.3.1.10.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">58.5</td>
<td id="S1.T1.3.1.10.4" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">65.4</td>
<td id="S1.T1.3.1.10.5" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">58.8</td>
<td id="S1.T1.3.1.10.6" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">65.3</td>
<td id="S1.T1.3.1.10.7" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">58.3</td>
<td id="S1.T1.3.1.10.8" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb ltx_border_r" style="padding-top: -0.45pt; padding-bottom: -0.45pt">55.6</td>
<td id="S1.T1.3.1.10.9" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">49.0/65.1</td>
<td id="S1.T1.3.1.10.10" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">53.3/60.9</td>
<td id="S1.T1.3.1.10.11" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">58.8/59.8</td>
<td id="S1.T1.3.1.10.12" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_center ltx_border_bb" style="padding-top: -0.45pt; padding-bottom: -0.45pt">6.9/60.3</td>
</tr>
</tbody>
</table>
<figcaption>Table S1: End-to-End Table TEDS Result grouped by Table Attributes</figcaption>
</figure>

<figure id="S1.T2" class="ltx_table">
<table id="S1.T2.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T2.3.1.1" class="ltx_tr">
<td rowspan="2" id="S1.T2.3.1.1.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Model Type</td>
<td rowspan="2" id="S1.T2.3.1.1.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_tt">Model</td>
<td colspan="3" id="S1.T2.3.1.1.3" class="ltx_td ltx_align_center ltx_border_r ltx_border_tt">Language</td>
<td colspan="3" id="S1.T2.3.1.1.4" class="ltx_td ltx_align_center ltx_border_tt">Text background</td>
</tr>
<tr id="S1.T2.3.1.2" class="ltx_tr">
<td id="S1.T2.3.1.2.1" class="ltx_td ltx_align_center">EN</td>
<td id="S1.T2.3.1.2.2" class="ltx_td ltx_align_center">ZH</td>
<td id="S1.T2.3.1.2.3" class="ltx_td ltx_align_center ltx_border_r">Mixed</td>
<td id="S1.T2.3.1.2.4" class="ltx_td ltx_align_center">White</td>
<td id="S1.T2.3.1.2.5" class="ltx_td ltx_align_center">Single</td>
<td id="S1.T2.3.1.2.6" class="ltx_td ltx_align_center">Multi</td>
</tr>
<tr id="S1.T2.3.1.3" class="ltx_tr">
<td rowspan="3" id="S1.T2.3.1.3.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Pipeline Tools</td>
<td id="S1.T2.3.1.3.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">MinerU</td>
<td id="S1.T2.3.1.3.3" class="ltx_td ltx_align_center ltx_border_t">0.124</td>
<td id="S1.T2.3.1.3.4" class="ltx_td ltx_align_center ltx_border_t">0.234</td>
<td id="S1.T2.3.1.3.5" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.742</td>
<td id="S1.T2.3.1.3.6" class="ltx_td ltx_align_center ltx_border_t">0.188</td>
<td id="S1.T2.3.1.3.7" class="ltx_td ltx_align_center ltx_border_t">0.15</td>
<td id="S1.T2.3.1.3.8" class="ltx_td ltx_align_center ltx_border_t">0.514</td>
</tr>
<tr id="S1.T2.3.1.4" class="ltx_tr">
<td id="S1.T2.3.1.4.1" class="ltx_td ltx_align_left ltx_border_r">Marker</td>
<td id="S1.T2.3.1.4.2" class="ltx_td ltx_align_center">0.163</td>
<td id="S1.T2.3.1.4.3" class="ltx_td ltx_align_center">0.379</td>
<td id="S1.T2.3.1.4.4" class="ltx_td ltx_align_center ltx_border_r">0.747</td>
<td id="S1.T2.3.1.4.5" class="ltx_td ltx_align_center">0.303</td>
<td id="S1.T2.3.1.4.6" class="ltx_td ltx_align_center">0.396</td>
<td id="S1.T2.3.1.4.7" class="ltx_td ltx_align_center">0.594</td>
</tr>
<tr id="S1.T2.3.1.5" class="ltx_tr">
<td id="S1.T2.3.1.5.1" class="ltx_td ltx_align_left ltx_border_r">Mathpix</td>
<td id="S1.T2.3.1.5.2" class="ltx_td ltx_align_center">0.175</td>
<td id="S1.T2.3.1.5.3" class="ltx_td ltx_align_center">0.793</td>
<td id="S1.T2.3.1.5.4" class="ltx_td ltx_align_center ltx_border_r">0.538</td>
<td id="S1.T2.3.1.5.5" class="ltx_td ltx_align_center">0.698</td>
<td id="S1.T2.3.1.5.6" class="ltx_td ltx_align_center">0.587</td>
<td id="S1.T2.3.1.5.7" class="ltx_td ltx_align_center">0.583</td>
</tr>
<tr id="S1.T2.3.1.6" class="ltx_tr">
<td rowspan="2" id="S1.T2.3.1.6.1" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">Expert Vision Models</td>
<td id="S1.T2.3.1.6.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GOT-OCR</td>
<td id="S1.T2.3.1.6.3" class="ltx_td ltx_align_center ltx_border_t">0.251</td>
<td id="S1.T2.3.1.6.4" class="ltx_td ltx_align_center ltx_border_t">0.763</td>
<td id="S1.T2.3.1.6.5" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.266</td>
<td id="S1.T2.3.1.6.6" class="ltx_td ltx_align_center ltx_border_t">0.669</td>
<td id="S1.T2.3.1.6.7" class="ltx_td ltx_align_center ltx_border_t">0.595</td>
<td id="S1.T2.3.1.6.8" class="ltx_td ltx_align_center ltx_border_t">0.440</td>
</tr>
<tr id="S1.T2.3.1.7" class="ltx_tr">
<td id="S1.T2.3.1.7.1" class="ltx_td ltx_align_left ltx_border_r">Nougat</td>
<td id="S1.T2.3.1.7.2" class="ltx_td ltx_align_center">0.587</td>
<td id="S1.T2.3.1.7.3" class="ltx_td ltx_align_center">0.991</td>
<td id="S1.T2.3.1.7.4" class="ltx_td ltx_align_center ltx_border_r">0.983</td>
<td id="S1.T2.3.1.7.5" class="ltx_td ltx_align_center">0.874</td>
<td id="S1.T2.3.1.7.6" class="ltx_td ltx_align_center">0.935</td>
<td id="S1.T2.3.1.7.7" class="ltx_td ltx_align_center">0.972</td>
</tr>
<tr id="S1.T2.3.1.8" class="ltx_tr">
<td rowspan="3" id="S1.T2.3.1.8.1" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r ltx_border_t">Vision Language Models</td>
<td id="S1.T2.3.1.8.2" class="ltx_td ltx_align_left ltx_border_r ltx_border_t">GPT4o</td>
<td id="S1.T2.3.1.8.3" class="ltx_td ltx_align_center ltx_border_t">0.170</td>
<td id="S1.T2.3.1.8.4" class="ltx_td ltx_align_center ltx_border_t">0.647</td>
<td id="S1.T2.3.1.8.5" class="ltx_td ltx_align_center ltx_border_r ltx_border_t">0.322</td>
<td id="S1.T2.3.1.8.6" class="ltx_td ltx_align_center ltx_border_t">0.536</td>
<td id="S1.T2.3.1.8.7" class="ltx_td ltx_align_center ltx_border_t">0.423</td>
<td id="S1.T2.3.1.8.8" class="ltx_td ltx_align_center ltx_border_t">0.406</td>
</tr>
<tr id="S1.T2.3.1.9" class="ltx_tr">
<td id="S1.T2.3.1.9.1" class="ltx_td ltx_align_left ltx_border_r">Qwen2-VL-72B</td>
<td id="S1.T2.3.1.9.2" class="ltx_td ltx_align_center">0.128</td>
<td id="S1.T2.3.1.9.3" class="ltx_td ltx_align_center">0.582</td>
<td id="S1.T2.3.1.9.4" class="ltx_td ltx_align_center ltx_border_r">0.209</td>
<td id="S1.T2.3.1.9.5" class="ltx_td ltx_align_center">0.494</td>
<td id="S1.T2.3.1.9.6" class="ltx_td ltx_align_center">0.388</td>
<td id="S1.T2.3.1.9.7" class="ltx_td ltx_align_center">0.217</td>
</tr>
<tr id="S1.T2.3.1.10" class="ltx_tr">
<td id="S1.T2.3.1.10.1" class="ltx_td ltx_align_left ltx_border_bb ltx_border_r">InternVL2-76B</td>
<td id="S1.T2.3.1.10.2" class="ltx_td ltx_align_center ltx_border_bb">0.418</td>
<td id="S1.T2.3.1.10.3" class="ltx_td ltx_align_center ltx_border_bb">0.606</td>
<td id="S1.T2.3.1.10.4" class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">0.251</td>
<td id="S1.T2.3.1.10.5" class="ltx_td ltx_align_center ltx_border_bb">0.589</td>
<td id="S1.T2.3.1.10.6" class="ltx_td ltx_align_center ltx_border_bb">0.366</td>
<td id="S1.T2.3.1.10.7" class="ltx_td ltx_align_center ltx_border_bb">0.221</td>
</tr>
</tbody>
</table>
<figcaption>Table S2: End-to-End Text Normalized Edit Distance results grouped by Text Attributes. “Mixed” represents a mixture of Chinese and English, “Single” and “Multi” represent single color and multi color.</figcaption>
</figure>

<figure id="S1.T3" class="ltx_table">
<table id="S1.T3.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T3.3.1.1" class="ltx_tr">
<td id="S1.T3.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Category</td>
<td id="S1.T3.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Attribute Name</td>
<td id="S1.T3.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Count</td>
</tr>
<tr id="S1.T3.3.1.2" class="ltx_tr">
<td id="S1.T3.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">PDF Type</td>
<td id="S1.T3.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Book</td>
<td id="S1.T3.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">104</td>
</tr>
<tr id="S1.T3.3.1.3" class="ltx_tr">
<td id="S1.T3.3.1.3.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">PPT2PDF</td>
<td id="S1.T3.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">133</td>
</tr>
<tr id="S1.T3.3.1.4" class="ltx_tr">
<td id="S1.T3.3.1.4.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Research Report</td>
<td id="S1.T3.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">81</td>
</tr>
<tr id="S1.T3.3.1.5" class="ltx_tr">
<td id="S1.T3.3.1.5.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Colorful Textbook</td>
<td id="S1.T3.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">96</td>
</tr>
<tr id="S1.T3.3.1.6" class="ltx_tr">
<td id="S1.T3.3.1.6.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Exam Paper</td>
<td id="S1.T3.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">114</td>
</tr>
<tr id="S1.T3.3.1.7" class="ltx_tr">
<td id="S1.T3.3.1.7.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Magazine</td>
<td id="S1.T3.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">97</td>
</tr>
<tr id="S1.T3.3.1.8" class="ltx_tr">
<td id="S1.T3.3.1.8.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Academic Literature</td>
<td id="S1.T3.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">129</td>
</tr>
<tr id="S1.T3.3.1.9" class="ltx_tr">
<td id="S1.T3.3.1.9.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Notes</td>
<td id="S1.T3.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">116</td>
</tr>
<tr id="S1.T3.3.1.10" class="ltx_tr">
<td id="S1.T3.3.1.10.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.10.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Newspaper</td>
<td id="S1.T3.3.1.10.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">111</td>
</tr>
<tr id="S1.T3.3.1.11" class="ltx_tr">
<td id="S1.T3.3.1.11.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Layout Type</td>
<td id="S1.T3.3.1.11.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Single Column</td>
<td id="S1.T3.3.1.11.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">477</td>
</tr>
<tr id="S1.T3.3.1.12" class="ltx_tr">
<td id="S1.T3.3.1.12.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.12.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Double Column</td>
<td id="S1.T3.3.1.12.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">126</td>
</tr>
<tr id="S1.T3.3.1.13" class="ltx_tr">
<td id="S1.T3.3.1.13.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.13.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Three Column</td>
<td id="S1.T3.3.1.13.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">45</td>
</tr>
<tr id="S1.T3.3.1.14" class="ltx_tr">
<td id="S1.T3.3.1.14.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.14.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">One&amp;More Mixed</td>
<td id="S1.T3.3.1.14.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">120</td>
</tr>
<tr id="S1.T3.3.1.15" class="ltx_tr">
<td id="S1.T3.3.1.15.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.15.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Complex Layout</td>
<td id="S1.T3.3.1.15.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">213</td>
</tr>
<tr id="S1.T3.3.1.16" class="ltx_tr">
<td id="S1.T3.3.1.16.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Language</td>
<td id="S1.T3.3.1.16.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">English</td>
<td id="S1.T3.3.1.16.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">290</td>
</tr>
<tr id="S1.T3.3.1.17" class="ltx_tr">
<td id="S1.T3.3.1.17.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.17.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Simplified Chinese</td>
<td id="S1.T3.3.1.17.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">612</td>
</tr>
<tr id="S1.T3.3.1.18" class="ltx_tr">
<td id="S1.T3.3.1.18.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.18.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Mixed</td>
<td id="S1.T3.3.1.18.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">79</td>
</tr>
<tr id="S1.T3.3.1.19" class="ltx_tr">
<td id="S1.T3.3.1.19.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Special Issues</td>
<td id="S1.T3.3.1.19.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Fuzzy Scan</td>
<td id="S1.T3.3.1.19.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">28</td>
</tr>
<tr id="S1.T3.3.1.20" class="ltx_tr">
<td id="S1.T3.3.1.20.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.20.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Watermark</td>
<td id="S1.T3.3.1.20.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right" style="padding-top: -0.5pt; padding-bottom: -0.5pt">65</td>
</tr>
<tr id="S1.T3.3.1.21" class="ltx_tr">
<td id="S1.T3.3.1.21.1" class="ltx_td ltx_nopad_r ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T3.3.1.21.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Colorful Background</td>
<td id="S1.T3.3.1.21.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_right ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">246</td>
</tr>
</tbody>
</table>
<figcaption>Table S3: The Page Attributes Statistics of OmniDocBench.</figcaption>
</figure>

<figure id="S1.T4" class="ltx_table">
<table id="S1.T4.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T4.3.1.1" class="ltx_tr">
<td id="S1.T4.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Attribute Category</td>
<td id="S1.T4.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Category Name</td>
<td id="S1.T4.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Count</td>
</tr>
<tr id="S1.T4.3.1.2" class="ltx_tr">
<td id="S1.T4.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Language</td>
<td id="S1.T4.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">English</td>
<td id="S1.T4.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">5857</td>
</tr>
<tr id="S1.T4.3.1.3" class="ltx_tr">
<td id="S1.T4.3.1.3.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Simplified Chinese</td>
<td id="S1.T4.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">16073</td>
</tr>
<tr id="S1.T4.3.1.4" class="ltx_tr">
<td id="S1.T4.3.1.4.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">EN&amp;CH Mixed</td>
<td id="S1.T4.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">1080</td>
</tr>
<tr id="S1.T4.3.1.5" class="ltx_tr">
<td id="S1.T4.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Text Background</td>
<td id="S1.T4.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">White</td>
<td id="S1.T4.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">19465</td>
</tr>
<tr id="S1.T4.3.1.6" class="ltx_tr">
<td id="S1.T4.3.1.6.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Single-Colored</td>
<td id="S1.T4.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">1116</td>
</tr>
<tr id="S1.T4.3.1.7" class="ltx_tr">
<td id="S1.T4.3.1.7.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Multi-Colored</td>
<td id="S1.T4.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">2429</td>
</tr>
<tr id="S1.T4.3.1.8" class="ltx_tr">
<td id="S1.T4.3.1.8.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Text Rotate</td>
<td id="S1.T4.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Normal</td>
<td id="S1.T4.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">22865</td>
</tr>
<tr id="S1.T4.3.1.9" class="ltx_tr">
<td id="S1.T4.3.1.9.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Rotate90</td>
<td id="S1.T4.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">14</td>
</tr>
<tr id="S1.T4.3.1.10" class="ltx_tr">
<td id="S1.T4.3.1.10.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.10.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Rotate270</td>
<td id="S1.T4.3.1.10.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">58</td>
</tr>
<tr id="S1.T4.3.1.11" class="ltx_tr">
<td id="S1.T4.3.1.11.1" class="ltx_td ltx_nopad_r ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T4.3.1.11.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Horizontal</td>
<td id="S1.T4.3.1.11.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">421</td>
</tr>
</tbody>
</table>
<figcaption>Table S4: Text Attributes Statistics of OmniDocBench.</figcaption>
</figure>

<figure id="S1.T5" class="ltx_table">
<table id="S1.T5.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T5.3.1.1" class="ltx_tr">
<td id="S1.T5.3.1.1.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Attribute Category</td>
<td id="S1.T5.3.1.1.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Category Name</td>
<td id="S1.T5.3.1.1.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_tt" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Count</td>
</tr>
<tr id="S1.T5.3.1.2" class="ltx_tr">
<td id="S1.T5.3.1.2.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Language</td>
<td id="S1.T5.3.1.2.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">English</td>
<td id="S1.T5.3.1.2.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">128</td>
</tr>
<tr id="S1.T5.3.1.3" class="ltx_tr">
<td id="S1.T5.3.1.3.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.3.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Simplified Chinese</td>
<td id="S1.T5.3.1.3.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">285</td>
</tr>
<tr id="S1.T5.3.1.4" class="ltx_tr">
<td id="S1.T5.3.1.4.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.4.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">EN&amp;CH Mixed</td>
<td id="S1.T5.3.1.4.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">15</td>
</tr>
<tr id="S1.T5.3.1.5" class="ltx_tr">
<td id="S1.T5.3.1.5.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Table Frame Type</td>
<td id="S1.T5.3.1.5.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Full Frame</td>
<td id="S1.T5.3.1.5.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">205</td>
</tr>
<tr id="S1.T5.3.1.6" class="ltx_tr">
<td id="S1.T5.3.1.6.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.6.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Omission Line</td>
<td id="S1.T5.3.1.6.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">62</td>
</tr>
<tr id="S1.T5.3.1.7" class="ltx_tr">
<td id="S1.T5.3.1.7.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.7.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Three Line</td>
<td id="S1.T5.3.1.7.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">147</td>
</tr>
<tr id="S1.T5.3.1.8" class="ltx_tr">
<td id="S1.T5.3.1.8.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.8.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">No Frame</td>
<td id="S1.T5.3.1.8.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">14</td>
</tr>
<tr id="S1.T5.3.1.9" class="ltx_tr">
<td id="S1.T5.3.1.9.1" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Special Issues</td>
<td id="S1.T5.3.1.9.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Merge Cell</td>
<td id="S1.T5.3.1.9.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_t" style="padding-top: -0.5pt; padding-bottom: -0.5pt">150</td>
</tr>
<tr id="S1.T5.3.1.10" class="ltx_tr">
<td id="S1.T5.3.1.10.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.10.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Colorful Background</td>
<td id="S1.T5.3.1.10.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">142</td>
</tr>
<tr id="S1.T5.3.1.11" class="ltx_tr">
<td id="S1.T5.3.1.11.1" class="ltx_td ltx_nopad_r" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.11.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Contain Formula</td>
<td id="S1.T5.3.1.11.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left" style="padding-top: -0.5pt; padding-bottom: -0.5pt">81</td>
</tr>
<tr id="S1.T5.3.1.12" class="ltx_tr">
<td id="S1.T5.3.1.12.1" class="ltx_td ltx_nopad_r ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt"></td>
<td id="S1.T5.3.1.12.2" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">Rotate</td>
<td id="S1.T5.3.1.12.3" class="ltx_td ltx_nopad_l ltx_nopad_r ltx_align_left ltx_border_bb" style="padding-top: -0.5pt; padding-bottom: -0.5pt">7</td>
</tr>
</tbody>
</table>
<figcaption>Table S5: Table Attributes Statistics of OmniDocBench.</figcaption>
</figure>

<figure id="S1.T6" class="ltx_table">
<table id="S1.T6.3.1" class="ltx_tabular ltx_align_middle">
<tbody>
<tr id="S1.T6.3.1.1" class="ltx_tr">
<td id="S1.T6.3.1.1.1" class="ltx_td ltx_align_left ltx_border_t">No.</td>
<td id="S1.T6.3.1.1.2" class="ltx_td ltx_align_left ltx_border_t">Category Name</td>
<td id="S1.T6.3.1.1.3" class="ltx_td ltx_align_left ltx_border_t">Explaination</td>
<td id="S1.T6.3.1.1.4" class="ltx_td ltx_align_center ltx_border_t">Total</td>
</tr>
<tr id="S1.T6.3.1.2" class="ltx_tr">
<td id="S1.T6.3.1.2.1" class="ltx_td ltx_align_left ltx_border_t">1</td>
<td id="S1.T6.3.1.2.2" class="ltx_td ltx_align_left ltx_border_t">Title</td>
<td id="S1.T6.3.1.2.3" class="ltx_td ltx_align_left ltx_border_t">Include main titles, chapter titles, etc.</td>
<td id="S1.T6.3.1.2.4" class="ltx_td ltx_align_center ltx_border_t">2972</td>
</tr>
<tr id="S1.T6.3.1.3" class="ltx_tr">
<td id="S1.T6.3.1.3.1" class="ltx_td ltx_align_left">2</td>
<td id="S1.T6.3.1.3.2" class="ltx_td ltx_align_left">Text Block</td>
<td id="S1.T6.3.1.3.3" class="ltx_td ltx_align_left">Text paragraphs, which are usually separated by double line breaks in Markdown.</td>
<td id="S1.T6.3.1.3.4" class="ltx_td ltx_align_center">15979</td>
</tr>
<tr id="S1.T6.3.1.4" class="ltx_tr">
<td id="S1.T6.3.1.4.1" class="ltx_td ltx_align_left">3</td>
<td id="S1.T6.3.1.4.2" class="ltx_td ltx_align_left">Figure</td>
<td id="S1.T6.3.1.4.3" class="ltx_td ltx_align_left">Including images, visual charts, etc.</td>
<td id="S1.T6.3.1.4.4" class="ltx_td ltx_align_center">989</td>
</tr>
<tr id="S1.T6.3.1.5" class="ltx_tr">
<td id="S1.T6.3.1.5.1" class="ltx_td ltx_align_left">4</td>
<td id="S1.T6.3.1.5.2" class="ltx_td ltx_align_left">Figure Caption</td>
<td id="S1.T6.3.1.5.3" class="ltx_td ltx_align_left">Typically starts with ’Figure’ followed by a number, or just descriptive language below the figure.</td>
<td id="S1.T6.3.1.5.4" class="ltx_td ltx_align_center">651</td>
</tr>
<tr id="S1.T6.3.1.6" class="ltx_tr">
<td id="S1.T6.3.1.6.1" class="ltx_td ltx_align_left">5</td>
<td id="S1.T6.3.1.6.2" class="ltx_td ltx_align_left">Figure Footnotes</td>
<td id="S1.T6.3.1.6.3" class="ltx_td ltx_align_left">Descriptive language, apart from the figure caption, usually starts with an asterisk (*).</td>
<td id="S1.T6.3.1.6.4" class="ltx_td ltx_align_center">133</td>
</tr>
<tr id="S1.T6.3.1.7" class="ltx_tr">
<td id="S1.T6.3.1.7.1" class="ltx_td ltx_align_left">6</td>
<td id="S1.T6.3.1.7.2" class="ltx_td ltx_align_left">Table</td>
<td id="S1.T6.3.1.7.3" class="ltx_td ltx_align_left">Content organized in table form usually includes borders or a clear table structure.</td>
<td id="S1.T6.3.1.7.4" class="ltx_td ltx_align_center">428</td>
</tr>
<tr id="S1.T6.3.1.8" class="ltx_tr">
<td id="S1.T6.3.1.8.1" class="ltx_td ltx_align_left">7</td>
<td id="S1.T6.3.1.8.2" class="ltx_td ltx_align_left">Table Caption</td>
<td id="S1.T6.3.1.8.3" class="ltx_td ltx_align_left">Typically starts with ’Table’ followed by a number, or just descriptive language above the Table.</td>
<td id="S1.T6.3.1.8.4" class="ltx_td ltx_align_center">299</td>
</tr>
<tr id="S1.T6.3.1.9" class="ltx_tr">
<td id="S1.T6.3.1.9.1" class="ltx_td ltx_align_left">8</td>
<td id="S1.T6.3.1.9.2" class="ltx_td ltx_align_left">Table Footnotes</td>
<td id="S1.T6.3.1.9.3" class="ltx_td ltx_align_left">Descriptive language, apart from the table caption, usually starts with an asterisk (*).</td>
<td id="S1.T6.3.1.9.4" class="ltx_td ltx_align_center">132</td>
</tr>
<tr id="S1.T6.3.1.10" class="ltx_tr">
<td id="S1.T6.3.1.10.1" class="ltx_td ltx_align_left">9</td>
<td id="S1.T6.3.1.10.2" class="ltx_td ltx_align_left">Header</td>
<td id="S1.T6.3.1.10.3" class="ltx_td ltx_align_left">Information located at the top of a PDF page or in the sidebar, separate from the main content, typically includes chapter names and other details.</td>
<td id="S1.T6.3.1.10.4" class="ltx_td ltx_align_center">1271</td>
</tr>
<tr id="S1.T6.3.1.11" class="ltx_tr">
<td id="S1.T6.3.1.11.1" class="ltx_td ltx_align_left">10</td>
<td id="S1.T6.3.1.11.2" class="ltx_td ltx_align_left">Footer</td>
<td id="S1.T6.3.1.11.3" class="ltx_td ltx_align_left">Information located at the bottom of a PDF page, separate from the main content, typically includes the publisher’s name and other details.</td>
<td id="S1.T6.3.1.11.4" class="ltx_td ltx_align_center">541</td>
</tr>
<tr id="S1.T6.3.1.12" class="ltx_tr">
<td id="S1.T6.3.1.12.1" class="ltx_td ltx_align_left">11</td>
<td id="S1.T6.3.1.12.2" class="ltx_td ltx_align_left">Page Number</td>
<td id="S1.T6.3.1.12.3" class="ltx_td ltx_align_left">It is usually represented by numbers, which may be located at the top, in the sidebar, or at the bottom of the page.</td>
<td id="S1.T6.3.1.12.4" class="ltx_td ltx_align_center">669</td>
</tr>
<tr id="S1.T6.3.1.13" class="ltx_tr">
<td id="S1.T6.3.1.13.1" class="ltx_td ltx_align_left">12</td>
<td id="S1.T6.3.1.13.2" class="ltx_td ltx_align_left">Page Footnote</td>
<td id="S1.T6.3.1.13.3" class="ltx_td ltx_align_left">It provides further explanation of the footnotes marked within the page content. For example, information about the authors’ affiliations.</td>
<td id="S1.T6.3.1.13.4" class="ltx_td ltx_align_center">92</td>
</tr>
<tr id="S1.T6.3.1.14" class="ltx_tr">
<td id="S1.T6.3.1.14.1" class="ltx_td ltx_align_left">13</td>
<td id="S1.T6.3.1.14.2" class="ltx_td ltx_align_left">Code Block</td>
<td id="S1.T6.3.1.14.3" class="ltx_td ltx_align_left">In Markdown, a code block is typically defined using triple backticks (“‘).</td>
<td id="S1.T6.3.1.14.4" class="ltx_td ltx_align_center">13</td>
</tr>
<tr id="S1.T6.3.1.15" class="ltx_tr">
<td id="S1.T6.3.1.15.1" class="ltx_td ltx_align_left">14</td>
<td id="S1.T6.3.1.15.2" class="ltx_td ltx_align_left">Code Block Caption</td>
<td id="S1.T6.3.1.15.3" class="ltx_td ltx_align_left">Descriptive language above the Code Block.</td>
<td id="S1.T6.3.1.15.4" class="ltx_td ltx_align_center">/</td>
</tr>
<tr id="S1.T6.3.1.16" class="ltx_tr">
<td id="S1.T6.3.1.16.1" class="ltx_td ltx_align_left">15</td>
<td id="S1.T6.3.1.16.2" class="ltx_td ltx_align_left">Reference</td>
<td id="S1.T6.3.1.16.3" class="ltx_td ltx_align_left">Typically found only in academic literature.</td>
<td id="S1.T6.3.1.16.4" class="ltx_td ltx_align_center">260</td>
</tr>
<tr id="S1.T6.3.1.17" class="ltx_tr">
<td id="S1.T6.3.1.17.1" class="ltx_td ltx_align_left ltx_border_t">16</td>
<td id="S1.T6.3.1.17.2" class="ltx_td ltx_align_left ltx_border_t">Text Span</td>
<td id="S1.T6.3.1.17.3" class="ltx_td ltx_align_left ltx_border_t">Span-Level text box, which is the plain text content can be directly written in Markdown format.</td>
<td id="S1.T6.3.1.17.4" class="ltx_td ltx_align_center ltx_border_t">73143</td>
</tr>
<tr id="S1.T6.3.1.18" class="ltx_tr">
<td id="S1.T6.3.1.18.1" class="ltx_td ltx_align_left">17</td>
<td id="S1.T6.3.1.18.2" class="ltx_td ltx_align_left">Equation Inline</td>
<td id="S1.T6.3.1.18.3" class="ltx_td ltx_align_left">Formulas that need to be represented using LaTeX format and embedded within the text.</td>
<td id="S1.T6.3.1.18.4" class="ltx_td ltx_align_center">4009</td>
</tr>
<tr id="S1.T6.3.1.19" class="ltx_tr">
<td id="S1.T6.3.1.19.1" class="ltx_td ltx_align_left">18</td>
<td id="S1.T6.3.1.19.2" class="ltx_td ltx_align_left">Equation Ignore</td>
<td id="S1.T6.3.1.19.3" class="ltx_td ltx_align_left">Some formulas that can be displayed correctly without using LaTeX formatting, such as 15 kg.</td>
<td id="S1.T6.3.1.19.4" class="ltx_td ltx_align_center">3685</td>
</tr>
<tr id="S1.T6.3.1.20" class="ltx_tr">
<td id="S1.T6.3.1.20.1" class="ltx_td ltx_align_left">19</td>
<td id="S1.T6.3.1.20.2" class="ltx_td ltx_align_left">Footnote Mark</td>
<td id="S1.T6.3.1.20.3" class="ltx_td ltx_align_left">Typically embedded within the text as superscripts or subscripts, and their numbering usually corresponds to page footnotes.</td>
<td id="S1.T6.3.1.20.4" class="ltx_td ltx_align_center">357</td>
</tr>
<tr id="S1.T6.3.1.21" class="ltx_tr">
<td id="S1.T6.3.1.21.1" class="ltx_td ltx_align_left ltx_border_t">20</td>
<td id="S1.T6.3.1.21.2" class="ltx_td ltx_align_left ltx_border_t">Other Abandoned Categories</td>
<td id="S1.T6.3.1.21.3" class="ltx_td ltx_align_left ltx_border_t">(Masked) Some uncategorizable, irrelevant page information, such as small icons, etc.</td>
<td id="S1.T6.3.1.21.4" class="ltx_td ltx_align_center ltx_border_t">538</td>
</tr>
<tr id="S1.T6.3.1.22" class="ltx_tr">
<td id="S1.T6.3.1.22.1" class="ltx_td ltx_align_left">21</td>
<td id="S1.T6.3.1.22.2" class="ltx_td ltx_align_left">Masked Text Block</td>
<td id="S1.T6.3.1.22.3" class="ltx_td ltx_align_left">(Masked) Some difficult-to-recognize information that disrupts text flow, such as pinyin annotations above Chinese characters.</td>
<td id="S1.T6.3.1.22.4" class="ltx_td ltx_align_center">34</td>
</tr>
<tr id="S1.T6.3.1.23" class="ltx_tr">
<td id="S1.T6.3.1.23.1" class="ltx_td ltx_align_left ltx_border_b">22</td>
<td id="S1.T6.3.1.23.2" class="ltx_td ltx_align_left ltx_border_b">Organic Chemical Formula</td>
<td id="S1.T6.3.1.23.3" class="ltx_td ltx_align_left ltx_border_b">(Masked) Organic chemistry formulas, which are difficult to write using Markdown and are easily recognized as Figures.</td>
<td id="S1.T6.3.1.23.4" class="ltx_td ltx_align_center ltx_border_b">24</td>
</tr>
</tbody>
</table>
<figcaption>Table S6: Annotation Explanations and Statistics.</figcaption>
</figure>

## II Dataset Statistics and Visualization

OmniDocBench contains 981 pages, including 9 types of PDF pages, 4 types of layouts, 3 types of languages, and 3 special issues in visual degradations (e.g., watermarks). Table [S3](#S1.T3 "Table S3 ‣ I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and Figure [S1](#S5.F1 "Figure S1 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show the number of pages with each page attribute. [Figures S5](#S5.F5 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S6](#S5.F6 "Figure S6 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S7](#S5.F7 "Figure S7 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S8](#S5.F8 "Figure S8 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") are examples of PDF pages with different PDF types, Layout Types, and Special Issues.

Table [S6](#S1.T6 "Table S6 ‣ I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [Figure S2](#S5.F2 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show all annotation categories included in OmniDocBench. All of them are annotated by bounding boxes. There are 15 types of block-level annotations and 4 types of span-level annotations, with span-level annotations nested within the block-level ones. In addition, there are 3 types of annotations marked as page interference information (No.20-22), whose bounding boxes are used to mask the specific regions of the PDF pages to avoid affecting the evaluation results. The recognition annotations are also provided for each annotation category except for Figures. Formulas is written in LaTeX format and Table is annotated in both HTML and LaTeX formats. Others are annotated in plain text.

Furthermore, the Text Attributes are also annotated for each block-level category that contains text. There are 3 types of Text Attributes that might influent OCR accuracy: Language, Text Background Color, and Text Rotation. Table [S5](#S1.T5 "Table S5 ‣ I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") shows the statistics of annotations with specific text attributes. There are 23,010 block-level annotations are labeled with text attributes.

Tables are also annotated with Table Attributes. There are 6 types of Table Attributes that might influent the Table Recognition accuracy: Language, Table Frame Type, Merge Cell, Colorful Background, Contain Formula, and Rotation. Table [S5](#S1.T5 "Table S5 ‣ I More End-to-End Evaluation Results ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") shows the numbers of annotations with specific table attributes. [Figures S9](#S5.F9 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S10](#S5.F10 "Figure S10 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") are the examples of Tables with different Frames and Special Issues.

## III Discussion on Model Predictions

Conclusion Combining scattered results from tasks and sub-attributes, it can be concluded that pipeline tools and expert models have better performance on common data like academic papers and challenging cases such as tables with merged cells compared to VLMs. However, VLMs demonstrate stronger generalization on uncommon PDF types like slides and exam papers, and they show greater robustness in special page situations, such as fuzzy scans. The low accuracy of VLMs is mainly due to:1) Missing Content in dense pages([Figure S11](#S5.F11 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")); 2) Hallucinations in hard-to-recognize pages([Figure S30](#S5.F30 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")). The low accuracy of Pipeline tools mainly due to: 1) Lower robustness in special page situations, e.g., watermark([Figure S21](#S5.F21 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")); 2) Weak generalization on uncommon PDF types, e.g., handwriting notes([Figure S16](#S5.F16 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")).

[Figures S12](#S5.F12 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S13](#S5.F13 "Figure S13 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S14](#S5.F14 "Figure S14 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S15](#S5.F15 "Figure S15 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S16](#S5.F16 "Figure S16 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S11](#S5.F11 "Figure S11 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S17](#S5.F17 "Figure S17 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S18](#S5.F18 "Figure S18 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S19](#S5.F19 "Figure S19 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show the examples of Good model outputs and Bad model outputs of Document Parsing among different PDF types. As it shown, different models exhibit varying performance across different PDF types. For example, MinerU detects all handwritten notes as figures, resulting in very low recognition accuracy in Notes. Marker and InternVL2 experience missed detections, leading to lower scores. InternVL2 and Qwen2-VL, in specific PDF types (such as slides or financial reports), tend to merge multi-column text.

[Figures S22](#S5.F22 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S20](#S5.F20 "Figure S20 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S21](#S5.F21 "Figure S21 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show the examples of Good model outputs and Bad model outputs under special issues of the PDF pages. It shows that Marker tends to generate typos when the PDF pages are fuzzy scanned or with watermarks, while GOT-OCR fails to recognize content on pages with colored backgrounds. MinerU performs well under special situations, while Mathpix occasionally generates typos.

[Figures S23](#S5.F23 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S24](#S5.F24 "Figure S24 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S25](#S5.F25 "Figure S25 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S26](#S5.F26 "Figure S26 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show examples of Good model outputs and Bad model outputs for PDF pages with different layouts. MinerU has a low reading order score for single-column layouts primarily because most notes are single-column, and MinerU performs poorly in recognizing Notes, leading to a low reading order score accordingly. InternVL2 scores high in Single-Column layouts but scores poorly on Double-Column and Three-Column layouts. It is mainly due to frequent missed content recognition and errors in reading order judgment in multi-column layouts pages. MinerU’s reading order and recognition accuracy decrease with complex layouts, primarily because it incorrectly merges multiple columns during recognition.

[Figures S29](#S5.F29 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S30](#S5.F30 "Figure S30 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show the model’s recognition ability under special issues of text. In text recognition with complex background colors, Marker may produce errors or miss content, whereas Qwen2-VL still performs well. Most models fail to recognize text when it is rotated 270 degrees. Some vision language models generate hallucinated information based on the content they can recognize.

[Figures S31](#S5.F31 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S32](#S5.F32 "Figure S32 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"), [S33](#S5.F33 "Figure S33 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") and [S34](#S5.F34 "Figure S34 ‣ V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations") show the examples of good and bad model results for tables with different attributes. For three-line tables, RapidTable demonstrates a good performance with accurate structure recognition, while PaddleOCR shows limitations by missing the last column in its outputs. Interestingly, in tables without frames, PaddleOCR performs well with accurate table predictions, while Qwen2-VL-7B exhibits errors in the last two columns. This indicates that the presence or absence of table frames can significantly impact different models’ performance in different ways. Rotated tables prove to be particularly challenging, with most models, including GOT-OCR, failing to recognize the table structure. However, StructEqTable shows promising results by correctly identifying most of the table content, though with a few detail errors. For tables containing formula, Qwen2-VL-7B shows more accurate table structure recognition compared to InternVL2-8B.

## IV Model Settings

For pipeline tools such as MinerU, Marker, and Mathpix, default settings are used for evaluation. Specifically, MinerU with Version 0.9.3<sup>88</sup> 8 <https://github.com/opendatalab/MinerU/releases/tag/magic_pdf-0.9.3-released> is employed. For Marker, Version 1.2.3<sup>99</sup> 9 <https://github.com/VikParuchuri/marker/releases/tag/v1.2.3> is evaluated. For Nougat, we utilize its 0.1.0-base model (350M). For GOT-OCR, we employ its format OCR mode to output structured data.

For general VLMs, we used the GPT4o, Qwen2-VL-72B, and InternVL2-Llama3-76B by setting the do_sample$`=`$False to ensure the reproducibility. After testing the different setting of max_token, the best setting is chosen for each VLMs. Specifically, max_token$`=`$<!-- -->32000 is set for Qwen2-VL-72B, and max_token$`=`$<!-- -->4096 is set for InternVL2-Llama3-76B. For GPT-4o, the default setting is used.

## V More Details on Methods

Ignore handling. The purpose of this process is to avoid fluctuations in accuracy caused by the lack of uniformity in the output standards among document parsing algorithm. (1) Some algorithm (e.g., GPT-OCR, Qwen2-VL) tends to remove headers and footers, while others (e.g., GPT4o) prefers to retain them ( [Figure S3](#S5.F3 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")). (2) Moreover, the reading order mismatch cause by captions and footnotes is also considered. For example, Nougat would put the image captions in the end of the page content( [Figure S4](#S5.F4 "In V More Details on Methods ‣ OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations")), while others tend to put the image captions in human reading order.

Ignore handling is to minimize the impact of varying standards of document parsing on evaluation. Our evaluation dataset aims to more fairly assess the parsing accuracy of various algorithms, and these trivial issues regarding standards are not within our scope of consideration.

<figure id="S5.F1" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/Page_Attribute.png" id="S5.F1.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/254;" width="685" height="254" alt="Refer to caption" />
<figcaption>Figure S1: The Data Proportion of Pages for each Attribute in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F2" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/page_anno_show.png" id="S5.F2.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/400;" width="685" height="400" alt="Refer to caption" />
<figcaption>Figure S2: The Visualization of vary Annotations in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F3" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/abandon_standard.png" id="S5.F3.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/310;" width="685" height="310" alt="Refer to caption" />
<figcaption>Figure S3: The Vary Standards in parsing Header, Footers, and so on.</figcaption>
</figure>

<figure id="S5.F4" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/captions_standard.png" id="S5.F4.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/307;" width="685" height="307" alt="Refer to caption" />
<figcaption>Figure S4: The Vary Standards in parsing Captions.</figcaption>
</figure>

<figure id="S5.F5" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/show_pdf_types_1.png" id="S5.F5.g1" class="ltx_graphics ltx_centering ltx_img_portrait" style="aspect-ratio:651/861;" width="651" height="861" alt="Refer to caption" />
<figcaption>Figure S5: The Examples of Academic Papers, Books, Textbooks, Notes, and Magazines in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F6" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/show_pdf_types_2.png" id="S5.F6.g1" class="ltx_graphics ltx_centering ltx_img_square" style="aspect-ratio:685/729;" width="685" height="729" alt="Refer to caption" />
<figcaption>Figure S6: The Examples of Finacial Reports, Newspapers, Example Papers, and Slides in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F7" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/showcase_layout.png" id="S5.F7.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/322;" width="685" height="322" alt="Refer to caption" />
<figcaption>Figure S7: The Examples of PDF pages with different Layout Types in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F8" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/showcase_special_issue.png" id="S5.F8.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/321;" width="685" height="321" alt="Refer to caption" />
<figcaption>Figure S8: The Examples of PDF pages under Special Issues in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F9" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/showcase_table_frame.png" id="S5.F9.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/339;" width="685" height="339" alt="Refer to caption" />
<figcaption>Figure S9: The Examples of Tables with different Frame in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F10" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/showcase_table_issue.png" id="S5.F10.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/336;" width="685" height="336" alt="Refer to caption" />
<figcaption>Figure S10: The Examples of Tables under Special Issues in OmniDocBench.</figcaption>
</figure>

<figure id="S5.F11" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/papers.png" id="S5.F11.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/320;" width="685" height="320" alt="Refer to caption" />
<figcaption>Figure S11: The Good Model Result and Bad Model Result for Academic Papers.</figcaption>
</figure>

<figure id="S5.F12" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/book.png" id="S5.F12.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/320;" width="685" height="320" alt="Refer to caption" />
<figcaption>Figure S12: The Good Model Result and Bad Model Result for Books.</figcaption>
</figure>

<figure id="S5.F13" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/exam.png" id="S5.F13.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/323;" width="685" height="323" alt="Refer to caption" />
<figcaption>Figure S13: The Good Model Result and Bad Model Result for Exam Papers.</figcaption>
</figure>

<figure id="S5.F14" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/magazine.png" id="S5.F14.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/322;" width="685" height="322" alt="Refer to caption" />
<figcaption>Figure S14: The Good Model Result and Bad Model Result for Magazines.</figcaption>
</figure>

<figure id="S5.F15" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/newspaper.png" id="S5.F15.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/321;" width="685" height="321" alt="Refer to caption" />
<figcaption>Figure S15: The Good Model Result and Bad Model Result for Newspaper.</figcaption>
</figure>

<figure id="S5.F16" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/notes.png" id="S5.F16.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/325;" width="685" height="325" alt="Refer to caption" />
<figcaption>Figure S16: The Good Model Result and Bad Model Result for Handwriting Notes.</figcaption>
</figure>

<figure id="S5.F17" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/Research_report.png" id="S5.F17.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/320;" width="685" height="320" alt="Refer to caption" />
<figcaption>Figure S17: The Good Model Result and Bad Model Result for Financial Reports.</figcaption>
</figure>

<figure id="S5.F18" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/slides.png" id="S5.F18.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/329;" width="685" height="329" alt="Refer to caption" />
<figcaption>Figure S18: The Good Model Result and Bad Model Result for Slides.</figcaption>
</figure>

<figure id="S5.F19" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/textbook.png" id="S5.F19.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/322;" width="685" height="322" alt="Refer to caption" />
<figcaption>Figure S19: The Good Model Result and Bad Model Result for Textbooks.</figcaption>
</figure>

<figure id="S5.F20" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/fuzzy_scan.png" id="S5.F20.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/328;" width="685" height="328" alt="Refer to caption" />
<figcaption>Figure S20: The Good Model Result and Bad Model Result for Fuzzy Scan Pages.</figcaption>
</figure>

<figure id="S5.F21" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/watermark.png" id="S5.F21.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/335;" width="685" height="335" alt="Refer to caption" />
<figcaption>Figure S21: The Good Model Result and Bad Model Result for Pages with Watermark.</figcaption>
</figure>

<figure id="S5.F22" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/colorful_background.png" id="S5.F22.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/336;" width="685" height="336" alt="Refer to caption" />
<figcaption>Figure S22: The Good Model Result and Bad Model Result for Colorful Background Pages.</figcaption>
</figure>

<figure id="S5.F23" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/single_col.png" id="S5.F23.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/327;" width="685" height="327" alt="Refer to caption" />
<figcaption>Figure S23: The Good Model Result and Bad Model Result for Single Column Pages.</figcaption>
</figure>

<figure id="S5.F24" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/double_col.png" id="S5.F24.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/326;" width="685" height="326" alt="Refer to caption" />
<figcaption>Figure S24: The Good Model Result and Bad Model Result for Double Column Pages.</figcaption>
</figure>

<figure id="S5.F25" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/three_col.png" id="S5.F25.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/325;" width="685" height="325" alt="Refer to caption" />
<figcaption>Figure S25: The Good Model Result and Bad Model Result for Three Column Pages.</figcaption>
</figure>

<figure id="S5.F26" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/complex_layout.png" id="S5.F26.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/323;" width="685" height="323" alt="Refer to caption" />
<figcaption>Figure S26: The Good Model Result and Bad Model Result for Complex Layout Pages.</figcaption>
</figure>

<figure id="S5.F27" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/text_chinese.png" id="S5.F27.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/325;" width="685" height="325" alt="Refer to caption" />
<figcaption>Figure S27: The Good Model Result and Bad Model Result for Text Language in Chinese.</figcaption>
</figure>

<figure id="S5.F28" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/text_english.png" id="S5.F28.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/324;" width="685" height="324" alt="Refer to caption" />
<figcaption>Figure S28: The Good Model Result and Bad Model Result for Text Language in English.</figcaption>
</figure>

<figure id="S5.F29" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/text_colorful_background.png" id="S5.F29.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/324;" width="685" height="324" alt="Refer to caption" />
<figcaption>Figure S29: The Good Model Result and Bad Model Result for Text with Colorful Background.</figcaption>
</figure>

<figure id="S5.F30" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/text_rotate.png" id="S5.F30.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/323;" width="685" height="323" alt="Refer to caption" />
<figcaption>Figure S30: The Bad Model Result for Text with Rotation.</figcaption>
</figure>

<figure id="S5.F31" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/badcase_table_threeline.png" id="S5.F31.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:548/386;" width="548" height="386" alt="Refer to caption" />
<figcaption>Figure S31: The Good Model Result and Bad Model Result for Three Line Frame Table.</figcaption>
</figure>

<figure id="S5.F32" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/badcase_table_noframe.png" id="S5.F32.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:548/408;" width="548" height="408" alt="Refer to caption" />
<figcaption>Figure S32: The Good Model Result and Bad Model Result for No Frame Table.</figcaption>
</figure>

<figure id="S5.F33" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/badcase_table_rotate.png" id="S5.F33.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:548/385;" width="548" height="385" alt="Refer to caption" />
<figcaption>Figure S33: The Good Model Result and Bad Model Result for Rotated Table.</figcaption>
</figure>

<figure id="S5.F34" class="ltx_figure">
<img src="https://arxiv.org/html/2412.07626v2/badcase_table_formula.png" id="S5.F34.g1" class="ltx_graphics ltx_centering ltx_img_landscape" style="aspect-ratio:685/371;" width="685" height="371" alt="Refer to caption" />
<figcaption>Figure S34: The Good Model Result and Bad Model Result for Table with Formula.</figcaption>
</figure>
