from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

import io
from io import StringIO
from flask import Flask, jsonify, make_response, request
import boto3
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.route('/process', methods=['POST'])
def insert():
    if request.method == "POST":
        url_key = request.get_json(silent=True)['urlKey']
        dir = request.get_json(silent=True)['dir']
        s3 = boto3.client('s3')
        bucket_name = 'test-upload-bucket-devy'

        object_key = url_key
        # object_key = 'unprocessed-data/2022-07-25T17:27:43.040Z-68bbf31f-f727-4746-93b8-1b3df1f39f6b/Dataset.xlsx'

        obj = s3.get_object(Bucket=bucket_name, Key=object_key)

        df = pd.read_excel(io.BytesIO(obj['Body'].read()))

        print(df.head())

        df["CSS Class"].fillna('no-css-class', inplace=True)
        df.head(5)

        # 'accent-color','align-content', 'align-items','align-self'	,'alignment-baseline', 'animation-direction','animation-fill-mode','animation-name',	'animation-play-state',	'animation-timing-function',	'app-region',	'appearance'
        df.drop(
            ['accent-color', 'align-content', 'align-items', 'align-self', 'alignment-baseline', 'animation-direction',
             'animation-fill-mode', 'animation-name', 'animation-play-state', 'animation-timing-function', 'app-region',
             'appearance'], axis=1, inplace=True)

        # 'backdrop-filter',	'backface-visibility',	'background-attachment',	'background-blend-mode',	'background-clip'
        df.drop(['backdrop-filter', 'backface-visibility', 'background-attachment', 'background-blend-mode',
                 'background-clip', 'background-image', 'background-origin', 'border-block-end-style',
                 'border-block-start-style', 'border-bottom-style', 'background-repeat', 'background-size',
                 'border-collapse', 'border-image-repeat', 'border-image-source', 'border-inline-end-style',
                 'border-inline-start-style', 'border-left-style', 'border-right-style', 'border-top-style',
                 'box-shadow', 'box-sizing', 'break-after', 'break-before', 'break-inside', 'buffered-rendering'],
                axis=1, inplace=True)

        # 'caption-side','clear','clip','clip-path','clip-rule','color-interpolation','color-interpolation-filters','color-rendering','column-count','column-gap','column-rule-style','column-span','column-width','contain-intrinsic-block-size','contain-intrinsic-height','contain-intrinsic-inline-size','contain-intrinsic-size','contain-intrinsic-width','content','cursor'
        df.drop(['CSS Class Parent', 'caption-side', 'clear', 'clip', 'clip-path', 'clip-rule', 'color-interpolation',
                 'color-interpolation-filters', 'color-rendering', 'column-count', 'column-gap', 'column-rule-style',
                 'column-span', 'column-width', 'contain-intrinsic-block-size', 'contain-intrinsic-height',
                 'contain-intrinsic-inline-size', 'contain-intrinsic-size', 'contain-intrinsic-width', 'content',
                 'cursor'], axis=1, inplace=True)

        # 'd','direction','display','dominant-baseline'
        df.drop(['d', 'direction', 'display', 'dominant-baseline'], axis=1, inplace=True)

        # empty-cells
        df.drop(['empty-cells'], axis=1, inplace=True)

        # fill-rule,filter,flex-basis,flex-direction,flex-wrap,float,font-family,font-kerning,font-optical-sizing,font-style,font-variant,font-variant-caps,font-variant-east-asian,font-variant-ligatures,font-variant-numeric
        df.drop(
            ['fill-rule', 'filter', 'flex-basis', 'flex-direction', 'flex-wrap', 'float', 'font-family', 'font-kerning',
             'font-optical-sizing', 'font-style', 'font-variant', 'font-variant-caps', 'font-variant-east-asian',
             'font-variant-ligatures', 'font-variant-numeric'], axis=1, inplace=True)

        # 'grid-auto-columns','grid-auto-flow','grid-auto-rows','grid-column-end','grid-column-start','grid-row-end','grid-row-start','grid-template-areas','grid-template-columns','grid-template-rows'
        df.drop(['grid-auto-columns', 'grid-auto-flow', 'grid-auto-rows', 'grid-column-end', 'grid-column-start',
                 'grid-row-end', 'grid-row-start', 'grid-template-areas', 'grid-template-columns',
                 'grid-template-rows'], axis=1, inplace=True)

        # hyphens
        df.drop(['hyphens'], axis=1, inplace=True)

        # 'image-orientation','image-rendering','isolation'
        df.drop(['image-orientation', 'image-rendering', 'isolation'], axis=1, inplace=True)

        # 'justify-content','justify-items','justify-self'
        df.drop(['justify-content', 'justify-items', 'justify-self'], axis=1, inplace=True)

        # 'letter-spacing','line-break','list-style-image','list-style-position','list-style-type'
        df.drop(['letter-spacing', 'line-break', 'list-style-image', 'list-style-position', 'list-style-type'], axis=1,
                inplace=True)

        # 'marker-end','marker-mid','marker-start','mask-type','max-block-size','max-height','max-inline-size','max-width','mix-blend-mode'
        df.drop(
            ['marker-end', 'marker-mid', 'marker-start', 'mask-type', 'max-block-size', 'max-height', 'max-inline-size',
             'max-width', 'mix-blend-mode'], axis=1, inplace=True)

        # 'object-fit','offset-path','offset-rotate','outline-style','overflow-anchor','overflow-wrap','overflow-x','overflow-y','overscroll-behavior-block','overscroll-behavior-inline'
        df.drop(['object-fit', 'offset-path', 'offset-rotate', 'outline-style', 'overflow-anchor', 'overflow-wrap',
                 'overflow-x', 'overflow-y', 'overscroll-behavior-block', 'overscroll-behavior-inline'], axis=1,
                inplace=True)

        # 'paint-order','perspective','pointer-events','position'
        df.drop(['paint-order', 'perspective', 'pointer-events', 'position'], axis=1, inplace=True)

        # 'resize','row-gap','ruby-position','rx','ry'
        df.drop(['resize', 'row-gap', 'ruby-position', 'rx', 'ry'], axis=1, inplace=True)

        # 'scroll-behavior','scroll-padding-block-end','scroll-padding-block-start','scroll-padding-inline-end','scroll-padding-inline-start','scrollbar-gutter','shape-outside','shape-rendering','speak','stroke','stroke-dasharray','stroke-linecap','stroke-linejoin'
        df.drop(
            ['scroll-behavior', 'scroll-padding-block-end', 'scroll-padding-block-start', 'scroll-padding-inline-end',
             'scroll-padding-inline-start', 'scrollbar-gutter', 'shape-outside', 'shape-rendering', 'speak', 'stroke',
             'stroke-dasharray', 'stroke-linecap', 'stroke-linejoin'], axis=1, inplace=True)

        # 'table-layout','text-align','text-align-last','text-anchor','text-decoration-line','text-decoration-skip-ink','text-decoration-style','text-overflow','text-rendering','text-shadow','text-transform','text-underline-position','touch-action','transform','transform-style','transition-property','transition-timing-function'
        df.drop(['table-layout', 'text-align', 'text-align-last', 'text-anchor', 'text-decoration-line',
                 'text-decoration-skip-ink', 'text-decoration-style', 'text-overflow', 'text-rendering', 'text-shadow',
                 'text-transform', 'text-underline-position', 'touch-action', 'transform', 'transform-style',
                 'transition-property', 'transition-timing-function'], axis=1, inplace=True)

        # 'unicode-bidi','user-select',
        df.drop(['unicode-bidi', 'user-select'], axis=1, inplace=True)

        # 'vector-effect','vertical-align','visibility'
        df.drop(['vector-effect', 'vertical-align', 'visibility'], axis=1, inplace=True)

        # 'white-space','will-change','word-break','writing-mode'
        df.drop(['white-space', 'will-change', 'word-break', 'writing-mode'], axis=1, inplace=True)

        # 'z-index'
        df.drop(['z-index'], axis=1, inplace=True)

        # '-webkit-border-image','-webkit-box-align','-webkit-box-decoration-break','-webkit-box-direction','-webkit-box-orient','-webkit-box-pack','-webkit-box-reflect','-webkit-font-smoothing','-webkit-highlight','-webkit-hyphenate-character','-webkit-line-break','-webkit-line-clamp','-webkit-locale','-webkit-mask-box-image','-webkit-mask-box-image-repeat','-webkit-mask-box-image-source','-webkit-mask-box-image-width','-webkit-mask-clip','-webkit-mask-composite','-webkit-mask-image','-webkit-mask-origin','-webkit-mask-repeat','-webkit-mask-size','-webkit-print-color-adjust','-webkit-rtl-ordering','-webkit-text-combine','-webkit-text-decorations-in-effect','-webkit-text-emphasis-position','-webkit-text-emphasis-style','-webkit-text-orientation','-webkit-text-security','-webkit-user-drag','-webkit-user-modify','-webkit-writing-mode'
        df.drop(['-webkit-border-image', '-webkit-box-align', '-webkit-box-decoration-break', '-webkit-box-direction',
                 '-webkit-box-orient', '-webkit-box-pack', '-webkit-box-reflect', '-webkit-font-smoothing',
                 '-webkit-highlight', '-webkit-hyphenate-character', '-webkit-line-break', '-webkit-line-clamp',
                 '-webkit-locale', '-webkit-mask-box-image', '-webkit-mask-box-image-repeat',
                 '-webkit-mask-box-image-source', '-webkit-mask-box-image-width', '-webkit-mask-clip',
                 '-webkit-mask-composite', '-webkit-mask-image', '-webkit-mask-origin', '-webkit-mask-repeat',
                 '-webkit-mask-size', '-webkit-print-color-adjust', '-webkit-rtl-ordering', '-webkit-text-combine',
                 '-webkit-text-decorations-in-effect', '-webkit-text-emphasis-position', '-webkit-text-emphasis-style',
                 '-webkit-text-orientation', '-webkit-text-security', '-webkit-user-drag', '-webkit-user-modify'],
                axis=1, inplace=True)

        df.head(5)

        def removeS(index, columnsWithS):
            output = []
            for column in columnsWithS:
                output.append(df.loc[index, column][:-1])
            return output

        columnsWithS = ["animation-delay", "animation-duration", "transition-delay", "transition-duration"]

        for x in df.index:
            df.loc[x, columnsWithS] = removeS(x, columnsWithS)

        df.head(5)

        def rgb_int(r, g, b):
            packed = int('%02x%02x%02x' % (r, g, b), 16)
            return packed

        def rgba_int(r, g, b, a):
            r = '{0:x}'.format(int(+r))
            g = '{0:x}'.format(int(+g))
            b = '{0:x}'.format(int(+b))
            a = '{0:x}'.format(int(round(+a * 255)))
            if (len(r) == 1):
                r = "0" + r
            if (len(g) == 1):
                r = "0" + g
            if (len(b) == 1):
                r = "0" + b
            if (len(a) == 1):
                r = "0" + a
            return int((r + g + b + a), 16)

        def color_int(x, colorColumnsArray):
            output = []
            for column in colorColumnsArray:
                chr = (df.loc[x, column][df.loc[x, column].find('(') + 1: df.loc[x, column].find(')')]).split(', ')
                if (len(chr) == 3):
                    output.append(rgb_int(int(chr[0]), int(chr[1]), int(chr[2])))
                if (len(chr) == 4):
                    output.append(rgba_int(int(chr[0]), int(chr[1]), int(chr[2]), float(chr[3])))
            return output

        # not included  box-shadow

        colorColumnsArray = ["background-color", "border-block-end-color", "border-block-start-color",
                             "border-bottom-color", "border-inline-end-color", "border-inline-start-color",
                             "border-left-color", "border-right-color",
                             "border-top-color", "caret-color", "color", "column-rule-color", "fill", "flood-color",
                             "lighting-color", "outline-color", "stop-color", "text-decoration",
                             "text-decoration-color",
                             "-webkit-text-emphasis-color", "-webkit-text-fill-color", "-webkit-text-stroke-color",
                             "-webkit-tap-highlight-color"
                             ]

        for x in df.index:
            df.loc[x, colorColumnsArray] = color_int(x, colorColumnsArray)

        df.head(5)

        def removePX(x, columnsWithPX):
            output = []
            for column in columnsWithPX:
                numeric_string = "".join(filter(str.isdigit, df.loc[x, column]))
                if (numeric_string.isnumeric()):
                    output.append(int(numeric_string))
                else:
                    output.append(numeric_string)
            return output

        # not included - block-size, bottom, height, inset-block-end, inset-block-start, inset-inline-end, inset-inline-start, left, min-block-size, min-height, min-inline-size, min-width, right, text-size-adjust,top, width(has auto with px values)
        # not included - line-height,  => (has normal with px values)
        # not included - font-size ( has float valeus)

        columnsWithPX = ["baseline-shift", "border-block-end-width", "border-block-start-width",
                         "border-bottom-left-radius", "border-bottom-right-radius", "border-bottom-width",
                         "border-end-end-radius",
                         "border-end-start-radius", "border-inline-end-width", "border-inline-start-width",
                         "border-left-width", "border-right-width", "border-start-end-radius",
                         "border-start-start-radius",
                         "border-top-left-radius", "border-top-right-radius", "border-top-width", "column-rule-width",
                         "cx", "cy", "inline-size", "margin-block-end", "margin-block-start",
                         "margin-bottom", "margin-inline-end", "margin-inline-start", "margin-left", "margin-right",
                         "margin-top", "offset-distance", "outline-offset", "outline-width", "overflow-clip-margin",
                         "padding-block-end", "padding-block-start", "padding-bottom", "padding-inline-end",
                         "padding-inline-start", "padding-left", "padding-right", "padding-top", "r",
                         "scroll-margin-block-end",
                         "scroll-margin-block-start", "scroll-margin-inline-end", "scroll-margin-inline-start",
                         "shape-margin", "stroke-dashoffset", "stroke-width", "text-indent", "word-spacing", "x", "y",
                         "-webkit-border-horizontal-spacing", "-webkit-border-vertical-spacing",
                         "-webkit-text-stroke-width"
                         ]

        for x in df.index:
            df.loc[x, columnsWithPX] = removePX(x, columnsWithPX)

        df.head(5)

        def removePercentagesAndFill(x, columnsWithPX):
            output = []
            for column in columnsWithPX:
                numeric_string = "".join(filter(str.isdigit, df.loc[x, column]))
                if (numeric_string.isnumeric()):
                    output.append(int(numeric_string))
                else:
                    print("error incompatible values", numeric_string)
                    output.append(numeric_string)
            return output

        # not included - text-size-adjust (has auto)
        columnsWithPercentagesAndFill = ["border-image-slice", "font-stretch", "-webkit-mask-box-image-slice"]

        for x in df.index:
            df.loc[x, columnsWithPercentagesAndFill] = removePercentagesAndFill(x, columnsWithPercentagesAndFill)

        df.head(5)

        # Removing px with float values -=> (font-size)

        def removePXFloat(x, columnsWithPX):
            output = []
            for column in columnsWithPX:
                output.append(float(df.loc[x, column].replace("px", "")))
            return output

        for x in df.index:
            df.loc[x, ['font-size']] = removePXFloat(x, ['font-size'])

        df.head(5)

        # Removing auto and normal from px values by setting up -1 for auto and -2 for normal

        # auto = -1
        # normal = -2

        def remove_px_auto_normal(x, columns):
            output = []
            for column in columns:
                if (df.loc[x, column] == 'auto'):
                    output.append(-1)
                elif (df.loc[x, column] == 'normal'):
                    output.append(-2)
                else:
                    output.append(float(df.loc[x, column].replace("px", "")))
            return output

        columns_with_px_auto_normal = ["block-size", "bottom", "height", "inset-block-end", "inset-block-start",
                                       "inset-inline-end", "inset-inline-start", "left", "line-height",
                                       "min-block-size",
                                       "min-height", "min-inline-size", "min-width", "right", "top", "width"
                                       ]
        for x in df.index:
            df.loc[x, columns_with_px_auto_normal] = remove_px_auto_normal(x, columns_with_px_auto_normal)

        df.head(5)

        # Removing auto and normal from percentages values by setting up -1 for auto and -2 for normal
        # auto = -1
        # normal = -2

        def remove_percentage_auto_normal(x, columns):
            output = []
            for column in columns:
                if (df.loc[x, column] == 'auto'):
                    output.append(-1)
                elif (df.loc[x, column] == 'normal'):
                    output.append(-2)
                else:
                    output.append(int(df.loc[x, column].replace("%", "")))
            return output

        columns_with_percentages_auto_normal = ["text-size-adjust"]
        for x in df.index:
            df.loc[x, columns_with_percentages_auto_normal] = remove_percentage_auto_normal(x,
                                                                                            columns_with_percentages_auto_normal)

        # Creating 2 columns for 2 percentages values in one column

        def create_2_columns_from_percentages(x, columns):
            for column in columns:
                list = df.loc[x, column].split('%')
                df.loc[x, (column + "-1")] = list[0]
                df.loc[x, (column + "-2")] = list[1]

        for x in df.index:
            create_2_columns_from_percentages(x, ["background-position", "object-position", "-webkit-mask-position"])

        # Remove unwanted columns

        df.drop(["background-position", "object-position", "-webkit-mask-position"], axis=1, inplace=True)
        df.head(5)

        # Creating 2 columns for 2 percentages or 2 px values in one column

        def create_2_columns_from_2_percentages_or_2_px_values(x, columns):
            for column in columns:
                list = df.loc[x, column].split(' ')
                if (list[0][-1] == 'x'):
                    val_1 = float(list[0].replace("px", ""))
                    val_2 = float(list[1].replace("px", ""))
                    df.loc[x, (column + "-1")] = val_1
                    df.loc[x, (column + "-2")] = val_2
                if (list[0][-1] == '%'):
                    val_1 = float(list[0].replace("%", ""))
                    val_2 = float(list[1].replace("%", ""))
                    df.loc[x, (column + "-1")] = val_1
                    df.loc[x, (column + "-2")] = val_2

        for x in df.index:
            create_2_columns_from_2_percentages_or_2_px_values(x, ["perspective-origin", "transform-origin"])

        df.head(5)

        # Remove unwanted columns

        df.drop(["perspective-origin", "transform-origin"], axis = 1, inplace = True)

        # Preprocessing box shadow column (rgba(0, 0, 0, 0.298) 0px 0px 3px 0px) or none

        none = -1

        def preprocess_rgba_with_4_px_values(x, colorColumnsArray):
            for column in colorColumnsArray:
                if (df.loc[x, column] == 'none'):
                    df.loc[x, column] = -1
                    df.loc[x, (column + "-rgba-color")] = -1
                    df.loc[x, (column + "-px-1")] = -1
                    df.loc[x, (column + "-px-2")] = -1
                    df.loc[x, (column + "-px-3")] = -1
                    df.loc[x, (column + "-px-4")] = -1
                else:
                    rgba_values = (
                    df.loc[x, column][df.loc[x, column].find('(') + 1: df.loc[x, column].find(')')]).split(', ')
                    rgba_value_decimal = rgba_int(int(rgba_values[0]), int(rgba_values[1]), int(rgba_values[2]),
                                                  float(rgba_values[3]))
                    df.loc[x, (column + "-rgba-color")] = rgba_value_decimal

                    px_values = df.loc[x, column].split(')')[1]
                    split_px_values = px_values.split('px')
                    # print("px value",float(split_px_values[2].strip()))
                    df.loc[x, (column + "-px-1")] = float(split_px_values[0].strip())
                    df.loc[x, (column + "-px-2")] = float(split_px_values[1].strip())
                    df.loc[x, (column + "-px-3")] = float(split_px_values[2].strip())
                    df.loc[x, (column + "-px-4")] = float(split_px_values[3].strip())
                    df.loc[x, column] = 1
            # chr = (df.loc[x, column][df.loc[x, column].find('(')+1 : df.loc[x, column].find(')')]).split(',
            # ') output.append(convert_rgba_with_float_to_decimal(float(chr[0]), float(chr[1]), float(chr[2]),
            # float(chr[3]))) return output

        # for x in df.index:
        #   preprocess_rgba_with_4_px_values(x, ["box-shadow"])



        return jsonify(message='completed preprocessing the dataset!', urlKey=url_key, s3Dir=dir)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
