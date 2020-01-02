# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.urls import reverse
from .items import ThumbnailImageField


class Item(models.Model):
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['id', 'name']
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])


class Photo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, blank=True)
    image = ThumbnailImageField(upload_to='media/photos',)
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo_detail', args=[str(self.id)])


class PhotoInline(admin.StackedInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ("name", "description")
    ordering = ['id', 'name']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('item', "title")


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo, PhotoAdmin)

