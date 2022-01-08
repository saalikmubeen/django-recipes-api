from rest_framework import serializers
from shared.models import Tag, Ingredient, Recipe

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredients objects"""
    class Meta:
        model = Ingredient
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link', 'ingredients', 'tags',)
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail object"""
    
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes"""
    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)