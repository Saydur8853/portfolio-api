from django.db import models

import wagtailutils.blocks as utilblocks
from wagtail.core import blocks
from django.core.validators import validate_unicode_slug

"""
.##.....##.########.####.##.......####.########.####.########..######.
.##.....##....##.....##..##........##.....##.....##..##.......##....##
.##.....##....##.....##..##........##.....##.....##..##.......##......
.##.....##....##.....##..##........##.....##.....##..######....######.
.##.....##....##.....##..##........##.....##.....##..##.............##
.##.....##....##.....##..##........##.....##.....##..##.......##....##
..#######.....##....####.########.####....##....####.########..######.
""" 

class CallToActionBlock(utilblocks.CallToActionBlock):
    label = blocks.CharBlock(required=False, default="See More")

    class Meta:
        icon = 'link'
        label = 'Call to Action'

class LabeledCallToActionBlock(CallToActionBlock):
    label = blocks.CharBlock(required=False, default="Details")

    class Meta:
        icon = "link"


class OptionsBlock(blocks.StructBlock):
    anchor = blocks.CharBlock(required=False, validators=[
                              validate_unicode_slug])
    top_padding = blocks.BooleanBlock(required=False, default=True)
    bottom_padding = blocks.BooleanBlock(required=False, default=True)

"""
.########..##........#######...######..##....##..######.
.##.....##.##.......##.....##.##....##.##...##..##....##
.##.....##.##.......##.....##.##.......##..##...##......
.########..##.......##.....##.##.......#####.....######.
.##.....##.##.......##.....##.##.......##..##.........##
.##.....##.##.......##.....##.##....##.##...##..##....##
.########..########..#######...######..##....##..######.
"""


class HeroSlide(blocks.StructBlock):
    image = utilblocks.ImageChooserBlock(help_text="Optimal_Dimension : 1920X941",rendition_rules={
        'original': 'fill-1920x941-c0|format-webp',
        'original_fallback': 'fill-1920x941-c0'
        # 'tab': 'fill-1920x1080-c0|format-webp',
        # 'tab_fallback': 'fill-1920x1080-c0'
        # 'mobile': 'fill-1920x1080-c0|format-webp',
        # 'mobile_fallback': 'fill-1920x1080-c0'
    })
    text = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"  