from rest_framework import serializers

from gamesapi_por_fazer.games.models import GameCategory, Score
from .models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):

	game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
												 slug_field='name')

	class Meta:
		model = Game
		fields = (
			'url',
			'game_category',
			'name'
			'release_date',
			'played'
		)


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	pass
	class Meta:
		model = GameCategory
		fields = ('url','pk','name','games')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):

	pass
	class Meta:

		model = Score
		fields = (
			'url',
			'pk',
			'score',
			'score_date',
			'player',
			'game',
		)

