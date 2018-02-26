from typing import Tuple, List, Optional, Text, BinaryIO, Union, Sequence, \
    ByteString, Callable, Any

HAS_ATSUI_FONT: bool = ...
HAS_FT_FONT: bool = ...
HAS_GLITZ_SURFACE: bool = ...
HAS_IMAGE_SURFACE: bool = ...
HAS_MIME_SURFACE: bool = ...
HAS_PDF_SURFACE: bool = ...
HAS_PNG_FUNCTIONS: bool = ...
HAS_PS_SURFACE: bool = ...
HAS_QUARTZ_SURFACE: bool = ...
HAS_RECORDING_SURFACE: bool = ...
HAS_SCRIPT_SURFACE: bool = ...
HAS_SVG_SURFACE: bool = ...
HAS_TEE_SURFACE: bool = ...
HAS_USER_FONT: bool = ...
HAS_WIN32_FONT: bool = ...
HAS_WIN32_SURFACE: bool = ...
HAS_XCB_SURFACE: bool = ...
HAS_XLIB_SURFACE: bool = ...

version: str = ...
version_info: Tuple[int, int, int] = ...

def cairo_version() -> int: ...
def cairo_version_string() -> str: ...

class Path: ...

class Rectangle(Tuple[float, float, float, float]):
    x: float = ...
    y: float = ...
    width: float = ...
    height: float = ...
    def __init__(self, x: float, y: float, width: float, height: float) -> None: ...

class _IntEnum(int):
    def __init__(self, value: int) -> None: ...

class Antialias(_IntEnum):
    BEST: "Antialias" = ...
    DEFAULT: "Antialias" = ...
    FAST: "Antialias" = ...
    GOOD: "Antialias" = ...
    GRAY: "Antialias" = ...
    NONE: "Antialias" = ...
    SUBPIXEL: "Antialias" = ...

class Content(_IntEnum):
    ALPHA: "Content" = ...
    COLOR: "Content" = ...
    COLOR_ALPHA: "Content" = ...

class FillRule(_IntEnum):
    EVEN_ODD: "FillRule" = ...
    WINDING: "FillRule" = ...

class Format(_IntEnum):
    A1: "Format" = ...
    A8: "Format" = ...
    ARGB32: "Format" = ...
    INVALID: "Format" = ...
    RGB16_565: "Format" = ...
    RGB24: "Format" = ...
    RGB30: "Format" = ...
    def stride_for_width(self, width: int) -> int: ...

class HintMetrics(_IntEnum):
    DEFAULT: "HintMetrics" = ...
    OFF: "HintMetrics" = ...
    ON: "HintMetrics" = ...

class HintStyle(_IntEnum):
    DEFAULT: "HintStyle" = ...
    FULL: "HintStyle" = ...
    MEDIUM: "HintStyle" = ...
    NONE: "HintStyle" = ...
    SLIGHT: "HintStyle" = ...

class SubpixelOrder(_IntEnum):
    BGR: "SubpixelOrder" = ...
    DEFAULT: "SubpixelOrder" = ...
    RGB: "SubpixelOrder" = ...
    VBGR: "SubpixelOrder" = ...
    VRGB: "SubpixelOrder" = ...

class LineCap(_IntEnum):
    BUTT: "LineCap" = ...
    ROUND: "LineCap" = ...
    SQUARE: "LineCap" = ...

class LineJoin(_IntEnum):
    BEVEL: "LineJoin" = ...
    MITER: "LineJoin" = ...
    ROUND: "LineJoin" = ...

class Filter(_IntEnum):
    BEST: "Filter" = ...
    BILINEAR: "Filter" = ...
    FAST: "Filter" = ...
    GAUSSIAN: "Filter" = ...
    GOOD: "Filter" = ...
    NEAREST: "Filter" = ...

class Operator(_IntEnum):
    ADD: "Operator" = ...
    ATOP: "Operator" = ...
    CLEAR: "Operator" = ...
    COLOR_BURN: "Operator" = ...
    COLOR_DODGE: "Operator" = ...
    DARKEN: "Operator" = ...
    DEST: "Operator" = ...
    DEST_ATOP: "Operator" = ...
    DEST_IN: "Operator" = ...
    DEST_OUT: "Operator" = ...
    DEST_OVER: "Operator" = ...
    DIFFERENCE: "Operator" = ...
    EXCLUSION: "Operator" = ...
    HARD_LIGHT: "Operator" = ...
    HSL_COLOR: "Operator" = ...
    HSL_HUE: "Operator" = ...
    HSL_LUMINOSITY: "Operator" = ...
    HSL_SATURATION: "Operator" = ...
    IN: "Operator" = ...
    LIGHTEN: "Operator" = ...
    MULTIPLY: "Operator" = ...
    OUT: "Operator" = ...
    OVER: "Operator" = ...
    OVERLAY: "Operator" = ...
    SATURATE: "Operator" = ...
    SCREEN: "Operator" = ...
    SOFT_LIGHT: "Operator" = ...
    SOURCE: "Operator" = ...
    XOR: "Operator" = ...

class Extend(_IntEnum):
    NONE: "Extend" = ...
    PAD: "Extend" = ...
    REFLECT: "Extend" = ...
    REPEAT: "Extend" = ...

class FontSlant(_IntEnum):
    ITALIC: "FontSlant" = ...
    NORMAL: "FontSlant" = ...
    OBLIQUE: "FontSlant" = ...

class FontWeight(_IntEnum):
    BOLD: "FontWeight" = ...
    NORMAL: "FontWeight" = ...

class Status(_IntEnum):
    CLIP_NOT_REPRESENTABLE: "Status" = ...
    DEVICE_ERROR: "Status" = ...
    DEVICE_FINISHED: "Status" = ...
    DEVICE_TYPE_MISMATCH: "Status" = ...
    FILE_NOT_FOUND: "Status" = ...
    FONT_TYPE_MISMATCH: "Status" = ...
    INVALID_CLUSTERS: "Status" = ...
    INVALID_CONTENT: "Status" = ...
    INVALID_DASH: "Status" = ...
    INVALID_DSC_COMMENT: "Status" = ...
    INVALID_FORMAT: "Status" = ...
    INVALID_INDEX: "Status" = ...
    INVALID_MATRIX: "Status" = ...
    INVALID_MESH_CONSTRUCTION: "Status" = ...
    INVALID_PATH_DATA: "Status" = ...
    INVALID_POP_GROUP: "Status" = ...
    INVALID_RESTORE: "Status" = ...
    INVALID_SIZE: "Status" = ...
    INVALID_SLANT: "Status" = ...
    INVALID_STATUS: "Status" = ...
    INVALID_STRIDE: "Status" = ...
    INVALID_STRING: "Status" = ...
    INVALID_VISUAL: "Status" = ...
    INVALID_WEIGHT: "Status" = ...
    JBIG2_GLOBAL_MISSING: "Status" = ...
    LAST_STATUS: "Status" = ...
    NEGATIVE_COUNT: "Status" = ...
    NO_CURRENT_POINT: "Status" = ...
    NO_MEMORY: "Status" = ...
    NULL_POINTER: "Status" = ...
    PATTERN_TYPE_MISMATCH: "Status" = ...
    READ_ERROR: "Status" = ...
    SUCCESS: "Status" = ...
    SURFACE_FINISHED: "Status" = ...
    SURFACE_TYPE_MISMATCH: "Status" = ...
    TEMP_FILE_ERROR: "Status" = ...
    USER_FONT_ERROR: "Status" = ...
    USER_FONT_IMMUTABLE: "Status" = ...
    USER_FONT_NOT_IMPLEMENTED: "Status" = ...
    WRITE_ERROR: "Status" = ...

class PDFVersion(_IntEnum):
    VERSION_1_4: "PDFVersion" = ...
    VERSION_1_5: "PDFVersion" = ...

class PSLevel(_IntEnum):
    LEVEL_2: "PSLevel" = ...
    LEVEL_3: "PSLevel" = ...

class PathDataType(_IntEnum):
    CLOSE_PATH: "PathDataType" = ...
    CURVE_TO: "PathDataType" = ...
    LINE_TO: "PathDataType" = ...
    MOVE_TO: "PathDataType" = ...

class RegionOverlap(_IntEnum):
    IN: "RegionOverlap" = ...
    OUT: "RegionOverlap" = ...
    PART: "RegionOverlap" = ...

class SVGVersion(_IntEnum):
    VERSION_1_1: "SVGVersion" = ...
    VERSION_1_2: "SVGVersion" = ...

class ScriptMode(_IntEnum):
    ASCII: "ScriptMode" = ...
    BINARY: "ScriptMode" = ...

class Matrix:
    x0: float = ...
    xx: float = ...
    xy: float = ...
    y0: float = ...
    yx: float = ...
    yy: float = ...
    def __init__(self, xx: float=1.0, yx: float=0.0, xy:float=0.0, yy: float=1.0, x0: float=0.0, y0: float=0.0) -> None: ...
    @classmethod
    def init_rotate(cls, radians: float) -> "Matrix": ...
    def invert(self) -> None: ...
    def multiply(self, matrix2: "Matrix") -> "Matrix": ...
    def rotate(self, radians: float) -> None: ...
    def scale(self, sx: float, sy: float) -> None: ...
    def transform_distance(self, dx: float, dy: float) -> Tuple[float, float]: ...
    def transform_point(self, x: float, y: float) -> Tuple[float, float]: ...
    def translate(self, tx: float, ty: float) -> None: ...

class Pattern:
    def get_extend(self) -> Extend: ...
    def get_filter(self) -> Filter: ...
    def get_matrix(self) -> Matrix: ...
    def set_extend(self, extend: Extend) -> None: ...
    def set_filter(self, filter: Filter) -> None: ...
    def set_matrix(self, matrix: Matrix) -> None: ...

class Glyph(Tuple[int, float, float]):
    index: int = ...  # type: ignore
    x: float = ...
    y: float = ...
    def __init__(self, index: int, x: float, y: float) -> None: ...

class TextCluster(Tuple[int, int]):
    num_bytes: int = ...
    num_glyphs: int = ...
    def __init__(self, num_bytes: int, num_glyphs: int) -> None: ...

class TextClusterFlags(_IntEnum):
    BACKWARD: "TextClusterFlags" = ...

class TextExtents(Tuple[float, float, float, float, float, float]):
    x_bearing: float = ...
    y_bearing: float = ...
    width: float = ...
    height: float = ...
    x_advance: float = ...
    y_advance: float = ...
    def __init__(self, x_bearing: float, y_bearing: float, width: float, height: float, x_advance: float, y_advance: float) -> None: ...

class RectangleInt:
    height: int = ...
    width: int = ...
    x: int = ...
    y: int = ...
    def __init__(self, x: int=0, y: int=0, width: int=0, height: int=0) -> None: ...

class FontFace: ...

class FontOptions:
    def copy(self) -> "FontOptions": ...
    def equal(self, other: "FontOptions") -> bool: ...
    def get_antialias(self) -> Antialias: ...
    def get_hint_metrics(self) -> HintMetrics: ...
    def get_hint_style(self) -> HintStyle: ...
    def get_subpixel_order(self) -> SubpixelOrder: ...
    def hash(self) -> int: ...
    def merge(self, other: "FontOptions") -> None: ...
    def set_antialias(self, antialias: Antialias) -> None: ...
    def set_hint_metrics(self, hint_metrics: HintMetrics) -> None: ...
    def set_hint_style(self, hint_style: HintStyle) -> None: ...
    def set_subpixel_order(self, subpixel_order: SubpixelOrder) -> None: ...

class ScaledFont:
    def __init__(self, font_face: FontFace, font_matrix: Matrix, ctm: Matrix, options: FontOptions) -> None: ...
    def extents(self) -> Tuple[float, float, float, float, float]: ...
    def get_ctm(self) -> Matrix: ...
    def get_font_face(self) -> FontFace: ...
    def get_font_matrix(self) -> Matrix: ...
    def get_font_options(self) -> FontOptions: ...
    def get_scale_matrix(self) -> Matrix: ...
    def glyph_extents(self, glyphs: Sequence[Glyph]) -> TextExtents: ...
    def text_extents(self, text: Text) -> TextExtents: ...
    def text_to_glyphs(self, x: float, y: float, utf8: Text, with_clusters: bool=True) -> Union[Tuple[List[Glyph], List[TextCluster], TextClusterFlags], List[Glyph]]: ...

class Device:
    def acquire(self) -> None: ...
    def finish(self) -> None: ...
    def flush(self) -> None: ...
    def release(self) -> None: ...

_PathLike = Union[Text, ByteString]
_FileLike = BinaryIO

class Surface:
    def copy_page(self) -> None: ...
    def create_for_rectangle(self, x: float, y: float, width: float, height: float) -> "Surface": ...
    def create_similar(self, content: Content, width: int, height: int) -> "Surface": ...
    def create_similar_image(self, format: Format, width: int, height: int) -> "ImageSurface": ...
    def finish(self) -> None: ...
    def flush(self) -> None: ...
    def get_content(self) -> Content: ...
    def get_device(self) -> Device: ...
    def get_device_offset(self) -> Tuple[float, float]: ...
    def get_device_scale(self) -> Tuple[float, float]: ...
    def get_fallback_resolution(self) -> Tuple[float, float]: ...
    def get_font_options(self) -> FontOptions: ...
    def get_mime_data(self) -> Optional[bytes]: ...
    def has_show_text_glyphs(self) -> bool: ...
    def map_to_image(self, extents: RectangleInt) -> "ImageSurface": ...
    def mark_dirty(self) -> None: ...
    def mark_dirty_rectangle(self, x: int, y: int, width: int, height: int) -> None: ...
    def set_device_offset(self, x_offset: float, y_offset: float) -> None: ...
    def set_device_scale(self, x_scale: float, y_scale: float) -> None: ...
    def set_fallback_resolution(self, x_pixels_per_inch: float, y_pixels_per_inch: float) -> None: ...
    def set_mime_data(self, mime_type: str, data: bytes) -> None: ...
    def show_page(self) -> None: ...
    def supports_mime_type(self, mime_type: str) -> bool: ...
    def unmap_image(self, image: "ImageSurface") -> None: ...
    def write_to_png(self, fobj: Union[_FileLike, _PathLike]) -> None: ...

class ImageSurface(Surface):
    def __init__(self, format: Format, width: int, height: int) -> None: ...
    @classmethod
    def create_for_data(cls, data: memoryview, format: Format, width: int, height: int, stride: int=...) -> "ImageSurface": ...
    @classmethod
    def create_from_png(cls, fobj: Union[_PathLike, _FileLike]) -> "ImageSurface": ...
    format_stride_for_width = Format.stride_for_width
    def get_data(self) -> memoryview: ...
    def get_format(self) -> Format: ...
    def get_height(self) -> int: ...
    def get_stride(self) -> int: ...
    def get_width(self) -> int: ...

class SurfacePattern(Pattern):
    def __init__(self, surface: Surface) -> None: ...
    def get_surface(self) -> Surface: ...

class Context:
    def __init__(self, target: Surface) -> None: ...
    def append_path(self, path: Path) -> None: ...
    def arc(self, xc: float, yc: float, radius: float, angle1: float, angle2: float) -> None: ...
    def arc_negative(self, xc: float, yc: float, radius: float, angle1: float, angle2: float) -> None: ...
    def clip(self) -> None: ...
    def clip_extents(self) -> Tuple[float, float, float, float]: ...
    def clip_preserve(self) -> None: ...
    def close_path(self) -> None: ...
    def copy_clip_rectangle_list(self) -> List[Rectangle]: ...
    def copy_page(self) -> None: ...
    def copy_path(self) -> Path: ...
    def copy_path_flat(self) -> Path: ...
    def curve_to(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None: ...
    def device_to_user(self, x: float, y: float) -> Tuple[float, float]: ...
    def device_to_user_distance(self, dx: float, dy: float) -> Tuple[float, float]: ...
    def fill(self) -> None: ...
    def fill_extents(self) -> Tuple[float, float, float, float]: ...
    def fill_preserve(self) -> None: ...
    def font_extents(self) -> Tuple[float, float, float, float, float]: ...
    def get_antialias(self) -> Antialias: ...
    def get_current_point(self) -> Tuple[float, float]: ...
    def get_dash(self) -> Tuple[List[float], float]: ...
    def get_dash_count(self) -> int: ...
    def get_fill_rule(self) -> FillRule: ...
    def get_font_face(self) -> FontFace: ...
    def get_font_matrix(self) -> Matrix: ...
    def get_font_options(self) -> FontOptions: ...
    def get_group_target(self) -> Surface: ...
    def get_line_cap(self) -> LineCap: ...
    def get_line_join(self) -> LineJoin: ...
    def get_line_width(self) -> float: ...
    def get_matrix(self) -> Matrix: ...
    def get_miter_limit(self) -> float: ...
    def get_operator(self) -> Operator: ...
    def get_scaled_font(self) -> ScaledFont: ...
    def get_source(self) -> Pattern: ...
    def get_target(self) -> Surface: ...
    def get_tolerance(self) -> float: ...
    def glyph_extents(self, glyphs: Sequence[Glyph]) -> TextExtents: ...
    def glyph_path(self, glyphs: Sequence[Glyph]) -> None: ...
    def has_current_point(self) -> bool: ...
    def identity_matrix(self) -> None: ...
    def in_clip(self, x: float, y: float) -> bool: ...
    def in_fill(self, x: float, y: float) -> bool: ...
    def in_stroke(self, x: float, y: float) -> bool: ...
    def line_to(self, x: float, y: float) -> None: ...
    def mask(self, pattern: Pattern) -> None: ...
    def mask_surface(self, surface: Surface, x: float=0.0, y: float=0.0) -> None: ...
    def move_to(self, x: float, y: float) -> None: ...
    def new_path(self) -> None: ...
    def new_sub_path(self) -> None: ...
    def paint(self) -> None: ...
    def paint_with_alpha(self, alpha: float) -> None: ...
    def path_extents(self) -> Tuple[float, float, float, float]: ...
    def pop_group(self) -> SurfacePattern: ...
    def pop_group_to_source(self) -> None: ...
    def push_group(self) -> None: ...
    def push_group_with_content(self, content: Content) -> None: ...
    def rectangle(self, x: float, y: float, width: float, height: float) -> None: ...
    def rel_curve_to(self, dx1: float, dy1: float, dx2: float, dy2: float, dx3: float, dy4: float) -> None: ...
    def rel_line_to(self, dx: float, dy: float) -> None: ...
    def rel_move_to(self, dx: float, dy: float) -> None: ...
    def reset_clip(self) -> None: ...
    def restore(self) -> None: ...
    def rotate(self, angle: float) -> None: ...
    def save(self) -> None: ...
    def scale(self, sx: float, sy: float) -> None: ...
    def select_font_face(self, family: Text, slant: FontSlant=..., weight: FontWeight=...) -> None: ...
    def set_antialias(self, antialias: Antialias) -> None: ...
    def set_dash(self, dashes: Sequence[float], offset: int=0) -> None: ...
    def set_fill_rule(self, fill_rule: FillRule) -> None: ...
    def set_font_face(self, font_face: FontFace) -> None: ...
    def set_font_matrix(self, matrix: Matrix) -> None: ...
    def set_font_options(self, options: FontOptions) -> None: ...
    def set_font_size(self, size: float) -> None: ...
    def set_line_cap(self, line_cap: LineCap) -> None: ...
    def set_line_join(self, line_join: LineJoin) -> None: ...
    def set_line_width(self, width: float) -> None: ...
    def set_matrix(self, matrix: Matrix) -> None: ...
    def set_miter_limit(self, limit: float) -> None: ...
    def set_operator(self, op: Operator) -> None: ...
    def set_scaled_font(self, scaled_font: ScaledFont) -> None: ...
    def set_source(self, source: Pattern) -> None: ...
    def set_source_rgb(self, red: float, green: float, blue: float) -> None: ...
    def set_source_rgba(self, red: float, green: float, blue: float, alpha: float=1.0) -> None: ...
    def set_source_surface(self, surface: Surface, x: float=0.0, y: float=0.0) -> None: ...
    def set_tolerance(self, tolerance: float) -> None: ...
    def show_glyphs(self, glyphs: Sequence[Glyph]) -> None: ...
    def show_page(self) -> None: ...
    def show_text(self, text: Text) -> None: ...
    def show_text_glyphs(self, utf8: Text, glyphs: Sequence[Glyph], clusters: Sequence[TextCluster], cluster_flags: TextClusterFlags) -> None: ...
    def stroke(self) -> None: ...
    def stroke_extents(self) -> Tuple[float, float, float, float]: ...
    def stroke_preserve(self) -> None: ...
    def text_extents(self, text: Text) -> TextExtents: ...
    def text_path(self, text: Text) -> None: ...
    def transform(self, matrix: Matrix) -> None: ...
    def translate(self, tx: float, ty: float) -> None: ...
    def user_to_device(self, x: float, y: float) -> Tuple[float, float]: ...
    def user_to_device_distance(self, dx: float, dy: float) -> Tuple[float, float]: ...

class Error(Exception):
    status: Status = ...

CairoError = Error

class Gradient(Pattern):
    def add_color_stop_rgb(self, offset: float, red: float, green: float, blue: float) -> None: ...
    def add_color_stop_rgba(self, offset: float, red: float, green: float, blue: float, alpha: float) -> None: ...
    def get_color_stops_rgba(self) -> List[Tuple[float, float, float, float, float]]: ...

class LinearGradient(Gradient):
    def __init__(self, x0: float, y0: float, x1: float, y1: float) -> None: ...
    def get_linear_points(self) -> Tuple[float, float, float, float]: ...

class MeshPattern(Pattern):
    def __init__(self) -> None: ...
    def begin_patch(self) -> None: ...
    def curve_to(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None: ...
    def end_patch(self) -> None: ...
    def get_control_point(self, patch_num: int, point_num: int) -> Tuple[float, float]: ...
    def get_corner_color_rgba(self, patch_num: int, corner_num: int) -> Tuple[float, float, float, float]: ...
    def get_patch_count(self) -> int: ...
    def get_path(self, patch_num: int) -> Path: ...
    def line_to(self, x: float, y: float) -> None: ...
    def move_to(self, x: float, y: float) -> None: ...
    def set_control_point(self, point_num: int, x: float, y: float) -> None: ...
    def set_corner_color_rgb(self, corner_num: int, red: float, green: float, blue: float) -> None: ...
    def set_corner_color_rgba(self, corner_num: int, red: float, green: float, blue: float, alpha: float) -> None: ...

class PDFSurface(Surface):
    @staticmethod
    def get_versions() -> List[PDFVersion]: ...
    @staticmethod
    def version_to_string(version: PDFVersion) -> str: ...
    def __init__(self, fobj: Optional[Union[_PathLike, _FileLike]], width_in_points: float, height_in_points: float) -> None: ...
    def restrict_to_version(self, version: PDFVersion) -> None: ...
    def set_size(self, width_in_points: float, height_in_points: float) -> None: ...

class PSSurface(Surface):
    @staticmethod
    def get_levels() -> List[PSLevel]: ...
    @staticmethod
    def level_to_string(level: PSLevel) -> str: ...
    ps_level_to_string = level_to_string
    def __init__(self, fobj: Optional[Union[_PathLike, _FileLike]], width_in_points: float, height_in_points: float) -> None: ...
    def dsc_begin_page_setup(self) -> None: ...
    def dsc_begin_setup(self) -> None: ...
    def dsc_comment(self, comment: str) -> None: ...
    def get_eps(self) -> bool: ...
    def restrict_to_level(self, level: PSLevel) -> None: ...
    def set_eps(self, eps: bool) -> None: ...
    def set_size(self, width_in_points: float, height_in_points: float) -> None: ...

class SVGSurface(Surface):
    @staticmethod
    def get_versions() -> List[SVGVersion]: ...
    @staticmethod
    def version_to_string(version: SVGVersion) -> str: ...
    def __init__(self, fobj: Optional[Union[_PathLike, _FileLike]], width_in_points: float, height_in_points: float) -> None: ...
    def restrict_to_version(self, version: SVGVersion) -> None: ...

class RadialGradient(Gradient):
    def __init__(self, cx0: float, cy0: float, radius0: float, cx1: float, cy1: float, radius1: float) -> None: ...
    def get_radial_circles(self) -> Tuple[float, float, float, float, float, float]: ...

_AcquireCallback = Callable[[Surface, RectangleInt], Surface]
_ReleaseCallback = Callable[[Surface], None]

class RasterSourcePattern(Pattern):
    def __init__(self, content: Content, width: int, height: int) -> None: ...
    def get_acquire(self) -> Tuple[Optional[_AcquireCallback], Optional[_ReleaseCallback]]: ...
    def set_acquire(self, acquire: Optional[_AcquireCallback], release: Optional[_ReleaseCallback]) -> None: ...

class RecordingSurface(Surface):
    def __init__(self, content: Content, rectangle: Rectangle) -> None: ...
    def get_extents(self) -> Optional[Rectangle]: ...
    def ink_extents(self) -> Tuple[float, float, float, float]: ...

class Region:
    def __init__(self, rectangle: Union[RectangleInt, List[RectangleInt]]) -> None: ...
    def contains_point(self, x: int, y: int) -> bool: ...
    def contains_rectangle(self, rectangle: RectangleInt) -> RegionOverlap: ...
    def copy(self) -> "Region": ...
    def equal(self, region: "Region") -> bool: ...
    def get_extents(self) -> RectangleInt: ...
    def get_rectangle(self, nth: int) -> RectangleInt: ...
    def intersect(self, other: "Union[Region, RectangleInt]") -> "Region": ...
    def is_empty(self) -> bool: ...
    def num_rectangles(self) -> int: ...
    def subtract(self, other: "Union[Region, RectangleInt]") -> "Region": ...
    def translate(self, dx: int, dy: int) -> None: ...
    def union(self, other: "Union[Region, RectangleInt]") -> "Region": ...
    def xor(self, other: "Union[Region, RectangleInt]") -> "Region": ...

class ScriptDevice(Device):
    def __init__(self, fobj: Union[_FileLike, _PathLike]) -> None: ...
    def from_recording_surface(self, recording_surface: RecordingSurface) -> None: ...
    def get_mode(self) -> ScriptMode: ...
    def set_mode(self, mode: ScriptMode) -> None: ...
    def write_comment(self, comment: Text) -> None: ...

class ScriptSurface(Surface):
    def __init__(self, script: ScriptDevice, content: Content, width: float, height: float) -> None: ...
    @classmethod
    def create_for_target(cls, script: ScriptDevice, target: Surface) -> "ScriptSurface": ...

class SolidPattern(Pattern):
    def __init__(self, red: float, green: float, blue: float, alpha: float=1.0) -> None: ...
    def get_rgba(self) -> Tuple[float, float, float, float]: ...

class SurfaceObserverMode(_IntEnum):
    NORMAL: "SurfaceObserverMode" = ...
    RECORD_OPERATIONS: "SurfaceObserverMode" = ...

class TeeSurface(Surface):
    def __init__(self, master: Surface) -> None: ...
    def add(self, target: Surface) -> None: ...
    def index(self, index: int) -> Surface: ...
    def remove(self, target: Surface) -> None: ...

class ToyFontFace(FontFace):
    def __init__(self, family: str, slant: FontSlant=..., weight: FontWeight=...) -> None: ...
    def get_family(self) -> str: ...
    def get_slant(self) -> FontSlant: ...
    def get_weight(self) -> FontWeight: ...

class XCBSurface(Surface):
    def __init__(self, connection: Any, drawable: Any, visualtype: Any, width: int, height: int) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...

class XlibSurface(Surface):
    def get_depth(self) -> int: ...
    def get_height(self) -> int: ...
    def get_width(self) -> int: ...

def get_include() -> _PathLike: ...

MIME_TYPE_JP2 = ... # type: str
MIME_TYPE_JPEG = ... # type: str
MIME_TYPE_PNG = ... # type: str
MIME_TYPE_UNIQUE_ID = ... # type: str
MIME_TYPE_URI = ... # type: str

CAPI: Any = ...

ANTIALIAS_BEST = Antialias.BEST
ANTIALIAS_DEFAULT = Antialias.DEFAULT
ANTIALIAS_FAST = Antialias.FAST
ANTIALIAS_GOOD = Antialias.GOOD
ANTIALIAS_GRAY = Antialias.GRAY
ANTIALIAS_NONE = Antialias.NONE
ANTIALIAS_SUBPIXEL = Antialias.SUBPIXEL
CONTENT_ALPHA = Content.ALPHA
CONTENT_COLOR = Content.COLOR
CONTENT_COLOR_ALPHA = Content.COLOR_ALPHA
EXTEND_NONE = Extend.NONE
EXTEND_PAD = Extend.PAD
EXTEND_REFLECT = Extend.REFLECT
EXTEND_REPEAT = Extend.REPEAT
FILL_RULE_EVEN_ODD = FillRule.EVEN_ODD
FILL_RULE_WINDING = FillRule.WINDING
FILTER_BEST = Filter.BEST
FILTER_BILINEAR = Filter.BILINEAR
FILTER_FAST = Filter.FAST
FILTER_GAUSSIAN = Filter.GAUSSIAN
FILTER_GOOD = Filter.GOOD
FILTER_NEAREST = Filter.NEAREST
FONT_SLANT_ITALIC = FontSlant.ITALIC
FONT_SLANT_NORMAL = FontSlant.NORMAL
FONT_SLANT_OBLIQUE = FontSlant.OBLIQUE
FONT_WEIGHT_BOLD = FontWeight.BOLD
FONT_WEIGHT_NORMAL = FontWeight.NORMAL
FORMAT_A1 = Format.A1
FORMAT_A8 = Format.A8
FORMAT_ARGB32 = Format.ARGB32
FORMAT_INVALID = Format.INVALID
FORMAT_RGB16_565 = Format.RGB16_565
FORMAT_RGB24 = Format.RGB24
FORMAT_RGB30 = Format.RGB30
HINT_METRICS_DEFAULT = HintMetrics.DEFAULT
HINT_METRICS_OFF = HintMetrics.OFF
HINT_METRICS_ON = HintMetrics.ON
HINT_STYLE_DEFAULT = HintStyle.DEFAULT
HINT_STYLE_FULL = HintStyle.FULL
HINT_STYLE_MEDIUM = HintStyle.MEDIUM
HINT_STYLE_NONE = HintStyle.NONE
HINT_STYLE_SLIGHT = HintStyle.SLIGHT
LINE_CAP_BUTT = LineCap.BUTT
LINE_CAP_ROUND = LineCap.ROUND
LINE_CAP_SQUARE = LineCap.SQUARE
LINE_JOIN_BEVEL = LineJoin.BEVEL
LINE_JOIN_MITER = LineJoin.MITER
LINE_JOIN_ROUND = LineJoin.ROUND
OPERATOR_ADD = Operator.ADD
OPERATOR_ATOP = Operator.ATOP
OPERATOR_CLEAR = Operator.CLEAR
OPERATOR_COLOR_BURN = Operator.COLOR_BURN
OPERATOR_COLOR_DODGE = Operator.COLOR_DODGE
OPERATOR_DARKEN = Operator.DARKEN
OPERATOR_DEST = Operator.DEST
OPERATOR_DEST_ATOP = Operator.DEST_ATOP
OPERATOR_DEST_IN = Operator.DEST_IN
OPERATOR_DEST_OUT = Operator.DEST_OUT
OPERATOR_DEST_OVER = Operator.DEST_OVER
OPERATOR_DIFFERENCE = Operator.DIFFERENCE
OPERATOR_EXCLUSION = Operator.EXCLUSION
OPERATOR_HARD_LIGHT = Operator.HARD_LIGHT
OPERATOR_HSL_COLOR = Operator.HSL_COLOR
OPERATOR_HSL_HUE = Operator.HSL_HUE
OPERATOR_HSL_LUMINOSITY = Operator.HSL_LUMINOSITY
OPERATOR_HSL_SATURATION = Operator.HSL_SATURATION
OPERATOR_IN = Operator.IN
OPERATOR_LIGHTEN = Operator.LIGHTEN
OPERATOR_MULTIPLY = Operator.MULTIPLY
OPERATOR_OUT = Operator.OUT
OPERATOR_OVER = Operator.OVER
OPERATOR_OVERLAY = Operator.OVERLAY
OPERATOR_SATURATE = Operator.SATURATE
OPERATOR_SCREEN = Operator.SCREEN
OPERATOR_SOFT_LIGHT = Operator.SOFT_LIGHT
OPERATOR_SOURCE = Operator.SOURCE
OPERATOR_XOR = Operator.XOR
PATH_CLOSE_PATH = PathDataType.CLOSE_PATH
PATH_CURVE_TO = PathDataType.CURVE_TO
PATH_LINE_TO = PathDataType.LINE_TO
PATH_MOVE_TO = PathDataType.MOVE_TO
PDF_VERSION_1_4 = PDFVersion.VERSION_1_4
PDF_VERSION_1_5 = PDFVersion.VERSION_1_5
PS_LEVEL_2 = PSLevel.LEVEL_2
PS_LEVEL_3 = PSLevel.LEVEL_3
REGION_OVERLAP_IN = RegionOverlap.IN
REGION_OVERLAP_OUT = RegionOverlap.OUT
REGION_OVERLAP_PART = RegionOverlap.PART
SCRIPT_MODE_ASCII = ScriptMode.ASCII
SCRIPT_MODE_BINARY = ScriptMode.BINARY
STATUS_CLIP_NOT_REPRESENTABLE = Status.CLIP_NOT_REPRESENTABLE
STATUS_DEVICE_ERROR = Status.DEVICE_ERROR
STATUS_DEVICE_FINISHED = Status.DEVICE_FINISHED
STATUS_DEVICE_TYPE_MISMATCH = Status.DEVICE_TYPE_MISMATCH
STATUS_FILE_NOT_FOUND = Status.FILE_NOT_FOUND
STATUS_FONT_TYPE_MISMATCH = Status.FONT_TYPE_MISMATCH
STATUS_INVALID_CLUSTERS = Status.INVALID_CLUSTERS
STATUS_INVALID_CONTENT = Status.INVALID_CONTENT
STATUS_INVALID_DASH = Status.INVALID_DASH
STATUS_INVALID_DSC_COMMENT = Status.INVALID_DSC_COMMENT
STATUS_INVALID_FORMAT = Status.INVALID_FORMAT
STATUS_INVALID_INDEX = Status.INVALID_INDEX
STATUS_INVALID_MATRIX = Status.INVALID_MATRIX
STATUS_INVALID_MESH_CONSTRUCTION = Status.INVALID_MESH_CONSTRUCTION
STATUS_INVALID_PATH_DATA = Status.INVALID_PATH_DATA
STATUS_INVALID_POP_GROUP = Status.INVALID_POP_GROUP
STATUS_INVALID_RESTORE = Status.INVALID_RESTORE
STATUS_INVALID_SIZE = Status.INVALID_SIZE
STATUS_INVALID_SLANT = Status.INVALID_SLANT
STATUS_INVALID_STATUS = Status.INVALID_STATUS
STATUS_INVALID_STRIDE = Status.INVALID_STRIDE
STATUS_INVALID_STRING = Status.INVALID_STRING
STATUS_INVALID_VISUAL = Status.INVALID_VISUAL
STATUS_INVALID_WEIGHT = Status.INVALID_WEIGHT
STATUS_JBIG2_GLOBAL_MISSING = Status.JBIG2_GLOBAL_MISSING
STATUS_LAST_STATUS = Status.LAST_STATUS
STATUS_NEGATIVE_COUNT = Status.NEGATIVE_COUNT
STATUS_NO_CURRENT_POINT = Status.NO_CURRENT_POINT
STATUS_NO_MEMORY = Status.NO_MEMORY
STATUS_NULL_POINTER = Status.NULL_POINTER
STATUS_PATTERN_TYPE_MISMATCH = Status.PATTERN_TYPE_MISMATCH
STATUS_READ_ERROR = Status.READ_ERROR
STATUS_SUCCESS = Status.SUCCESS
STATUS_SURFACE_FINISHED = Status.SURFACE_FINISHED
STATUS_SURFACE_TYPE_MISMATCH = Status.SURFACE_TYPE_MISMATCH
STATUS_TEMP_FILE_ERROR = Status.TEMP_FILE_ERROR
STATUS_USER_FONT_ERROR = Status.USER_FONT_ERROR
STATUS_USER_FONT_IMMUTABLE = Status.USER_FONT_IMMUTABLE
STATUS_USER_FONT_NOT_IMPLEMENTED = Status.USER_FONT_NOT_IMPLEMENTED
STATUS_WRITE_ERROR = Status.WRITE_ERROR
SUBPIXEL_ORDER_BGR = SubpixelOrder.BGR
SUBPIXEL_ORDER_DEFAULT = SubpixelOrder.DEFAULT
SUBPIXEL_ORDER_RGB = SubpixelOrder.RGB
SUBPIXEL_ORDER_VBGR = SubpixelOrder. VBGR
SUBPIXEL_ORDER_VRGB = SubpixelOrder.VRGB
SURFACE_OBSERVER_NORMAL = SurfaceObserverMode.NORMAL
SURFACE_OBSERVER_RECORD_OPERATIONS = SurfaceObserverMode.RECORD_OPERATIONS
SVG_VERSION_1_1 = SVGVersion.VERSION_1_1
SVG_VERSION_1_2 = SVGVersion.VERSION_1_2
TEXT_CLUSTER_FLAG_BACKWARD = TextClusterFlags.BACKWARD
