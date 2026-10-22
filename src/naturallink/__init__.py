"""自然衔接（NaturalLink）：把任何内容，翻译成 AI 最容易理解的形式。

一个通用多模态转化引擎：任何输入（画面/文档/视频/音频/表格/代码/网页）
→ 对当前大脑模型最优、最省 token 的形态。

用法::

    from naturallink import NaturalLink
    nl = NaturalLink()
    result = nl.convert("输入路径或帧")
    print(result.markdown)   # 或 result.image / result.structured
"""

from .transformer import (
    # 主引擎
    OpticNerve,
    OpticNerveStream,
    default_engine,
    reset_default_engine,
    # 结果类型
    ResultKind,
    DocumentConverterResult,
    EncodedFrame,
    StructuredPayload,
    TokenReport,
    # 框架
    StreamInfo,
    DocumentConverter,
    ConverterRegistration,
    # 视觉
    VisionConverter,
    VisionOptions,
    CoordinateMapper,
    BlockPlacement,
    ContentBlock,
    detect_blocks,
    enhance_pixels,
    readability,
    estimate_image_tokens,
    estimate_text_tokens,
    # 其他转换器
    StructuredConverter,
    CodeConverter,
    VideoConverter,
    PlainTextConverter,
    MarkdownConverter,
    HtmlConverter,
    DocxConverter,
    XlsxConverter,
    PptxConverter,
    PdfConverter,
    EpubConverter,
    ImageDocumentConverter,
    ZipConverter,
)

# 面向用户的友好名称：自然衔接（NaturalLink）＝ OpticNerve 转化引擎
NaturalLink = OpticNerve

__all__ = [
    "NaturalLink",
    "OpticNerve",
    "OpticNerveStream",
    "default_engine",
    "reset_default_engine",
    "ResultKind",
    "DocumentConverterResult",
    "EncodedFrame",
    "StructuredPayload",
    "TokenReport",
    "StreamInfo",
    "DocumentConverter",
    "ConverterRegistration",
    "VisionConverter",
    "VisionOptions",
    "CoordinateMapper",
    "BlockPlacement",
    "ContentBlock",
    "detect_blocks",
    "enhance_pixels",
    "readability",
    "estimate_image_tokens",
    "estimate_text_tokens",
    "StructuredConverter",
    "CodeConverter",
    "VideoConverter",
    "PlainTextConverter",
    "MarkdownConverter",
    "HtmlConverter",
    "DocxConverter",
    "XlsxConverter",
    "PptxConverter",
    "PdfConverter",
    "EpubConverter",
    "ImageDocumentConverter",
    "ZipConverter",
]
