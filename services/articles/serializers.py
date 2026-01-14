from articles.models import Article
from packages.kernel.adapters import ModelSerializerAdapter


class ArticleSerializer(ModelSerializerAdapter):

    class Meta:
        model = Article
        fields = "__all__"
