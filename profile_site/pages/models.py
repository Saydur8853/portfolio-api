from django.db import models

# Create your models here.
from .blocks import HeroSlide
from wagtail.core.fields import RichTextField, StreamField
from wagtailmenus.models import MenuPage, AbstractMainMenuItem
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtailutils.fields import ImageRenditionField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    HelpPanel,
    MultiFieldPanel,
    RichTextFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface
)
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.api import APIField



class CustomImage(AbstractImage):

    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + ("caption",)



class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class BasePage(MenuPage):

    opengraph_image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    menu_image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    promote_panels = MenuPage.promote_panels + [
        ImageChooserPanel("opengraph_image"),
        ImageChooserPanel("menu_image"),
    ]

    api_fields = [
        APIField("last_published_at"),
        APIField("opengraph_image", serializer=ImageRenditionField({
            'facebook': "fill-600x315-c0",
            'twitter': "fill-300x157-c0"
        }))
    ]

"""
.##.....##..#######..##.....##.########
.##.....##.##.....##.###...###.##......
.##.....##.##.....##.####.####.##......
.#########.##.....##.##.###.##.######..
.##.....##.##.....##.##.....##.##......
.##.....##.##.....##.##.....##.##......
.##.....##..#######..##.....##.########
"""

class HomePage(BasePage):
    body = StreamField([
        ("hero_slider", HeroSlide()),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    api_fields = BasePage.api_fields + [
        APIField('body')
    ]

    subpage_types = ["pages.BasicPage"]