from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
from post.models import PostForHour, PostAll, PostArabic, PostBengali, PostChinese, PostEnglish, PostFrench, PostGerman, PostHindi, PostJapanese, PostJavanese, PostKorean, PostLahnda, PostMalay, PostPortuguese, PostRussian, PostSpanish, PostTelugu


class Command(BaseCommand):
    help = "make a instance"

    def handle(self, *args, **options):
        eth = timezone.now() - timedelta(minutes=70)
        etm = timezone.now() - timedelta(seconds=70)
        PostForHour.objects.filter(createdAt__lt=eth).delete()
        PostAll.objects.filter(createdAt__lt=etm).delete()
        PostArabic.objects.filter(createdAt__lt=etm).delete()
        PostBengali.objects.filter(createdAt__lt=etm).delete()
        PostChinese.objects.filter(createdAt__lt=etm).delete()
        PostEnglish.objects.filter(createdAt__lt=etm).delete()
        PostFrench.objects.filter(createdAt__lt=etm).delete()
        PostGerman.objects.filter(createdAt__lt=etm).delete()
        PostHindi.objects.filter(createdAt__lt=etm).delete()
        PostJapanese.objects.filter(createdAt__lt=etm).delete()
        PostJavanese.objects.filter(createdAt__lt=etm).delete()
        PostKorean.objects.filter(createdAt__lt=etm).delete()
        PostMalay.objects.filter(createdAt__lt=etm).delete()
        PostKorean.objects.filter(createdAt__lt=etm).delete()
        PostPortuguese.objects.filter(createdAt__lt=etm).delete()
        PostRussian.objects.filter(createdAt__lt=etm).delete()
        PostSpanish.objects.filter(createdAt__lt=etm).delete()
        PostTelugu.objects.filter(createdAt__lt=etm).delete()

