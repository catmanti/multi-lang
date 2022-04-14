"""Add Changers to HomePage"""
from django.db import models

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    def main_image(self):
        """Get a One image"""

        gallery_item = self.carousel_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel(
                    "carousel_images", max_num=5, min_num=1, label="Carousel images"
                ),
            ],
            heading="Images for Carousels",
        )
    ]

    parent_page_types = []


class HomePageCarouselImages(Orderable):
    """Between 1 to 5 images for HomePage Carousel"""

    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="carousel_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel("image"),
        FieldPanel("caption"),
    ]
