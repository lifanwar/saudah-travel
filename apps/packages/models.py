from django.db import models
from django.utils.text import slugify


class Package(models.Model):
    """Model untuk paket travel"""
    name = models.CharField(max_length=200, verbose_name="Nama Paket")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    destination = models.CharField(max_length=100, verbose_name="Destinasi")
    description = models.TextField(verbose_name="Deskripsi")
    duration_days = models.IntegerField(verbose_name="Durasi (Hari)")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Harga (Rp)")
    image = models.ImageField(upload_to='packages/', blank=True, null=True, verbose_name="Gambar")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Paket Travel"
        verbose_name_plural = "Paket Travel"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
