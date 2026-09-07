# <span id="page-0-0"></span>OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations

Linke Ouyang<sup>1</sup><sup>∗</sup> Yuan Qu<sup>1</sup><sup>∗</sup> Hongbin Zhou<sup>1</sup><sup>∗</sup> Jiawei Zhu<sup>1</sup><sup>∗</sup> Rui Zhang<sup>1</sup><sup>∗</sup> Qunshu Lin<sup>2</sup><sup>∗</sup> Bin Wang<sup>1</sup>∗† Zhiyuan Zhao<sup>1</sup> Man Jiang<sup>1</sup> Xiaomeng Zhao<sup>1</sup> Jin Shi<sup>1</sup> Fan Wu<sup>1</sup> Pei Chu<sup>1</sup> Minghao Liu<sup>3</sup> Zhenxiang Li<sup>1</sup> Chao Xu<sup>1</sup> Bo Zhang<sup>1</sup> Botian Shi<sup>1</sup> Zhongying Tu<sup>1</sup> Conghui He<sup>1</sup>‡

> 1 Shanghai AI Laboratory <sup>2</sup>Abaka AI <sup>3</sup> 2077AI

#### Abstract

*Document content extraction is a critical task in computer vision, underpinning the data needs of large language models (LLMs) and retrieval-augmented generation (RAG) systems. Despite recent progress, current document parsing methods have not been fairly and comprehensively evaluated due to the narrow coverage of document types and the simplified, unrealistic evaluation procedures in existing benchmarks. To address these gaps, we introduce OmniDocBench, a novel benchmark featuring high-quality annotations across nine document sources, including academic papers, textbooks, and more challenging cases such as handwritten notes and densely typeset newspapers. OmniDocBench supports flexible, multi-level evaluations—ranging from an end-to-end assessment to the task-specific and attribute-based analysis—using 19 layout categories and 15 attribute labels. We conduct a thorough evaluation of both pipeline-based methods and endto-end vision-language models, revealing their strengths and weaknesses across different document types. OmniDocBench sets a new standard for the fair, diverse, and fine-grained evaluation in document parsing. Dataset and code are available at* [https://github.com/](https://github.com/opendatalab/OmniDocBench) [opendatalab/OmniDocBench](https://github.com/opendatalab/OmniDocBench)*.*

### 1. Introduction

As large language models [\[1,](#page-8-0) [28,](#page-9-0) [39,](#page-9-1) [44\]](#page-9-2) increasingly rely on high-quality, knowledge-rich data, the importance of accurate document parsing has grown substantially. Document parsing, a core task in computer vision and document intelligence, aims to extract structured, machine-readable content from unstructured documents such as PDFs. This task is particularly critical for ingesting academic papers, technical reports, textbooks, and other rich textual sources

![](_page_0_Picture_5.jpeg)

Figure 1. Results of End-to-End Text Recognition on OmniDocBench across 9 PDF page types.

into large language models, thereby enhancing their factual accuracy and knowledge grounding [\[19,](#page-8-1) [42,](#page-9-3) [45,](#page-9-4) [47,](#page-9-5) [52\]](#page-10-0). Moreover, with the emergence of retrieval-augmented generation (RAG) systems [\[12,](#page-8-2) [22\]](#page-8-3), which retrieve and generate answers conditionally with external documents, the demand for precise document understanding has further intensified.

To address this challenging task, two main paradigms have emerged: 1) Pipeline-based approaches that decompose the task into layout analysis, OCR, formula/table recognition, and reading order estimation [\[34,](#page-9-6) [42\]](#page-9-3); and 2) End-to-end vision-language models (VLMs) that directly output structured representations (e.g., Markdown) [\[3,](#page-8-4) [7,](#page-8-5) [8,](#page-8-6) [29,](#page-9-7) [45,](#page-9-4) [46,](#page-9-8) [48\]](#page-9-9). Although both approaches have demonstrated promising results, conducting a broad comparison of their effectiveness remains challenging due to the absence of a comprehensive and unified evaluation benchmark.

As shown in Table [1,](#page-2-0) for pipeline-based document parsing systems, dedicated benchmarks [\[10,](#page-8-7) [26,](#page-9-10) [54\]](#page-10-1) have been

<sup>∗</sup> The authors contributed equally.

<sup>†</sup> Project lead.

<sup>‡</sup> Corresponding author (heconghui@pjlab.org.cn).

<span id="page-1-0"></span>![](_page_1_Diagram_0.jpeg)

Figure 2. Overview of OmniDocBench Data Diversity. The benchmark includes 9 diverse PDF document types. It supports rich annotation types, including layout annotations (e.g., title, table, figure) and recognition annotations (e.g., text spans, equations, tables). Each page is annotated with 6 page-level attributes (e.g., PDF type, layout type), along with fine-grained 3 text attributes (e.g., language) and 6 tables attributes (Items under "*special issues*" are treated as individual binary attributes (yes/no)), enabling detailed and robust evaluation.

developed to target specific sub-tasks. For end-to-end evaluation, works like Nougat [\[7\]](#page-8-5) and GOT-OCR [\[45\]](#page-9-4) provide relatively small validation sets and assess predictions using page-level metrics such as Edit Distance [\[21\]](#page-8-8).

However, these benchmarks present several key limitations: 1) Limited document diversity: Existing datasets primarily focus on academic papers, overlooking other realworld document types such as textbooks, exams, financial reports, and newspapers; 2) Inconsistent evaluation metrics: Current benchmarks rely heavily on generic text similarity metrics (e.g., Edit Distance [\[21\]](#page-8-8) and BLEU [\[33\]](#page-9-11)), which fail to fairly assess the accuracy of formulas and tables in LaTeX or HTML formats that allow for diverse syntactic expressions; and 3) Lack of fine-grained evaluation: Most evaluations report only an overall score, lacking insights into specific weaknesses, such as element-level score (e.g., text vs. formula) or per document-type performance (e.g., magazine or notes).

To address these limitations, we introduce OmniDocBench, a new benchmark designed to provide a rigorous and comprehensive evaluation for document parsing models across both pipeline-based and end-to-end paradigms. In summary, our benchmark introduces the following key contributions:

- High-quality, diverse evaluation set: We include pages from 9 distinct document types, ranging from textbooks

to newspapers, annotated using a combination of automated tools, manual verification, and expert review.

- Flexible, multi-dimensional evaluation: We support comprehensive evaluation at three levels—end-to-end, task-specific, and attribute-based. End-to-end evaluation measures the overall quality of full-page parsing results. Task-specific evaluation allows users to assess individual components such as layout detection, OCR, table recognition, or formula parsing. Attribute-based evaluation provides fine-grained analysis across 9 document types, 6 page-level attributes and 9 bbox-level attributes.
- Comprehensive benchmarking of state-of-the-art methods: We systematically evaluate a suite of representative document parsing systems, including both pipeline-based tools and VLMs, providing the most comprehensive comparison and identifying performance bottlenecks across document types and content structures.

#### 2. Related Work

#### 2.1. Pipeline-based Document Content Extraction

Pipeline-based methods treat the document content extraction task as a collection of single modules, such as document layout detection [\[13,](#page-8-9) [17,](#page-8-10) [36,](#page-9-12) [53\]](#page-10-2), optical character recognition [\[15,](#page-8-11) [23,](#page-8-12) [30,](#page-9-13) [38,](#page-9-14) [43\]](#page-9-15), formula recognition [\[6,](#page-8-13) [27,](#page-9-16) [40,](#page-9-17) [51\]](#page-9-18), and table recognition [\[16,](#page-8-14) [18,](#page-8-15) [23\]](#page-8-12). In

<span id="page-2-1"></span><span id="page-2-0"></span>

| Benchmark Single-Task Eval Benchmark Robust Reading [20] PubLayNet [49] , DocBank [26] , | Document Domain 1 | BBox " Text " | Annotaion Table Type Formula | Attributes | OCR " Single-Task DLA | Eval TR MFR | OCR End-to-End TR | Eval MFR ROD |
|------------------------------------------------------------------------------------------|-------------------|---------------|------------------------------|------------|-----------------------|-------------|-------------------|--------------|
| DocLayNet [35] , M 6 Doc [9]                                                             |                   |               |                              |            |                       |             |                   |              |
|                                                                                          | 1, 1,             |               |                              |            |                       |             |                   |              |
|                                                                                          | 5, 6              | "             |                              |            | "                     |             |                   |              |
| PubTabNet [54] ,TableX [11]                                                              | 1, 1              |               | "                            |            |                       | "           |                   |              |
| TableBank [25]                                                                           | 1                 | "             | "                            |            |                       | "           |                   |              |
| Im2Latex-100K [10] ,UniMER-Test [40]                                                     | 1                 |               | "                            |            |                       | "           |                   |              |
| End-to-end Eval Benchmarks                                                               |                   |               |                              |            |                       |             |                   |              |
| Fox [29]                                                                                 | 2                 | " "           |                              |            | "                     |             | "                 |              |
| Nougat [7]                                                                               | 1                 | "             | " "                          |            |                       |             | " "               | "            |
| GOT OCR 2.0 [45]                                                                         | 2                 | "             | " "                          |            |                       |             | " "               | "            |
| OmniDocBench                                                                             | 9                 | " "           | " "                          | "          | " "                   | " "         | " "               | " "          |

Table 1. A Comparison between OmniDocBench and existing benchmarks. *BBox*: Bounding boxes. *Text*: Text in Unicode. *Table*: Table in LaTeX/HTML/Markdown. *Formula*: Formula in LaTeX. *Attributes*: Page- and BBox-Level Attributes. *OCR*: Optical Character Recognition; *DLA*: Document Layout Analysis; *TR*: Table Recognition; *MFR*: Math Formula Recognition; *ROD*: Reading Order Detection

this sense, such methods can utilize different expert models to address each specific task. Marker [\[34\]](#page-9-6) integrates opensource models to parse documents into structured formats such as Markdown, JSON, and HTML. To get higher accuracy, an optional LLM-enabled version can also be integrated to merge tables across pages, handle inline math, and so on. Similarly, MinerU [\[42\]](#page-9-3) first utilizes a layout detection model to segment the document page into different regions, then applies task-specific models for corresponding regions. Finally, it outputs the complete content in Markdown format with a reading order algorithm. By leveraging lightweight models and parallelized operations, pipelinebased methods can achieve efficient parsing speeds.

#### 2.2. VLM-based Document Content Extraction

Document understanding and optical character recognition (OCR) are crucial tasks for evaluating the perception capabilities of vision-language models (VLMs). By incorporating extensive OCR corpus into the pretraining stage, VLMs like GPT4o [\[2\]](#page-8-20) and Qwen2-VL [\[3\]](#page-8-4) have demonstrated comparable performance in document content extraction tasks. Unlike pipeline-based methods, VLMs perform document parsing in an end-to-end manner. Furthermore, without requiring specialized data fine-tuning, these models are able to deal with diverse and even unseen document types for their generalization capabilities.

To integrate the efficiency of lightweight models and the generalizability of VLMs, many works [\[7,](#page-8-5) [14,](#page-8-21) [29,](#page-9-7) [32,](#page-9-21) [45,](#page-9-4) [46\]](#page-9-8) have focus on training specialized end-to-end expert models for document parsing. These VLM-driven models excel at comprehending both visual layouts and textual contents, balancing a trade-off between accuracy and efficiency.

#### 2.3. Benchmarks for Document Content Extraction

Document content extraction requires the ability to understand document layouts and recognize various types of content. However, current benchmarks fall short of a comprehensive page-level evaluation, as they focus solely on evaluating the model's performance on module-level recognition. PubLayNet [\[49\]](#page-9-19) and concurrent benchmarks [\[9,](#page-8-17) [26,](#page-9-10) [35\]](#page-9-20) specialize in evaluating a model's ability to detect document page layouts. OCRBench [\[31\]](#page-9-22) proposes five OCR-related tasks with a greater emphasis on evaluating the model's visual understanding and reasoning capabilities. Only linelevel assessments are provided for text recognition and handwritten mathematical expression recognition (HMER). Similarly, single-module benchmarks [\[20,](#page-8-16) [26,](#page-9-10) [40,](#page-9-17) [54\]](#page-10-1) disentangle the task into different dimensions and focus narrowly on specific parts. Such paradigm overlooks the importance of structural and semantic information like the reading order and fails to evaluate the model's overall ability when processing the full-page documents as a whole.

Page-level benchmarks have been proposed alongside some recent VLM-driven expert models [\[7,](#page-8-5) [29,](#page-9-7) [45\]](#page-9-4). However, the robustness of these benchmarks is compromised by limitations in data size, language, document type, and annotation. For example, Nougat [\[7\]](#page-8-5) evaluates models using only printed English documents collected from arXiv while the page-level benchmark introduced by GOT-OCR [\[45\]](#page-9-4) consists of only 90 pages of Chinese and English documents in total. Commonly-seen document types like handwritten notes, newspapers, and exam papers are further neglected. Lacking detailed annotations, the benchmarks can only conduct naive evaluation between the full-page results of Ground Truths and predictions without special handling for different output formats and specialized metrics for different content types. The evaluation of the model performance can be severely biased due to limited document domains, unaligned output format and mismatched metrics. *Therefore, there is an urgent need for a more finely annotated, diverse, and reasonable page-level document content extraction benchmark.*

<span id="page-3-4"></span><span id="page-3-0"></span>![](_page_3_Diagram_0.jpeg)

Figure 3. Overview of the OmniDocBench dataset construction.

## 3. OmniDocBench Dataset

Constructing a diverse and comprehensive document parsing benchmark with precise annotations is a significant challenge. As illustrated in Figure [3,](#page-3-0) we have designed a systematic and professional annotation framework for OmniDocBench, encompassing data acquisition, intelligent pre-annotation, and manual refinement. This ensures that OmniDocBench possesses the following key attributes:

- Page Diversity. We sourced document pages from a variety of origins to ensure a wide range of document types.
- Comprehensive Annotation. We meticulously annotated all elements on the pages, including bounding boxes, specific contents, and various potential attributes.
- Annotation Accuracy. By integrating semi-automated annotation processes, annotator corrections, and expert quality checks, we ensure the reliability of all annotations.

The following sections detail the data acquisition process, the annotation methodology, and a statistical analysis of the final annotated dataset.

### 3.1. Data Acquisition

During the data acquisition phase, we sourced document pages from diverse origins and used clustering algorithms to initially select visually diverse pages, followed by manual annotation of page attributes to finalize the OmniDocBench pages. Specifically, we collected over 200,000 initial PDF documents from Common Crawl, Google, Baidu search engines, and internal data. Subsequently, we extracted visual features from these document pages using ResNet-50 and performed clustering using Faiss [<sup>1</sup>](#page-3-1) , sampling 6,000 visually diverse pages from 10 cluster centers. Finally, annotators provided page-level attribute annotations, including page type, layout type, and language type, and further balanced the selection to 981 samples for the final dataset. The OmniDocBench dataset includes pages from nine distinct types, multiple layout categories, and various attribute annotations, covering a wide range of real-world scenarios.

#### 3.2. Data Annotation

To ensure the comprehensiveness of OmniDocBench's annotations, we conducted detailed annotations for layout detection and content recognition.

#### 3.2.1. Annotation Types

Layout Detection Annotations: Unlike typical layout detection tasks, OmniDocBench includes four comprehensive types of annotations: (1) Layout Bounding Box Annotations: Positioanl information for 19 distinct region categories such as titles, text paragraphs, tables, and images. (2) Layout Attribute Annotations: Detailed attribute annotations for detected boxes, including 3 text box attribute categories, 6 table attribute categories, 9 bbox-level attribute labels in total. (3) Reading Order Annotations: Annotating the reading sequence of detected boxes. (4) Affiliation Annotations: For images, tables, formulas, and code blocks, we annotate captions and titles to distinguish them from main text. Similarly, for cross-page paragraphs, we annotate affiliation relationships.

Content Recognition Annotations: Based on the content type within each region, we conduct the following three types of annotations: (1) Text Annotations: Pure text annotations for titles, text paragraphs, and other plain text content. (2) Formula Annotations: LaTeX format annotations for inline formulas, display formulas, and subscripts. (3) Table Annotations: Providing both HTML and LaTeX annotations for table data.

#### 3.2.2. Annotation Process

For these annotation tasks on diverse pages, we design a standardized process to ensure quality and efficiency, comprising intelligent automatic annotation, annotator correction, and expert quality inspection.

Automatic Annotation. Manually annotating entire documents is time-consuming and costly. To enhance efficiency, we employ state-of-the-art detection and recognition models for pre-annotation of layout detection and content recognition. Specifically, we use fine-tuned LayoutLMv3 [\[17\]](#page-8-10) for layout detection annotations and PaddleOCR [\[23\]](#page-8-12), UniMERNet [\[40\]](#page-9-17), and GPT-4o [\[2\]](#page-8-20) for text, formula, and table annotations, respectively.

Annotator Correction. After the layout detection phase, annotators refine the detection boxes and enhance annotations with reading order and affiliation details. Each character is verified to ensure accuracy in content recognition. For complex annotations of tables and formulas, requiring LaTeX and HTML formats, annotators use tools like Tables Generator [<sup>2</sup>](#page-3-2) and latexlive [<sup>3</sup>](#page-3-3) for verification and correction.

Expert Quality Inspection. Despite thorough annotator corrections, the complexity of formulas and tables may re-

<span id="page-3-1"></span><sup>1</sup><https://github.com/facebookresearch/faiss>

<span id="page-3-2"></span><sup>2</sup><https://www.tablesgenerator.com/>

<span id="page-3-3"></span><sup>3</sup><https://www.latexlive.com/>

<span id="page-4-2"></span>sult in residual issues. To address these, we use CDM's rendering techniques [\[41\]](#page-9-23) to identify unrenderable elements. These elements are then reviewed and corrected by three researchers to ensure accuracy in the final annotations.

#### 3.3. Dataset Statistics

Page Diversity. OmniDocBench comprises a total of 981 PDF pages across 9 distinct types. Each page is annotated with global attributes, including text language, column layout type, and indicators for blurred scans, watermarks, and colored backgrounds.

Annotation Diversity: OmniDocBench contains over 100,000 annotations for page detection and recognition: (1) More than 20,000 block-level annotations across 15 categories, including over 15,979 text paragraphs, 989 image boxes, 428 table boxes, and so on. All document components except headers, footers, and page notes are labeled with reading order information, totaling over 16,000 annotations. (2) The dataset also includes more than 70,000 span-level annotations across 4 categories, with 4,009 inline formulas and 357 footnote markers represented in LaTeX format, while the remaining annotations are in text format.

Annotation Attribute Diversity: (1) *Text Attributes:* All block-level annotations, except for tables and images, include text attribute tags. In addition to standard Chinese and English text, there are over 2,000 blocks with complex backgrounds and 493 with rotated text. (2) *Table Attributes:* In addition to standard Chinese and English tables, there are 142 tables with complex backgrounds, 81 containing formulas, 150 with merged cells, and 7 vertical tables.

## 4. OmniDocBench Evaluation Methodology

To provide a fair and comprehensive evaluation for various models, we proposed an end-to-end evaluation pipeline consisting of several modules, including extraction, matching algorithm, and metric calculation, as shown in Figure [4.](#page-4-0) It ensures that OmniDocBench automatically performs unified evaluation on document parsing, thereby producing reliable and effective evaluation results.

#### 4.1. Extraction

Preprocessing. The model-generated markdown text should be preprocessed, which includes removing images, eliminating markdown tags at the beginning of the document, and standardizing the number of repeated characters. Elements Extraction. Extraction is primarily carried out using regular expression matching. To ensure that the extraction of elements does not interfere with each other, it is necessary to follow a specific order. The extraction sequence is as follows: LaTeX tables, HTML tables, display formulas, markdown tables (which are then converted into HTML format), and code blocks.

<span id="page-4-0"></span>![](_page_4_Diagram_0.jpeg)

Figure 4. OmniDocBench Evaluation Pipeline.

Pure Text Extraction. After extracting special components, the remaining content is considered pure text. Paragraphs are separated by double line breaks, allowing them to participate in subsequent matching processes, thus aligning with reading order annotation units in the GTs. If no double line break exists, single line breaks are used for paragraph separation. Additionally, previously extracted code blocks are merged into the text category for processing.

Inline Formula Format Converting. We standardized inline formulas within paragraphs to Unicode format. This was necessary because different models produce inconsistent outputs for inline formulas. For formulas originally written in Unicode, it is hard to extract them using regular expressions. Therefore, to ensure a fair comparison, we do not extract inline formulas for separate evaluation. Instead, we include them in their Unicode format alongside the text paragraphs for evaluation.

Reading Order Extraction. Upon completion of the extraction, the start and end positions of the extracted content in the original markdown are recorded for subsequent reading order calculation.

#### 4.2. Matching Algorithm

Adjacency Search Match. To avoid the impact of paragraph splitting on the final results, we proposed Adjacency Search Match, that merges and splits paragraphs in both GTs and Preds to achieve the best possible match. The specific strategy involves: i) Calculate a metrix of Normalized Edit Distance between GTs and Preds. The Pred and GT pairs whose similarity exceeds a specific threshold are considered as successful match. ii) For the rest, we apply fuzzy matching to determine whether one string is a subset of another string. If so, we further apply the merging algorithm which would try to merge adjacent paragraph. This process would continue to merge more paragraph until the Normalized Edit Distance starts to decrease. After this process, the best match will be found for GTs and Preds.

<span id="page-4-1"></span><sup>4</sup><https://mathpix.com/>

<span id="page-5-6"></span><span id="page-5-0"></span>

| Method Type         | Methods | EN         | Text Edit ↓ ZH | EN    | Formula Edit ZH | ↓ EN | Formula CDM ZH | ↑ Table EN | TEDS ZH | ↑ EN  | Table Edit ↓ ZH | Read EN | Order Edit ZH | ↓ EN  | Overall Edit ↓ ZH |
|---------------------|---------|------------|----------------|-------|-----------------|------|----------------|------------|---------|-------|-----------------|---------|---------------|-------|-------------------|
| Pipeline Tools      |         |            |                |       |                 |      |                |            |         |       |                 |         |               |       |                   |
| MinerU              | [42]    | 0.061      | 0.215          | 0.278 | 0.577           | 57.3 | 42.9           | 78.6       | 62.1    | 0.18  | 0.344           | 0.079   | 0.292         | 0.15  | 0.357             |
| Marker              | [34]    | 0.08       | 0.315          | 0.53  | 0.883           | 17.6 | 11.7           | 67.6       | 49.2    | 0.619 | 0.685           | 0.114   | 0.34          | 0.336 | 0.556             |
| Mathpix             | 4       | 0.105      | 0.384          | 0.306 | 0.454           | 62.7 | 62.1           | 77.0       | 67.1    | 0.243 | 0.32            | 0.108   | 0.304         | 0.191 | 0.365             |
| Expert VLMs GOT-OCR | [45]    | 0.189      | 0.315          | 0.360 | 0.528           | 74.3 | 45.3           | 53.2       | 47.2    | 0.459 | 0.52            | 0.141   | 0.28          | 0.287 | 0.411             |
| Nougat              | [7]     | 0.365      | 0.998          | 0.488 | 0.941           | 15.1 | 16.8           | 39.9       | 0.0     | 0.572 | 1.000           | 0.382   | 0.954         | 0.452 | 0.973             |
| General VLMs        |         |            |                |       |                 |      |                |            |         |       |                 |         |               |       |                   |
| GPT4o               | [2]     | 0.144      | 0.409          | 0.425 | 0.606           | 72.8 | 42.8           | 72.0       | 62.9    | 0.234 | 0.329           | 0.128   | 0.251         | 0.233 | 0.399             |
| Qwen2-VL-72B        |         | [44] 0.096 | 0.218          | 0.404 | 0.487           | 82.2 | 61.2           | 76.8       | 76.4    | 0.387 | 0.408           | 0.119   | 0.193         | 0.252 | 0.327             |
| InternVL2-76B       | [8]     | 0.353      | 0.290          | 0.543 | 0.701           | 67.4 | 44.1           | 63.0       | 60.2    | 0.547 | 0.555           | 0.317   | 0.228         | 0.44  | 0.443             |

Table 2. Comprehensive evaluation of document parsing algorithms on OmniDocBench: performance metrics for text, formula, table, and reading order extraction, with overall scores derived from ground truth comparisons.

<span id="page-5-1"></span>

| Model Type Models   |      | Book       | Slides | Financial Report | Textbook | Exam Paper | Magazine | Academic Papers | Notes | Newspaper | Overall |
|---------------------|------|------------|--------|------------------|----------|------------|----------|-----------------|-------|-----------|---------|
| Pipeline Tools      |      |            |        |                  |          |            |          |                 |       |           |         |
| MinerU              | [42] | 0.055      | 0.124  | 0.033            | 0.102    | 0.159      | 0.072    | 0.025           | 0.984 | 0.171     | 0.206   |
| Marker              | [34] | 0.074      | 0.34   | 0.089            | 0.319    | 0.452      | 0.153    | 0.059           | 0.651 | 0.192     | 0.274   |
| Mathpix             | 4    | 0.131      | 0.22   | 0.202            | 0.216    | 0.278      | 0.147    | 0.091           | 0.634 | 0.69      | 0.3     |
| Expert VLMs GOT-OCR | [45] | 0.111      | 0.222  | 0.067            | 0.132    | 0.204      | 0.198    | 0.179           | 0.388 | 0.771     | 0.267   |
| Nougat              | [7]  | 0.734      | 0.958  | 1.000            | 0.820    | 0.930      | 0.83     | 0.214           | 0.991 | 0.871     | 0.806   |
| General VLMs        |      |            |        |                  |          |            |          |                 |       |           |         |
| GPT4o               | [2]  | 0.157      | 0.163  | 0.348            | 0.187    | 0.281      | 0.173    | 0.146           | 0.607 | 0.751     | 0.316   |
| Qwen2-VL-72B        |      | [44] 0.096 | 0.061  | 0.047            | 0.149    | 0.195      | 0.071    | 0.085           | 0.168 | 0.676     | 0.179   |
| InternVL2-76B       | [8]  | 0.216      | 0.098  | 0.162            | 0.184    | 0.247      | 0.150    | 0.419           | 0.226 | 0.903     | 0.3     |

Table 3. End-to-end text recognition performance on OmniDocBench: evaluation using edit distance across 9 PDF page types.

<span id="page-5-2"></span>

| Models        |      | Fuzzy             | Water        | Color        | None         |
|---------------|------|-------------------|--------------|--------------|--------------|
| MinerU        | [42] | 0.15/0.048        | 0.151/0.031  | 0.107/0.052  | 0.079/ 0.035 |
| Marker        | [34] | 0.333/0.092       | 0.484/0.126  | 0.319/0.127  | 0.062 /0.125 |
| Mathpix       | 4    | 0.294/0.064       | 0.290/0.059  | 0.216/0.09   | 0.135/0.043  |
| GOT-OCR       | [45] | 0.175/0.05        | 0.190/0.056  | 0.186/0.097  | 0.177/0.081  |
| Nougat        | [7]  | 0.934/0.051       | 0.915/0.071  | 0.873/0.096  | 0.615/0.208  |
| GPT4o         | [2]  | 0.263/0.078       | 0.195/0.057  | 0.184/0.078  | 0.186/0.072  |
| Qwen2-VL-72B  |      | [44] 0.082 / 0.01 | 0.172/ 0.078 | 0.104 / 0.05 | 0.084/0.042  |
| InternVL2-76B | [8]  | 0.120/0.013       | 0.197/0.042  | 0.155/0.059  | 0.261/0.082  |

Table 4. End-to-end text recognition on OmniDocBench: evaluation under various page attributes using the edit distance metric. The value is Mean/Variance of scores in the attribute group. Columns represent: *Fuzzy* (Fuzzy scan), *Water* (Watermark), *Color* (Colorful background). *None* (No special issue)

| Models        |      | Single             | Double        | Three        | Complex      |
|---------------|------|--------------------|---------------|--------------|--------------|
| MinerU        | [42] | 0.311/0.187        | 0.101 / 0.013 | 0.117 /0.046 | 0.385/ 0.057 |
| Marker        | [34] | 0.299/0.143        | 0.299/0.299   | 0.149/0.063  | 0.363 /0.086 |
| Mathpix       | 4    | 0.207/0.123        | 0.188/0.07    | 0.225/ 0.029 | 0.452/0.177  |
| GOT-OCR       | [45] | 0.163/0.106        | 0.145/0.059   | 0.257/0.072  | 0.468/0.185  |
| Nougat        | [7]  | 0.852/0.084        | 0.601/0.224   | 0.662/0.093  | 0.873/0.09   |
| GPT4o         | [2]  | 0.109/0.112        | 0.204/0.076   | 0.254/0.046  | 0.426/0.188  |
| Qwen2-VL-72B  |      | [44] 0.066 / 0.048 | 0.145/0.049   | 0.204/0.055  | 0.394/0.203  |
| InternVL2-76B | [8]  | 0.082/0.052        | 0.312/0.069   | 0.682/0.098  | 0.444/0.174  |

Table 5. End-to-end reading order evaluation on OmniDocBench: results across different column layout types using Normalized Edit Distance. The value is Mean/Variance of scores in the attribute group.

Ignore Handling. We implement an ignore logic for certain components in PDF page content, meaning they participate in matching but are excluded from metric calculations. This is mainly because of inconsistent output standards among models, which should not affect the validation results. For fairness, we ignore: (1) Headers, footers, page numbers, and page footnotes, which are handled inconsistently by different models. (2) Captions for figures, tables, and footnotes often have uncertain placements, thus complicating the reading order. Additionally, some models embed table captions in HTML or LaTeX tables, while others treat them as plain text.

#### 4.3. Metric Calculation

Pure Text. We calculate Normalized Edit Distance [\[21\]](#page-8-8), averaging these metrics at the sample level to obtain the final scores.

Tables. All tables are converted to HTML format before calculating the Tree-Edit-Distance-based Similarity (TEDS) [\[54\]](#page-10-1) metric and Normalized Edit Distance.

Formulas. Formulas are currently evaluated using the Character Detection Matching (CDM) metric [\[41\]](#page-9-23), Normalized Edit Distance, and BLEU [\[33\]](#page-9-11).

Reading Order. Reading order is evaluated using the Normalized Edit Distance as metric. It only involves text com-

<span id="page-5-3"></span><sup>5</sup><https://github.com/tesseract-ocr/tesseract>

<span id="page-5-4"></span><sup>6</sup><https://github.com/VikParuchuri/surya>

<span id="page-5-5"></span><sup>7</sup><https://github.com/lukas-blecher/LaTeX-OCR>

<span id="page-6-2"></span><span id="page-6-0"></span>

| Model            |      | Backbone  | Params | Book  | Slides | Research Report | Textbook | Exam Paper | Magazine | Academic Literature | Notes | Newspaper | Average |
|------------------|------|-----------|--------|-------|--------|-----------------|----------|------------|----------|---------------------|-------|-----------|---------|
| DiT-L [24]       |      | ViT-L     | 361.6M | 43.44 | 13.72  | 45.85           | 15.45    | 3.40       | 29.23    | 66.13               | 0.21  | 23.65     | 26.90   |
| LayoutLMv3       | [17] | RoBERTa-B | 138.4M | 42.12 | 13.63  | 43.22           | 21.00    | 5.48       | 31.81    | 64.66               | 0.80  | 30.84     | 28.84   |
| DocLayout-YOLO   | [53] | v10m      | 19.6M  | 43.71 | 48.71  | 72.83           | 42.67    | 35.40      | 51.44    | 64.64               | 9.54  | 57.54     | 47.38   |
| SwinDocSegmenter | [4]  | Swin-L    | 223M   | 42.91 | 28.20  | 47.29           | 32.44    | 20.81      | 52.35    | 48.54               | 12.38 | 38.06     | 35.89   |
| GraphKD          | [5]  | R101      | 44.5M  | 39.03 | 16.18  | 39.92           | 22.82    | 14.31      | 37.61    | 44.43               | 5.71  | 23.86     | 27.10   |
| DOCX-Chain       | [50] |           |        | 30.86 | 11.71  | 39.62           | 19.23    | 10.67      | 23.00    | 41.60               | 1.80  | 16.96     | 21.27   |

Table 6. Component-level layout detection evaluation on OmniDocBench layout subset: mAP results by PDF page type.

<span id="page-6-1"></span>

| Model Type Model OCR-based |      | EN   | Language ZH | Mixed | Full | Table Omission | Frame Type Three | Zero | Merge Cell | Special (+/-) Formula | Situation (+/-) Colorful | (+/-) Rotate | Overall (+/-) |
|----------------------------|------|------|-------------|-------|------|----------------|------------------|------|------------|-----------------------|--------------------------|--------------|---------------|
| PaddleOCR Models           | [23] | 76.8 | 71.8        | 80.1  | 67.9 | 74.3           | 81.1             | 74.5 | 70.6/75.2  | 71.3/74.1             | 72.7/74.0                | 23.3/74.6    | 73.6          |
| RapidTable                 | [37] | 80.0 | 83.2        | 91.2  | 83.0 | 79.7           | 83.4             | 78.4 | 77.1/85.4  | 76.7/83.9             | 77.6/84.9                | 25.2/ 83.7   | 82.5          |
| Expert VLMs StructEqTable  | [55] | 72.8 | 75.9        | 83.4  | 72.9 | 76.2           | 76.9             | 88.0 | 64.5/81.0  | 69.2/76.6             | 72.8/76.4                | 30.5 /76.2   | 75.8          |
| GOT-OCR                    | [45] | 72.2 | 75.5        | 85.4  | 73.1 | 72.7           | 78.2             | 75.7 | 65.0/80.2  | 64.3/77.3             | 70.8/76.9                | 8.5/76.3     | 74.9          |
| General VLMs Qwen2-VL-7B   | [44] | 70.2 | 70.7        | 82.4  | 70.2 | 62.8           | 74.5             | 80.3 | 60.8/76.5  | 63.8/72.6             | 71.4/70.8                | 20.0/72.1    | 71.0          |
| InternVL2-8B               | [8]  | 70.9 | 71.5        | 77.4  | 69.5 | 69.2           | 74.8             | 75.8 | 58.7/78.4  | 62.4/73.6             | 68.2/73.1                | 20.4/72.6    | 71.5          |

Table 7. Component-level Table Recognition evaluation on OmniDocBench table subset. *(+/-)* means *with/without* special situation.

ponents, with tables, images, and ignored components excluded from the final reading order calculation.

#### 5. Benchmarks

Based on the distinct characteristics of these algorithms, we categorize document content extraction methods into three main classes:

- Pipeline Tools: These methods integrate layout detection and various content recognition tasks (such as OCR, table recognition, and formula recognition) into a document parsing pipeline for content extraction. Prominent examples include MinerU [\[42\]](#page-9-3) (v0.9.3), Marker [\[34\]](#page-9-6) (v1.2.3), and Mathpix[<sup>4</sup>](#page-4-1) .
- Expert VLMs: These are large multimodal models specifically trained for document parsing tasks. Representative models include GOT-OCR2.0 [\[45\]](#page-9-4) and Nougat [\[7\]](#page-8-5).
- General VLMs: These are general-purpose large multimodal models inherently capable of document parsing. Leading models in this category include GPT-4o [\[2\]](#page-8-20), Qwen2-VL-72B [\[44\]](#page-9-2), and InternVL2-76B [\[8\]](#page-8-6).

#### 5.1. End-to-End Evaluation Results

Overall Evaluation Results. As illustrated in Table [2,](#page-5-0) pipeline tools such as MinerU and Mathpix, demonstrate superior performance across sub-tasks like text recognition, formula recognition, and table recognition. Moreover, the general Vision Language Models (VLMs), Qwen2-VL, and GPT4o, also exhibit competitive performance. Almost all algorithms score higher on English than on Chinese pages. Performance Across Diverse Page Types. To gain deeper insights into model performance on diverse document types, we evaluated text recognition tasks across different page types. Intriguingly, as shown in Table [3,](#page-5-1) pipeline tools perform well for commonly used data, such as academic papers and financial reports. Meanwhile, for more specialized data, such as slides and handwritten notes, general VLMs demonstrate stronger generalization. Notably, most VLMs fail to recognize when dealing with the Newspapers, while pipeline tools achieve significantly better performance.

Performance on Pages with Visual Degradations. In Table [4,](#page-5-2) we further analyze performance on pages containing common document-specific challenges, including fuzzy scans, watermarks, and colorful backgrounds. VLMs like InternVL2 and Qwen2-VL exhibit higher robustness in these scenarios despite visual noise. Among pipeline tools, MinerU remains competitive due to its strong layout segmentation and preprocessing capabilities.

Performance on Different Layout Types. Page layout is a critical factor in document understanding, especially for tasks involving reading order. OmniDocBench annotates layout attributes such as single-column, multi-column, and complex custom formats. Across all models, we observe a clear drop in accuracy on multi-column and complex layouts. MinerU shows the most consistent reading order prediction, though its performance dips on handwritten singlecolumn pages due to recognition noise.

Discussion on End-to-End Results. 1) While general VLMs often lag behind specialized pipelines and expert models on standard documents (e.g., academic papers), they generalize better to unconventional formats (e.g., notes) and perform more robustly under degraded conditions (e.g., fuzzy scans). This is largely due to their broader training data, enabling better handling of long-tail scenarios compared to models trained on narrow domains. 2) VLMs, how-

<span id="page-7-2"></span><span id="page-7-0"></span>

| Model Type Model     |       | EN    | Language ZH | Mixed | White | Text Single | background Multi | Normal | Rotate90 | Text Rotate Rotate270 | Horizontal |
|----------------------|-------|-------|-------------|-------|-------|-------------|------------------|--------|----------|-----------------------|------------|
| Expert Vision        |       |       |             |       |       |             |                  |        |          |                       |            |
| PaddleOCR            | [23]  | 0.071 | 0.055       | 0.118 | 0.060 | 0.038       | 0.085            | 0.060  | 0.015    | 0.285                 | 0.021      |
| Tesseract            | OCR 5 | 0.179 | 0.553       | 0.553 | 0.453 | 0.463       | 0.394            | 0.448  | 0.369    | 0.979                 | 0.982      |
| Surya Models         | 6     | 0.057 | 0.123       | 0.164 | 0.093 | 0.186       | 0.235            | 0.104  | 0.634    | 0.767                 | 0.255      |
| GOT-OCR              | [45]  | 0.041 | 0.112       | 0.135 | 0.092 | 0.052       | 0.155            | 0.091  | 0.562    | 0.966                 | 0.097      |
| Mathpix              | 4     | 0.033 | 0.240       | 0.261 | 0.185 | 0.121       | 0.166            | 0.180  | 0.038    | 0.185                 | 0.638      |
| Vision Language      |       |       |             |       |       |             |                  |        |          |                       |            |
| Qwen2-VL-72B         | [44]  | 0.072 | 0.274       | 0.286 | 0.234 | 0.155       | 0.148            | 0.223  | 0.273    | 0.721                 | 0.067      |
| InternVL2-76B Models | [8]   | 0.074 | 0.155       | 0.242 | 0.113 | 0.352       | 0.269            | 0.132  | 0.610    | 0.907                 | 0.595      |
| GPT4o                | [2]   | 0.020 | 0.224       | 0.125 | 0.167 | 0.140       | 0.220            | 0.168  | 0.115    | 0.718                 | 0.132      |

Table 8. Component-level evaluation on OmniDocBench OCR subset: results grouped by text attributes using the edit distance metric.

<span id="page-7-1"></span>

| Models        |      | CDM  | ExpRate@CDM | BLEU  | Norm Edit |
|---------------|------|------|-------------|-------|-----------|
| GOT-OCR       | [45] | 74.1 | 28.0        | 55.07 | 0.290     |
| Mathpix       | 4    | 86.6 | 2.8         | 66.56 | 0.322     |
| Pix2Tex       | 7    | 73.9 | 39.5        | 46.00 | 0.337     |
| UniMERNet-B   | [40] | 85.0 | 60.2        | 60.84 | 0.238     |
| GPT4o         | [2]  | 86.8 | 65.5        | 45.17 | 0.282     |
| InternVL2-76B | [8]  | 67.4 | 54.5        | 47.63 | 0.308     |
| Qwen2-VL-72B  | [44] | 83.8 | 55.4        | 53.71 | 0.285     |

Table 9. Component-level formula recognition evaluation on OmniDocBench formula subset.

ever, struggle with high-density documents like newspapers due to limitations in input resolution and token length. In contrast, pipeline tools leverage layout-based segmentation to process components individually, maintaining accuracy in complex layouts. Enhancing VLMs with layout-aware designs and domain-specific fine-tuning offers a promising path forward. OmniDocBench facilitates this by providing detailed annotations for layout, text, formulas, and tables, enabling comprehensive benchmarking and modular tool development for diverse document parsing tasks.

#### 5.2. Single Task Evaluation Results

Layout Detection Results. Layout detection is the first step in document parsing using pipeline tools. A robust layout detection algorithm should perform well across a variety of document types. Table [6](#page-6-0) presents an evaluation of leading layout detection models. The DocLayout-YOLO method, which is pre-trained on diverse synthetic document data, significantly outperforms other approaches. This superiority is a key factor in MinerU's integration of DocLayout-YOLO, contributing to its outstanding overall performance. Other methods perform well on books and academic literature but struggle with more diverse formats due to limited training data.

Table Recognition Results. In Table [7,](#page-6-1) We evaluate table recognition models across three dimensions on our OmniDocBench table subset: language diversity, table frame types, and special situations. Among all models, OCRbased models demonstrate superior overall performance, with RapidTable achieving the highest scores in language diversity and maintaining stable performance across different frame types. Expert VLMs show competitive results in specific scenarios, with StructEqTable [\[55\]](#page-10-3) excelling in noframe tables and showing better rotation robustness. General VLMs (Qwen2-VL-7B and InternVL2-8B) exhibit relatively lower but consistent performance, suggesting that while general-purpose VLMs have made progress in table understanding, they still lag behind specialized solutions.

Text Recognition Results. Table [8](#page-7-0) compares OCR tools across languages, backgrounds, and rotations using Edit Distance. PaddleOCR outperforms all competitors, followed by GOT-OCR and Mathpix. General VLMs struggle to handle text rotation or mixed-language scenarios.

Formula Recognition Results. Table [9](#page-7-1) presents results on formula parsing, using CDM, BLEU, and normalized Edit Distance. GPT-4o, Mathpix, and UniMERNet achieve results of 86.8%, 86.6%, and 85.0%, respectively. Notably, GPT-4o excels with a recall rate of 65.5% under strict conditions requiring perfect character accuracy. Although Mathpix shows high character-level precision, it occasionally omits punctuation, such as commas, leading to a lower overall correctness rate. Nonetheless, all three models are strong candidates for formula recognition tasks.

#### 6. Conclusion

This paper addresses the lack of diverse and realistic benchmarks in document parsing research by introducing OmniDocBench, a dataset featuring a variety of page types with comprehensive annotations, along with a flexible and reliable evaluation framework. OmniDocBench enables systematic and fair assessments of document parsing methods, providing crucial insights for advancing the field. Its task-specific and attribute-level evaluations facilitate targeted model optimization, promoting more robust and effective parsing solutions.

#### References

<span id="page-8-24"></span><span id="page-8-23"></span><span id="page-8-22"></span><span id="page-8-21"></span><span id="page-8-20"></span><span id="page-8-19"></span><span id="page-8-18"></span><span id="page-8-17"></span><span id="page-8-16"></span><span id="page-8-15"></span><span id="page-8-14"></span><span id="page-8-13"></span><span id="page-8-12"></span><span id="page-8-11"></span><span id="page-8-10"></span><span id="page-8-9"></span><span id="page-8-8"></span><span id="page-8-7"></span><span id="page-8-6"></span><span id="page-8-5"></span><span id="page-8-4"></span><span id="page-8-3"></span><span id="page-8-2"></span><span id="page-8-1"></span><span id="page-8-0"></span>[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. *arXiv:2303.08774*, 2023. [1](#page-0-0) [2] Open AI. Hello gpt 4o, 2024. Accessed July 24, 2024. [3,](#page-2-1) [4,](#page-3-4) [6,](#page-5-6) [7,](#page-6-2) [8](#page-7-2) [3] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv:2308.12966*, 2024. [1,](#page-0-0) [3](#page-2-1) [4] Ayan Banerjee, Sanket Biswas, Josep Llados, and Uma- ´ pada Pal. Swindocsegmenter: An end-to-end unified domain adaptive transformer for document instance segmentation. In *ICDAR*, 2023. [7](#page-6-2) [5] Ayan Banerjee, Sanket Biswas, Josep Llados, and Umapada ´ Pal. Graphkd: Exploring knowledge distillation towards document object detection with structured graph creation. In *IC-DAR*, 2024. [7](#page-6-2) [6] Lukas Blecher. pix2tex - latex ocr. [https://github.](https://github.com/lukas-blecher/LaTeX-OCR) [com/lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR), 2022. Accessed: 2024-2-29. [2](#page-1-0) [7] Lukas Blecher, Guillem Cucurull, Thomas Scialom, and Robert Stojnic. Nougat: Neural optical understanding for academic documents. *arXiv:2308.13418*, 2024. [1,](#page-0-0) [2,](#page-1-0) [3,](#page-2-1) [6,](#page-5-6) [7](#page-6-2) [8] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, Bin Li, Ping Luo, Tong Lu, Yu Qiao, and Jifeng Dai. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 24185–24198, 2024. [1,](#page-0-0) [6,](#page-5-6) [7,](#page-6-2) [8](#page-7-2) [9] Hiuyi Cheng, Peirong Zhang, Sihang Wu, Jiaxin Zhang, Qiyuan Zhu, Zecheng Xie, Jing Li, Kai Ding, and Lianwen Jin. M6doc: A large-scale multi-format, multi-type, multilayout, multi-language, multi-annotation category dataset for modern document layout analysis. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 15138–15147, 2023. [3](#page-2-1) [10] Yuntian Deng, Anssi Kanervisto, Jeffrey Ling, and Alexander M Rush. Image-to-markup generation with coarse-tofine attention. In *International Conference on Machine Learning*, pages 980–989. PMLR, 2017. [1,](#page-0-0) [3](#page-2-1) [11] Harsh Desai, Pratik Kayal, and Mayank Singh. Tablex: a benchmark dataset for structure and content information extraction from scientific tables. In *Document Analysis and Recognition–ICDAR 2021: 16th International Conference*, pages 554–569, 2021. [3](#page-2-1) [12] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and Haofen Wang. Retrieval-augmented generation for large language models: A survey. *arXiv:2312.10997*, 2023. [1](#page-0-0) [13] Jiuxiang Gu, Jason Kuen, Vlad I Morariu, Handong Zhao, Rajiv Jain, Nikolaos Barmpalios, Ani Nenkova, and Tong Sun. Unidoc: Unified pretraining framework for document understanding. *Advances in Neural Information Processing Systems*, 34:39–50, 2021. [2](#page-1-0) [14] Anwen Hu, Haiyang Xu, Liang Zhang, Jiabo Ye, Ming Yan, Ji Zhang, Qin Jin, Fei Huang, and Jingren Zhou. mplug-docowl2: High-resolution compressing for ocrfree multi-page document understanding. *arXiv preprint arXiv:2409.03420*, 2024. [3](#page-2-1) [15] Mingxin Huang, Yuliang Liu, Zhenghao Peng, Chongyu Liu, Dahua Lin, Shenggao Zhu, Nicholas Yuan, Kai Ding, and Lianwen Jin. Swintextspotter: Scene text spotting via better synergy between text detection and text recognition. In *proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 4593–4603, 2022. [2](#page-1-0) [16] Xin Huang, Ashish Khetan, Milan Cvitkovic, and Zohar Karnin. Tabtransformer: Tabular data modeling using contextual embeddings. arxiv 2020. *arXiv preprint arXiv:2012.06678*, 2012. [2](#page-1-0) [17] Yupan Huang, Tengchao Lv, Lei Cui, Yutong Lu, and Furu Wei. Layoutlmv3: Pre-training for document ai with unified text and image masking, 2022. [2,](#page-1-0) [4,](#page-3-4) [7](#page-6-2) [18] Yongshuai Huang, Ning Lu, Dapeng Chen, Yibo Li, Zecheng Xie, Shenggao Zhu, Liangcai Gao, and Wei Peng. Improving table structure recognition with visual-alignment sequential coordinate modeling. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 11134–11143, 2023. [2](#page-1-0) [19] Wonseok Hwang, Jinyeong Yim, Seunghyun Park, Sohee Yang, and Minjoon Seo. Spatial dependency parsing for semi-structured document information extraction. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP*, pages 330–343. Association for Computational Linguistics (ACL), 2021. [1](#page-0-0) [20] Dimosthenis Karatzas, Lluis Gomez-Bigorda, Anguelos Nicolaou, Suman Ghosh, Andrew Bagdanov, Masakazu Iwamura, Jiri Matas, Lukas Neumann, Vijay Ramaseshan Chandrasekhar, Shijian Lu, Faisal Shafait, Seiichi Uchida, and Ernest Valveny. Icdar 2015 competition on robust reading. In *2015 13th International Conference on Document Analysis and Recognition*, pages 1156–1160, 2015. [3](#page-2-1) [21] Vladimir I Levenshtein et al. Binary codes capable of correcting deletions, insertions, and reversals. In *Doklady Physics*, pages 707–710. Soviet Union, 1966. [2,](#page-1-0) [6](#page-5-6) [22] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, Mike Lewis, Wen-tau Yih, Tim Rockt ¨ aschel, et al. ¨ Retrieval-augmented generation for knowledge-intensive nlp tasks. *Advances in Neural Information Processing Systems*, 33:9459–9474, 2020. [1](#page-0-0) [23] Chenxia Li, Weiwei Liu, Ruoyu Guo, Xiaoting Yin, Kaitao Jiang, Yongkun Du, Yuning Du, Lingfeng Zhu, Baohua Lai, Xiaoguang Hu, Dianhai Yu, and Yanjun Ma. Pp-ocrv3: More attempts for the improvement of ultra lightweight ocr system, 2022. [2,](#page-1-0) [4,](#page-3-4) [7,](#page-6-2) [8](#page-7-2) [24] Junlong Li, Yiheng Xu, Tengchao Lv, Lei Cui, Cha Zhang, and Furu Wei. Dit: Self-supervised pre-training for document image transformer. In *ACMMM*, 2022. [7](#page-6-2) [25] Minghao Li, Lei Cui, Shaohan Huang, Furu Wei, Ming Zhou, and Zhoujun Li. Tablebank: Table benchmark for

<span id="page-9-25"></span><span id="page-9-24"></span><span id="page-9-23"></span><span id="page-9-22"></span><span id="page-9-21"></span><span id="page-9-20"></span><span id="page-9-19"></span><span id="page-9-18"></span><span id="page-9-17"></span><span id="page-9-16"></span><span id="page-9-15"></span><span id="page-9-14"></span><span id="page-9-13"></span><span id="page-9-12"></span><span id="page-9-11"></span><span id="page-9-10"></span><span id="page-9-9"></span><span id="page-9-8"></span><span id="page-9-7"></span><span id="page-9-6"></span><span id="page-9-5"></span><span id="page-9-4"></span><span id="page-9-3"></span><span id="page-9-2"></span><span id="page-9-1"></span><span id="page-9-0"></span>image-based table detection and recognition. In *Proceedings of the Twelfth Language Resources and Evaluation Conference*, pages 1918–1925, 2020. [3](#page-2-1) [26] Minghao Li, Yiheng Xu, Lei Cui, Shaohan Huang, Furu Wei, Zhoujun Li, and Ming Zhou. Docbank: A benchmark dataset for document layout analysis. *arXiv:2006.01038*, 2020. [1,](#page-0-0) [3](#page-2-1) [27] Zhe Li, Lianwen Jin, Songxuan Lai, and Yecheng Zhu. Improving attention-based handwritten mathematical expression recognition with scale augmentation and drop attention. In *2020 17th International Conference on Frontiers in Handwriting Recognition (ICFHR)*, pages 175–180. IEEE, 2020. [2](#page-1-0) [28] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024. [1](#page-0-0) [29] Chenglong Liu, Haoran Wei, Jinyue Chen, Lingyu Kong, Zheng Ge, Zining Zhu, Liang Zhao, Jianjian Sun, Chunrui Han, and Xiangyu Zhang. Focus anywhere for fine-grained multi-page document understanding. *arXiv:2405.14295*, 2024. [1,](#page-0-0) [3](#page-2-1) [30] Yuliang Liu, Hao Chen, Chunhua Shen, Tong He, Lianwen Jin, and Liangwei Wang. Abcnet: Real-time scene text spotting with adaptive bezier-curve network. In *proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 9809–9818, 2020. [2](#page-1-0) [31] Yuliang Liu, Zhang Li, Mingxin Huang, Biao Yang, Wenwen Yu, Chunyuan Li, Xu-Cheng Yin, Cheng-Lin Liu, Lianwen Jin, and Xiang Bai. Ocrbench: on the hidden mystery of ocr in large multimodal models. *Science China Information Sciences*, 67(12), 2024. [3](#page-2-1) [32] Tengchao Lv, Yupan Huang, Jingye Chen, Yuzhong Zhao, Yilin Jia, Lei Cui, Shuming Ma, Yaoyao Chang, Shaohan Huang, Wenhui Wang, Li Dong, Weiyao Luo, Shaoxiang Wu, Guoxin Wang, Cha Zhang, and Furu Wei. Kosmos-2.5: A multimodal literate model, 2024. [3](#page-2-1) [33] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. pages 311–318, 2002. [2,](#page-1-0) [6](#page-5-6) [34] Vik Paruchuri. Marker, 2024. [1,](#page-0-0) [3,](#page-2-1) [6,](#page-5-6) [7](#page-6-2) [35] Birgit Pfitzmann, Christoph Auer, Michele Dolfi, Ahmed S Nassar, and Peter Staar. Doclaynet: A large humanannotated dataset for document-layout segmentation. In *Proceedings of the 28th ACM SIGKDD conference on knowledge discovery and data mining*, pages 3743–3751, 2022. [3](#page-2-1) [36] Subhojeet Pramanik, Shashank Mujumdar, and Hima Patel. Towards a multi-modal, multi-task learning based pretraining framework for document representation learning. *arXiv preprint arXiv:2009.14457*, 2020. [2](#page-1-0) [37] RapidAI. Rapidtable. [https : / / github . com /](https://github.com/RapidAI/RapidTable) [RapidAI/RapidTable](https://github.com/RapidAI/RapidTable), 2023. [7](#page-6-2) [38] Ray Smith, Daria Antonova, and Dar-Shyang Lee. Adapting the tesseract open source ocr engine for multilingual ocr. In *Proceedings of the International Workshop on Multilingual OCR*, 2009. [2](#page-1-0) [39] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste ´ Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. ` Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023. [1](#page-0-0) [40] Bin Wang, Zhuangcheng Gu, Guang Liang, Chao Xu, Bo Zhang, Botian Shi, and Conghui He. Unimernet: A universal network for real-world mathematical expression recognition, 2024. [2,](#page-1-0) [3,](#page-2-1) [4,](#page-3-4) [8](#page-7-2) [41] Bin Wang, Fan Wu, Linke Ouyang, Zhuangcheng Gu, Rui Zhang, Renqiu Xia, Bo Zhang, and Conghui He. Cdm: A reliable metric for fair and accurate formula recognition evaluation. *arXiv:2409.03643*, 2024. [5,](#page-4-2) [6](#page-5-6) [42] Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, Fan Wu, Zhiyuan Zhao, Rui Xu, Kaiwen Liu, Yuan Qu, Fukai Shang, Bo Zhang, Liqun Wei, Zhihao Sui, Wei Li, Botian Shi, Yu Qiao, Dahua Lin, and Conghui He. Mineru: An open-source solution for precise document content extraction. *arXiv:2409.18839*, 2024. [1,](#page-0-0) [3,](#page-2-1) [6,](#page-5-6) [7](#page-6-2) [43] Pengfei Wang, Chengquan Zhang, Fei Qi, Shanshan Liu, Xiaoqiang Zhang, Pengyuan Lyu, Junyu Han, Jingtuo Liu, Errui Ding, and Guangming Shi. Pgnet: Real-time arbitrarilyshaped text spotting with point gathering network. In *Proceedings of the AAAI Conference on Artificial Intelligence*, pages 2782–2790, 2021. [2](#page-1-0) [44] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. Qwen2-vl: Enhancing vision-language model's perception of the world at any resolution. *arXiv preprint arXiv:2409.12191*, 2024. [1,](#page-0-0) [6,](#page-5-6) [7,](#page-6-2) [8](#page-7-2) [45] Haoran Wei, Chenglong Liu, Jinyue Chen, Jia Wang, Lingyu Kong, Yanming Xu, Zheng Ge, Liang Zhao, Jianjian Sun, Yuang Peng, et al. General ocr theory: Towards ocr-2.0 via a unified end-to-end model. *arXiv:2409.01704*, 2024. [1,](#page-0-0) [2,](#page-1-0) [3,](#page-2-1) [6,](#page-5-6) [7,](#page-6-2) [8](#page-7-2) [46] Haoran Wei, Lingyu Kong, Jinyue Chen, Liang Zhao, Zheng Ge, Jinrong Yang, Jianjian Sun, Chunrui Han, and Xiangyu Zhang. Vary: Scaling up the vision vocabulary for large vision-language model. In *European Conference on Computer Vision*, pages 408–424. Springer, 2025. [1,](#page-0-0) [3](#page-2-1) [47] Renqiu Xia, Song Mao, Xiangchao Yan, Hongbin Zhou, Bo Zhang, Haoyang Peng, Jiahao Pi, Daocheng Fu, Wenjie Wu, Hancheng Ye, et al. Docgenome: An open largescale scientific document benchmark for training and testing multi-modal large language models. *arXiv preprint arXiv:2406.11633*, 2024. [1](#page-0-0) [48] Renqiu Xia, Bo Zhang, Hancheng Ye, Xiangchao Yan, Qi Liu, Hongbin Zhou, Zijun Chen, Min Dou, Botian Shi, Junchi Yan, et al. Chartx & chartvlm: A versatile benchmark and foundation model for complicated chart reasoning. *arXiv preprint arXiv:2402.12185*, 2024. [1](#page-0-0) [49] Zhong Xu, Jianbin Tang, and Antonio Jimeno Yepes. Publaynet: largest dataset ever for document layout analysis. In *2019 International conference on document analysis and recognition*, pages 1015–1022, 2019. [3](#page-2-1) [50] Cong Yao. DocXChain: A Powerful Open-Source Toolchain for Document Parsing and Beyond. *ArXiv*, 2023. [7](#page-6-2) [51] Jianshu Zhang, Jun Du, and Lirong Dai. Multi-scale attention with dense encoder for handwritten mathematical

expression recognition. In *2018 24th international conference on pattern recognition (ICPR)*, pages 2245–2250.

<span id="page-10-3"></span><span id="page-10-2"></span><span id="page-10-1"></span><span id="page-10-0"></span>IEEE, 2018. [2](#page-1-0) [52] Qintong Zhang, Victor Shea-Jay Huang, Bin Wang, Junyuan Zhang, Zhengren Wang, Hao Liang, Shawn Wang, Matthieu Lin, Wentao Zhang, and Conghui He. Document parsing unveiled: Techniques, challenges, and prospects for structured information extraction. *arXiv preprint arXiv:2410.21169*, 2024. [1](#page-0-0) [53] Zhiyuan Zhao, Hengrui Kang, Bin Wang, and Conghui He. Doclayout-yolo: Enhancing document layout analysis through diverse synthetic data and global-to-local adaptive perception, 2024. [2,](#page-1-0) [7](#page-6-2) [54] Xu Zhong, Elaheh ShafieiBavani, and Antonio Jimeno Yepes. Image-based table recognition: data, model, and evaluation. In *European conference on computer vision*, pages 564–580, 2020. [1,](#page-0-0) [3,](#page-2-1) [6](#page-5-6) [55] Hongbin Zhou, Xiangchao Yan, and Bo Zhang. Structeqtable-deploy: A high-efficiency open-source toolkit for table-to-latex transformation. [https://github.](https://github.com/UniModal4Reasoning/StructEqTable-Deploy) [com / UniModal4Reasoning / StructEqTable -](https://github.com/UniModal4Reasoning/StructEqTable-Deploy) [Deploy](https://github.com/UniModal4Reasoning/StructEqTable-Deploy), 2024. [7,](#page-6-2) [8](#page-7-2)

# OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations Supplementary Material

#### I. More End-to-End Evaluation Results

Table [S1](#page-12-0) presents the evaluation results of End2End Tables grouped by Table Attributes. As it shows, most of the models perform better in English Tables rather than Chinese ones. Most models perform relatively poorly with Full Frame and No Frame tables. The accuracy of most models is affected by special conditions. Merged cells and formulas mainly test the breadth of data the model can recognize, while colored backgrounds and table rotation test their robustness. The results show that table rotation significantly impacts the accuracy of all models. Pipeline Tools' performance would not be affected by more challenging tables (e.g., merge cell), but colored backgrounds can affect recognition accuracy. Several Vision Language Models (VLMs) tend to perform worse on tables with merged cells, but colored backgrounds do not significantly impact table recognition accuracy.

Table [S2](#page-12-1) shows the evaluation results of End2End Text blocks grouped by Text Attributes. Almost all models have lower recognition accuracy in Chinese compared to English. Some models, such as MinerU and Marker, experience a further decrease in accuracy when recognizing mixed Chinese and English content. The main reason is that minerU's text recognition module is PaddleOCR model. According to the performance of the PaddleOCR model in text recognition module, its accuracy will decline in the case of mixed language. Moreover, complex background colors significantly affect the recognition accuracy of pipeline tools, but it has only little impact on accuracy for VLMs.

## II. Dataset Statistics and Visualization

OmniDocBench contains 981 pages, including 9 types of PDF pages, 4 types of layouts, 3 types of languages, and 3 special issues in visual degradations (e.g., watermarks). Table [S3](#page-12-2) and Figure [S1](#page-14-0) show the number of pages with each page attribute. Figures [S5](#page-16-0) to [S8](#page-18-0) are examples of PDF pages with different PDF types, Layout Types, and Special Issues.

Table [S6](#page-13-0) and Figure [S2](#page-14-1) show all annotation categories included in OmniDocBench. All of them are annotated by bounding boxes. There are 15 types of block-level annotations and 4 types of span-level annotations, with span-level annotations nested within the block-level ones. In addition, there are 3 types of annotations marked as page interference information (No.20-22), whose bounding boxes are used to mask the specific regions of the PDF pages to avoid affecting the evaluation results. The recognition annotations are also provided for each annotation category except for Figures. Formulas is written in LaTeX format and Table is annotated in both HTML and LaTeX formats. Others are annotated in plain text.

Furthermore, the Text Attributes are also annotated for each block-level category that contains text. There are 3 types of Text Attributes that might influent OCR accuracy: Language, Text Background Color, and Text Rotation. Table [S5](#page-12-3) shows the statistics of annotations with specific text attributes. There are 23,010 block-level annotations are labeled with text attributes.

Tables are also annotated with Table Attributes. There are 6 types of Table Attributes that might influent the Table Recognition accuracy: Language, Table Frame Type, Merge Cell, Colorful Background, Contain Formula, and Rotation. Table [S5](#page-12-3) shows the numbers of annotations with specific table attributes. Figures [S9](#page-19-0) and [S10](#page-19-1) are the examples of Tables with different Frames and Special Issues.

## III. Discussion on Model Predictions

Conclusion Combining scattered results from tasks and sub-attributes, it can be concluded that pipeline tools and expert models have better performance on common data like academic papers and challenging cases such as tables with merged cells compared to VLMs. However, VLMs demonstrate stronger generalization on uncommon PDF types like slides and exam papers, and they show greater robustness in special page situations, such as fuzzy scans. The low accuracy of VLMs is mainly due to:1) Missing Content in dense pages(Figure [S11\)](#page-20-0); 2) Hallucinations in hard-to-recognize pages(Figure [S30\)](#page-29-0). The low accuracy of Pipeline tools mainly due to: 1) Lower robustness in special page situations, e.g., watermark(Figure [S21\)](#page-25-0); 2) Weak generalization on uncommon PDF types, e.g., handwriting notes(Figure [S16\)](#page-22-0).

Figures [S11](#page-20-0) to [S19](#page-24-0) show the examples of Good model outputs and Bad model outputs of Document Parsing among different PDF types. As it shown, different models exhibit varying performance across different PDF types. For example, MinerU detects all handwritten notes as figures, resulting in very low recognition accuracy in Notes. Marker and InternVL2 experience missed detections, leading to lower scores. InternVL2 and Qwen2-VL, in specific PDF types (such as slides or financial reports), tend to merge multi-column text.

Figures [S20](#page-24-1) to [S22](#page-25-1) show the examples of Good model outputs and Bad model outputs under special issues of the

<span id="page-12-0"></span>

| Model Type      | Model        | EN   | Language ZH | Mixed | Full | Table Frame Omission | Type Three | Zero | Merge Cell (+/-) | Special Formula (+/-) | Situation Colorful (+/-) | Rotate (+/-) |
|-----------------|--------------|------|-------------|-------|------|----------------------|------------|------|------------------|-----------------------|--------------------------|--------------|
| Pipeline Tools  |              |      |             |       |      |                      |            |      |                  |                       |                          |              |
|                 | MinerU       | 75.1 | 59.3        | 79.1  | 59.4 | 71.6                 | 69.7       | 60.0 | 63.6/65.3        | 66.0/64.4             | 59.2/67.5                | 3.0/65.8     |
|                 | Marker       | 64.9 | 47.3        | 49.8  | 44.5 | 61.8                 | 59.0       | 63.6 | 52.6/52.7        | 53.2/52.5             | 48.0/54.9                | 35.5/52.9    |
|                 | Mathpix      | 75.4 | 63.2        | 71.3  | 67.4 | 77.3                 | 66.3       | 25.5 | 70.3 /65.4       | 68.7/66.7             | 59.7/70.8                | 19.2/67.9    |
| Expert Vision   |              |      |             |       |      |                      |            |      |                  |                       |                          |              |
| Models          | GOT-OCR      | 51.7 | 46.2        | 49.0  | 45.5 | 48.3                 | 51.3       | 46.2 | 46.0/48.9        | 45.7/48.4             | 39.8/51.9                | 0.0/48.7     |
|                 | Nougat       | 36.2 | 0.3         | 0.0   | 6.1  | 3.5                  | 22.1       | 0.0  | 15.0/8.9         | 21/8.7                | 2.6/15.2                 | 0.0/11.2     |
| Vision Language |              |      |             |       |      |                      |            |      |                  |                       |                          |              |
|                 | GPT4o        | 71.1 | 58.0        | 57.3  | 62.5 | 68.7                 | 61.3       | 31.2 | 56.8/64.7        | 60.8/62.2             | 61.4/62.2                | 14.2/62.7    |
| Models          | Qwen2-VL-72B | 73.2 | 75.1        | 76.1  | 72.0 | 79.0                 | 77.5       | 63.2 | 67.9/ 78.1       | 71.6 / 75.3           | 77.9 / 72.9              | 42.7 / 75.1  |
|                 | InterVL2-76B | 60.9 | 58.5        | 65.4  | 58.8 | 65.3                 | 58.3       | 55.6 | 49.0/65.1        | 53.3/60.9             | 58.8/59.8                | 6.9/60.3     |

Table S1. End-to-End Table TEDS Result grouped by Table Attributes

<span id="page-12-1"></span>

| Model Type      | Model         | EN    | Language ZH | Mixed | Text White | background Single | Multi |
|-----------------|---------------|-------|-------------|-------|------------|-------------------|-------|
| Pipeline Tools  |               |       |             |       |            |                   |       |
|                 | MinerU        | 0.124 | 0.234       | 0.742 | 0.188      | 0.15              | 0.514 |
|                 | Marker        | 0.163 | 0.379       | 0.747 | 0.303      | 0.396             | 0.594 |
|                 | Mathpix       | 0.175 | 0.793       | 0.538 | 0.698      | 0.587             | 0.583 |
| Expert Vision   |               |       |             |       |            |                   |       |
| Models          | GOT-OCR       | 0.251 | 0.763       | 0.266 | 0.669      | 0.595             | 0.440 |
|                 | Nougat        | 0.587 | 0.991       | 0.983 | 0.874      | 0.935             | 0.972 |
| Vision Language |               |       |             |       |            |                   |       |
|                 | GPT4o         | 0.170 | 0.647       | 0.322 | 0.536      | 0.423             | 0.406 |
| Models          | Qwen2-VL-72B  | 0.128 | 0.582       | 0.209 | 0.494      | 0.388             | 0.217 |
|                 | InternVL2-76B | 0.418 | 0.606       | 0.251 | 0.589      | 0.366             | 0.221 |

Table S2. End-to-End Text Normalized Edit Distance results grouped by Text Attributes. "Mixed" represents a mixture of Chinese and English, "Single" and "Multi" represent single color and multi color.

<span id="page-12-2"></span>

| Category Attribute   | Name       | Count |
|----------------------|------------|-------|
| PDF Type Book        |            | 104   |
| PPT2PDF              |            | 133   |
| Research             | Report     | 81    |
| Colorful             | Textbook   | 96    |
| Exam                 | Paper      | 114   |
| Magazine             |            | 97    |
| Academic             | Literature | 129   |
| Notes                |            | 116   |
| Newspaper            |            | 111   |
| Layout Type Single   | Column     | 477   |
| Double               | Column     | 126   |
| Three                | Column     | 45    |
| One&More             | Mixed      | 120   |
| Complex              | Layout     | 213   |
| Language English     |            | 290   |
| Simplified           | Chinese    | 612   |
| Mixed                |            | 79    |
| Special Issues Fuzzy | Scan       | 28    |
| Watermark            |            | 65    |
| Colorful             | Background | 246   |

Table S3. The Page Attributes Statistics of OmniDocBench.

PDF pages. It shows that Marker tends to generate typos when the PDF pages are fuzzy scanned or with watermarks, while GOT-OCR fails to recognize content on pages with colored backgrounds. MinerU performs well under special situations, while Mathpix occasionally generates typos.

| Attribute Category Category Name | Count         |
|----------------------------------|---------------|
| Language English                 | 5857          |
| Simplified                       | Chinese 16073 |
| EN&CH Mixed                      | 1080          |
| Text Background White            | 19465         |
| Single-Colored                   | 1116          |
| Multi-Colored                    | 2429          |
| Text Rotate Normal               | 22865         |
| Rotate90                         | 14            |
| Rotate270                        | 58            |
| Horizontal                       | 421           |

<span id="page-12-3"></span>Table S4. Text Attributes Statistics of OmniDocBench.

| Attribute Category Category | Name       | Count |
|-----------------------------|------------|-------|
| Language English            |            | 128   |
| Simplified                  | Chinese    | 285   |
| EN&CH                       | Mixed      | 15    |
| Table Frame Type Full       | Frame      | 205   |
| Omission                    | Line       | 62    |
| Three                       | Line       | 147   |
| No Frame                    |            | 14    |
| Special Issues Merge        | Cell       | 150   |
| Colorful                    | Background | 142   |
| Contain                     | Formula    | 81    |
| Rotate                      |            | 7     |

Table S5. Table Attributes Statistics of OmniDocBench.

Figures [S23](#page-26-0) to [S26](#page-27-0) show examples of Good model outputs and Bad model outputs for PDF pages with different layouts. MinerU has a low reading order score for single-column layouts primarily because most notes are single-column, and MinerU performs poorly in recognizing Notes, leading to a low reading order score accordingly. InternVL2 scores high in Single-Column layouts but scores poorly on Double-Column and Three-Column layouts. It is mainly due to frequent missed content recognition and errors in reading order judgment in multi-column layouts pages. MinerU's reading order and recognition accuracy decrease with complex layouts, primarily because it incorrectly merges multiple columns during recognition.

<span id="page-13-0"></span>

| No. |       | Category Name     |            | Explaination |               |                  |                        |                 |              |              |             |             |             |                                                  | Total                                 |
|-----|-------|-------------------|------------|--------------|---------------|------------------|------------------------|-----------------|--------------|--------------|-------------|-------------|-------------|--------------------------------------------------|---------------------------------------|
| 1   | Title |                   |            | Include      | main titles,  | chapter          | titles,                | etc.            |              |              |             |             |             |                                                  | 2972                                  |
| 2   | Text  | Block             |            | Text         | paragraphs,   | which            | are usually            | separated       | by           | double       | line        | breaks      | in          | Markdown.                                        | 15979                                 |
| 3   |       | Figure            |            | Including    | images,       | visual           | charts,                | etc.            |              |              |             |             |             |                                                  | 989                                   |
| 4   |       | Figure Caption    |            | Typically    | starts with   | ’Figure’         |                        | followed by     | a number,    | or           | just        |             | descriptive | language below the figure.                       | 651                                   |
| 5   |       | Figure Footnotes  |            | Descriptive  | language,     | apart            | from                   | the figure      | caption,     |              | usually     | starts      | with        | an asterisk (*).                                 | 133                                   |
| 6   | Table |                   |            | Content      | organized     | in table         | form                   | usually         | includes     | borders      | or          | a clear     |             | table structure.                                 | 428                                   |
| 7   | Table | Caption           |            | Typically    | starts with   | ’Table’          | followed               | by a            | number,      | or           | just        | descriptive |             | language above the Table.                        | 299                                   |
| 8   | Table | Footnotes         |            | Descriptive  | language,     | apart            | from                   | the table       | caption,     | usually      |             | starts      | with        | an asterisk (*).                                 | 132                                   |
| 9   |       | Header            |            | Information  | located       | at the           | top of a               | PDF page        | or in        | the          | sidebar,    |             | separate    | from the main content, typically includes        | chapter names and other details. 1271 |
| 10  |       | Footer            |            | Information  | located       | at the           | bottom                 | of a PDF        | page,        | separate     |             | from        | the         | main content, typically includes the publisher’s | name and other details. 541           |
| 11  | Page  | Number            | It         | is usually   | represented   |                  | by numbers,            | which           | may          | be           | located     | at the      | top,        | in the sidebar, or at the bottom of the          | page. 669                             |
| 12  | Page  | Footnote          | It         | provides     | further       | explanation      | of                     | the footnotes   |              | marked       | within      | the         | page        | content. For example, information about          | the authors’ affiliations. 92         |
| 13  | Code  | Block             | In         | Markdown,    | a             | code block       | is                     | typically       | defined      | using        | triple      |             | backticks   | (“‘).                                            | 13                                    |
| 14  | Code  | Block Caption     |            | Descriptive  | language      | above            | the                    | Code Block.     |              |              |             |             |             |                                                  | /                                     |
| 15  |       | Reference         |            | Typically    | found         | only in          | academic               | literature.     |              |              |             |             |             |                                                  | 260                                   |
| 16  | Text  | Span              |            | Span-Level   | text          | box, which       | is the                 | plain text      | content      | can          | be          | directly    |             | written in Markdown format.                      | 73143                                 |
| 17  |       | Equation Inline   |            | Formulas     | that need     | to be            | represented            | using           | LaTeX        | format       |             | and         | embedded    | within the text.                                 | 4009                                  |
| 18  |       | Equation Ignore   |            | Some         | formulas that | can              | be displayed           | correctly       |              | without      | using       |             | LaTeX       | formatting, such as 15 kg                        | 3685                                  |
| 19  |       | Footnote Mark     |            | Typically    | embedded      | within           | the text               | as              | superscripts | or           | subscripts, |             | and         | their numbering usually corresponds to           | page footnotes. 357                   |
| 20  | Other | Abandoned         | Categories | (Masked)     | Some          | uncategorizable, |                        | irrelevant      | page         | information, |             | such        | as          | small icons, etc.                                | 538                                   |
| 21  |       | Masked Text Block |            | (Masked)     | Some          |                  | difficult-to-recognize |                 | information  | that         | disrupts    |             | text        | flow, such as pinyin annotations above           | Chinese characters. 34                |
| 22  |       | Organic Chemical  | Formula    | (Masked)     | Organic       | chemistry        |                        | formulas, which | are          | difficult    | to          | write       | using       | Markdown and are easily recognized               | as Figures. 24                        |

Table S6. Annotation Explanations and Statistics.

Figures [S29](#page-29-1) and [S30](#page-29-0) show the model's recognition ability under special issues of text. In text recognition with complex background colors, Marker may produce errors or miss content, whereas Qwen2-VL still performs well. Most models fail to recognize text when it is rotated 270 degrees. Some vision language models generate hallucinated information based on the content they can recognize.

Figures [S31](#page-30-0) to [S34](#page-31-0) show the examples of good and bad model results for tables with different attributes. For three-line tables, RapidTable demonstrates a good performance with accurate structure recognition, while PaddleOCR shows limitations by missing the last column in its outputs. Interestingly, in tables without frames, PaddleOCR performs well with accurate table predictions, while Qwen2-VL-7B exhibits errors in the last two columns. This indicates that the presence or absence of table frames can significantly impact different models' performance in different ways. Rotated tables prove to be particularly challenging, with most models, including GOT-OCR, failing to recognize the table structure. However, StructEqTable shows promising results by correctly identifying most of the table content, though with a few detail errors. For tables containing formula, Qwen2-VL-7B shows more accurate table structure recognition compared to InternVL2-8B.

## IV. Model Settings

For pipeline tools such as MinerU, Marker, and Mathpix, default settings are used for evaluation. Specifically, MinerU with Version 0.9.3[<sup>8</sup>](#page-13-1) is employed. For Marker, Version 1.2.3[<sup>9</sup>](#page-13-2) is evaluated. For Nougat, we utilize its 0.1.0 base model (350M). For GOT-OCR, we employ its format OCR mode to output structured data.

For general VLMs, we used the GPT4o, Qwen2- VL-72B, and InternVL2-Llama3-76B by setting the *do sample*=*False* to ensure the reproducibility. After testing the different setting of *max token*, the best setting is chosen for each VLMs. Specifically, *max token*=*32000* is set for Qwen2-VL-72B, and *max token*=*4096* is set for InternVL2-Llama3-76B. For GPT-4o, the default setting is used.

# V. More Details on Methods

Ignore handling. The purpose of this process is to avoid fluctuations in accuracy caused by the lack of uniformity in the output standards among document parsing algorithm. (1) Some algorithm (e.g., GPT-OCR, Qwen2-VL) tends to remove headers and footers, while others (e.g., GPT4o) prefers to retain them ( Figure [S3\)](#page-15-0). (2) Moreover, the reading order mismatch cause by captions and footnotes is also considered. For example, Nougat would put the image captions in the end of the page content( Figure [S4\)](#page-15-1), while others tend to put the image captions in human reading order.

Ignore handling is to minimize the impact of varying standards of document parsing on evaluation. Our evaluation dataset aims to more fairly assess the parsing accuracy of various algorithms, and these trivial issues regarding standards are not within our scope of consideration.

<span id="page-13-1"></span><sup>8</sup>[https : / / github . com / opendatalab / MinerU /](https://github.com/opendatalab/MinerU/releases/tag/magic_pdf-0.9.3-released) [releases/tag/magic\\_pdf-0.9.3-released](https://github.com/opendatalab/MinerU/releases/tag/magic_pdf-0.9.3-released)

<span id="page-13-2"></span><sup>9</sup>[https : / / github . com / VikParuchuri / marker /](https://github.com/VikParuchuri/marker/releases/tag/v1.2.3) [releases/tag/v1.2.3](https://github.com/VikParuchuri/marker/releases/tag/v1.2.3)

<span id="page-14-0"></span>

| PDF Type        |                       | Layout Type           |                    | Language            |                         | Special issue |                         |                  |
|-----------------|-----------------------|-----------------------|--------------------|---------------------|-------------------------|---------------|-------------------------|------------------|
| PPT2PDF, 133    | Academic Papers, 129  | Notes, 116            |                    |                     |                         |               |                         |                  |
| Exam Paper, 114 | Book, 104             | Magazine, 97          | Single Column, 477 | Other Layout, 213   | Simplified Chinese, 612 |               | Colorful Backgroud, 246 |                  |
| Newspaper, 111  | Colorful Textbook, 96 | Financial Reports, 81 | Double Column, 126 | One&More Mixed, 120 | Three Column, 45        | English, 290  | Watermark, 65           | Fuzzy Search, 29 |

Figure S1. The Data Proportion of Pages for each Attribute in OmniDocBench.

<span id="page-14-1"></span>![](_page_14_Figure_2.jpeg)

Figure S2. The Visualization of vary Annotations in OmniDocBench.

<span id="page-15-0"></span>

|                                      | Plant Growth Regul (2010) 62:181–188                           |
|--------------------------------------|----------------------------------------------------------------|
|                                      | multiplication in *Lotus corniculatus* L.                      |
|                                      | Radomirka Nikolić · Nevena Mitić                               |
|                                      | Slavica Nikn̆ović · Branka Vinterhalter                        |
|                                      | Snežana Zdravković-Korać · Mirjana Nešković                    |
|                                      | © Springer Science+Business Media B.V. 2010                    |
|                                      | Shoots of *Lotus corniculatus* L., previously transformed with |
|                                      | *Agrobacterium tumefaciens* LBA4404/ pTOK233, were grown in    |
| multiplication in Lotus corniculatus | L.                                                             |
| **Authors:**                         | Radomirka Nikolić, Nevena Mitić, Slavica Ninković,             |
| Branka Vinterhalter, Snežana         | Zdravković-Korać, Mirjana Nešković                             |
| **Received:**                        | 22 December 2009 / **Accepted:** 22 July 2010 /                |
| **Published online:**                | 1 August 2010                                                  |
| Shoots of                            | *Lotus corniculatus* L., previously transformed with           |
| *Agrobacterium tumefaciens*          | LBA4404/ pTOK233, were grown in                                |
| gibberellic                          | acid (GA₃)-containing media in an attempt to improve their     |
| Original PDF page                    | Markdown Content (Qwen2-VL) Markdown Content (GPT4o)           |
|                                      | Headers Omitted Headers Recognized                             |
| Footers Page Footnotes               |                                                                |

Figure S3. The Vary Standards in parsing Header, Footers, and so on.

\(\Delta\theta=f[\text{Ac-D-

Trp}]*\_{\text{m}}=f\!k\_*{\text{A,app}}[\text{Ac-D-Trp}]\) and those for the L-isomer can be represented by the following equation:

\[\Delta\theta =f[\text{Ac-L-Trp}]*\_{\text{m}}\] \[=f\left\{p\_*{\text{A,app}}[\text{Ac-L-

Trp}]+\frac{K\_{\text{S,app}}[ \text{Site}]*\_{0}[\text{Ac-L-Trp}]}{1+K\_*{\text{S,app}}[\text{Ac-L-Trp}]}\right\}\]

Fig. 5: Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-D-Trp imprinted **\*\*ODMAAN-533\*\***. \([(\text{Ac-D-Trp})/(\text{ODMA})=0.17\), \(K\_{\text{S,app}}=5.5\times 10^{3}\,\text{mol}^{-1}\,\text{dm}^{3}]\).

Fig. 6: Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-D-Trp imprinted **\*\*ODMAAN-533\*\***. \([(\text{Ac-L-Trp})/(\text{ODMA})=0.17\), \(K\_{\text{S,app}}=5.5\times 10^{3}\,\text{mol}^{-1}\,\text{dm}^{3}]\).

Fig. 7: Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-D-Trp imprinted **\*\*ODMAAN-533\*\***. \([(\text{Ac-D-Trp})/(\text{ODMA})=0.21\), \(K\_{\text{S,app}}=1.20\times 10^{4}\,\text{mol}^{-1}\,\text{dm}^{3}]\).

![](\_page\_0\_Figure\_1.jpeg)

Fig. 5. Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-D-Trp imprinted ODMAAN-533. [(Ac-D-Trp)/(ODMA) = 0.17,

KS,app = 5.5 × 103 mol-1 dm3]. ![](\_page\_0\_Figure\_3.jpeg)

Fig. 6. Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-1-Trp imprinted ODMAAN-533. [(Ac-L-Trp)/(ODMA) = 0.17,

KS,app = 5.5 × 103 mol-1 dm3]. ![](\_page\_0\_Figure\_5.jpeg)

Fig. 7. Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-D-Trp imprinted ODMAAN-533. [(Ac-D-Trp)/(ODMA) = 0.21,

KS.app = 1.20 × 104 mol-1 dm3]. ![](\_page\_0\_Figure\_7.jpeg)

Fig. 8. Adsorption isotherms of Ac-Trp's and adsorption selectivity of the Ac-1-Trp imprinted ODMAAN-533. [(Ac-L-Trp)/(ODMA) = 0.21,

KS,app = 1.16 × 104 mol-1 dm3].

\$\Delta\theta=f\$[Ac-D-Trip]\${}\_{\rm m}=f\$[Ac-D-Trip] and those for the L-isomer can be represented by the following equation:

\$\Delta\theta=f[\text{Ac-L-Trp}]\_{\text{m}}\$

<span id="page-15-1"></span>**Original PDF page Markdown Content (Marker) Markdown Content (Nougat)**

**Human Reading Order Different Reading Order for Image Captions**

Figure S4. The Vary Standards in parsing Captions.

<span id="page-16-0"></span>**Academic Papers**

**Books**

**Colorful Textbooks**

**Magzines**

**Notes**

![](_page_17_Figure_0.jpeg)

Figure S6. The Examples of Finacial Reports, Newspapers, Example Papers, and Slides in OmniDocBench.

**Complex Layout**

**Double Column Three Column**

Figure S7. The Examples of PDF pages with different Layout Types in OmniDocBench.

**Colorful Background**

PDF Special Issues Figure S8. The Examples of PDF pages under Special Issues in OmniDocBench.

<span id="page-18-0"></span>**Fuzzy Scan Watermark**

Table Frame Type Figure S9. The Examples of Tables with different Frame in OmniDocBench.

<span id="page-19-0"></span>**Full Frame Omission Line**

**No Frame**

**Tree Line**

<span id="page-19-1"></span>**Table Rotate Table contain Formula**

**Table with Merge Cell**

**Table with Colorful Background**

Figure S10. The Examples of Tables under Special Issues in OmniDocBench.

<span id="page-20-0"></span>![](_page_20_Diagram_0.jpeg)

docstructbench\_llm-raw-scihub-o.O-ajhb.10190.pdf\_5 Figure S11. The Good Model Result and Bad Model Result for Academic Papers.

| Book                              | Markdown Content (Nougat) Markdown Content (Mathpix)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <table border=1><tr>              | <td>Constant</td> <td>Value</td> <td>Meaning</td> </tr><tr><td>kAlertStdAlertOKButton</td> Missing Table <td>1</td><td><table><tr><td>The OK push button. The default text for this push button is</td></tr><tr><td>”OK”.</td></tr></table>.......                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| The Dialog Structure              | .......{WindowRecord window;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| };.......                         | The Dialog Manager sets the windowKind field of this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                   | Creating Dialog Boxes Dialog boxes may be created in one of two ### Creating Dialog Boxes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ways:-                            | Using the function GetNewDialog, which takes descriptive Dialog boxes may be created in one of two ways: information about the dialog from dialog ( \$\cdot\$ DLOG \$\cdot\$ ) * Using the function GetNewDialog, which takes descriptive and extended dialog \$(\cdot \mathrm{d} 1 \mathrm{gx} \cdot)\$ information about the dialog from **dialog** ("dLog") and                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| resources. ...... Historical Note | Using NewDialog, NewColorDialog, or **extended dialog** ("dIgx") **resources**. The resource ID of the NewFeaturesDialog, which take descriptive information passed in the "dLog" and "dIgx" resources must be the same, and is passed in the parameters of those functions. first parameter of this function. ...... ### Historical Note The extended dialog resource and the NewFeaturesDialog function The extended dialog resource and the NewFeaturesDialog function were introduced with OS 8 and the Appearance Manager. ...... were introduced with OS 8 and the Appearance Manager. ...... If NULL is specified as the second parameter in the If null is specified as the second parameter in the GetNewDialog call, GetNewDialog call, GetNewDialog itself creates a GetNewDialog itself creates a non-relocatable block for the dialog nonrelocatable block for the dialog structure. ...... structure. Regardless of which method is used to create the dialog, a dialog Regardless of which method is used to create the dialog, a **dialog structure and a window structure will be created, and a pointer to structure** and a window structure will be created, and a pointer to the dialog structure will be returned to the calling function. the dialog structure will be returned to the calling function. |
|                                   | ### The Dialog Structure .......WindowRecord window; // Dialog's // Dialog's window record. Handle items; // Item list resource. window record. Handle items; // Item list resource. TEhandle textH; TEHandle textH; // Current editable text item. // Current editable textit item. SInt16 editField; // Editable textit item SInt16 editField; // Editable text item number minus 1. number minus 1. SInt16 editOpen; // (Used internally.) SInt16 SInt16 editOpen; // (Used internally_) aberIfen; // Default push button item number.); ......The Dialog SInt16 aDefItem; // Default push button item number. Manager sets the windowKind field of this window structure to kDialogWindowKind. window structure to KDialogWindowKind.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

docstructbench\_llm-raw-the-eye-o.O-chap08.pdf\_12 Figure S12. The Good Model Result and Bad Model Result for Books.

Lessons 1~2 测试卷 时间:90 分钟 满分:100 分 \*NI 茹 出 岗 <table border=1>

<tr> <td>题号</td> <td>I</td> <td>II</td><td>III</td> <td>IV</td> <td>V</td> <td>VI</td> <td>VII</td> <td>VIII</td> <td>IX</td> <td>X</td> <td>总分</td> <td>等级</td> </tr> <tr> <td>得分</td> <td></td> <td></td> <td></td> <td></td><td></td><td></td> <td></td><td></td><td></td><td></td><td></td><td><

/td></tr></table>管

II. 听录音, 按你所听内容, 用数字" \$\mathbf{1 \sim 5 \text { "给下

列图片排序。(10 分) }}\$

![图片1](https://i.imgur.com/1.png) ![图片2](https://i.imgur.com/2.png) ![图片3](https://i.imgur.com/3.png) ![图片4](https://i.imgur.com/4.png) ![图片5](https://i.imgur.com/5.png) **Markdown Content (Mathpix)**

**---Prediction Content Error ---**

**Category and**

**Markdown Content (Qwen2-VL)**

jiaocaineedrop\_jiaocai\_needrop\_en\_922 Figure S13. The Good Model Result and Bad Model Result for Exam Papers.

**Exam Papers** 

# Lessons 1~2 测试卷 时间:90分钟 满分:100分

<table border=\"1\" >\n <tr>\n rowspan=\"1\"> ...... 总分 </td>\n <td colspan=\"1\" rowspan=\"1\">等级</td>\n

</tr>\n</table> ## 听力部分 (30 分)

### I. 听录音,选出你所听到的单词。(10 分)

1. A. must B. much C. may 2. A. put B. eat C. sit 3. A. seat B. street C. skate 4. A. line B. learn C. light 5. A. too B. into C. in

### II. 听录音,按你所听内容,用数字"1~5"给下列图片排序。(10

分)

### III. 听录音,选择正确的答语。(10 分) 1. A. Good afternoon, Mrs Read. B. Sorry, she's not in. 2. A. I'm having lunch. B. I'm in the park. 3. A. Hello, John! B. Yes. Here it is. 4. A. Yes, we can. B. You're welcome. 5. A. You can sit here. B. At the sports centre. 关注微信公众号"教辅资料站"获取更多学习资料

㚓冠新课堂 \$\cdot\$ 五年级英语(下).KP

听力部分 (30 分)

I. 听录音,选出你所听到的单词。(10 分)

多 \$=\$ 离 出 管 尖

( ) B. much B. eat B. street B. learn B. into C. may C. sit C. skate

C. light C. in

III. 听录音, 选择正确的答语。(10 分)

( )1. A. Good afternoon, Mrs Read. B. Sorry, she's not in. ( )2. A. I'm having lunch. B. I'm in the park. ( )3. A. Hello, John! B. Yes. Here it is. ( )4. A. Yes, we can. B. You're welcome. ( )5. A. You can sit here. B. At the sports centre. 关注微信占攵号"教辅资料站" 47 获取更多

**Markdown Content (MinerU) Markdown Content (GPT4o)**

docstructbench\_dianzishu\_zhongwenzaixian-o.O-61521185.pdf\_167 Figure S14. The Good Model Result and Bad Model Result for Magazines.

**Magazines**

### 制作过程

香葱切段,大葱、葱头切丝,油菜切开备用;葱油制作:锅内 放油烧至三成热,将香葱、大葱、葱头入锅小火熬制20分钟后 加酱油、水,开锅10分钟盛出;锅中煮面条的同时放一个小油 菜,煮熟后浇上葱油、撒上香葱粒即可(原料按35碗计算)。

# 第四章 主食类 ## 葱油面 ### 材料成分

- \*\*主料\*\*:香葱 500g,大葱 500g,紫葱头 500g,切面

(细)5kg;

- \*\*辅料\*\*:水 300g,油菜 500g,食用油 500g;

- \*\*调料\*\*:酱油 1kg。

### 工艺技巧

面条要细;熬油温度不宜太高。

### 品质特点 柔韧爽滑,葱香可口。 <div align="center"> <h2>葱油面</h2>

<img src="image-url" alt="葱油面图片" width="200">

</div> ### 材料成分

<table><tr><td><b>主料:</b>香葱 500g, 大葱 500g, 紫葱头 500g, 切面(细)5kg;</td><td><img src="image-url" alt="原材

料图" width="100"></td></tr> <tr>

<d><b>辅料:</b>水 300g, 油菜 500g, 食用油 500g;</td> </tr><tr><td><b>调料:</b>酱油 1kg。

</td></tr></table>

### 制作过程

香葱切段,大葱、葱头切丝,油菜切开备用;葱油制作: 锅内放 油烧至三成热,将香葱、大葱、葱头入锅小火熬制 20 分钟后加 酱油、水,开锅 10 分钟盛出;锅中煮面条的同时放一个小油菜, 煮熟后浇上葱油,撒上香葱粒即可(原料按 35 碗计算)。

### 工艺技巧

面条要细;熬油温度不宜太高。

### 品质特点 柔韧爽滑,葱香可口。 <div align="right"> <b>王广勇 提供</b> </div> <p align="center">157</p>

**--- Prediction Category Error ---**

001或85815522传真:(010)85832154广告热线:010) 84395085广告经营许可证:京朝工商广字第0055号每份:0.63元

月价:16.5元农民日报社印刷厂印

![](images/1a146a1de25d1a209982d632961f6edb85cf9e297e135ef3

491ec9f1e83c560c.jpg)

票星12009-2011年回库支持排广的农业机楼产品日票】 中营庆2006年国家科学技术进步二等奖票获2005年河南省科学 技术进步一等奖 中荣获2008年河南省科学技木进步二等奖 十国家标准(GB/T24689:1\~GB/T24689.7-2009)......

三部门再次公布举报电话严查虚假报道

据悉,各省、自治区,直辖市有关部门和单位也将陆续公市举

报电话。

**Markdown Content (MinerU) Markdown Content (Mathpix)**

newspaper\_4b4ad1f6cba28a4844d7ffa9306223a4\_1 Figure S15. The Good Model Result and Bad Model Result for Newspaper.

**Newspapers**

新华社北京12月31日电为深人推动全国新网战线开展"杜绝虚假

报道、培强社会责任 ......

国家广电总局举报电话: 010-86093956 新闻出版总署举报电话: 010-65212787 中国记协举报电话:010-58262800

新华社北京12月31日电(记老李志勇1211年北京春运期 司农民工团体订票将于1月5日开始:......

记者从北京市交通委了解到.2011年1月5日至16日.北京农民工 春运团体票预订将在北京站和北京西站办理:1月10日至22日 ,农民工可以到北京站,北京西站和北京北站开设的农民工团

体售票专口直接购买衣民工团体火车票,......

4 |时事新闻 2011年1月1日 星期六 业民日赫

河南佳多科工稀有限责任公司致以最崇高敬意,并恭祝新春愉 快!\* 葉犾2008年河南少科学技术进步二等奖\* 荣录《河南省重 点工业产品达标备案目录》政府招投标优先采购产品

**---Missing Content---**

每倣 \$: 0.63 \bar{\pi}\$

![](images/d6e62c1f3bca13d93dd62442a66a910bfb154389067c

97d348fcc16849282197.jpg)

![](images/32a06f10479ad580c8423f8f6401fb83946853181349f5

37d49fe85b3b63c3b0.jpg)

![](images/f6a43cf829ed4b946b68d16c96e865f3465ecb9e43a20

dbf165d1bdd6229e77b.jpg)

![](images/051bae4f955132e3f0a14a876fcb2349a22a4f7aa3671

5021fbed42de3e32c78.jpg)

![](images/0523e1d22f515063d46eda0cbfdd507dc4af30efdafc0

5badc26d766fad4aa6c.jpg)

![](images/657ed990bb085cb6a5b7a301b832906dfe354292132c

67a3d49a44ddafc3f56f.jpg)

![](images/9bbaed986aeeb43c298d6a713027c3f7e96e17dd93e1

abd7701fc7b74754be98.jpg)

![](images/270e71dda8feff50dbe12d4edbed260e4e09c2e47e2b

401d2d6fc3cbb4a99bee.jpg)

![](images/46a4b83145fbc5f4887bbcbd4accdaf737ae50309c723

d3b34ad9daff97d85c1.jpg)

![](images/de22f94bd80039cb06e9ab34302a5e27a8d864637c3a

f0c44f2abd3ec06bf729.jpg)

**Markdown Content (MinerU)**

**---Handle Writing Text Missing---**

**Markdown Content (InternVL2)**

notes\_1ba14cb325bc448f7201b20502ecf2b5\_52 Figure S16. The Good Model Result and Bad Model Result for Handwriting Notes.

<span id="page-22-0"></span>**Notes**

```markdown NO. \_\_\_\_\_\_\_\_\_ Date \_\_\_\_\_\_\_\_\_\_

1992年6月,《21世纪议程》破坏环境→可持续发展

4. 城市化问题 (1) 人口和城市的分布

① 特点:人口分布极不平衡,90%的人口居住在东部沿海地带,

而且大城市占十分之七。

② 带来许多"城市病":交通拥堵、住房困难、就业紧张、污染

严重、犯罪增多。

③ 解决措施:进行合理的城市规划,建立卫星城;城市中工业 和人口向郊区分散;加强城市管理,重视保护和治理城市环境。

(2) 主要城市:

圣保罗:经济中心、最大的城市和工业中心。 里约热内卢:商业和金融中心、第二大城市。 巴西利亚:政治中心、首都,是新建城市。

```

![](_page_23_Figure_0.jpeg)

eastmoney\_66eea274d39b939da0f10253d279e119d87646f Figure S17. The Good Model Result and Bad Model Result for Financial Reports.

3.---Does he speak Chinese or English ?

A.Yes , he does B.No, he doesn't C.None D.Neither , he speaks Japanese

**Slides**

示例讲解(3)

**Markdown Content (MinerU) Markdown Content (Marker)**

合作探究 AAAAA

# 0

![0\_image\_0.png](0\_image\_0.png)

**--------Missing Text Content------** 

![0\_image\_1.png](0\_image\_1.png) ![0\_image\_2.png](0\_image\_2.png) ![0\_image\_0.png](0\_image\_0.png)

**--------Missing Text Content------** 

改对,包括对文章段落的进一步调整和加工。段落安排是否 合理,段与段之间是否衔接,详略安排是否恰当等等,都是

修改是应该重点关注的。

![](images/eb64e4894e8beea67242ef779bea7b3900447c5a59ca1

cf2aed3f22b7578412d.jpg)

示例讲解 (3)

# 【答案】

【解析】这是选择疑问句两选一,或两都不选,C是 三都以

上都不,不合题意。

yanbaopptmerge\_yanbaoPPT\_6070 Figure S18. The Good Model Result and Bad Model Result for Slides.

合作探究

<span id="page-24-0"></span>

|                                     |                   |                      |          |   |  | 法确定。例如，问题 1 中“抽到的数字是 1 ”，问题 2 中“出现的点   |
|-------------------------------------|-------------------|----------------------|----------|---|--|----------------------------------------|
|                                     |                   |                      |          |   |  | 数是 4 ”，                                |
| 在一定条件下，有些事件必然会发生，例如，问题              |                   | 1 中                  | “ 抽到的数   |   |  |                                        |
| 字小于 6” ，问题 2 中 “ 出现的点数大于 \$D^{+}\$  |                   |                      | 这样的事件称为必 |   |  |                                        |
| 然事件相反地：有些事件必然不会发生，例如，问题             |                   | 1                    | 中 “ 抽到的  |   |  |                                        |
| 数字是 \$n^{5+}\$ 问题 2 中 “ 出现的点数是      |                   | \$T^{\ast}\$ ....... |          |   |  |                                        |
| Markdown Content (MinerU)           |                   |                      |          |   |  | Markdown Content (Qwen2-VL)            |
| （ 1 ）从 1 到 6 的每一个点数都有可能出现，所有可能的点数共有 |                   |                      |          | 6 |  |                                        |
| 种，但是事先无法预料掷一次骰子会出现哪一种结果；（           |                   |                      | 2 ）出     |   |  |                                        |
| 现的点数肯定大于 0 ；（ 3 ）出现的点数绝对不会是         |                   | 7 ；（                 | 4 ）出现    |   |  |                                        |
| 的点数可能是 4 ，也可能不是 4 ，事先无法确定           |                   |                      |          |   |  |                                        |
| 法确定例如，问题 1 中“抽到的数字是                 | \$1^{\ast}\$      | ，问题                  | 2 中“出现   |   |  |                                        |
| 的点数是 4 ”                            |                   |                      |          |   |  |                                        |
| 是随机事件（ 1 ）通常加热到 100C                | 时，水沸腾；（           | 2                    | ）蓝球队员    |   |  |                                        |
|                                     |                   |                      |          |   |  | （ 1 ）从 1 到 6 的每一个点数都有可能出现，所有可能的点数共     |
|                                     |                   |                      |          |   |  | 有 6 种，但是事先无法预料掷一次骰子会出现哪一种结果；           |
|                                     |                   |                      |          |   |  | （ 2 ）出现的点数肯定大于 0 ；（ 3 ）出现的点数绝对不会是 7 ；  |
|                                     |                   |                      |          |   |  | （ 4 ）出现的点数可能是 4 ，也可能不是 4 ，事先无法确定。      |
| 问题 3 袋子中装有 4 个黑球， 2                 | 个白球，这些球的形状、大小、    |                      |          |   |  |                                        |
| 质地等完全相同，                            | 如果两种球都有可能被摸出，那么摸出 |                      |          |   |  |                                        |
|                                     |                   |                      |          |   |  | 在一定条件下，有些事件必然会发生。例如，问题 1 中 “ 抽到的       |
|                                     |                   |                      |          |   |  | 数字小于 6” ，问题 2 中 “ 出现的点数大于 0” ，这样的事件称为必 |
|                                     |                   |                      |          |   |  | 然事件。相反地，有些事件必然不会发生。例如，问题 1 中 “ 抽       |
|                                     |                   |                      |          |   |  | 到的数字是 0” ，问题 2 中 “ 出现的点数是 7”           |

jiaocaineedrop\_jiaocai\_needrop\_en\_1719 Figure S19. The Good Model Result and Bad Model Result for Textbooks.

<span id="page-24-1"></span>

| Fuzzy Scan                      |                                                                                                                                                 |                                    |                                                                                                                            |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|                                 | \$a_{1}\$ \$=1, q=2, n=64\$,                                                                                                                    | 可得                                 |                                                                                                                            |
| \$2^{64}-1\$                    | 这个数很大，超过了                                                                                                                                       |                                    | \$1.84 \times 10^{19}\$ 。假                                                                                                 |
|                                 | 定千粒麦子的质量为                                                                                                                                       | 40 g ，那么麦粒的总质量超过了                  | 7000                                                                                                                       |
| 因为                              | \$a_{m}=a_{1} q^{n-1}\$,                                                                                                                        |                                    | 所以上面的公式还可以写成                                                                                                               |
| 例 1                             | 求下列等比数列前                                                                                                                                        | 8 项的和：                             |                                                                                                                            |
|                                 |                                                                                                                                                 | Markdown Content (MinerU)          | Markdown Content (Marker)                                                                                                  |
| 第二章 第二章                         | 数列                                                                                                                                              | --------Missing Paragraphs------   | ![0_image_0.png](0_image_0.png) --------Missing Paragraphs------                                                           |
| 解 : （ 1                         | ）因为                                                                                                                                             | \$a_{1}=1, q=\frac{1}{2}\$,        | 所以当 \$n=8\$ 时 ,                                                                                                            |
| (2) 由                           |                                                                                                                                                 | \$a_{1}=27, a_{9}=\frac{1}{243}\$, | 可得                                                                                                                         |
| 又由                              | \$q<0\$, 可得                                                                                                                                     |                                    |                                                                                                                            |
| 于是当                             | \$n=8\$ 时 ,                                                                                                                                     |                                    |                                                                                                                            |
|                                 |                                                                                                                                                 |                                    | 求下列等比数列前 8 项的和 : 例 1 (1) - (2) a1=27, as=243.                                                                              |
|                                 |                                                                                                                                                 |                                    | q<0. 解 :(1) 因为 a1=1.=q=, 所以当 n=8 时 , 11-  حت 255 S 256"                                                                    |
|                                 |                                                                                                                                                 |                                    | ও। (2) 由 a =27, a = 243 · 可得 243=27 * 9 .                                                                                  |
|                                 |                                                                                                                                                 |                                    | 于是当 n=8 时 ,                                                                                                                |
|                                 |                                                                                                                                                 |                                    | 1-q 有了上述公式 , 就可以解决本节开头提出的问题 由 a1                                                                                           |
|                                 |                                                                                                                                                 |                                    | =1,g=2,m=64, 可得                                                                                                            |
|                                 |                                                                                                                                                 |                                    | s, l-q 1 × (1-26) 1-2                                                                                                      |
|                                 |                                                                                                                                                 |                                    | 2%-1 这个数很大 , 超过了 1.84 × 10%. 假定手粒麦子 的质量为                                                                                   |
|                                 |                                                                                                                                                 |                                    | 40g, 那么麦粒的总质量超过了 7000 亿吨 , 因此 , 国王不能实现                                                                                     |
| & =2^{64}-1 . \end{aligned}\$\$ | \$\$\begin{aligned} 亿吨，因此，国王不能实现他的诺言。 (2) \$a_{1}=27, a_{9}=\frac{1}{243}, q<0\$. \$\$\frac{1}{243}=27 \cdot q^{8}\$\$ \$\$q=-\frac{1}{3} .\$\$ |                                    | 因为 an=aiq"], 所以上面的公式还可以写成 S = at add (g = 1). =26 =1. 他的诺言。 4= ـــ {array}\$ ![0_image_1.png](0_image_1.png) 1993 163 1990 |

fuzzy\_scan: jiaocaineedrop\_jiaocai\_needrop\_en\_913 Figure S20. The Good Model Result and Bad Model Result for Fuzzy Scan Pages.

| | TIT 主

--------------------------------|-------------------------------------------|-

| | 増大

| | -、新修订的体育法贯彻 落实"健康第一"的教│ | A. 提高 | and the state of the states of the states of the states of the states of the states of the states of the states of the states of the states of the

state of the state of the ...s | | | | 香蕉 | 改良 |

【倡议体育活动】 # 倡议书 全体同学:

为响应我校"知体育健体魄强精神"主题活动,提高学生的身

体素质,锻炼体能,特提出以下倡议:

\$\textcircled{1}\$ 充分利用学校健身场地,积极参加课内外

体育锻炼,如踢足球、跳绳等。

\$\circled{2}\$ 每天坚持跑步运动,完成以班级为单位的集体

跑步任务。 雏燕展翅竞飞跃同学们, ...

2.请根据上面的材料,完成下列题目。(4分)(1)针对倡议书 中的上联"雏燕展翅竞飞跃",与它对仗可作下联的一项是(2分

)....

# 【理解体育内涵】

1.小萌欲通过阅读下列语段来加深对体育内涵的理解,但遇

到了一些小问题,请你帮她解决。(6分)

体育,是一种以身体与智力活动为基本手段,根据人体生长

发育、技能形成和机能提高等规律...

(2)给语段拼音后的括号内填人汉字,全都 正确的一项是(2

分)

A.衡育 B.恒寓 C.恒育 D.衡寓 (3)依次填人上面语段横线上的

词语,正确的一项是(2分)

A.提高 增大 改善 B.提升增强改良C.提高 增强 改善 D.提升

增大改良

一、新修订的体育法贯彻落实"健康第一"的教育理念,为深 化具有中国特色的体教融合发展,推动青少年文化学习和体

育锻炼协调发展...

**Markdown Content (Mathpix) Markdown Content (Marker)**

watermark: jiaocaineedrop\_jiaocai\_needrop\_en\_237 Figure S21. The Good Model Result and Bad Model Result for Pages with Watermark.

# 1.情境基础小练

时间:30分钟满分:20分班级:姓名:得分:

| | 周测小卷 | | |------------|-------------------------|------| | 、与新考法 | 1. 情境基础小练 | | | | 时间:30 分钟 满分:20 分 | 得分 | | | 姓名 | | | | 班级: | |

**--------Missing Paragraphs------**  | | 关注微信公众号"初高教 辅站"获取更多初高中教辅资料 | | **--------Wrong Orders------** 

<span id="page-25-0"></span>**Watermark**

\section\*{PCB——全球产值}

**Markdown Content (Mathpix) Markdown Content (GOT)**

colorful\_background: eastmoney\_d09a006aa02ddc09299bbb9a1b5efa0d77408191f0c1ff1fca8c8 Figure S22. The Good Model Result and Bad Model Result for Colorful Background Pages.

PCB——全球产值 全球PCB产值规模(亿美元) 表: 全球各类PCB市场规模预估(亿美元)

\begin{tabular}{|c|c|c|c|c|}

\hline & RPCB多层板 & 软板+模组 & HDI & IC载板 \\ \hline 2022(E) & 387.21 & 138.42 & 117.63 & 174.15 \\ \hline 2023(F) & 373.40 & 134.27 & 115.28 & 160.73 \\ \hline 2024(F) & 381.79 & 141.31 & 122.25 & 174.41 \\ \hline 2025(F) & 419.39 & 148.72 & 129.65 & 189.26 \\ \hline 2026(F) & 444.30 & 156.52 & 137.49 & 205.38 \\ \hline 2027 (F) & 450.48 & 164.73 & 145.81 & 222.86 \\ \hline \begin{tabular}{c}\$2022-2027\$ \\CAGR \end{tabular} & \$3.1 \%\$ & \$3.5 \%\$ & \$4.4 \%\$ & \$5.1 \%\$ \\

\hline \end{tabular} ...

<|im\_end|>};

**--------Missing Tables------**  资料来源: Prismark, 前瞻产业研究院, PCB网城ISPCAGPCA 公众号, 中时新闻网, 诚领智慧助您成功公众号, 天风证券研

究所

**--------Missing Content------** 

Are you looking for more great free books like this one?

FREE KIDS BOOKS https://www.freekidsbooks.org

Preschool, early grades, picture books, learning to read, early

chapter books, middle grade, young adult Always Free - Always will be!

This book was shared online by Free Kids Books at https://www.freekidsbooks.org in terms of the creative commons

license provided by the publisher or author. This page is added for identification purposes

<span id="page-25-1"></span>**Colorful Background**

**Markdown Content (InternVL2) Markdown Content (MinerU)**

1 **--------Only Contain Images-------** 

notes\_1ba14cb325bc448f7201b20502ecf2b5\_103.jpg Figure S23. The Good Model Result and Bad Model Result for Single Column Pages.

4. 西南地区地质灾害严重

形成原因:

(1)自然原因:山区面积广大,岩石破碎,风化平量;干旱季分明...

(2)人为原因:对植被的破坏 治理措施:恢复植被 三、农业区位分析 1. 农业区位分析

典型地区:宁夏平原、河套平原、河西走廊、南疆等 分析自然区位因素:热量充足,温差大,地形平坦;土壤肥沃;灌溉水

源充足

不足:水资源短缺;冬季受寒潮和暴风雪影响;土壤的盐碱化等

2. 商品谷物农业 典型地区:东北地区 分析区位因素:

(1)自然因素:温带季风气候,夏季高温多雨,雨热同期… (2)社会经济因素:地广人稀,农产品商品率高,生产规模大… 不足:热量不足;土地沙化;水土流失加剧;工矿用地下降;冬季…

与美国商品谷物农业比较:

相同点:农业地域类型相同;地广人稀,农产品商品率高;生产…

98

12 13

<span id="page-26-0"></span>1

13

![](images/03eb2611c2c87491f3533c3eb2611c2c87491f3533c.jpg) ![](images/7e61756b6fe98212c2d4e53eb2611c2c87491f3533c.jpg) ![](images/ed94aa7f621bbd9db74c0c3eb2611c2c87491f3533c.jpg) ![](images/5ff0ae8dee57236126fa64d3eb2611c2c87491f3533c.jpg) ![](images/e73d9b6e0eb70b6c3efae23eb2611c2c87491f3533c.jpg)

# 三农业区位会析

![](images/af8604662daf442866d37ac3eb2611c2c87491f3533c.jpg) ![](images/187c0bd45ca5d58ccb3a8ff23eb2611c2c87491f3533c.jpg) ![](images/0c5235975494b6803dc09f4f3eb2611c2c87491f3533c.jpg) ![](images/4bf1fa83763619b675295da13eb2611c2c87491f3533c.jpg) ![](images/b7e3b4acaac179f365021e1c3eb2611c2c87491f3533c.jpg) ![](images/e7159c72a508bd1594fe4db33eb2611c2c87491f3533c.jpg) ![](images/734ed147410129c5f2ee3c7103eb2611c2c87491f3533c.jpg) ![](images/41cbd7b2331e8ea755919ddbf3eb2611c2c87491f3533c.jpg) ![](images/444c235d15727b6e23b29ca123eb2611c2c87491f3533c.jpg) ![](images/19a81928e1a650ba2fcac17ad33eb2611c2c87491f3533c.jpg) ![](images/7edfb821864233a0042f81b3c1d63eb2611c2c8741f353c.jpg)

**Single Column**

|                        | # Bull Environ Contam Toxicol (2007) 78:304-307   |   |
|------------------------|---------------------------------------------------|---|
|                        | duplicated samples and the difference was always… | 5 |
| Markdown Content (GOT) | Markdown Content (InternVL2)                      |   |

docstructbench\_llm-raw-scihub-o.O-s00128-007-9171-1.pdf\_2 Figure S24. The Good Model Result and Bad Model Result for Double Column Pages.

1 2

3

4 5

Based on our review of the best available scientific and commercial information pertaining…

As a result of the Service's 2011 multistate litigation settlement with the Center for Biological Diversity and WildEarth…

2

\section\*{Arkansas Darter (Etheostoma cragini)}

The Arkansas darter was first identified as a candidate for listing under the Act in 1989 (54 FR 554; January 6, 1989)… On March 11, 2004, the Service received a petition dated May 4, 2004, from the Center for Biological Diversity…

\section\*{Background}

The Arkansas darter (Etheostoma cragini) is a small fish in the

perch family native to the Arkansas…

The Arkansas darter's range includes eastern Oklahoma,

southwest and central

\section\*{Summary of Status Review}

In completing our status review for the Arkansas darter, we

reviewed the best available scientific….

3 4 5

1&2 4|3 5&6 4|&7&8

> 9|10 12|11

14-half

15

**Markdown Content (Qwen2-VL) Markdown Content (InterVL2)**

\section\*{Previous Federal Actions}

Water depletion is the stressor with the largest potential impact

to the Arkansas darter's..

12

Water depletion results in decreased resiliency of populations

affected in the portions of the range..

13&14

6

7

8

9

10

11 12

13

14 15

16

17

15 16 |69428|Federal Register / Vol. 81, No. 194/Thursday, October 6, 2016/Rules

and Regulations|

|Finding|Based on our review of the best available ...|

|Arkansas Darter (Etheostoma cragini)|As a result of the Service's 2011 multi-

listing settlement with the Center for Biological...|

|Previous Federal Actions|The Arkansas darter was first identified as a candidate species for listing under the Act in 1989. …. In 2002, we| |Arkansas Darter (Etheostoma cragini)|changed the LPN from 5 to 11 (67 FR

40657), June 13, 2002). On May 11, 2004,...|

|Background|The Arkansas darter (Etheostoma cragini) is a small fish in the perch family (Percidae) native ...southwest Missouri, and southeast Colorado.| |Status Review|The Arkansas darter is currently considered to be extant a total

of 80 populations ...|

|In completing our status review for the Arkansas darter, we reviewed the best

available …|

|development, confined-animal feeding operations, dams and reservoirs, salt

cedar invasion, disease, and predation.|

|Although localized, negative effects have been observed at all of these stressors (other than …and species level is minimal.|

|Water depletion is the stressor with the … decreased water availability in the

Arkansas darter's range.|

|Water depletion results in decreased reservoirs …the species has endured over 40 years of groundwater withdrawals in these areas.| |indicating continued resilience of the ... Over the next 30 years, under our

expected scenario, we are likely to see|

13 14-half

16-half 16-half&17

newspaper\_2a6b4fa088699701a6fa9ccecfb5c25d\_4 Figure S25. The Good Model Result and Bad Model Result for Three Column Pages.

**Three Column**

<span id="page-27-0"></span>![](_page_27_Figure_1.jpeg)

Figure S26. The Good Model Result and Bad Model Result for Complex Layout Pages.

| # 办公                         |                                      |
|------------------------------|--------------------------------------|
| 了市场对优质资产的需求。例如，从 2023 年（荷兰）和 | 2030 年                               |
| （英国）起，办公楼必须拥有能源绩效证书（ EPC ）   | C 级或以上。                              |
|                              | ## 办公                                |
|                              | 市场对优质资产的需求。例如，从 2023 年（荷兰）和 2030 年（  |
|                              | 英国）的起，办公建筑必须达到 A 级或 B 级能效认证。 EPIC （英 |
|                              | 国）和 Sofidy （法国）等公司致力于实现去碳化，提出明确的净    |
| Markdown Content (MinerU)    | Markdown Content (InternVL2)         |

yanbaor2\_965b491c51a8fcd511bcb12adcebca5836ab96fe Figure S27. The Good Model Result and Bad Model Result for Text Language in Chinese.

docstructbench\_llm-raw-scihub-o.O-bf00326833 Figure S28. The Good Model Result and Bad Model Result for Text Language in English.

docstructbench\_llm-raw-scihub-o.O-bf00326833 Figure S29. The Good Model Result and Bad Model Result for Text with Colorful Background.

<span id="page-29-1"></span>

|                          |                           | Markdown Content (Qwen2-VL) |                                                |
|--------------------------|---------------------------|-----------------------------|------------------------------------------------|
| Multi-Colored Background | 当堂练习：                     |                             | Markdown Content (Marker) 当堂练习：                |
| 2                        | 、人和其它动植物的呼吸以及燃料的燃烧要消耗大量的（ |                             | B ）                                            |
| A.                       | 氮气 B. 氧气 C. 二氧化碳          | D. 稀有气体                     |                                                |
| 3                        | 、空气中能使澄清石灰水变浑浊的气体是（       | C ）                         |                                                |
| A.                       | 氮气 B. 氧气 C. 二氧化碳          | D. 稀有气体                     |                                                |
|                          |                           |                             | 1 、空气的成份按体积计算 , 下列结论不正确的是 C                    |
|                          |                           |                             | A. 氮气占 78% B. 其它气体和杂质约占 0.03%                  |
|                          |                           |                             | C. 二氧化碳占 0.94% D. 氧气占 21%                      |
| 1                        | 、空气的成份按体积计算，下列结论不正确的是（    | C                           | ）                                              |
| A.                       | 氮气占 78% B. 其它气体和杂质约占      | 0.03%                       |                                                |
| C.                       | 二氧化碳占 0.94% D. 氧气占        | 21%                         |                                                |
|                          |                           |                             | 2 、人和其它动植物的呼吸以及燃料的燃烧要消耗 大量的 ( B. 氧气 C. 二氧化碳 A. |
|                          |                           |                             | 氮气 D . 稀有气体 Missing option 3                   |

yanbaopptmerge\_yanbaoPPT\_4570 Figure S30. The Bad Model Result for Text with Rotation.

<span id="page-29-0"></span>

| Rotate270 | Markdown Content (Qwen2 Markdown Content (Mathpix)     |
|-----------|--------------------------------------------------------|
| ##        | 作品简介                                                   |
| ##        | 作者简介                                                   |
| 陈忠实，      | 1939 年出生于陕西省西安市，中国当代著名作家。他的作品以描写农村生活和人物命运为主，具有深刻的社会意义和 |
| ##        | 主要作品                                                   |
| ##        | 作品风格                                                   |
| ##        | 评价与影响                                                  |
| ##        | 个人荣誉                                                   |
| ##        | 读者评价                                                   |
| ##        | 书籍信息                                                   |
| **        | 出版社 ** : 中国作家出版社                                       |
| **        | 出版时间 ** : 2022 年                                       |
| **ISBN**  | : 978-7-5063-xxxx-x                                    |
| **        | 页数 ** : 320 页                                          |
| **        | 定价 ** : 39.8 元                                         |
| ##        | 购买链接                                                   |
| [ 点击购买    | ](http://example.com)                                  |
| ##        | 读者评论                                                   |
| >         | “陈忠实的作品让我看到了一个真实的中国，感受到了人性的光辉和黑暗。”                     |
| >         | —— 小明                                                  |
| >         | “他的小说不仅仅是故事，更是对社会和人性的深刻剖析。”                            |
| >         | —— 小红                                                  |
| >         | “每读一本陈忠实的作品，都会有不同的感悟和收获。”                              |
| >         | —— 小李                                                  |
|           | 言 , 以文为㻍。                                              |
|           | 桴 , 皆志于比卷。                                             |
|           | 诶史也 " 铬卷首，用㥯深丐。 \( \square \)                          |
| #         | 陈忠实                                                    |

<span id="page-30-0"></span>

|  | 企业类型     | 目的                                                  | 模式和特点                                            | 优势                                                                          | 典型企业                                                |
|--|----------|-----------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------|
|  | 云服务提供商   | <ul><li>以物联网为抓手带动上层应用服务业绩增长</li></ul>               | <ul><li>目前多以提供底层计算资源、提供应用使能平台为主</li></ul>        | <ul><li>在互联网领域中积累了丰富的技术、商业、生态优势经验</li> <li>底层IaaS能力突出、共性技术能力提炼</li></ul>    | 阿里云、腾讯云、百度云、亚马逊AWS IoT等                             |
|  | 通信领域厂商   | <ul><li>获得流量业务收入，战略布局物联网、把握新增市场机遇</li></ul>         | <ul><li>多以连接管理、应用使能为平台主要功能服务为主</li></ul>         | <ul><li>在连接管理平台具有绝对优势，具有全球通用连接能力</li></ul>                                  | 电信迅营商、通信设备厂商、中国电信天翼物联、如中国移动ONENet、中国联通物联网平台、华为云IoT等 |
|  | 软件系统服务商  | <ul><li>解决内部开发效率的问题，优化产品服务</li></ul>                | <ul><li>以应用开发平台为主要服务内容为主</li></ul>               | <ul><li>擅长软件设计、生产、管理、运维等服务，具备丰富的行业软件开发及服务经验</li></ul>                       | 紫光云、广联达筑联等                                          |
|  | 垂直领域传统厂商 | <ul><li>利用自身对行业的理解与经验、打造垂直型平台，实现传统企业的转型升级</li></ul> | <ul><li>垂直专业领域的物联网平台</li></ul>                   | <ul><li>深刻的行业理解和行业技术、对行业有深度应用，拥有行业数据和客户资源</li></ul>                         | 西门子、工业富联、美的M-Smart等企业                               |
|  | 初创企业     | <ul><li>看好物联网未来的发展潜能</li></ul>                      | <ul><li>目前阶段很多初创型平台企业多以SaaS解决方案公司的形式存在</li></ul> | <ul><li>拥有与选定细分行业相关的软件、硬件经验</li> <li>服务延伸到通用型平台厂商难以触及的细分领域，形成错位竞争</li></ul> | 涂鸦智能、云智易、机智云、艾拉物联等                                  |

**Three Line Table**

| Good Model Result (RapidTable) |  |                                    |  |                                    |                                      |                                                  |                                                   | Bad Model Result (PaddleOCR)                                             |            |                                                   |    | 企业类型 |  | 目的 |  | 模式和特点 | 优势 | 企业类型 |  | 目的 |  | 模式和特点 | 优势 | 云服务组 |  | 应用应用务绩绩等 |  | 以物理为抓手电动上——目的多以模式实施计算能力 | 无线网、高速、生态优势的结合 —— IoSEK型的出现、共计技术和互联式 | 阿里亚、腾讯、百度云、亚运云 Websrver |  | 在互联网领域中靠重力的丰富、商业、生态优势经验、度层IoS能力突出、共性技术能力提高 |  | 阿里亚、腾讯、百度云、亚马逊 AWSrver | 通信类型 |  | 获得通信业务收入、战略与目的、优化产品服务 |  | 多以通信管理、应用使用为主 主要功能服务为主 | 在线管理中必自我有利的经验、具有通信通用技能力 | 电信管理、通信设备厂商、中国电信天援助、如中国移动 ONENe、中国通信物理平台、华为云rver |  | 多以通信管理、应用使能力 平台主动功能服务为主 |  | 电信运营商、通信设备厂商、中国电信天援助、如中国移动 ONENe、中国通信物理平台、华为云rver | 软件系统服务 |  | 解决部分行业效率的问题、优化产品服务 |  | 提长软件设计、生产、管理、通用服务、具体产量的行业软件开发及服务经验 | 开发光、广泛站筑联等 |  | 提长软件设计、生产、管理、通信等服务 具备丰富的行业软件开发及服务经验（以应用开发为台主力服务服） |  | 开发光、广泛站筑联等 |  | 事故类型 |  | 利用自身对行业的理解与经验，打击事量型平台、实现新创业企业的 型环境 |  | 事量型平台的物理平台开发 | 实际的行业理解和行业技术、对行业有深层用、拥有行业数据和产品资源 | 西门子、工业重新、美M-Smart等企业 |  | 实际的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台 |  | 西门子、工业重新、美M-Smart等企业 |  | 初创企业 |  | 自我物理和未来的发展 理论 企业多Soas解决方案企业 |  | 目前阶段多设创型空间企业多Soas解决方案企业 | 目前阶段多设创型空间企业多Soas解决方案企业 | 未来的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台 |  | 拥有互透定细分行业相关的软件、硬件经验 服务延伸到通用型平台厂商难以触及的细分领域，将成信型平台 目前阶段多设创型空间企业多Soas解决方案企业 |  | 未来的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台 |  |
|--------------------------------|--|------------------------------------|--|------------------------------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|--------------------------------------------------------------------------|------------|---------------------------------------------------|----|------|--|----|--|-------|----|------|--|----|--|-------|----|------|--|----------|--|-------------------------|--------------------------------------|-------------------------|--|--------------------------------------------|--|------------------------|------|--|-----------------------|--|------------------------|-------------------------|--------------------------------------------------|--|-------------------------|--|---------------------------------------------------|--------|--|--------------------|--|------------------------------------|------------|--|---------------------------------------------------|--|------------|--|------|--|------------------------------------|--|--------------|----------------------------------|----------------------|--|-----------------------------------------------|--|----------------------|--|------|--|-----------------------------|--|-------------------------|-------------------------|-----------------------------------------------|--|--------------------------------------------------------------------------|--|-----------------------------------------------|--|
| Good Model Result (RapidTable) |  |                                    |  |                                    |                                      |                                                  |                                                   | Bad Model Result (PaddleOCR)                                             |            |                                                   |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 企业类型                           |  | 目的                                 |  | 模式和特点                              | 优势                                   | 企业类型                                             |                                                   | 目的                                                                       |            | 模式和特点                                             | 优势 |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 云服务组                           |  | 应用应用务绩绩等                           |  | 以物理为抓手电动上——目的多以模式实施计算能力            | 无线网、高速、生态优势的结合 —— IoSEK型的出现、共计技术和互联式 | 阿里亚、腾讯、百度云、亚运云 Websrver                          |                                                   | 在互联网领域中靠重力的丰富、商业、生态优势经验、度层IoS能力突出、共性技术能力提高                               |            | 阿里亚、腾讯、百度云、亚马逊 AWSrver                            |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 通信类型                           |  | 获得通信业务收入、战略与目的、优化产品服务              |  | 多以通信管理、应用使用为主 主要功能服务为主             | 在线管理中必自我有利的经验、具有通信通用技能力              | 电信管理、通信设备厂商、中国电信天援助、如中国移动 ONENe、中国通信物理平台、华为云rver |                                                   | 多以通信管理、应用使能力 平台主动功能服务为主                                                  |            | 电信运营商、通信设备厂商、中国电信天援助、如中国移动 ONENe、中国通信物理平台、华为云rver |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 软件系统服务                         |  | 解决部分行业效率的问题、优化产品服务                 |  | 提长软件设计、生产、管理、通用服务、具体产量的行业软件开发及服务经验 | 开发光、广泛站筑联等                           |                                                  | 提长软件设计、生产、管理、通信等服务 具备丰富的行业软件开发及服务经验（以应用开发为台主力服务服） |                                                                          | 开发光、广泛站筑联等 |                                                   |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 事故类型                           |  | 利用自身对行业的理解与经验，打击事量型平台、实现新创业企业的 型环境 |  | 事量型平台的物理平台开发                       | 实际的行业理解和行业技术、对行业有深层用、拥有行业数据和产品资源     | 西门子、工业重新、美M-Smart等企业                             |                                                   | 实际的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台                            |            | 西门子、工业重新、美M-Smart等企业                              |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |
| 初创企业                           |  | 自我物理和未来的发展 理论 企业多Soas解决方案企业        |  | 目前阶段多设创型空间企业多Soas解决方案企业            | 目前阶段多设创型空间企业多Soas解决方案企业              | 未来的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台    |                                                   | 拥有互透定细分行业相关的软件、硬件经验 服务延伸到通用型平台厂商难以触及的细分领域，将成信型平台 目前阶段多设创型空间企业多Soas解决方案企业 |            | 未来的行业理解和行业技术、对行业有深 层应用、拥有行业数据和资源 重要性专业物理物理网平台     |    |      |  |    |  |       |    |      |  |    |  |       |    |      |  |          |  |                         |                                      |                         |  |                                            |  |                        |      |  |                       |  |                        |                         |                                                  |  |                         |  |                                                   |        |  |                    |  |                                    |            |  |                                                   |  |            |  |      |  |                                    |  |              |                                  |                      |  |                                               |  |                      |  |      |  |                             |  |                         |                         |                                               |  |                                                                          |  |                                               |  |

Figure S31. The Good Model Result and Bad Model Result for Three Line Frame Table.

**Table No Frame**

|     |        | AXIAL TILT | TEMP MINUS | NIGHTTIME | ORBIT ECC | LOWEST TEMP FOR HEX ROW |
|-----|--------|------------|------------|-----------|-----------|-------------------------|
| HEX | WINTER | AXIAL TILT | IN WINTER  | MINUS     | MINUS     | HEX ROW                 |
| 1   | -45    | 0.5        | -23        | 101       | 0.0       | -113                    |
| 2   | -45    | 0.75       | -34        | 101       | 0.0       | -139                    |
| 3   | -45    | 1          | -45        | 101       | 0.0       | -147                    |
| 4   | -45    | 1          | -45        | 101       | 0.0       | -153                    |
| 5   | -45    | 1          | -45        | 101       | 0.0       | -159                    |
| 6   | -45    | 1          | -45        | 101       | 0.0       | -165                    |
| 7   | -45    | 1          | -45        | 101       | 0.0       | -171                    |
| 8   | -45    | 1          | -45        | 101       | 0.0       | -177                    |
| 9   | -45    | 1          | -45        | 101       | 0.0       | -183                    |
| 10  | -45    | 1          | -45        | 101       | 0.0       | -189                    |
| 11  | -45    | 1          | -45        | 101       | 0.0       | -195                    |

#### **Good Model Result (PaddleOCR) Bad Model Result (Qwen2VL-7B)**

| HEX | WINTER | AXIAL | TILT | TEMP   | LOWEST    |
|-----|--------|-------|------|--------|-----------|
| ROW | MINUS  | ACTAL | TILT | WINTER | NIGHTTIME |
|     |        |       |      |        | ORBIT EC  |
| 1   | -45    | 0.5   | -23  | 101    | TEMP FOR  |
| 2   | -45    | 0.75  | -34  | 101    | -113      |
| 3   | -45    | 1     | -45  | 101    | -130      |
| 4   | -45    | 1     | -45  | 101    | -147      |
| 5   | -45    | 1     | -45  | 101    | -153      |
| 6   | -45    | 1     | -45  | 101    | -159      |
| 7   | -45    | 1     | -45  | 101    | -165      |
| 8   | -45    | 1     | -45  | 101    | -171      |
| 9   | -45    | 1     | -45  | 101    | -177      |
| 10  | -45    | 1     | -45  | 101    | -183      |
| 11  | -45    | 1     | -45  | 101    | -189      |

|     |        | AXIAL TILT | TEMP MINUS | NINHTIME | ORBIT ECC | TEMPO HE |
|-----|--------|------------|------------|----------|-----------|----------|
| HE. | WINTER | AXIAL TILT | TEMP MINUS | NINHTIME | ORBIT ECC | TEMPO HE |
| ROW | MINUS  | FACTOR     | IN WINTER  | MINUS    | MINUS     | HEX ROW  |
| 1   | -45    | 0.5        | -23        | 101      | 0.0       | -113     |
|     | -45    | 0.75       | -45        | 101      | 0.0       | -130     |
| 3   | -45    |            | -45        |          |           | -147     |
| 4   | -45    | 1          | -45        |          |           | -153     |
| 5   | -45    | 1          | -45        | 101      | 0.0       | -159     |
|     | -45    | 1          | -45        | 101      | 0.0       | -165     |
| 7   | -45    |            | -45        |          |           | -171     |
| 8   | -45    | 1          | -45        | 101      | 0.0       | -177     |
| 9   | -45    | 1          | -45        | 101      | 0.0       | -183     |
|     | -45    | 1          | -45        | 101      | 0.0       | -189     |
| 11  | -45    | 1          | -45        | 101      | 0.0       | -195     |

Figure S32. The Good Model Result and Bad Model Result for No Frame Table.

| Table 1. Anticonvulsant activity and protective index of intraperitoneal AEDs in mice |                  | Good Model Result (StuctEqTable) |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|---------------------------------------------------------------------------------------|------------------|----------------------------------|---------------------------|--------------------|---------------------------|--------------------|---------------------------|--------------------|---------------------------|------------------|---------------------------|--|
| AD TD <sub>50</sub> (95% CI)                                                          | Rotored star     | TD <sub>50</sub> (95% CI)        | MES test                  |                    | Penylententrazol          |                    | Bicucline                 |                    | Strychinine               |                  |                           |  |
|                                                                                       |                  |                                  | ED <sub>50</sub> (95% CI) | mg/kg              | ED <sub>50</sub> (95% CI) | mg/kg              | ED <sub>50</sub> (95% CI) | mg/kg              | ED <sub>50</sub> (95% CI) | mg/kg            | ED <sub>50</sub> (95% CI) |  |
| Maximum protection, 50/% AED                                                          | AD               | <200 (100)                       |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|                                                                                       | Animals          | 15.5 (12.4-18.1)                 | > 323                     | 54.0 (9.0-14.9)    | > 9.3                     | 58.0 (10.4-8.7)    | > 9.9                     | 74.1 (6.4-9.2)     | > 5.4                     | 15.8 (4.7-11.8)  |                           |  |
|                                                                                       | Peripron         | 9.5 (8.1-10.4)                   | 6.9                       | 30.0 no protection | <0.2                      | 10.0 no protection | <0.7                      | NA (no protection) | <0.7                      | <0.7             |                           |  |
|                                                                                       | Peritoneal       | 12.8 (10.2-13.5)                 | 3.2                       | 18.1 (10.2-15.7)   | 2.2                       | 37.7 (10.4-14.9)   | 1.8                       | 37.7 (10.4-14.9)   | 1.3                       | 38.3 (10.1-23.5) |                           |  |
|                                                                                       | Peritoneal       | 7.9 (6.8-7.6)                    |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|                                                                                       | Animals          | 12.2 (10.2-13.5)                 | 3.2                       | 18.1 (10.2-15.7)   | 2.2                       | 37.7 (10.4-14.9)   | 1.8                       | 37.7 (10.4-14.9)   | 1.3                       | 38.3 (10.1-23.5) |                           |  |
|                                                                                       | Peritoneal       | 7.9 (6.8-7.6)                    |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|                                                                                       | Animals          | 12.2 (10.2-13.5)                 | 3.2                       | 18.1 (10.2-15.7)   | 2.2                       | 37.7 (10.4-14.9)   | 1.8                       | 37.7 (10.4-14.9)   | 1.3                       | 38.3 (10.1-23.5) |                           |  |
|                                                                                       | Peritoneal       | 7.9 (6.8-7.6)                    |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|                                                                                       | Animals          | 12.2 (10.2-13.5)                 | 3.2                       | 18.1 (10.2-15.7)   | 2.2                       | 37.7 (10.4-14.9)   | 1.8                       | 37.7 (10.4-14.9)   | 1.3                       | 38.3 (10.1-23.5) |                           |  |
|                                                                                       | Peritoneal       | 7.9 (6.8-7.6)                    |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
|                                                                                       | Animals          | 12.2 (10.2-13.5)                 | 3.2                       | 18.1 (10.2-15.7)   | 2.2                       | 37.7 (10.4-14.9)   | 1.8                       | 37.7 (10.4-14.9)   | 1.3                       | 38.3 (10.1-23.5) |                           |  |
| Peritoneal                                                                            | 7.9 (6.8-7.6)    |                                  |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
| Animals                                                                               | 12.2 (10.2-13.5) | 3.2                              | 18.1 (10.2-15.7)          | 2.2                | 37.7 (10.4-14.9)          | 1.8                | 37.7 (10.4-14.9)          | 1.3                | 38.3 (10.1-23.5)          |                  |                           |  |
| Peritoneal                                                                            | 7.9 (6.8-7.6)    |                                  |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
| Animals                                                                               | 12.2 (10.2-13.5) | 3.2                              | 18.1 (10.2-15.7)          | 2.2                | 37.7 (10.4-14.9)          | 1.8                | 37.7 (10.4-14.9)          | 1.3                | 38.3 (10.1-23.5)          |                  |                           |  |
| Peritoneal                                                                            | 7.9 (6.8-7.6)    |                                  |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |
| Animals                                                                               | 12.2 (10.2-13.5) | 3.2                              | 18.1 (10.2-15.7)          | 2.2                | 37.7 (10.4-14.9)          | 1.8                | 37.7 (10.4-14.9)          | 1.3                | 38.3 (10.1-23.5)          |                  |                           |  |
| Peritoneal                                                                            | 7.9 (6.8-7.6)    |                                  |                           |                    |                           |                    |                           |                    |                           |                  |                           |  |

<span id="page-31-0"></span>Figure S33. The Good Model Result and Bad Model Result for Rotated Table.

**Table Contain Formula**

|                                           | 名称                                                            | 氧化亚铁                                                                                     | 氧化铁（俗称铁红）                                                                                                   | 四氧化三铁（俗称磁性氧化铁）                 |
|-------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------|
| 化学式                                       |                                                               | FeO                                                                                      | Fe <sub>2</sub> O <sub>3</sub>                                                                              | Fe <sub>3</sub> O <sub>4</sub> |
| 颜色、状态                                     | 黑色、状态                                                         | 黑色粉末                                                                                     | 红棕色粉末                                                                                                       | 黑色晶体                           |
| 铁的价态                                      |                                                               | +2 价                                                                                     | +3 价                                                                                                        | +2、+3 价                        |
| 水溶性                                       |                                                               |                                                                                          |                                                                                                             | 均溶于水                           |
| 与非氧化性酸反应                                  | FeO+2H <sup>+</sup> = Fe <sup>2+</sup> + H <sub>2</sub> O     | Fe <sub>2</sub> O <sub>3</sub> + 6H <sup>+</sup> = 2Fe <sup>3+</sup> + 3H <sub>2</sub> O | Fe <sub>2</sub> O <sub>4</sub> + 8H <sup>+</sup> = Fe <sup>2+</sup> + 2Fe <sup>3+</sup> + 4H <sub>2</sub> O |                                |
| 与 H <sub>2</sub> 、CO <sub>2</sub> 、Al 等反应 | FeO + H <sub>2</sub> $\xrightleftharpoons[\Delta]{Fe + H_2O}$ | Fe <sub>2</sub> O <sub>3</sub> + 3CO 2Fe + 3CO <sub>2</sub>                              | Fe <sub>3</sub> O <sub>4</sub> + 8Al $\xrightleftharpoons[\Delta]{Fe + 4Al_2O_7}$                           |                                |

**Good Model Result (Qwen2VL-7B)** 

| 名称            | 氧化亚铁           | 氧化铁 (俗称铁红)        | 四氧化三铁 (俗称磁性氧化铁)        |
|---------------|----------------|-------------------|------------------------|
| 化学式           | FeO            | Fe O              | Fe O                   |
| 颜色、状态         | 黑色粉末           | 红棕色粉末             | 黑色晶体                   |
| 铁的价态          | +2 价           | +3 价              | +2、+3 价                |
| 水溶性           | 均不溶于水          | 均不溶于水             | 均不溶于水                  |
| 与非氧化性酸反应      | FeO+2H=Fe²+H O | Fe O +H=2Fe²+3H O | Fe O +8H=Fe²+2Fe³+4H O |
| 与 H、CO、Al 等反应 | FeO+H=Fe+H O   | Fe O +3CO=2Fe+3CO | 3Fe O +8Al=9Fe+4Al O   |

#### **Bad Model Result (InternVL2-8B)**

|                             | 化学式                                                         | 颜色、状态                                                           | 铁的价态                                                                               |
|-----------------------------|-------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------|
|                             | FeO                                                         | 黑色粉末                                                            | +2 价                                                                               |
|                             | Fe2O3                                                       | 红棕色粉末                                                           | +3 价                                                                               |
|                             | Fe3O4                                                       | 黑色晶体                                                            | +2、+3 价                                                                            |
| <b>水溶性</b>                  |                                                             |                                                                 | 均不溶于水                                                                              |
| 与非氧化物酸反应                    | FeO + 2H <sup>+</sup> = Fe <sup>2+</sup> + H <sub>2</sub> O | Fe2O3 + 6H <sup>+</sup> = 2Fe <sup>3+</sup> + 3H <sub>2</sub> O | Fe3O4 + 8H <sup>+</sup> = Fe <sup>2+</sup> + 2Fe <sup>3+</sup> + 4H <sub>2</sub> O |
| 与 H <sub>2</sub> 、CO、Al 等反应 | FeO + H <sub>2</sub> = Fe + H <sub>2</sub> O                | Fe2O3 + 3CO = 2Fe + 3CO <sub>2</sub>                            | Fe3O4 + 8Al = 9Fe + 4Al <sub>2</sub> O <sub>3</sub>                                |

Figure S34. The Good Model Result and Bad Model Result for Table with Formula.