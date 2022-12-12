from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Product


class ProductSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, obj):
        image_path, file_extension = obj.image.url.split('.')

        return {
                "path": image_path,
                "formats": [
                    file_extension,
                    "webp"
                ]
            }

    class Meta:
        model = Product
        fields = '__all__'
